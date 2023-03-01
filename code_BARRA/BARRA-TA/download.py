#!/usr/bin/python

import urllib.request
import calendar

url = 'https://dapds00.nci.org.au/thredds/fileServer/cj37/BARRA/BARRA_TA/v1/forecast/prs/'
# url = 'https://dapds00.nci.org.au/thredds/fileServer/cj37/BARRA/BARRA_TA/v1/forecast/prs/'

region = 'TA'


for year in ['1999','1998','1997','1996','1995','1994','1993','1992','1991','1990']:
	for month in ['01','02','03','04','05','06','07','08','09','10','11','12']:
		if month == '01':
			days_in_month = 31
		elif month == '02':
			if (calendar.isleap(int(year))):
				days_in_month = 29
			else:
				days_in_month = 28
		elif month == '03':
			days_in_month = 31
		elif month == '04':
			days_in_month = 30
		elif month == '05':
			days_in_month = 31
		elif month == '06':
			days_in_month = 30
		elif month == '07':
			days_in_month = 31
		elif month == '08':
			days_in_month = 31
		elif month == '09':
			days_in_month = 30
		elif month == '10':
			days_in_month = 31
		elif month == '11':
			days_in_month = 30
		elif month == '12':
			days_in_month = 31
			
		for day_int in range(1, days_in_month + 1, 1):

			if day_int < 10:
				day = '0' + str(day_int)
			else:
				day = str(day_int)

			for time in ['00','06','12','18']:

				
				filename_u = 'wnd_ucmp-fc-prs-PT1H-BARRA_' + region + '-v1-' + year + month + day + 'T' + time + '00Z.sub.nc'	# wind speed u component
				filename_u_1 = 'wnd_ucmp-fc-prs-PT1H-BARRA_' + region + '-v1.1-' + year + month + day + 'T' + time + '00Z.sub.nc'	# wind speed u component
				filename_v = 'wnd_vcmp-fc-prs-PT1H-BARRA_' + region + '-v1-' + year + month + day + 'T' + time + '00Z.sub.nc'	# wind speed v component
				filename_v_1 = 'wnd_vcmp-fc-prs-PT1H-BARRA_' + region + '-v1.1-' + year + month + day + 'T' + time + '00Z.sub.nc'	# wind speed v component
				filename_g = 'geop_ht-fc-prs-PT1H-BARRA_' + region + '-v1-'  + year + month + day + 'T' + time + '00Z.sub.nc'	# geopotential height - converts pressure level (HPa) to height above surface (m)
				filename_g_1 = 'geop_ht-fc-prs-PT1H-BARRA_' + region + '-v1.1-'  + year + month + day + 'T' + time + '00Z.sub.nc'	# geopotential height - converts pressure level (HPa) to height above surface (m)
				
				url_u = url + 'wnd_ucmp/' + year + '/' + month + '/' + filename_u
				url_u_1 = url + 'wnd_ucmp/' + year + '/' + month + '/' + filename_u_1
				url_v = url + 'wnd_vcmp/' + year + '/' + month + '/' + filename_v
				url_v_1 = url + 'wnd_vcmp/' + year + '/' + month + '/' + filename_v_1
				url_g = url + 'geop_ht/' + year + '/' + month + '/' + filename_g
				url_g_1 = url + 'geop_ht/' + year + '/' + month + '/' + filename_g_1
				
				flag_u = 0

				print (url_u)

				try:
					conn = urllib.request.urlopen(url_u)		# just check wnd_u
				except urllib.error.HTTPError as e:
					# Return code error (e.g. 404, 501, ...)
					# ...
					print('HTTPError: {}'.format(e.code))
				else:			# use v1
					urllib.request.urlretrieve(url_u, filename = str(year) + '/wnd_ucmp/' + filename_u)
					urllib.request.urlretrieve(url_v, filename = str(year) + '/wnd_vcmp/' + filename_v)
					urllib.request.urlretrieve(url_g, filename = str(year) + '/geop_ht/' + filename_g)
					flag_u = 1
				
				if flag_u == 0:	# use v1.1
					urllib.request.urlretrieve(url_u_1, filename = str(year) + '/wnd_ucmp/' + filename_u)
					urllib.request.urlretrieve(url_v_1, filename = str(year) + '/wnd_vcmp/' + filename_v)
					urllib.request.urlretrieve(url_g_1, filename = str(year) + '/geop_ht/' + filename_g)
					print ('caught 404 error  ', filename_g)
					
					
				
				



