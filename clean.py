# import zipfile
#
# old_zip = "wikiart.zip"
# new_zip = "wikiart_clean.zip"
#
# with zipfile.ZipFile(old_zip, "r") as zin:
#     with zipfile.ZipFile(new_zip, "w", compression=zipfile.ZIP_DEFLATED) as zout:
#         for item in zin.infolist():
#             data = zin.read(item.filename)
#             new_name = item.filename.replace("'", "")
#             zout.writestr(new_name, data)
#
# print("Zip cleaned.")


import pandas as pd
import glob

csv_files = glob.glob("*.csv")

for file in csv_files:
    df = pd.read_csv(file)
    df.iloc[:, 0] = df.iloc[:, 0].str.replace("'", "", regex=False)
    df.to_csv(file.replace(".csv", "_clean.csv"), index=False)
    print(f"Cleaned {file}")

print("All CSVs cleaned.")
