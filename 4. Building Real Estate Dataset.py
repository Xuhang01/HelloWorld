###########################4 class: building real data##############################
import os
os.chdir(r'D:\AllFiles\Study\Program\Python\pandas\Practice')

import quandl
import pandas as pd

api_key = open('quandlapikey.txt','r').read()
df = quandl.get('FMAC/HPI_AK', authtoken=api_key)

print df.head()


fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
