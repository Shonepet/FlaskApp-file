#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['survey_db']
collection = db['user_data']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_data = {
            'age': request.form['age'],
            'gender': request.form['gender'],
            'total_income': request.form['total_income'],
            'expenses': {
                'utilities': float(request.form.get('utilities', 0)),
                'entertainment': float(request.form.get('entertainment', 0)),
                'school_fees': float(request.form.get('school_fees', 0)),
                'shopping': float(request.form.get('shopping', 0)),
                'healthcare': float(request.form.get('healthcare', 0))
            }
        }
        collection.insert_one(user_data)
        return redirect('/')
    return render_template('survey.html')

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




