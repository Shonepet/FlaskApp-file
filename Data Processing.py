#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Data processing with python
import csv
from pymongo import MongoClient

class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['survey_db']
        self.collection = self.db['user_data']

    def export_to_csv(self, filename='user_data.csv'):
        data = self.collection.find()
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Age', 'Gender', 'Total Income', 'Utilities', 'Entertainment', 'School Fees', 'Shopping', 'Healthcare'])
            for user in data:
                writer.writerow([user['age'], user['gender'], user['total_income'], user['expenses']['utilities'], user['expenses']['entertainment'], user['expenses']['school_fees'], user['expenses']['shopping'], user['expenses']['healthcare']])

                writer.writeheader()
        for user in users:
            writer.writerow({
                'Age': user.age,
                'Gender': user.gender,
                'Total Income': user.total_income,
                'Utilities': user.expenses.get('utilities', 0),
                'Entertainment': user.expenses.get('entertainment', 0),
                'School Fees': user.expenses.get('school_fees', 0),
                'Shopping': user.expenses.get('shopping', 0),
                'Healthcare': user.expenses.get('healthcare', 0)
            })

user = User("age", "gender", "total_income", "expenses")
user.export_to_csv()


# In[ ]:




