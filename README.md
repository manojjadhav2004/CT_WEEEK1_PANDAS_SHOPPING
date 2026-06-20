# Week 1 — Python & Pandas: Shopping Dataset

This is my Week 1 project where I learned how to use Python and Pandas to load, explore, and clean a dataset.

---

## What I Did

I used a shopping dataset from Kaggle (Myntra products) and did the following steps:

1. **Loaded the CSV file** into a Pandas DataFrame
2. **Explored the data** — checked first/last rows, shape, column names, and data types
3. **Handled missing values** — dropped columns with too many nulls, filled discount column with 0
4. **Filtered and selected data** — selected specific columns, filtered products with rating >= 4.0
5. **Removed duplicate rows**
6. **Created a new column** — `total_amount = initial_price × ratings_count`
7. **Saved the cleaned data** as a new CSV file

---

## Files in This Repo

| File | What it is |
|------|------------|
| `week1_shopping_analysis.ipynb` | Jupyter Notebook with all the code |
| `Combined_dataset.csv` | Original raw dataset |
| `shopping_cleaned.csv` | Cleaned dataset (output) |
| `README.md` | This file |

---

## Dataset

- Source: [Kaggle — Shopping Dataset](https://www.kaggle.com/datasets/anvitkumar/shopping-dataset)
- 1000 rows, 24 columns
- Contains Myntra product info like price, rating, category, discount, etc.

---

## Tools Used

- Python 3
- Pandas
- Jupyter Notebook

---

## How to Run This Project

1. Download or clone this repo
2. Install the required library:
   ```
   pip install pandas
   ```
3. Open the notebook:
   ```
   jupyter notebook week1_shopping_analysis.ipynb
   ```
4. Run all cells from top to bottom

---

## What I Learned

- How to load a CSV file using `pd.read_csv()`
- How to explore data using `.head()`, `.tail()`, `.shape`, `.dtypes`
- How to find and handle missing values
- How to filter rows and select columns
- How to remove duplicate rows
- How to create a new calculated column
- How to save a cleaned DataFrame using `.to_csv()`
