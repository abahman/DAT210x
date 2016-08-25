print 'hello world'

import pandas as pd
students = pd.read_csv('student_por.csv', sep=';')
print students.iloc[0:2]
print students.loc[0:5,['school','age','sex']]


