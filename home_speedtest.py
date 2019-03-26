#Speedtest.py for calling Speedtest.com API
#and logging results for future reference and
#graphing

import speedtest
import csv
import datetime

def get_timestamp():
	time = datetime.datetime.now()
	print(time)
	return time
	
def run_test():
	time = get_timestamp()
	s = speedtest.Speedtest()
	s.get_best_server()
	download = '%.2f'%(s.download() / 1000000)
	upload = '%.2f'%(s.upload() / 1000000)
	return time, download, upload;
	
def write_results(time, download, upload):
	with open('file.csv','a',newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([time, download, upload])	
		


time, download, upload = run_test()
write_results(time, download, upload)

print("Download: " + str(download))
print("Upload: " + str(upload))


	
