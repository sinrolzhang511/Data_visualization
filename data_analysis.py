import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../data/processed/df_filtered.csv")

st.set_page_config(layout="wide")
st.title("🌍 Global Indicators of 🏭 💲 💨 from 2000 to 2022")

metrics = {
    "CO2 Emissions (Mt CO2e) ": "CO2 Emissions",
    "GDP per Capita (USD)": "GDP per Capita (USD)",
    "% of chemicals in manufacturing": "Chemicals (percent of Value added in manufacturing)",
}

years = sorted(df["Year"].unique())

cols = st.columns(3)

for i, (metric_name, metric_col) in enumerate(metrics.items()):
    with cols[i]: 
        st.subheader(metric_name)

        selected_year = st.selectbox(f"Select Year for {metric_name}", years, key=f"year_{metric_col}")

        df_year = df[df["Year"] == selected_year]

        fig = px.bar(
            df_year.groupby("Continent")[metric_col].mean().reset_index(),
            x="Continent",
            y=metric_col,
            labels={metric_col: metric_name},
            title=f"{metric_name} by Continent ({selected_year})",
            template="gridon",
            height=500
        )
        fig.update_layout(
            title=dict(
                text=f"{metric_name} by Continent ({selected_year})",
                font=dict(size=18, family="Arial, sans-serif", color="darkblue")
            )
        )

        st.plotly_chart(fig, use_container_width=True)


st.header("📈Trend Over Time by Continent")

cols = st.columns(3)

for i, (metric_name, metric_col) in enumerate(metrics.items()):
    with cols[i]: 
        st.subheader(metric_name)

        selected_continent = st.selectbox(f"Select Continent for {metric_name}", df["Continent"].unique(), key=f"continent_{metric_col}")

        df_continent = df[df["Continent"] == selected_continent]

        df_continent_grouped = df_continent.groupby("Year")[metric_col].mean().reset_index()

        fig = px.line(
            df_continent_grouped,
            x="Year",
            y=metric_col,
            labels={metric_col: metric_name},
            title=f"{metric_name} in {selected_continent} Over Time",
            template="gridon",
            height=500
        )

        fig.update_layout(
            title=dict(
                font=dict(size=18, family="Arial, sans-serif", color="darkblue")
            ),
            xaxis_title="Year",
            yaxis_title=metric_name
        )

        st.plotly_chart(fig, use_container_width=True)
        

st.title("CO₂ Emissions and GDP per Capita Visualization")

st.header("Filter Options")
selected_continent = st.selectbox("Select Continent:", df["Continent"].unique())
selected_year = st.selectbox("Select Year:", sorted(df["Year"].unique()))

filtered_df = df[(df["Continent"] == selected_continent) & (df["Year"] == selected_year)]
filtered_df = filtered_df.sort_values(by="CO2 Emissions", ascending=False)

fig, ax1 = plt.subplots(figsize=(16, 12))

ax1.bar(filtered_df["Country Name"], filtered_df["CO2 Emissions"], color='blue', label="CO₂ Emissions")
ax1.set_ylabel("CO₂ Emissions (Mt CO2e)")

ax1.set_xticks(range(len(filtered_df["Country Name"])))
ax1.set_xticklabels(filtered_df["Country Name"], rotation=45, ha="right")

ax2 = ax1.twinx()
ax2.plot(filtered_df["Country Name"], filtered_df["GDP per Capita (USD)"], color='orange', marker='o', label="GDP per Capita")
ax2.set_ylabel("GDP per Capita (USD)")

ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.pyplot(fig)
plt.close(fig)

st.write("### Filtered Data Table")
st.dataframe(filtered_df)



st.title("CO₂ Emissions and % of Chemicals in Manufacturing Visualization")

st.header("Filter Options")
selected_continent = st.selectbox("Select Continent:", df["Continent"].unique(), key="continent_select")
selected_year = st.selectbox("Select Year:", sorted(df["Year"].unique()), key="year_select")

filtered_df = df[(df["Continent"] == selected_continent) & (df["Year"] == selected_year)]
filtered_df = filtered_df.sort_values(by="CO2 Emissions", ascending=False)

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.bar(filtered_df["Country Name"], filtered_df["CO2 Emissions"], color='blue', label="CO₂ Emissions")
ax1.set_ylabel("CO₂ Emissions (Mt CO2e)")

ax1.set_xticks(range(len(filtered_df["Country Name"])))
ax1.set_xticklabels(filtered_df["Country Name"], rotation=45, ha="right")

ax2 = ax1.twinx()
ax2.plot(filtered_df["Country Name"], 
         filtered_df["Chemicals (percent of Value added in manufacturing)"], 
         color='orange', marker='o', label="% of Chemicals in Manufacturing")

ax2.set_ylabel("% of Chemicals in Manufacturing")

ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.pyplot(fig)
plt.close(fig) 

st.write("### Filtered Data Table")
st.dataframe(filtered_df)

st.title("GDP per Capita (USD) and % of Chemicals in Manufacturing Visualization")

st.header("Filter Options")
selected_continent = st.selectbox("Select Continent:", df["Continent"].unique(), key="continent_select_1")
selected_year = st.selectbox("Select Year:", sorted(df["Year"].unique()), key="year_select_1")

filtered_df = df[(df["Continent"] == selected_continent) & (df["Year"] == selected_year)]
filtered_df = filtered_df.sort_values(by="CO2 Emissions", ascending=False)

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.bar(filtered_df["Country Name"], filtered_df["GDP per Capita (USD)"], color='blue', label="CO₂ Emissions (Mt CO2e)")
ax1.set_ylabel("GDP per Capita (USD)")

ax1.set_xticks(range(len(filtered_df["Country Name"])))
ax1.set_xticklabels(filtered_df["Country Name"], rotation=45, ha="right")

ax2 = ax1.twinx()
ax2.plot(filtered_df["Country Name"], 
         filtered_df["Chemicals (percent of Value added in manufacturing)"], 
         color='orange', marker='o', label="% of Chemicals in Manufacturing")

ax2.set_ylabel("% of Chemicals in Manufacturing")

ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.pyplot(fig)
plt.close(fig)

st.write("### Filtered Data Table")
st.dataframe(filtered_df)


df = df.sort_values(by='Year')

st.title("The Relationship among CO₂ Emissions, GDP per capita and % of Chemicals in Manufacturing")

fig = px.scatter(
    df, 
    x="Chemicals (percent of Value added in manufacturing)", 
    y="GDP per Capita (USD)",  
    size="CO2 Emissions", 
    color="Continent",
    animation_frame="Year", 
    animation_group="Country Name",
    hover_name="Country Name", 
    log_x=True, 
    size_max=80,
    title="Energy Consumption Animation"
)

st.plotly_chart(fig)



st.title("🌍 Global Data Visualization")

year = st.slider("Year", int(df["Year"].min()), int(df["Year"].max()), int(df["Year"].min()))

metric = st.selectbox("Index", ["CO2 Emissions", "GDP per Capita (USD)", "Chemicals (percent of Value added in manufacturing)"])

df_year = df[df["Year"] == year]

fig = px.choropleth(
    df_year,
    locations="Country Code",
    color=metric,
    hover_name="Country Name",
    color_continuous_scale="Viridis",
    title=f"{metric} ({year})",
    width=1200,
    height=800
)

st.plotly_chart(fig)
