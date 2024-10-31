# trends between age and job satisfaction 

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("employee_experience_survey_data.csv")

# Convert categorical responses to numerical values
response_mapping = {
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly Agree": 5
}

# Apply the mapping to the 'Job Satisfaction' column
df['Job Satisfaction'] = df['Job Satisfaction'].map(response_mapping)

# Group by 'Age Bracket' and calculate the mean job satisfaction
age_job_satisfaction = df.groupby('Age Bracket')['Job Satisfaction'].mean().reset_index()

# Plot the trends
plt.figure(figsize=(10, 6))
plt.bar(age_job_satisfaction['Age Bracket'], age_job_satisfaction['Job Satisfaction'], color='skyblue')
plt.title('Average Job Satisfaction by Age Bracket')
plt.xlabel('Age Bracket')
plt.ylabel('Average Job Satisfaction')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

