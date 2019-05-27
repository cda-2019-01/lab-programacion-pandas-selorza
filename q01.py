##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

df0 = pd.read_csv('lab/tbl0.tsv', sep='\t')
df1 = pd.read_csv('lab/tbl1.tsv', sep='\t')
df2 = pd.read_csv('lab/tbl2.tsv', sep='\t')

df0.head()

df0.groupby('_c1').count()['_c0']