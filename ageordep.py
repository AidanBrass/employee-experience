#age gender and ethnicity 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

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

# Function to calculate average scores for a group
def group_average(group):
    return group[columns_to_convert].mean()

# Calculate average scores by Age Bracket
age_bracket_avg = df.groupby('Age Bracket').apply(group_average)

# Calculate average scores by Department
department_avg = df.groupby('Department').apply(group_average)

# Calculate average scores by Gender
gender_avg = df.groupby('Gender').apply(group_average)

# Calculate average scores by Ethnicity
ethnicity_avg = df.groupby('Ethnicity').apply(group_average)

print("Average scores by Age Bracket:")
print(age_bracket_avg)

print("\
Average scores by Department:")
print(department_avg)

print("\
Average scores by Gender:")
print(gender_avg)

print("\
Average scores by Ethnicity:")
print(ethnicity_avg)

# Create heatmap for Age Bracket
plt.figure(figsize=(12, 8))
sns.heatmap(age_bracket_avg, annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('Average Scores by Age Bracket')
plt.tight_layout()
plt.savefig('age_bracket_heatmap.png')
plt.close()

# Create heatmap for Department
plt.figure(figsize=(12, 8))
sns.heatmap(department_avg, annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('Average Scores by Department')
plt.tight_layout()
plt.savefig('department_heatmap.png')
plt.close()

print("Heatmaps have been saved as 'age_bracket_heatmap.png' and 'department_heatmap.png'") 