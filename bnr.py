import pandas as pd
import numpy as np


df = pd.read_csv("bnr.csv")
df_max = df[['acu','global_max','phase_max']].rename(index=str, columns={"global_max": 0, "phase_max": 6})
df_min = df[['acu','global_min','phase_min']].rename(index=str, columns={"global_min": 0, "phase_min": 6})
df_max_1 = pd.melt(df_max, id_vars= ['acu'], value_vars  = [0, 6]).sort_values(by=['acu']).rename(index=str, columns={"variable": 'phase', "value": 'RangeMax'})
df_min_1 = pd.melt(df_min, id_vars= ['acu'], value_vars  = [0, 6]).sort_values(by=['acu']).rename(index=str, columns={"variable": 'phase', "value": 'RangeMin'})

df_max_1_1 = []
for name, new_df in df_max_1.groupby('acu'):
	val = new_df.loc[new_df.phase == 0,'RangeMax']
	new = new_df.fillna(val.values[0])
	df_max_1_1.append(new)

df_min_1_1 = []
for name, new_df in df_min_1.groupby('acu'):
	val = new_df.loc[new_df.phase == 0,'RangeMin']
	new = new_df.fillna(val.values[0])
	df_min_1_1.append(new)

df_max_1_1 = pd.concat(df_max_1_1, axis=0)
df_min_1_1 = pd.concat(df_min_1_1, axis=0)
# print (df_max_1_1)
# print (df_min_1_1)
result = pd.merge(df_max_1_1, df_min_1_1,  how = 'left', on=['acu', 'phase'])
print pd.merge(result, df_min_1_1,  how = 'left', on=['acu', 'phase'])
# print(df_max_1.isnull().any().any())
# df_max_1 = df_max_1.fillna(0)
# print((df_max_1))
# print((df_max_1_1))
# print(type(df_max_1['value'][3]))