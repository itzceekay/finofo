import pandas as pd
from utils import calculate_average_percentage_increase
from model import FinancialCategory

#reading the csv file containing financial data
file_path = 'fp2.csv'
df = pd.read_csv(file_path)

#extracting categories names by isolating the column containing the category names
df_filtered = df[df.iloc[:, 0].notna()]
categories = df_filtered.iloc[:, 0].values

#extracting monthly data projections
monthly_data = df.iloc[2:, 1:].values


#combining the above values to form a dictionary while replacing string values to float for calculations
components = {category: [float(str(value).replace('$', '').replace(',', '')) for value in monthly_data[i]] for i, category in enumerate(categories)}

#creating instances of financial data by iterating through the dictionary
financial_categories = []
for category, values in components.items():
    fin_category = FinancialCategory(
        name = category,
        present_value = values[0],
        growth_rate = calculate_average_percentage_increase(values[1:])
    )
    financial_categories.append(fin_category)

#printing the instances
for category in financial_categories:
    print(category)
