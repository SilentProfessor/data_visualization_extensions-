import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


file_path = "your_data.xlsx"
df = pd.read_excel(file_path)

print(df.head())
df_clean = df.dropna()


plt.figure(figsize=(10, 6))
sns.heatmap(df_clean.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

sns.pairplot(df_clean)
plt.suptitle("Pair Plot of Features", y=1.02)
plt.show()

if 'Revenue' in df_clean.columns and 'Profit' in df_clean.columns:
    fig = px.scatter(df_clean, x='Revenue', y='Profit', color='Category', size='Profit',
                     title="Revenue vs Profit by Category")
    fig.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df_clean, x='Category', y='Revenue')
plt.title("Revenue Distribution by Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
