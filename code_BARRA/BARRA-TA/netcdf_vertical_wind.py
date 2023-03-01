#!/usr/bin/python

import matplotlib.pyplot as plt
import netCDF4
import numpy as np
import pandas as pd 

print('*******************************************************************************************************************')
print('starting ...')

# print('Loading latitudes ...')
# lat_full = np.genfromtxt ('latitude.csv', delimiter=",")
# lat = lat_full[:,1]
# print (lat)

# print('Loading longitudes ...')
# lon_full = np.genfromtxt ('longitude.csv', delimiter=",")
# lon = lon_full[:,1]
# print (lon)

filename = 'vertical_wnd-fc-prs-PT1H-BARRA_TA-v1-20180101T0000Z.sub.nc'

print ('Reading netCDF file ...' + filename)

nc = netCDF4.Dataset(filename)


print('file format ',nc.file_format)
print ('nc.variables.keys()  ',nc.variables.keys())   
print('nc.dimensions.keys()  ',nc.dimensions.keys())  
# print('nc.dimensions[time]  ',nc.dimensions['time'])  

print ('nc.cmptypes  ',nc.cmptypes)
print('data_model  ',nc.data_model)
print('enumtypes  ',nc.enumtypes)
print('groups  ',nc.groups)
print (nc.variables['vertical_wnd'])


##print (nc.variables['geop_ht'])
##print (nc.variables['geop_ht'][:,:,1,1])
# print (nc.variables['time'][:])
# 
# 
# 
##print (nc.variables['latitude'])
##print (nc.variables['latitude'][:])
## 
##print (nc.variables['longitude'])
##print (nc.variables['longitude'][:])
# 
# print (nc.variables['pressure'])
# print (nc.variables['pressure'][:])
# 
# print (nc.variables['wnd_ucmp'])
# 
# 
# print('pressure (HPa) [  10.   20.   30.   50.   70.  100.  150.  200.  250.  300.  400.  500. 600.  700.  800.  850.  900.  925.  950.  975. 1000.]')
# print('wnd_ucmp(time, pressure, latitude, longitude)')
# print (nc.variables['wnd_ucmp'][:,:,1,1])
# print (nc.variables['wnd_ucmp'][1,:,1,1])
# print (nc.variables['wnd_ucmp'][2,:,1,1])


# print (nc.variables[['latitude']][:,:])

# file format  NETCDF4
# nc.variables.keys()   dict_keys(['time', 'pressure', 'latitude', 'longitude', 'wnd_ucmp', 'latitude_longitude', 'forecast_period', 'forecast_reference_time'])
# nc.dimensions.keys()   dict_keys(['time', 'pressure', 'latitude', 'longitude'])
# nc.dimensions[time]   <class 'netCDF4._netCDF4.Dimension'>: name = 'time', size = 6
# nc.cmptypes   {}
# data_model   NETCDF4
# enumtypes   {}
# groups   {}



# float32 utotal(time, y, x)
# long_name: 80m interppolated wind speed using the available ACCESS-A files
# units: m/s
# unlimited dimensions: time
# current shape = (17520, 542, 679) (time, y (lat), x (long))
# ?half-hourly for 1 year or hourly for 2 years? 365 x 24 x 2 = 17520
# 679 longitude increments, 542 latitude increments


# y, latitude 4.73 to -55.00    (542)
# x, longitude 95.00 to 169.69  (679)

# x = #1 4.73N, #100 6.20S, #200 17.24S, #300 28.28S, #400 39.32S, #500 50.36S, #542 55.00S
# y = #1 95.00E, #100 105.91E, #200 116.92E, #300 127.94E, #400 138.95E, #500 149.97E, #600 160.99E, #679 169.69E

# enter x and y here, refer to csv files or interpolate lines above to calculate lat/long
# df_1 = pd.DataFrame(index=index, columns=columns)


# for y in range(0, 679, 3):
# 
# 	x = 1
# 	a = np.zeros(shape=(17521))
# 	a = nc.variables['utotal'][:,y,x] # this produces 1d array
# 	df_1 = pd.DataFrame(a, columns=['wind']) 
# 	df_1['long'] = lon[y]
# 
# 	df_1['wind'] = df_1['wind'].interpolate(method='linear', limit_direction='forward', axis=0)
# 	df_1 = df_1[['long','wind']]	# move long to the left
# 
# 	x_label = str(x)
# 	df_1 = df_1.rename(columns={'long': 'long', 'wind': x_label})
# 
# 	df_1 = df_1[:8760]
# 	df_1 = round(df_1,3)
# 
# 	# print (df_1)
# 
# 	
# 
# 	for x in range(2, 542):
# 
# 		a = np.zeros(shape=(17521))
# 		a = nc.variables['utotal'][:,y,x] # this produces 1d array
# 		df_2 = pd.DataFrame(a, columns=['wind']) 
# 
# 		df_2['wind'] = df_2['wind'].interpolate(method='linear', limit_direction='forward', axis=0)
# 	
# 		x_label = str(x)
# 		df_2 = df_2.rename(columns={'wind': x_label})
# 
# 		df_2 = df_2[:8760]
# 		df_2 = round(df_2,3)
# 		# print (df_2)
# 
# 		df_1 = pd.concat([df_1, df_2], axis=1, join='inner')
# 
# 
# 	print (df_1)
# 
# 	filename = "csv/wind_y_" + str(lon[y]) + ".csv"
# 	print ("printing to file ....", filename)
# 
# 	df_1.to_csv(filename)
# 	print('*******************************************************************************************************************')





print("done")
print('finished')
print('*******************************************************************************************************************')
