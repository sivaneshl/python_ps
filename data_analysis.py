import numpy
import pandas as pd
from matplotlib import pyplot as plt

# Load data
df = pd.read_csv('page_visits.csv')

# Display data
print(df.head())

# calculate survey results
survey_results = df.groupby('website_goal').first_name.count()

# Display survey results
print(
    survey_results
        .reset_index()
        .rename(columns={'first_name': 'number_of_citizens'})
)

# make a pie chart
plt.pie(survey_results.values,
        labels=survey_results.index,
        autopct='%d%%')
plt.title('Why do citizens use our website?')
plt.axis("equal")
plt.show()


by_day = df.groupby('visit_date').first_name.count()
# print(by_day.index, by_day.values)
plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.plot(by_day.values, marker='o', markersize=8, linewidth=3)
plt.ylabel("Number of visits")
ax.set_xticks(range(len(by_day))[::8])
ax.set_xticklabels(by_day.index[::8], rotation=45)
plt.show()

# histogram
plt.hist(df.age, range=(10, 65), bins=11, edgecolor='white')
plt.xlabel("Visitor Age")
plt.ylabel("Number of Visitors")
plt.title("Histogram of Visitor Age")
plt.show()