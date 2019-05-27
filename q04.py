##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 

uniques = df1['_c4'].unique()
res = []
for elemt in uniques:
    res.append(elemt.upper())
res = sorted(res)
res