# TASK1- ARTIST 

**code file:** [artist_final_wOutliers.ipynb](https://github.com/Karvy-Singh/g/blob/main/task1/artist/artist_final_wOutliers.ipynb)

## Model Performance Summary (Artist Classification)

| Metric | Value |
| :--- | :--- |
| **Top-1 Accuracy** | 90.92% |
| **Top-5 Accuracy** | 98.39% |
| **Macro F1 Score** | 90.48% |
| **Weighted F1 Score** | 90.90% |

---

## Per-Class Recall
This list showcases the percentage of each artist's work that was correctly identified.

| Artist | Recall |
| :--- | :--- |
| **Gustave_Dore** | 97.33% |
| **Rembrandt** | 96.57% |
| **Nicholas_Roerich** | 96.15% |
| **Raphael_Kirchner** | 96.10% |
| **Ivan_Aivazovsky** | 95.95% |
| **Ivan_Shishkin** | 95.51% |
| **Eugene_Boudin** | 95.18% |
| **Vincent_van_Gogh** | 94.71% |
| **Albrecht_Durer** | 93.55% |
| **Pyotr_Konchalovsky** | 92.73% |
| **Marc_Chagall** | 92.14% |
| **Camille_Pissarro** | 90.98% |
| **Claude_Monet** | 90.50% |
| **Edgar_Degas** | 90.16% |
| **Pierre_Auguste_Renoir** | 90.00% |
| **Childe_Hassam** | 89.09% |
| **Martiros_Saryan** | 87.21% |
| **John_Singer_Sargent** | 86.38% |
| **Boris_Kustodiev** | 84.13% |
| **Paul_Cezanne** | 82.08% |
| **Ilya_Repin** | 80.75% |
| **Pablo_Picasso** | 77.19% |
| **Salvador_Dali** | 76.92% |

---

## Detailed Classification Report



| Artist Name | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| Albrecht_Durer | 0.921 | 0.935 | 0.928 | 248 |
| Boris_Kustodiev | 0.878 | 0.841 | 0.859 | 189 |
| Camille_Pissarro | 0.818 | 0.910 | 0.861 | 266 |
| Childe_Hassam | 0.980 | 0.891 | 0.933 | 165 |
| Claude_Monet | 0.903 | 0.905 | 0.904 | 400 |
| Edgar_Degas | 0.927 | 0.902 | 0.914 | 183 |
| Eugene_Boudin | 0.963 | 0.952 | 0.958 | 166 |
| Gustave_Dore | 1.000 | 0.973 | 0.986 | 225 |
| Ilya_Repin | 0.861 | 0.807 | 0.833 | 161 |
| Ivan_Aivazovsky | 0.982 | 0.960 | 0.971 | 173 |
| Ivan_Shishkin | 0.898 | 0.955 | 0.925 | 156 |
| John_Singer_Sargent | 0.860 | 0.864 | 0.862 | 235 |
| Marc_Chagall | 0.930 | 0.921 | 0.925 | 229 |
| Martiros_Saryan | 0.893 | 0.872 | 0.882 | 172 |
| Nicholas_Roerich | 0.884 | 0.961 | 0.921 | 545 |
| Pablo_Picasso | 0.830 | 0.772 | 0.800 | 228 |
| Paul_Cezanne | 0.940 | 0.821 | 0.877 | 173 |
| Pierre_Auguste_Renoir | 0.952 | 0.900 | 0.925 | 420 |
| Pyotr_Konchalovsky | 0.955 | 0.927 | 0.941 | 275 |
| Raphael_Kirchner | 0.943 | 0.961 | 0.952 | 154 |
| Rembrandt | 0.930 | 0.966 | 0.947 | 233 |
| Salvador_Dali | 0.780 | 0.769 | 0.775 | 143 |
| Vincent_van_Gogh | 0.913 | 0.947 | 0.930 | 567 |
| | | | | |
| **Accuracy** | | | **0.909** | **5706** |
| **Macro Avg** | 0.910 | 0.901 | 0.905 | 5706 |
| **Weighted Avg** | 0.910 | 0.909 | 0.909 | 5706 |
