# TASK-1: Technical Details

## MODEL
* Selected ResNet-50 backbone because ResNet-18/34 are too shallow to capture deep artistic textures and hierarchies, while ResNet-101+ versions are computationally too heavy for efficient training.
* Truncated the backbone at layer4 to retain the full 7×7 spatial feature map (instead of early collapse) so rows and columns can be treated as sequences.
* Applied global average pooling to extract a compact, translation-invariant 2048-dimensional whole-image descriptor.
* Used a projection layer to reduce channels from 2048 to 320, lowering memory and compute for subsequent recurrent layers while preserving rich information.
* Processed horizontal (row-wise) dependencies by reshaping the feature map into sequences and feeding them through a 2-layer bidirectional GRU, followed by mean pooling and attention collapse into a 512-dimensional vector.
* Applied identical vertical (column-wise) processing with a separate bidirectional GRU and attention pooling to explicitly capture directional alignments common in paintings.
* Fused the global CNN descriptor with the row-wise and column-wise vectors via concatenation, creating a strong multi-view 3072-dimensional representation.
* Added dropout before the final linear classifier to regularize training and reduce overfitting on WikiArt’s fine-grained, noisy labels.



## DATA TRANSFORMS
* **RandomResizedCrop:** for size 384 to keep training data variety but reduce size for computation.
* **RandomHorizontalFlip:** to safely double data variety, as most paintings remain semantically valid after flipping.
* **Moderate ColorJitter:** to build robustness against lighting, aging, and scanning differences common in WikiArt.
* **RandomErasing:** for regularization, forcing distributed feature use across rows and columns.

## Runtime Regularizations
* **Weighted sampler:** on train_loader to address severe class imbalance typical in WikiArt style/genre/artist labels.
* **Partial layer freezing:** early stem blocks frozen to preserve strong pretrained low-level features and prevent rough features in early stages to pollute the whole training, later blocks kept trainable.
* **Label smoothing (0.03):** in CrossEntropyLoss to reduce overconfidence and improve generalization on fine-grained tasks.
* **Differential learning rates (AdamW):** higher LR (8e-4) for new modules (proj, GRUs, pools, head), lower LR (1.5e-4) for unfrozen backbone, carefully assigned after multiple experiments.
* **CosineAnnealingLR scheduler:** (T_max=15, eta_min=1e-6) for smooth learning rate decay.
* **Automatic Mixed Precision (AMP):** with GradScaler for faster training and lower GPU memory usage.
* **Data mixing:** MixUp (p=0.35, α=0.3) + CutMix (p=0.35, α=1.0) applied per batch.
* **Gradient clipping:** (max_norm=1.0) to stabilize training with bidirectional GRUs.

## EVALUATION METRICS
* **Validation Loss:** Measures confidence + correctness (via cross-entropy); Used for convergence and overfitting detection.
* **Top-1 Accuracy:** Exact match metric; Primary performance indicator.
* **Top-5 Accuracy:** Checks if true label ∈ top-5 predictions; Important for large class spaces (artist/style), less informative for small class count (genre).
* **Macro F1:** Equal weight per class; Detects failure on minority classes; Critical for imbalanced WikiArt labels.
* **Weighted F1:** Weighted by class frequency; Reflects practical performance under dataset distribution.
* **Per-Class Recall:** Measures how many true samples per class are correctly detected; Identifies underrepresented or hard classes.
* **Classification Report:** Precision, recall, F1 per class; Distinguishes low recall (missed class) vs low precision (over-predicted class).
* **Confusion Matrix:** Shows structured misclassification patterns; Useful for visually similar styles (e.g., Impressionism vs Post-Impressionism), overlapping genres, and artist confusion.

## Outlier detection
* Used final feature embeddings before the classifier.
* Normalized features and computed class centroids.
* Flagged samples with low similarity to their own centroid, small margin to the nearest other class, or prediction mismatches.
