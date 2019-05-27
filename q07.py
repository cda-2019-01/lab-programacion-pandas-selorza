##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 

df0['suma'] = df0['_c0'] + df0['_c2']
df0.head()