
# In[0] Package
import pandas as pd
import os 
import numpy as np
import time
from .setting import *


#In[3] Step 2: join field names in the link.csv

def joinVdfFieldToLink(dict_type,linkfilename ='link.csv',dictfilename='vdf_table.csv'):
	time_start =time.time()

	dict_df=pd.read_csv(dictfilename,encoding='UTF-8')
	one_way_link_df=pd.read_csv(linkfilename,encoding='UTF-8')

	dictionary = dict(zip(dict_df['VDF'], dict_df[dict_type]))
	one_way_link_df[dict_type]= one_way_link_df.apply(lambda x: dictionary.setdefault(int(x.VDF),''), axis=1)
	#one_way_link_df[dict_type]= one_way_link_df.apply(lambda x: dictionary[x.VDF], axis=1)
	one_way_link_df.to_csv(linkfilename, index=False)
	time_end=time.time()
	print('Add new field name "', dict_type ,'" in the link.csv, CPU time:',time_end-time_start)

def joinAllVdfFieldToLink(linkfilename ='link.csv', dictfilename ='vdf_table.csv'):
	link_file=linkfilename
	dict_file=dictfilename 
	vdf_table_df=pd.read_csv(dictfilename,encoding='UTF-8')
	for field_name in vdf_table_df.columns:
		if str(field_name) != "VDF":
			joinVdfFieldToLink(dict_type=str(field_name),linkfilename =link_file,dictfilename=dict_file)


def updateVDFTable(default_vdf_table='default_vdf_table.csv',updated_vdf_table='updated_vdf_table.csv'):
	print('---combine default vdf table and updated vdf tables---')
	default_vdf_table = pd.read_csv('default_vdf_table.csv')
	updated_vdf_table = pd.read_csv('updated_vdf_table.csv')
	# df_new_table = df_default_table.copy()
	default_vdf_table.index = list(default_vdf_table['VDF'])
	updated_vdf_table.index = list(updated_vdf_table['VDF'])
	for i in updated_vdf_table.index:
		for j in updated_vdf_table.columns:
			if (i in default_vdf_table.index) and (j in default_vdf_table.columns):
				if ~np.isnan(updated_vdf_table.loc[i,j]):
	 				default_vdf_table.loc[i,j] = updated_vdf_table.loc[i,j]
	default_vdf_table.to_csv('vdf_table.csv',index=False)
	print('DONE')
