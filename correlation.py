import pandas as pd
import numpy as np
from scipy import stats

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

# Apply the mapping to relevant columns
columns_to_convert = ['Job Satisfaction', 'Work-Life Balance', 'Overall Engagement']
for col in columns_to_convert:
    df[col] = df[col].map(response_mapping)

# 1. Hypothesis Test: Job Satisfaction between IT and HR departments
dept1 = "IT"
dept2 = "HR"

job_satisfaction_dept1 = df[df['Department'] == dept1]['Job Satisfaction']
job_satisfaction_dept2 = df[df['Department'] == dept2]['Job Satisfaction']

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(job_satisfaction_dept1, job_satisfaction_dept2)

print("Hypothesis Test Results:")
print("T-statistic: " + str(t_stat))
print("P-value: " + str(p_value))
print("Sample size for " + dept1 + ": " + str(len(job_satisfaction_dept1)))
print("Sample size for " + dept2 + ": " + str(len(job_satisfaction_dept2)))
print("Mean Job Satisfaction for " + dept1 + ": " + str(job_satisfaction_dept1.mean()))
print("Mean Job Satisfaction for " + dept2 + ": " + str(job_satisfaction_dept2.mean()))

# 2. Correlation Analysis: Work-Life Balance and Overall Engagement
correlation_coefficient, p_value = stats.pearsonr(df['Work-Life Balance'], df['Overall Engagement'])

print("\
Correlation Analysis Results:")
print("Correlation coefficient: " + str(correlation_coefficient))
print("P-value: " + str(p_value))

# Display summary statistics
print("\
Summary Statistics:")
print(df[['Work-Life Balance', 'Overall Engagement']].describe())