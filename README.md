# 🐦 Bird Species Observation Analysis

## 📌 Project Overview

This project analyzes bird observation records collected from Forest and Grassland habitats as part of a bird monitoring program.

The project combines:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- SQL Analysis
- Biodiversity Assessment
- Environmental Impact Analysis
- Interactive Streamlit Dashboard

The goal is to understand bird observation patterns, species diversity, habitat characteristics, and environmental influences that affect bird activity.

---

## 🎯 Objectives

- Analyze bird observation trends over time.
- Compare Forest and Grassland habitats.
- Identify biodiversity hotspots.
- Study species diversity and abundance.
- Evaluate environmental conditions affecting observations.
- Perform SQL-based analytical queries.
- Develop an interactive dashboard for exploration.

---

## 📊 Dataset Summary

| Metric | Value |
|----------|----------|
| Total Observations | 15,372 |
| Unique Bird Species | 127 |
| Forest Observations | 8,546 |
| Grassland Observations | 6,826 |
| Observation Period | May–July 2018 |

---

## 🛠️ Technologies Used

### Programming

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit

### Database

- SQLite

### Development Environment

- Jupyter Notebook
- VS Code

---

## 📁 Project Structure

```text
Bird_Species_Observation_Analysis_Project

├── cleaned_data
│   └── birds_cleaned.csv

├── data
│   ├── Forest Dataset.xlsx
│   └── Grassland Dataset.xlsx

├── database
│   └── bird_species.db

├── dashboard
│   ├── app.py
│   ├── pages
│   └── assets

├── images
│   ├── temporal
│   ├── spatial
│   ├── species
│   └── environmental

├── nb
│   ├── 01_Data_Loading.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_EDA_Temporal.ipynb
│   ├── 04_EDA_Spatial.ipynb
│   ├── 05_EDA_Species.ipynb
│   ├── 06_EDA_Environmental.ipynb
│   ├── 07_SQL.ipynb
│   └── 08_Final_Insights.ipynb

├── reports
├── README.md
└── requirements.txt
```

---

## 📈 Analysis Performed

### 1. Data Cleaning

- Merged Forest and Grassland datasets
- Removed duplicate records
- Handled missing values
- Converted data types
- Created new temporal features

### 2. Temporal Analysis

- Monthly observation trends
- Seasonal distribution
- Daily observation patterns
- Visit-wise analysis

### 3. Spatial Analysis

- Habitat comparison
- Administrative unit analysis
- Biodiversity hotspots
- Plot activity analysis

### 4. Species Analysis

- Species diversity
- Most common species
- Rare species
- Sex distribution
- Flyover behavior

### 5. Environmental Analysis

- Temperature analysis
- Humidity analysis
- Sky condition analysis
- Wind condition analysis
- Disturbance analysis

### 6. SQL Analysis

- Observation statistics
- Habitat analysis
- Species queries
- Biodiversity queries

---

## 🔍 Key Findings

### Temporal Insights

- June recorded the highest number of observations.
- Summer accounted for the majority of bird activity.

### Spatial Insights

- ANTI recorded the highest observation count.
- MONO exhibited the highest biodiversity.

### Species Insights

- Northern Cardinal was the most observed species.
- Total species observed: 127.

### Environmental Insights

- Bird activity peaked under moderate temperatures.
- Low-wind conditions produced more observations.
- Low disturbance levels supported higher detection rates.

---

## 🌱 Conservation Insights

- Forest habitats produced more observations.
- Grasslands exhibited nearly identical species diversity.
- Both habitat types contribute significantly to biodiversity.
- Biodiversity hotspots should receive focused conservation attention.

---

## 📊 Interactive Dashboard

The project includes a multi-page Streamlit dashboard featuring:

- KPI Metrics
- Filters
- Temporal Analysis
- Spatial Analysis
- Species Analysis
- Environmental Analysis
- Dataset Download Functionality

Run locally:

```bash
cd dashboard
streamlit run app.py
```

---

## 🚀 Future Improvements

- Geospatial Mapping
- Predictive Modeling
- Species Forecasting
- Cloud Deployment
- Real-Time Monitoring Dashboard

---

## 👨‍💻 Author

Deep Gotecha