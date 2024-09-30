import pandas as pd
import numpy as np  # Importing numpy directly

# Creating a sample dataset with the necessary columns
data = {
    'Employee ID': range(1, 101),
    'Satisfaction Level': [round(x, 2) for x in np.random.uniform(0.4, 1, 100)],
    'Last Evaluation': [round(x, 2) for x in np.random.uniform(0.5, 1, 100)],
    'Number of Projects': np.random.randint(2, 7, 100),
    'Average Monthly Hours': np.random.randint(150, 300, 100),
    'Years Spent in Company': np.random.randint(1, 10, 100),
    'Work Accident': np.random.choice([0, 1], 100),
    'Promotion in Last 5 Years': np.random.choice([0, 1], 100),
    'Department': np.random.choice(['Sales', 'IT', 'HR', 'Operations', 'Finance', 'Marketing'], 100),
    'Salary': np.random.choice(['Low', 'Medium', 'High'], 100),
    'Employee Left': np.random.choice([0, 1], 100)
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Saving the sample dataset as a CSV file for use in Power BI
file_path = r"C:\Users\ikchu\OneDrive\Desktop\RAW PROJECTS\sample_employee_data.csv"
df.to_csv(file_path, index=False)

file_path
