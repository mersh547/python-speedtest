#Speedtest.py for calling Speedtest.com API
#and logging results for future reference and
#graphing

import speedtest
import csv
import datetime
import os, ssl

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
    with open('C:\Scripts\Speedtest\export.csv','a',newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([time, download, upload])    
        



if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context
		
time, download, upload = run_test()
write_results(time, download, upload)

print("Download: " + str(download))
print("Upload: " + str(upload))
