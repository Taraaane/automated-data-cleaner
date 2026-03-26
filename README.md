# Automated Data Cleaning Pipeline 🧹

## Overview
This project is a Python-based automation script designed to clean, preprocess, and standardize messy datasets. It takes raw CSV files, handles missing values, removes duplicates, and formats the data for further analysis. This tool significantly reduces the manual effort required in the data preparation phase.

## Features
* **Duplicate Removal:** Automatically identifies and removes duplicate rows to ensure data integrity.
* **Missing Value Handling:** Fills missing numerical data with the column's mean value, and handles missing text data by replacing it with 'Unknown'.
* **Data Normalization:** Standardizes column names (lowercase with underscores) and strips extra whitespace from text fields.
* **Automated Export:** Processes the raw data and exports a clean, ready-to-use CSV file.

## Technologies Used
* **Python 3.x**
* **Pandas** (for data manipulation and analysis)
* **NumPy** (for numerical operations)

## How to Run the Project

1. **Install the required libraries:**
   It is recommended to use a virtual environment. Install dependencies using:
   ```bash
   pip install pandas numpy

