import pandas as pd
import numpy as np


# Read the CSV file
df = pd.read_csv('employee_experience_survey_data.csv')

# Convert categorical responses to numerical values
response_mapping = {
    'Strongly Disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly Agree': 5
}

# Apply the mapping to relevant columns
columns_to_convert = ['Job Satisfaction', 'Work-Life Balance', 'Management Support', 'Team Collaboration', 
                      'Workload Fairness', 'Career Development Opportunities', 'Workplace Inclusivity', 
                      'Company Communication', 'Compensation Satisfaction', 'Job Security', 'Overall Engagement']

for col in columns_to_convert:
    df[col] = df[col].map(response_mapping)

# Calculate descriptive statistics for Overall Engagement and Job Satisfaction
engagement_stats = df['Overall Engagement'].describe()
satisfaction_stats = df['Job Satisfaction'].describe()

print("Descriptive Statistics for Overall Engagement:")
print(engagement_stats)
print("\
Descriptive Statistics for Job Satisfaction:")
print(satisfaction_stats)

# Calculate mode for Overall Engagement and Job Satisfaction
engagement_mode = df['Overall Engagement'].mode().values[0]
satisfaction_mode = df['Job Satisfaction'].mode().values[0]

print(f"\
Mode for Overall Engagement: {engagement_mode}")
print(f"Mode for Job Satisfaction: {satisfaction_mode}")

# Convert mode back to categorical response
engagement_mode_category = {v: k for k, v in response_mapping.items()}[engagement_mode]
satisfaction_mode_category = {v: k for k, v in response_mapping.items()}[satisfaction_mode]

print(f"Mode category for Overall Engagement: {engagement_mode_category}")
print(f"Mode category for Job Satisfaction: {satisfaction_mode_category}")