# TASK1- STYLE 

**Code File:** [style_final_wOutliers.ipynb](https://github.com/Karvy-Singh/g/blob/main/task1/style/style_final_wOutliers.ipynb)

### Metrics:

## Model Performance Summary

| Metric | Value |
| :--- | :--- |
| **Top-1 Accuracy** | 67.37% |
| **Top-5 Accuracy** | 95.54% |
| **Macro F1 Score** | 68.24% |
| **Weighted F1 Score** | 67.50% |

---

## Per-Class Recall
This metric highlights the model's ability to correctly identify all relevant instances of a specific art movement.

| Art Movement | Recall |
| :--- | :--- |
| **Ukiyo_e** | 92.00% |
| **Northern_Renaissance** | 82.35% |
| **Pointillism** | 81.70% |
| **Color_Field_Painting** | 81.40% |
| **Baroque** | 81.05% |
| **Early_Renaissance** | 76.98% |
| **Naive_Art_Primitivism** | 73.65% |
| **Analytical_Cubism** | 72.73% |
| **Cubism** | 72.39% |
| **Minimalism** | 71.57% |
| **Impressionism** | 69.98% |
| **Rococo** | 69.81% |
| **High_Renaissance** | 69.40% |
| **Realism** | 68.44% |
| **Abstract_Expressionism** | 67.27% |
| **Pop_Art** | 66.89% |
| **Symbolism** | 65.10% |
| **Mannerism_Late_Renaissance** | 64.49% |
| **Art_Nouveau** | 64.38% |
| **Romanticism** | 58.95% |
| **Expressionism** | 58.76% |
| **Post_Impressionism** | 56.80% |
| **Contemporary_Realism** | 53.47% |
| **Synthetic_Cubism** | 50.00% |
| **Fauvism** | 46.43% |
| **Action_painting** | 41.38% |
| **New_Realism** | 39.36% |

---

## Detailed Classification Report



| Class Name | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| Abstract_Expressionism | 0.686 | 0.673 | 0.679 | 834 |
| Action_painting | 0.923 | 0.414 | 0.571 | 29 |
| Analytical_Cubism | 0.800 | 0.727 | 0.762 | 33 |
| Art_Nouveau | 0.687 | 0.644 | 0.665 | 1300 |
| Baroque | 0.690 | 0.811 | 0.745 | 1272 |
| Color_Field_Painting | 0.716 | 0.814 | 0.762 | 484 |
| Contemporary_Realism | 0.811 | 0.535 | 0.644 | 144 |
| Cubism | 0.615 | 0.724 | 0.665 | 670 |
| Early_Renaissance | 0.713 | 0.770 | 0.740 | 417 |
| Expressionism | 0.549 | 0.588 | 0.568 | 2020 |
| Fauvism | 0.476 | 0.464 | 0.470 | 280 |
| High_Renaissance | 0.603 | 0.694 | 0.645 | 402 |
| Impressionism | 0.783 | 0.700 | 0.739 | 3918 |
| Mannerism_Late_Renaissance | 0.694 | 0.645 | 0.668 | 383 |
| Minimalism | 0.765 | 0.716 | 0.740 | 401 |
| Naive_Art_Primitivism | 0.786 | 0.736 | 0.760 | 721 |
| New_Realism | 0.661 | 0.394 | 0.493 | 94 |
| Northern_Renaissance | 0.830 | 0.824 | 0.827 | 765 |
| Pointillism | 0.817 | 0.817 | 0.817 | 153 |
| Pop_Art | 0.737 | 0.669 | 0.701 | 444 |
| Post_Impressionism | 0.531 | 0.568 | 0.549 | 1935 |
| Realism | 0.628 | 0.684 | 0.655 | 3219 |
| Rococo | 0.779 | 0.698 | 0.736 | 626 |
| Romanticism | 0.750 | 0.590 | 0.660 | 2105 |
| Symbolism | 0.545 | 0.651 | 0.593 | 1358 |
| Synthetic_Cubism | 0.821 | 0.500 | 0.621 | 64 |
| Ukiyo_e | 0.973 | 0.920 | 0.946 | 350 |
| **Accuracy** | | | **0.674** | **24421** |
| **Macro Avg** | 0.717 | 0.665 | 0.682 | 24421 |
| **Weighted Avg** | 0.682 | 0.674 | 0.675 | 24421 |
