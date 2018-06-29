#imports for DataStax Cassandra driver and sys
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import SimpleStatement
import sys
import xlwt
from xlrd import open_workbook
from geopy import distance

cords_from = (19.14689,72.84343)
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Cass_mongo123')

# reading my hostname, username, and password from the command line; defining my Cassandra keyspace as as variable.
hostname='cass01.do-blr.mpgps.aspade.in' # ADD HOSTNAME OR IP HERE FOR CASSANDRA
username='mpdbadmin' # ADD USERNAME HERE OF CASSANDRA
password='nimdabdpm' # ADD PASSWORD HERE FOR CASSANDRA
keyspace="matchsitedb"
#adding my hostname to an array, setting up auth, and connecting to Cassandra
nodes = []
nodes.append(hostname)
auth_provider = PlainTextAuthProvider(username=username, password=password)
cluster = Cluster(nodes,auth_provider=auth_provider)
session = cluster.connect(keyspace)
#preparing and executing my INSERT statement
# serial_number = str(input("Enter Tracker number"))
file_path_load = raw_input('Enter the path name of file  ')
book = open_workbook(file_path_load)
sheet123 = book.sheet_by_index(0)

for w,row_index in enumerate(xrange(0,sheet123.nrows)):
	serial_no = sheet123.cell(row_index, 0).value
	print str(serial_no).replace('.0',''), "<<<<<<<<<<<<<<<<<<<<"
	strCQL = "select latitude,longitude,serial_number_id from tr_last_parked_by_serial_no where serial_number_id = '"+ str(serial_no).replace('.0','') +"' ;"
	pStatement = session.prepare(strCQL)
	f = session.execute(pStatement)
	for i in f:
		# print i[0], i[1], i[2],
		try:
			# sheet.write(0, v, i[0])
			# sheet.write(1, v, i[0])
			# sheet.write(2, v, i[0])
			distance_in_mtr = distance.distance(cords_from,(i[0],i[1])).m
			sheet.write(w,0,i[2])
			sheet.write(w,1, distance_in_mtr)
			# print distance_in_mtr, "OOOOOOOO"
			# sheet.write(3, v, distance_in_mtr)
			print "Distance of Tracker %s from Jogeshwari is %s meter"%(i[2],distance_in_mtr)
		except Exception as e:
			print e
		#for x in o:
		#print o
#

#for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
#print(x)
workbook.save('output12.xls')
print "<<<<<<<<<<<<<<<Closing>>>>>>>>>>>>>>"

#closing my connection
session.shutdown()
