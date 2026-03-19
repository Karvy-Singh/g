# TASK1- GENERAL MODEL with combined classification of Artist, Genre, Style

**code file:** [gcomb.ipynb](https://github.com/Karvy-Singh/g/blob/main/task1/combined/gcomb.ipynb)

## Overall Joint Model Performance
These metrics represent the model's ability to correctly predict multiple attributes (Artist, Style, and Genre) simultaneously for a single artwork.

| Metric | Score |
| :--- | :--- |
| **Joint Exact Match** | **68.18%** |
| **Mean Top-1 Accuracy** | 86.14% |
| **Mean Top-5 Accuracy** | 98.63% |
| **Mean Macro F1 Score** | 78.07% |
| **Mean Weighted F1** | 86.07% |

---

### Understanding the Results



* **Joint Exact Match (68.18%):** This is the "strictest" metric. It means that in nearly 7 out of 10 cases, the model correctly identified **every single label** assigned to the image across all categories.
* **Mean Top-1 Accuracy (86.14%):** Across all individual tasks (Artists, Movements, and Subjects), the model is correct about 86% of the time on its first guess.
* **Mean Top-5 Accuracy (98.63%):** The "true" label is almost always within the model's top 5 predictions, showing extremely strong feature extraction capabilities.

---

### Technical Implications
The high **Mean Top-5 Accuracy** compared to the **Macro F1 Score** suggests that while the model is incredibly powerful, it may still face challenges with "Long-Tail" classes (rare artists or niche movements with very few training samples).
