import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df_clean = pd.read_csv("cleaned_data.csv")  # Use the file saved from Task 2

# Update these column names to match your dataset
category_col = "category_column"  # e.g., 'Department'
date_col = "date_column"          # e.g., 'Date'
numeric_col = "numeric_column"    # e.g., 'Sales'

# Bar Chart
if category_col in df_clean.columns:
    df_clean[category_col].value_counts().plot(kind='bar', color='skyblue')
    plt.title(f"Bar Chart of {category_col}")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Line Chart
if date_col in df_clean.columns and numeric_col in df_clean.columns:
    df_clean[date_col] = pd.to_datetime(df_clean[date_col], errors='coerce')
    df_clean.sort_values(date_col, inplace=True)
    plt.plot(df_clean[date_col], df_clean[numeric_col], color='green')
    plt.title(f"Line Chart: {numeric_col} Over Time")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.show()

# Pie Chart
if category_col in df_clean.columns:
    df_clean[category_col].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title(f"Pie Chart of {category_col}")
    plt.ylabel('')
    plt.show()
