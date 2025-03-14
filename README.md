# Global Industrial & Economic Indicators Dashboard

## 📌 Project Overview

This project presents an interactive dashboard for visualizing global industrial and economic indicators, including CO₂ emissions, GDP per capita, and the percentage of chemicals in manufacturing, from 2000 to 2022. The aim is to provide insights into global economic and industrial trends through interactive visualizations.

## 🚀 Installation Instructions

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- pip
- Git

### Clone the Repository
```sh
git clone https://github.com/你的GitHub用户名/Global-Industrial-Indicators.git
cd Global-Industrial-Indicators
```

### Install Dependencies
Create a virtual environment and install required libraries:
```sh
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

### Run the Streamlit App
```sh
streamlit run app.py
```

## 📑 Usage Guide

Once the application is running, open the provided local URL in your browser. You will have access to several interactive visualizations:

### 🌍 Interactive World Map
- Select a year and metric (CO₂ emissions, GDP per capita, or % of chemicals in manufacturing) to visualize global trends.
- Hover over countries to see detailed statistics.

### 📊 Bar Chart & Line Chart Analysis
- Compare continent-wise breakdown of selected metrics.
- View trends over time for different continents using line charts.

### 🔍 Click-to-View Feature
- Filter data by continent and year to explore specific statistics.

---

## 📂 Data Management

### 🔗 Data Source
The dataset is compiled from multiple global databases, including:
- World Bank Open Data
- Global Carbon Atlas
- OECD Industrial Database
- United Nations Industrial Development Organization (UNIDO)

The data has been cleaned and structured into a CSV file (`df_filtered.csv`) stored in the `/data/processed/` directory.

### 🛠 Data Cleaning Process
- **Standardizing Country Codes**: Unified country names and ISO 3166 country codes for consistency.
- **Handling Missing Data**: Applied interpolation and regional averages for missing values.
- **Unit Conversion**: Standardized units across different sources for direct comparison.

## 📊 Visualization Components

### **Choropleth Map (Global Indicator Visualization)**
- Illustrates country-wise distribution of selected indicators.
- Users can select metrics such as CO₂ emissions, GDP per capita, and % of chemicals in manufacturing.

### **Bar Chart (Continent-Based Analysis)**
- Shows the average metric values per continent for a selected year.
- Users can explore trends in industrialization and economic growth.

### **Line Chart (Trend Over Time)**
- Displays how selected indicators evolve over time within a chosen continent.
- Useful for tracking long-term industrial and economic changes.

### **Bubble Chart (Comparative Analysis)**
- Visualizes the relationship between CO₂ emissions, GDP per capita, and % of chemicals in manufacturing.
- Animated time-series feature to observe trends dynamically.

---

## 📌 Data Preparation Decisions

### Why Standardize Country Codes?
Ensures seamless data integration across multiple sources and prevents mismatches in mapping.

### Why Adjust for Missing Values?
Prevents incomplete insights due to missing data, ensuring a comprehensive analysis.

### Why Include Multiple Economic Indicators?
Captures the interplay between industrialization, economic growth, and environmental impact.

---

## 🔍 Critical Analysis

### **Limitations of the Current Approach**

- **Limited Scope of Indicators**: The dataset does not include other crucial industrial metrics like energy consumption or labor productivity.
- **No Real-Time Data**: The dataset does not update in real-time, meaning recent fluctuations in industrial output may not be reflected.
- **Data Gaps in Certain Countries**: Some regions have sparse data availability, leading to reliance on estimations.

### **Future Improvements & Directions**

#### 📌 Expanding Data Coverage
- Adding metrics such as energy consumption, trade balance, and industrial automation rates.
- Incorporating real-time API data sources for up-to-date insights.

#### 🎥 Time-Series Animation
- Enhancing the animated visualization to track global trends dynamically over the years.

#### 📊 Machine Learning Integration
- Using predictive models to forecast industrial trends based on historical data.

---

## 💡 Inspiration & Motivation

The motivation for this project arose from increasing discussions about industrial development and sustainability. Key questions driving this analysis include:
- How do different continents compare in terms of industrialization and economic growth?
- What is the relationship between industrial output and environmental impact?
- How has global manufacturing evolved over time?

By providing an interactive and user-friendly data visualization tool, this project aims to facilitate a deeper understanding of these critical global issues.

---

## 🔗 Additional Resources
- [World Bank Data](https://data.worldbank.org/)
- [OECD Industrial Indicators](https://www.oecd.org/)
- [Global Carbon Atlas](http://www.globalcarbonatlas.org/)
- [UNIDO Industrial Data](https://www.unido.org/statistics)

For contributions, feedback, or discussions, please feel free to reach out via GitHub Issues!

---

📌 **Developed with**: Python, Streamlit, Plotly, Pandas, Matplotlib

