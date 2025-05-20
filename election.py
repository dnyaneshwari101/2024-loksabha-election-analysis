import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv('candidates_with_phase.csv')

st.title("2024 Loksabha Elections")

nav = st.sidebar.radio("Navigation",['Male Female Participation','Age Wise Representation','Result','Maharashtra'])

if nav == "Male Female Participation" :
    gender = ['male', 'female', 'third' ]
    candidates = [7634,801,6]

    fig, ax = plt.subplots()
    ax.pie(candidates, labels = gender, autopct = '%1.1f%%')
    ax.set_title('Total Candidates')
    st.pyplot(fig)

election_res=pd.read_csv("results_2024_winners.csv")
winning_party=election_res['Winning Party'].value_counts()
winning_party=winning_party.reset_index() # converting series to dataframe
winning_party.columns=['Party','Count']

if nav =='Result':
    #plot a histogram
    fig, ax= plt.subplots(figsize=(12, 6)) #creates a figure and axes object that can be used to plot the graph.
    sns.barplot(x='Party', y='Count', data=winning_party)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.set_xlabel('Party')
    ax.set_ylabel('No. of seats won')
    ax.set_title('Number of seats won by each political party')
    st.pyplot(fig)

# Define the bins and labels
bins = [20, 30, 40, 50, 60, 70, float('inf')]  # float('inf') for ages 70 and above
labels = ['20-30', '30-40', '40-50', '50-60', '60-70', '70 and above']

# Assuming 'Age' is the column with the candidates' ages
bins = [20, 30, 40, 50, 60, 70, float('inf')]
labels = ['20-30', '30-40', '40-50', '50-60', '60-70', '70 and above']

# Categorize the data based on age
data['Age Category'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# Get the counts of candidates in each age category
age_wise_data = data['Age Category'].value_counts().reset_index()
age_wise_data.columns = ['Age category', 'Total candidates']

# Sort by age category to maintain the order of bins
age_wise_data['Age category'] = pd.Categorical(age_wise_data['Age category'], categories=labels, ordered=True)
age_wise_data = age_wise_data.sort_values('Age category').reset_index(drop=True)

# Streamlit code for age-wise representation
if nav == 'Age Wise Representation':
    # Display the table
    st.table(age_wise_data)

    # Create a bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Age category', y='Total candidates', data=age_wise_data, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.set_xlabel('Age categories')
    ax.set_ylabel('No. of candidates')
    ax.set_title('Age Wise Representation')

    # Display the plot in Streamlit
    st.pyplot(fig)

    


    
