import pandas as pd
import numpy as np

###
# TASK 1.1 LOAD DATA
###

file = 'TeachingRatings.csv'

df = pd.read_csv(file,
                 sep = ',',
                 decimal = '.',
                 header = 0,
                 names = ['minority', 'age', 'gender', 'credits', 'beauty', 'eval', 'division', 'native', 'tenure', 'students', 'allstudents', 'prof'])

###
# TASK 1.2 CHECK DATA
###

def check_dtype(key, type):
  if not isinstance(df[key], type):
      df[key] = df[key].astype(type)

check_dtype('minority', object)
check_dtype('age', float)
check_dtype('gender', object)
check_dtype('credits', object)
check_dtype('beauty', float)
check_dtype('eval', float)
check_dtype('division', object)
check_dtype('native', object)
check_dtype('tenure', object)
check_dtype('students', int)
check_dtype('allstudents', int)
check_dtype('prof', int)

###
# TASK 1.3 CHECK FOR TYPOS
###

mask_gender = (df['gender'] != 'male') & (df['gender'] != 'female')
mask_minority = (df['minority'] != 'yes') & (df['minority'] != 'no')
mask_credits = (df['credits'] != 'single') & (df['credits'] != 'more')
mask_division = (df['division'] != 'upper') & (df['division'] != 'lower')
mask_native = (df['native'] != 'yes') & (df['native'] != 'no')
mask_tenure = (df['tenure'] != 'yes') & (df['tenure'] != 'no')

df['minority'] = df['minority'].replace('y[a-zA-Z0-9]*', 'yes', regex=True)
df['minority'] = df['minority'].replace('n[a-zA-Z0-9]*', 'no', regex=True)
df['credits'] = df['credits'].replace('m[a-zA-Z0-9]*', 'more', regex=True)
df['division'] = df['division'].replace('l[a-zA-Z0-9]*', 'lower', regex=True)
df['native'] = df['native'].replace('y[a-zA-Z0-9]*', 'yes', regex=True)
df['native'] = df['native'].replace('n[a-zA-Z0-9]*', 'no', regex=True)
df['tenure'] = df['tenure'].replace('y[a-zA-Z0-9]*', 'yes', regex=True)
df['tenure'] = df['tenure'].replace('n[a-zA-Z0-9]*', 'no', regex=True)

###
# TASK 1.4 CHECK WHITESPACE
###

for key, value in df.select_dtypes(include=['object']).iteritems():
  df[key] = df[key].str.strip()

###
# TASK 1.5 CAST TEXT TO LOWERCASE
###

for key, value in df.select_dtypes(include=['object']).iteritems():
  df[key] = df[key].str.lower()

###
# TASK 1.6 PERFORM SANITY CHECKS
###

for key, value in df['age'].iteritems():
  if value < 18 or value > 100:
    print(value)

for key, value in df['eval'].iteritems():
  if value < 1 or value > 5:
    print(value)

###
# TASK 1.7 CHECK FOR MISSING DATA
###

def replace_missing_data(key):
  df[key] = df[key].fillna(df[key].mean())

for key, value in df.iteritems():
  if not isinstance(df[key], object):
    replace_missing_data(key)