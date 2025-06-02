import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('fifa_players.csv')

# Data cleaning
# Convert 'Value' to numeric (handle formats like '€10.5M' or numeric)
if df['Value'].dtype == 'object':
    df['Value'] = df['Value'].str.replace('€', '').str.replace('M', '').astype(float)
else:
    df['Value'] = df['Value'].astype(float)  # Ensure numeric if already clean

# Convert 'Weight' to numeric (handle formats like '70kg' or numeric)
if df['Weight'].dtype == 'object':
    df['Weight'] = df['Weight'].str.replace('kg', '').astype(float)
else:
    df['Weight'] = df['Weight'].astype(float)  # Ensure numeric if already clean

# 1. Line Chart: Average FIFA Player Overall Skill by Age
avg_skill_by_age = df.groupby('Age')['Overall'].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(avg_skill_by_age['Age'], avg_skill_by_age['Overall'], marker='o', color='#4B8BBE', linewidth=2)
plt.title('Average FIFA Player Overall Skill by Age', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Average Overall Skill', fontsize=12)
plt.grid(True)
plt.savefig('line_chart_skill_by_age.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. Line Graph: Average FIFA Player Value by Age
avg_value_by_age = df.groupby('Age')['Value'].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(avg_value_by_age['Age'], avg_value_by_age['Value'], marker='s', color='#FF6F61', linewidth=2)
plt.title('Average FIFA Player Value by Age', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Average Value (€M)', fontsize=12)
plt.grid(True)
plt.savefig('line_graph_value_by_age.png', dpi=300, bbox_inches='tight')
plt.show()

# 3. Histogram: FIFA Overall Skill Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Overall'], bins=20, color='#6A9C89', edgecolor='black')
plt.title('FIFA Overall Skill Distribution', fontsize=14)
plt.xlabel('Overall Skill Score', fontsize=12)
plt.ylabel('Number of Players', fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig('histogram_skill_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. Pie Chart #1: Preferred Foot Distribution
foot_counts = df['Preferred Foot'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(foot_counts, labels=foot_counts.index, autopct='%1.1f%%', colors=['#4B8BBE', '#FF6F61'], startangle=90)
plt.title('FIFA Players Preferred Foot Distribution', fontsize=14)
plt.savefig('pie_chart_preferred_foot.png', dpi=300, bbox_inches='tight')
plt.show()

# 5. Pie Chart #2: Weight Distribution of FIFA Players
bins = [0, 70, 80, 1000]
labels = ['<70kg', '70-80kg', '>80kg']
df['Weight Category'] = pd.cut(df['Weight'], bins=bins, labels=labels)
weight_counts = df['Weight Category'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(weight_counts, labels=weight_counts.index, autopct='%1.1f%%', colors=['#6A9C89', '#FF6F61', '#4B8BBE'], startangle=90)
plt.title('FIFA Players Weight Distribution', fontsize=14)
plt.savefig('pie_chart_weight_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# 6. Box & Whisker Plot: Comparing FIFA Teams
top_clubs = df['Club'].value_counts().head(5).index
df_top_clubs = df[df['Club'].isin(top_clubs)]
plt.figure(figsize=(12, 6))
sns.boxplot(x='Club', y='Overall', hue='Club', data=df_top_clubs, palette=['#4B8BBE', '#FF6F61', '#6A9C89', '#FFD166', '#9B59B6'], legend=False)
plt.title('FIFA Player Overall Skill by Club', fontsize=14)
plt.xlabel('Club', fontsize=12)
plt.ylabel('Overall Skill Score', fontsize=12)
plt.xticks(rotation=45)
plt.savefig('box_plot_club_skill.png', dpi=300, bbox_inches='tight')
plt.show()
print(df.head())