# -*- coding: utf-8 -*-
"""
Created on Sat May 25 01:33:03 2024

@author: munju
"""

import pandas as pd

# Define the data
data = {
    "Name": ["Munjurul", "Jane Smith", "Alice Johnson", "Bob Brown"],
    "Email": ["munjurul2001@gmail.com", "jane.smith@example.com", "alice.johnson@example.com", "bob.brown@example.com"],
    "Birthday": ["2024-05-26", "2024-05-27", "1985-06-15", "1980-03-22"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the path where you want to save the CSV file
full_path = "C:\\Users\\munju\\Desktop\\Python\\birthday.csv"

# Save the DataFrame to a CSV file
df.to_csv(full_path, index=False)

print(f"CSV file created successfully at {full_path}.")
