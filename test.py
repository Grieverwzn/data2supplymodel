import data2supply as ds

# two_way_node_filename='input_node.csv'
# two_way_link_filename='input_link.csv'

#ds.checkNetFile(two_way_node_filename,two_way_link_filename)
# ds.convertNodeToGMNS(two_way_node_filename,node_id='NODE_ID')
# ds.convertLinkToGMNS(two_way_link_filename,ba_lanes='BBBB',keep_original_attributes=True)

# data_calibration_folder='./data_calibration/'
# directional_link_filename='link.csv'
# ds.convertObsToGMNS(data_calibration_folder,directional_link_filename='link.csv')

# demand_folder='./demand_folder/'
# ds.concatenateDemandFile(demand_folder,'AM','am')



period_list=['1400_1800']
ds.joinDemandPeriod(period_list,performance_file_name='link_performance_1.csv')

ds.calibrateFundamentalDiagram(ft_list=[1],at_list=[1],link_performance_file='link_performance_1.csv')
ds.calibrateVdfCurve(ft_list=[1],at_list=[1],link_performance_file='link_performance_1.csv')
ds.updateVDFTable(default_vdf_table='default_vdf_table.csv',updated_vdf_table='updated_vdf_table.csv')

ds.joinAllVdfFieldToLink(linkfilename ='link.csv', dictfilename ='vdf_table.csv')

# # ds.matrix2column(matrix_file_name='DA_GP.csv')


# file_mapping_dict={'period':['am','md','pm','nt'],
# 'file_name':['demand_am.csv','demand_md.csv','demand_pm.csv','demand_nt.csv']}


# ds.splitMultiColumnToSingleColumn(file_mapping_dict)



import path4gmns as pg

# no need to call read_network() like the python module
# as network and demand loading will be handled within DTALite

# path-based UE
mode = 1
assignment_num = 10
column_update_num = 10

pg.perform_network_assignment_DTALite(mode, assignment_num, column_update_num)

# no need to call output_columns() and output_link_performance()
# since outputs will be processed within DTALite

print('\npath finding results can be found in agent.csv')