import data2supplymodel as ds
period_list=['1400_1800']
ds.joinDemandPeriod(period_list,performance_file_name='link_performance_1.csv')

ds.calibrateFundamentalDiagram(ft_list=[1],at_list=[1],link_performance_file='link_performance.csv')
ds.calibrateVdfCurve(ft_list=[1],at_list=[1],link_performance_file='link_performance.csv')
ds.updateVDFTable(default_vdf_table='default_vdf_table.csv',updated_vdf_table='updated_vdf_table.csv')

ds.joinAllVdfFieldToLink(linkfilename ='link.csv', dictfilename ='vdf_table.csv')


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