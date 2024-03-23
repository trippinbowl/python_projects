import pandas as pd
import plotly.express as px

# Load your dataset
data_path = 'Book2.csv'  # Replace this with the path to your CSV file
data = pd.read_csv(data_path)

# Data cleaning and preparation
data['Players in Shaded region'] = data['Players in Shaded region'].str.replace(',', '').astype(int)
data['Revenue Decline'] = data['Revenue Decline'].str.rstrip('%').astype(float)
data['Interventions'] = data['Interventions'].ffill()

# Aggregating data for the treemap
treemap_data = data.groupby(['Interventions', 'Action']).agg({
    'Revenue Decline': 'sum',
    'Players in Shaded region': 'sum'
}).reset_index()

# Creating the treemap
fig = px.treemap(treemap_data, path=['Interventions', 'Action'], values='Players in Shaded region',
                 color='Revenue Decline', color_continuous_scale='RdYlGn_r',
                 title='Treemap of Revenue Decline by Action within Interventions')

# Display the treemap
fig.show()
