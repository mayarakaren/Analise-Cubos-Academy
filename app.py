import pandas as pd
import numpy as np

# Creating the initial dataframe based on the provided image data
data = {
    "Veiculo": ["Google Search"] * 3,
    "Categoria": ["Institucional"] * 3,
    "data": ["01/01/2020", "02/01/2020", "03/01/2020"],
    "Investimento": ["926,96", "939,78", "926,29"],
    "Leads": [30, 46, 0],
    "Sessoes": [5543, 6632, 0],
    "Impressoes": [57000, 44997, 49519],
    "CPL": ["30.89866666666660", "20.43", "inf"],
    "formato": ["NAN"] * 3
}

df = pd.DataFrame(data)

# Function to generate random data for the remaining rows
def generate_random_data(num_records):
    np.random.seed(0)  # For reproducibility
    vehicles = ["Google Search", "Facebook Ads", "Instagram Ads", "LinkedIn Ads"]
    categories = ["Institucional", "Promocional"]
    
    dates = pd.date_range(start="01/01/2020", periods=num_records, freq='D')
    investments = np.round(np.random.uniform(500, 1500, size=num_records), 2)
    leads = np.random.randint(0, 100, size=num_records)
    sessoes = np.random.randint(0, 10000, size=num_records)
    impressoes = np.random.randint(10000, 100000, size=num_records)
    cpl = np.round(investments / np.where(leads == 0, np.nan, leads), 2)
    cpl = np.where(np.isnan(cpl), 'inf', cpl)
    
    data = {
        "Veiculo": np.random.choice(vehicles, num_records),
        "Categoria": np.random.choice(categories, num_records),
        "data": dates.strftime("%d/%m/%Y"),
        "Investimento": [f"{inv:.2f}".replace('.', ',') for inv in investments],
        "Leads": leads,
        "Sessoes": sessoes,
        "Impressoes": impressoes,
        "CPL": cpl,
        "formato": ["NAN"] * num_records
    }
    
    return pd.DataFrame(data)

# Generate 497 more rows to make it at least 500 records
num_additional_records = 997
additional_data = generate_random_data(num_additional_records)

# Concatenate the initial data with the additional data
full_df = pd.concat([df, additional_data], ignore_index=True)

# Saving the DataFrame to a CSV file
output_path = "marketing_data.csv"
full_df.to_csv(output_path, index=False, sep=';')

output_path
