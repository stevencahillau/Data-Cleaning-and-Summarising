import matplotlib.pyplot as plt

###
# TASK 1
###

# minority

df['minority'].value_counts().plot(kind='bar')
plt.title('Minority')
plt.xlabel('Is the instructor a Minority?')
plt.ylabel('Count')
plt.show()

# age

df['age'].plot(kind='hist')
plt.title('What is the instructors age?')
plt.xlabel('Ages')
plt.ylabel('Count')
plt.axis([df['age'].min(), df['age'].max(), 0, df['age'].count()])
plt.show()

# gender

df['gender'].value_counts().plot(kind='pie', autopct='%.2f')
plt.title('What is the instructors gender?')
plt.show()

# credits

df['credits'].value_counts().plot(kind='bar')
plt.title('Credits')
plt.xlabel('Type of Credit')
plt.ylabel('Count')
plt.show()

# beauty

df['beauty'].value_counts().plot(kind='hist')
plt.title('Instructors beauty')
plt.axis([df['beauty'].min(), df['beauty'].max(), 0, df['beauty'].count()])
plt.show()

# eval

df['eval'].value_counts().plot(kind='bar')
df.iloc[df['eval'].sort_values(axis=0, ascending=list)]
plt.title('Evaluation')
plt.xlabel('Score')
plt.ylabel('Count')
plt.show()

# division

df['division'].value_counts().plot(kind='pie', autopct='%.2f')
plt.title('What is the courses division?')
plt.xlabel('Divisions')
plt.ylabel('Count')
plt.show()

# native

df['native'].value_counts().plot(kind='bar')
plt.xlabel('Is the instructor a native English speaker?')
plt.ylabel('Count')
plt.show()

# tenure

df['tenure'].value_counts().plot(kind='bar')
plt.title('Tenure')
plt.xlabel('Does the instructor have Tenure?')
plt.ylabel('Count')
plt.show()

# students

df['age'].plot(kind='hist')
plt.title('Students')
plt.ylabel('Count')
plt.axis([df['students'].min(), df['students'].max(), 0, df['age'].count()])
plt.show()

# allstudents

df['allstudents'].plot(kind='hist')
plt.title('Students')
plt.ylabel('Count')
plt.axis([df['allstudents'].min(), df['allstudents'].max(), 0, df['age'].count()])
plt.show()

###
# TASK 2
###

# TENURE AND AGE
df.boxplot(column='age', by='tenure')
plt.show()

# MINORITY AND BEAUTY
df.boxplot(column='beauty', by='minority')
plt.show()

# EVAL BEAUTY
df.boxplot(column='beauty', by='eval')
plt.show()

###
# TASK 3
###

from pandas.tools.plotting import scatter_matrix
scatter_matrix(df, alpha=0.2, figsize=(16, 16), diagonal='hist')
plt.show()

