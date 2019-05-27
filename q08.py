##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 

df0['ano'] = [i.split('-')[0] for i in df0['_c3']]
df0.head()