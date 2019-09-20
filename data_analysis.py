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

