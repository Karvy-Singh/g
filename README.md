# Overview: Task 1 & Task 2

## Task 1: Convolutional-Recurrent Architectures
Task: Build a model based on convolutional-recurrent architectures for classifying Style, Artist, Genre, and other attributes. General and Specific. Pick the most appropriate approach and discuss your strategy. Use the ArtGAN dataset: https://github.com/cs-chan/ArtGAN/blob/master/WikiArt%20Dataset/README.md

Evaluation Metrics: discuss which evaluation metrics you are using to evaluate your model performance. Find outliers, e.g. paintings that do not fit a particular artist or genre despite their assignment.


### Overview
* **Architecture:** ResNet50 → BiGRU (Row) + BiGRU (Column) → Attention Pooling → FC Layer → Output
* **Regularisation:** RandomResizedCrop → Scale Jitter → CutMix → Label Mixing
* **Training Details:** Partial layer freezing (in artist/genre, style all layers learn after a certain epoch). Also using Dropout, Label Smoothing, with AdamW optimizer and CosineAnnealingLR scheduler.
* **Reference:** Credibility for the achieved accuracy from a CNN-RNN Model:
https://www.researchgate.net/publication/392709479_CLASSIFICATION_OF_ART_PAINTINGS_USING_VISION_TRANSFORMERS

### Results
| Category | Top-1 Accuracy | Top-5 Accuracy | Macro F1 Score | Weighted F1 Score |
| :--- | :--- | :--- | :--- | :--- |
| **Artist** | 90.92% | 98.39% | 90.48% | 90.90% |
| **Genre** | 79.19% | 98.61% | 77.53% | 79.27% |
| **Style** | 67.37% | 95.54% | 68.24% | 67.50% |
| **Combined** | 86.14% | 98.63% | 78.07% | 86.07% |

---

## TASK-2: Image Retrieval & Reranking
Task: Build a model to find similarities in paintings, e.g. portraits with a similar face or pose.. Pick the most appropriate approach and discuss your strategy. Use the National Gallery Of Art open data set: https://github.com/NationalGalleryOfArt/opendata

Evaluation Metrics: discuss which evaluation metrics you are using to evaluate your model performance.

### Overview
* **Pipeline:** Image → DINOv2 ViT-B/14 → 768-d Feature Embedding → L2 Normalization → FAISS Index (IndexFlatIP) → k-NN Retrieval (cosine similarity) → (Top-K Candidates)
* **Reranking:** Face Detection → Face Crop → Face Embedding → Pose (face-box geometry) → Composition (face position / scale) → Metadata (filtered, no label leakage) → Weighted Reranking → Final Top-K Similar Results



### Metrics
| Stage | HitRate@5 | Precision@5 | mAP@5 |
| :--- | :--- | :--- | :--- |
| **Base Retrieval** | 0.9740 | 0.7508 | 0.6867 |
| **Reranked Retrieval** | **0.9760** | **0.7968** | **0.7477** |

### Retrieval Strategy Details
* **Stage 1:** retrieve top candidates using global DINOv2 embedding similarity.
* **Stage 2:** rerank the retrieved candidates using more portrait-specific cues.
* **Base retrieval captures:** overall semantics, composition, texture, and subject-level similarity.
* **Reranking focus:** similar face, similar pose, and similar portrait framing.
