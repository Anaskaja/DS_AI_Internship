# Mini-Project 1: Customer Analytics EDA

## Overview
This repository contains my first independent Exploratory Data Analysis (EDA) project. The goal of this project was to take a raw dataset (`customer_analytics.csv`), clean the data using statistical justifications, and uncover actionable business insights using Python.

## Project Structure
* `customer_analytics.csv`: The raw dataset containing 255 records of customer demographics, income, and purchasing metrics.
* `MiniProject1_EDA.ipynb`: The Jupyter Notebook containing the full workflow (Setup, Preprocessing, Deep Dive, Big Picture).
* `requirements.txt`: Python package dependencies.
* `Insights_Report.pdf/md`: The final summarized business insights report.

## Key Learnings
1. **Data Cleaning:** Realized that dropping data requires strict statistical justification. Opted for median imputation due to heavy outliers in the income column.
2. **Visualizations:** Utilized Seaborn to build properly labeled distributions, scatter plots, boxplots, and correlation heatmaps.
3. **Data Storytelling:** Focused heavily on translating raw Python correlations (like the -0.38 relationship between income and spending) into real-world business insights.

## How to Run
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Jupyter Notebook: `jupyter notebook MiniProject1_EDA.ipynb`