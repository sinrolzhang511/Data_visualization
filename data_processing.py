import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(script_dir, "..", "data", "cleaned")  
processed_dir = os.path.join(script_dir, "..", "data", "processed")

os.makedirs(processed_dir, exist_ok=True)

co2_file = os.path.join(data_dir, "CO2_Emissions_Cleaned.csv")
gdp_file = os.path.join(data_dir, "GDP_per_Capita_Cleaned.csv")
chemicals_file = os.path.join(data_dir, "Chemicals_Cleaned.csv")

if not (os.path.exists(co2_file) and os.path.exists(gdp_file) and os.path.exists(chemicals_file)):
    raise FileNotFoundError("error")

co2emission_cleaned = pd.read_csv(co2_file)
gdp_cleaned = pd.read_csv(gdp_file)
chemicals_cleaned = pd.read_csv(chemicals_file)

co2emission_new_long = co2emission_cleaned.melt(id_vars=["Continent", "Country Name", "Country Code"],
                                                var_name="Year", value_name="CO2 Emissions")

gdp_new_long = gdp_cleaned.melt(id_vars=["Continent", "Country Name", "Country Code"],
                                var_name="Year", value_name="GDP per Capita (USD)")

chemicals_new_long = chemicals_cleaned.melt(id_vars=["Continent", "Country Name", "Country Code"],
                                            var_name="Year", value_name="Chemicals (percent of Value added in manufacturing)")

co2emission_new_long["Year"] = co2emission_new_long["Year"].astype(int)
gdp_new_long["Year"] = gdp_new_long["Year"].astype(int)
chemicals_new_long["Year"] = chemicals_new_long["Year"].astype(int)


df_merged = co2emission_new_long.merge(chemicals_new_long, on=["Continent", "Country Name", "Country Code", "Year"], how="outer")
df_merged = df_merged.merge(gdp_new_long, on=["Continent", "Country Name", "Country Code", "Year"], how="outer")


output_path = os.path.join(processed_dir, "df_merged.csv")
df_merged.to_csv(output_path, index=False, encoding="utf-8")

df_filtered = df_merged[(df_merged["Year"] >= 2000) & (df_merged["Year"] <= 2022)]

df_filtered = df_filtered.dropna().reset_index(drop=True)

filtered_output_path = os.path.join(processed_dir, "df_filtered.csv")
df_filtered.to_csv(filtered_output_path, index=False, encoding="utf-8")  

print(f"successfully saved \n- {output_path}\n- {filtered_output_path}")



