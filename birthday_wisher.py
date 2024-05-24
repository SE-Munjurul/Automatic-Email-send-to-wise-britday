# -*- coding: utf-8 -*-
"""
Created on Sat May 25 01:35:57 2024

@author: munju
"""

import smtplib
import pandas as pd
from datetime import datetime

# Function to send email
def send_email(to_email, subject, body):
    from_email = "jusnu2001@gmail.com"
    password = "567@Rasal"

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(from_email, password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(from_email, to_email, message)

# Read the CSV file
# Full path to the CSV file
full_path = "C:\\Users\\munju\\Desktop\\Python\\birthdays.csv"

# Read the CSV file with the full path
df = pd.read_csv(full_path)


# Get today's date
today = datetime.today().strftime("%m-%d")

# Check for birthdays
for index, row in df.iterrows():
    birthday = datetime.strptime(row["Birthday"], "%Y-%m-%d").strftime("%m-%d")
    if birthday == today:
        subject = "Happy Birthday!"
        # বার্তার মেসেজ পরিবর্তন করুন
        body = f"Happy Birthday, {row['Name']}!"
        
        # আপনার নামের উপরে ভিত্তি করে বার্তার মেসেজ পরিবর্তন করুন
        if row['Name'] == "Munjurul":
            body += " Wishing you all the best on your special day! Have a fantastic birthday!"
        else:
            body += " Wishing you a fantastic day filled with joy and happiness!"
        
        send_email(row["Email"], subject, body)


print("Birthday emails sent if there were any birthdays today.")
