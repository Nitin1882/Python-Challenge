#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
files="Resources/election_data.csv"
df_electiondata = pd.read_csv(files)
df_electiondata.head()


# In[2]:


# The total number of votes cast
Total = df_electiondata['Voter ID'].count()
Total


# In[3]:


# A complete list of candidates who received votes
List_Candidate = df_electiondata['Candidate'].unique()
List_Candidate


# In[4]:


# The total number of votes each candidate won
# df_electiondata.loc[df_electiondata['Candidate'] == 'Khan', 'Voter ID'].count()
Candidate_Vote_Count = df_electiondata.groupby('Candidate')['Voter ID'].count()
Candidate_Vote_Count


# In[5]:


# The percentage of votes each candidate won rounded up to nearest integer 
Pct_Vote_Count = Candidate_Vote_Count/Total*100
Pct_Vote_Count.round(2)


# In[ ]:


Candidate_Vote_Count.sort_values(by=['Candidate'], inplace=True)
Candidate_Vote_Count

