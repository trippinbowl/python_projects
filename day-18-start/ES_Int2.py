import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data_path = 'Book2.csv'  # Update this path
data = pd.read_csv(data_path)
data['Players in Shaded region'] = data['Players in Shaded region'].str.replace(',', '').astype(int)
data['Revenue Decline'] = data['Revenue Decline'].str.rstrip('%').astype(float)
data['Interventions'] = data['Interventions'].fillna(method='ffill')

# Creating a clustered bar chart
plt.figure(figsize=(14, 8))
chart = sns.barplot(x='Interventions', y='Revenue Decline', hue='Action', data=data, palette='pastel')
plt.title('Clustered Bar Chart of Revenue Decline by Actions across Interventions')
plt.xlabel('Intervention')
plt.ylabel('Revenue Decline (%)')
plt.legend(title='Action', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
