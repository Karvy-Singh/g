# TASK1: GENRE

**code file:** [genre_final_wOutliers.ipynb](https://github.com/Karvy-Singh/g/blob/main/task1/genre/genre_final_wOutliers.ipynb)

## Model Performance Summary

| Metric | Value |
| :--- | :--- |
| **Top-1 Accuracy** | 79.19% |
| **Top-5 Accuracy** | 98.61% |
| **Macro F1 Score** | 77.53% |
| **Weighted F1 Score** | 79.27% |

---

## Per-Class Recall

| Subject Category | Recall |
| :--- | :--- |
| **Abstract Painting** | 91.07% |
| **Landscape** | 87.05% |
| **Still Life** | 84.57% |
| **Portrait** | 80.13% |
| **Cityscape** | 78.70% |
| **Religious Painting** | 78.38% |
| **Nude Painting** | 75.69% |
| **Illustration** | 72.63% |
| **Sketch and Study** | 69.63% |
| **Genre Painting** | 67.42% |

---

## Detailed Classification Report



| Subject Class | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **Abstract Painting** | 0.878 | 0.911 | 0.894 | 1490 |
| **Cityscape** | 0.734 | 0.787 | 0.759 | 1380 |
| **Genre Painting** | 0.684 | 0.674 | 0.679 | 3257 |
| **Illustration** | 0.735 | 0.726 | 0.731 | 570 |
| **Landscape** | 0.856 | 0.870 | 0.863 | 4007 |
| **Nude Painting** | 0.667 | 0.757 | 0.709 | 576 |
| **Portrait** | 0.872 | 0.801 | 0.835 | 4233 |
| **Religious Painting** | 0.831 | 0.784 | 0.807 | 1961 |
| **Sketch and Study** | 0.613 | 0.696 | 0.652 | 1182 |
| **Still Life** | 0.802 | 0.846 | 0.823 | 836 |
| | | | | |
| **Accuracy** | | | **0.792** | **19492** |
| **Macro Avg** | 0.767 | 0.785 | 0.775 | 19492 |
| **Weighted Avg** | 0.795 | 0.792 | 0.793 | 19492 |
