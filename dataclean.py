import numpy as np
import pandas as pd

df = pd.read_csv('student.csv')
print(df.head(10))

df.drop_duplicates(subset=['Student_ID'], keep='first')
print(df.head(10))
    
df['Gender'] = df['Gender'].astype(str).str.strip().str.upper()
gender_map ={
    'female': 'F',
    'Female': 'F',
    'FEMALE': 'F',
    'f': 'F',
    'F': 'F',
    'male': 'M',
    'Male': 'M',
    'MALE': 'M',
    'm': 'M',
    'M': 'M'
}
df['Gender'] = df['Gender'].map(gender_map).fillna('Unknown')
print(df.head(10))
df['Semester'] = df['Semester'].astype(str).str.strip().str.upper()
semester_map={
    '4':'1',
    '3':'1',
    '2':'1',
    '1':'1'
}
df['Semester'] = df['Semester'].map(semester_map).fillna('Unknown')
df['Student_ID'] = df['Student_ID'].str[5:]
df['Student_ID'] = pd.to_numeric(df['Student_ID'])
df = df.sort_values(by='Student_ID') 
df['Student_ID'] = '2026B0' + df['Student_ID'].astype(str)
print(df.head(10))
df.to_csv('cleaned_student.csv', index=False)