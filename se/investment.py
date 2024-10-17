import pandas as pd

# Defining the variables
initial_investment = 36.76  # monthly investment
monthly_rate = 0.009  # 0.9% per month
years = 40
months = years * 12  # Total months

# Create lists to store the data
month_list = []
investment_list = []
earnings_list = []

# Initialize variables for the calculations
total_investment = 0
total_value = 0

# Calculate for each month
for month in range(1, months + 1):
    total_investment += initial_investment
    total_value = total_value * (1 + monthly_rate) + initial_investment
    month_list.append(month)
    investment_list.append(round(total_investment, 2))
    earnings_list.append(round(total_value, 2))

# Create a DataFrame to represent the table
df = pd.DataFrame({
    'Month': month_list,
    'Total Investment': investment_list,
    'Total Value (With Interest)': earnings_list
})

# Show the DataFrame
df
