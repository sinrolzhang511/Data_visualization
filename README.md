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
git clone https://github.com/sinrolzhang511/Data_visualization

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
The dataset is compiled from World Bank Open Data

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

## 📌 Methodology explanation

Understanding the relationships between CO₂ emissions, GDP per capita, and the percentage of chemicals in manufacturing is crucial for assessing their combined impact on society, the environment, and industrial development. CO₂ emissions are a key indicator of environmental impact and climate change, while GDP per capita reflects economic prosperity and living standards. The percentage of chemicals in manufacturing serves as a proxy for industrial intensity and technological advancement, given the chemical sector’s pivotal role in various industries.  

Studying these variables between 2000 and 2022 is particularly meaningful due to significant global changes during this period. The early 2000s marked rapid industrialization in emerging economies, while advancements in technology and increased environmental awareness shaped global production patterns. Additionally, international climate agreements, such as the Paris Agreement, gained momentum during this time, influencing emission trends and industrial practices. Analyzing this period provides valuable insights into how economic growth, environmental impact, and industrial strategies have evolved in response to these global shifts.

---

## 🔍 Critical Analysis

### ** Limitations of the Current Approach**

- **Limited Scope of Indicators**: The dashboard focuses on only three key indicators—CO₂ emissions, GDP per capita, and the percentage of chemicals in manufacturing. However, industrialization and economic development are influenced by a broader set of factors, such as energy consumption, labor productivity, foreign direct investment (FDI), and infrastructure development. Incorporating additional economic and industrial indicators would provide a more comprehensive analysis.
- **No Real-Time Data**: The dataset only covers the period from 2000 to 2022, and it is static rather than continuously updated. Given the rapidly changing nature of global industry, having real-time or more frequently updated data would provide more timely insights.
- **Data Gaps and Aggregation Issues**:Some countries have missing or incomplete data, requiring the use of regional averages or interpolation methods. While these methods help fill gaps, they may introduce biases or inaccuracies. Additionally, industrial classifications and data collection standards vary between countries, which could affect comparability.
- **Correlation vs. Causation Challenge**:While visualizing relationships between CO₂ emissions, GDP per capita, and the percentage of chemicals in manufacturing helps identify trends, it does not establish causation. For instance, higher GDP per capita could be linked to greater industrial efficiency, but it might also be due to a service-based economy rather than manufacturing growth. Future analysis could incorporate causal inference techniques to better understand these relationships.
- **Data Gaps in Certain Countries**: Some regions have sparse data availability, leading to reliance on estimations.

### ** Ptential Improvements & Future Directions**

#### 📌 Expanding Data Coverage
- Include more economic and industrial indicators such as labor productivity, trade balance, energy consumption, and renewable energy adoption.
- Integrate real-time data APIs to keep the dashboard updated with the latest information.

#### 🎥 User Interactivity and Customization
- Enhancing the animated visualization to track global trends dynamically over the years.
- Allow users to select multiple countries for comparative analysis.
- Provide filtering options based on economic regions (e.g., OECD, BRICS) or income groups (low-income, middle-income, high-income).
- Enable users to customize visualization settings, such as adjusting inflation for GDP comparisons.

#### 📊 Enhanced Visualization Techniques
- Introduce additional charts such as heatmaps for regional comparisons or scatter plots with regression analysis to explore relationships between variables more precisely.
- Implement animated time-series visualizations to showcase trends dynamically, making it easier to identify industrial shifts over time.

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

For contributions, feedback, or discussions, please feel free to reach out via GitHub Issues!

---

📌 **Developed with**: Python, Streamlit, Plotly, Pandas, Matplotlib

