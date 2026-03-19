# TASK-2: Technical Details

**Code File:** [g-sim.ipynb](https://github.com/Karvy-Singh/g/blob/main/task2/g-sim.ipynb)

### Metrics
| Stage | HitRate@5 | Precision@5 | mAP@5 |
| :--- | :--- | :--- | :--- |
| **Base Retrieval** | 0.9740 | 0.7508 | 0.6867 |
| **Reranked Retrieval** | **0.9760** | **0.7968** | **0.7477** |

## MODEL
* Used **DINOv2 ViT-B/14** as the feature extractor because it produces strong semantic embeddings without requiring task-specific labels. 
* It captures high-level structure, composition, texture, and subject information better than standard supervised classifier features, making it suitable for visual similarity retrieval in paintings.
* Chose an **embedding-retrieval setup** instead of classification because the task is to find visually similar paintings, not assign a fixed label.
* Extracted a 768-dim feature vector for each painting and applied **L2 normalization** so similarity search is stable.
* Built a **FAISS IndexFlatIP** index for fast nearest-neighbor retrieval over all paintings.
* Used **inner product** on normalized embeddings, which is effectively cosine similarity.

## RETRIEVAL STRATEGY
* Used a **two-stage pipeline**:
  * **Stage 1:** retrieve top candidates using global DINOv2 embedding similarity.
  * **Stage 2:** rerank the retrieved candidates using more portrait-specific cues.
* **Base retrieval captures:** overall semantics, composition, texture, and subject-level similarity.
* **Reranking necessity:** global embeddings alone are not enough for cases like similar face, similar pose, or similar portrait framing.

## RERANKING
* Used **face detection** to locate the main face in portrait-like paintings.
* Cropped the face region and extracted a **face-level DINOv2 embedding**.
* Compared face crops to improve local similarity matching.
* Added a **pose score** using face-box geometry: face center, face size, and aspect ratio.
* Added a **composition score** using relative face position and scale.
* Added a small **metadata score** as a weak prior, excluding fields that overlap with the evaluation label.
* Combined all signals with **weighted score fusion** to produce the final ranking.

## EVALUATION METRICS
* Evaluated both base retrieval and reranked retrieval on the same random 300 query paintings for fair comparison.
* Used classification as a coarse relevance label, since the dataset does not provide direct annotations for “same face”, “same pose”, or “same composition”.
* **Precision@5:** Measures how many of the top-5 retrieved paintings belong to the same relevant group as the query; Used to check whether the retrieved shortlist is visually and semantically clean.
* **HitRate@5:** Measures whether at least one relevant painting appears in the top-5 results; Used to check whether the system can successfully retrieve a useful match for a given query painting.
* **mAP@5:** Measures ranking quality within the top-5 retrieved paintings; Important because similarity search depends not only on retrieving relevant works, but also on ordering them well.
