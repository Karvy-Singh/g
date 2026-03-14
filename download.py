import os
import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

os.makedirs("./images", exist_ok=True)

objects = pd.read_csv("./objects.csv", low_memory=False)
images = pd.read_csv("./published_images.csv", low_memory=False)

objects.columns = objects.columns.str.lower()
images.columns = images.columns.str.lower()

images["openaccess"] = images["openaccess"].astype(str).str.lower().str.strip()

images = images[
    (images["openaccess"].isin(["1", "true", "yes"]))
    & (images["iiifurl"].notna())
    & (images["depictstmsobjectid"].notna())
].copy()

images = images.drop_duplicates(subset="depictstmsobjectid")

df = images.merge(
    objects, left_on="depictstmsobjectid", right_on="objectid", how="inner"
).copy()

df = df.drop_duplicates(subset="objectid").copy()
df["classification"] = df["classification"].astype(str).str.strip().str.lower()

print("Total rows after merge:", len(df))
print("\nClassification counts:")
print(df["classification"].value_counts().head(20))

RANDOM_STATE = 42


def safe_sample(frame, n, random_state=42):
    if len(frame) == 0:
        return frame.copy()
    return frame.sample(n=min(n, len(frame)), random_state=random_state).copy()


paintings = safe_sample(df[df["classification"] == "painting"], 2000, RANDOM_STATE)
drawings = safe_sample(df[df["classification"] == "drawing"], 1200, RANDOM_STATE)
prints = safe_sample(df[df["classification"] == "print"], 1200, RANDOM_STATE)
photos = safe_sample(df[df["classification"] == "photograph"], 400, RANDOM_STATE)
sculptures = safe_sample(df[df["classification"] == "sculpture"], 200, RANDOM_STATE)

df = (
    pd.concat([paintings, drawings, prints, photos, sculptures], ignore_index=True)
    .drop_duplicates(subset="objectid")
    .reset_index(drop=True)
)

print("\nBalanced dataset size:", len(df))
print(df["classification"].value_counts())

df["download_url"] = df["iiifurl"].apply(
    lambda x: x.rstrip("/") + "/full/!512,512/0/default.jpg"
)


def get_field(row, col, default=""):
    return row[col] if col in row and pd.notna(row[col]) else default


def download_row(row):
    objectid = row["objectid"]
    url = row["download_url"]
    filename = f"./images/{objectid}.jpg"

    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        with open(filename, "wb") as f:
            f.write(r.content)

        return {
            "objectid": objectid,
            "title": get_field(row, "title"),
            "classification": get_field(row, "classification"),
            "dated": get_field(row, "dated"),
            "artist": get_field(row, "displayname"),
            "medium": get_field(row, "medium"),
            "department": get_field(row, "department"),
            "image_path": filename,
            "image_url": url,
        }
    except Exception as e:
        return {
            "objectid": objectid,
            "error": str(e),
            "image_url": url,
        }


saved_rows = []
failed_rows = []
i = 0

with ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(download_row, row) for _, row in df.iterrows()]
    for future in as_completed(futures):
        result = future.result()
        if result is not None:
            if "error" in result:
                failed_rows.append(result)
            else:
                print("done:", i)
                i += 1
                saved_rows.append(result)

manifest = pd.DataFrame(saved_rows)
manifest["embedding_idx"] = range(len(manifest))
manifest.to_csv("./dataset_manifest.csv", index=False)

failed_manifest = pd.DataFrame(failed_rows)
failed_manifest.to_csv("./failed_downloads.csv", index=False)

print("done,", len(manifest), "images saved")
print("failed,", len(failed_manifest), "images")
