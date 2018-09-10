import pandas as pd
import numpy as np
import re

#df=pd.read_csv('test.csv')
#X=np.array(df['body'])
#print(X)
pattern = re.compile(r'INR\s+([\d,\.]+)')

with open('data.txt','r') as rf:
 contents=rf.read()
 matches = pattern.finditer(contents)
 for match in matches:
  print(match)
 
#X='NEFT Transaction with reference number N015170233274273 for INR 2,000.00 has been credited to the beneficiary account on 16-01-2017 at 09:55:12.'

#pattern = re.compile(r'Avl\s+Bal\s+INR\s+([\d,\.]+)')
#pattern = re.compile(r'INR\s+([\d,\.]+)')

#matches = pattern.finditer(str(X))


#for match in matches:
	#print(match)

#print (X)