import pandas as pd
import os


script_dir = os.path.dirname(os.path.abspath(__file__))


raw_dir = os.path.join(script_dir, "..", "data", "raw")
cleaned_dir = os.path.join(script_dir, "..", "data", "cleaned")


os.makedirs(cleaned_dir, exist_ok=True)


co2emission_path_new = os.path.join(raw_dir, "CO2_Emissions_by_Country_with_Continent.csv")
forest_cover_path_new = os.path.join(raw_dir, "Forest_Cover_by_Country_with_Continent.csv")
gdp_path_new = os.path.join(raw_dir, "GDP_per_Capita_by_Country_with_Continent.csv")
chemicals_path_new = os.path.join(raw_dir, "Chemicals_value added in manufacturing.csv")


co2emission_new = pd.read_csv(co2emission_path_new)
forest_cover_new = pd.read_csv(forest_cover_path_new)
gdp_new = pd.read_csv(gdp_path_new)
chemicals_new = pd.read_csv(chemicals_path_new)


chemicals_new = chemicals_new.drop(columns=['Continent'])
chemicals_new = chemicals_new.rename(columns={'Country Name': 'Continent', 'Country Code': 'Country Name'})
chemicals_new = chemicals_new.drop(columns=["Country Code.2", "Country Code.3", "Indicator Name", "Indicator Code"])
chemicals_new = chemicals_new.rename(columns={"Country Code.1": "Country Code"})

co2emission_new = co2emission_new.dropna(subset=['Country Name', 'Country Code'])
co2emission_new = co2emission_new.dropna(axis=1, how='all')
co2emission_new = co2emission_new.dropna(subset=co2emission_new.columns[3:], how='all')

gdp_new = gdp_new.dropna(subset=['Country Name', 'Country Code'])
gdp_new = gdp_new.dropna(axis=1, how='all')
gdp_new = gdp_new.dropna(subset=gdp_new.columns[3:], how='all')

forest_cover_new = forest_cover_new.dropna(subset=['Country Name', 'Country Code'])
forest_cover_new = forest_cover_new.dropna(axis=1, how='all')
forest_cover_new = forest_cover_new.dropna(subset=forest_cover_new.columns[3:], how='all')

chemicals_new = chemicals_new.dropna(subset=['Country Name', 'Country Code'])
chemicals_new = chemicals_new.dropna(axis=1, how='all')
chemicals_new = chemicals_new.dropna(subset=chemicals_new.columns[3:], how='all')

co2emission_clean_path = os.path.join(cleaned_dir, "CO2_Emissions_Cleaned.csv")
forest_cover_clean_path = os.path.join(cleaned_dir, "Forest_Cover_Cleaned.csv")
gdp_clean_path = os.path.join(cleaned_dir, "GDP_per_Capita_Cleaned.csv")
chemicals_clean_path = os.path.join(cleaned_dir, "Chemicals_Cleaned.csv")

co2emission_new.to_csv(co2emission_clean_path, index=False)
forest_cover_new.to_csv(forest_cover_clean_path, index=False)
gdp_new.to_csv(gdp_clean_path, index=False)
chemicals_new.to_csv(chemicals_clean_path, index=False)

print(f"✅ 清洗后的数据已成功保存到 {cleaned_dir}")
