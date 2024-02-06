# Python program to calculate RTT

import time
import requests

# Function to calculate the RTT
def RTT(url):

	# time when the signal is sent
	t1 = time.time()

	r = requests.get(url)

	# time when acknowledgement of signal 
	# is received
	t2 = time.time()

	# total time taken
	tim = str(t2-t1)

	print("Time in seconds :" + tim)

import dns.resolver 
def resolveDNS(domain): 
	
	return dns.resolver.Resolver.resolve(domain , "A") 
    

# driver program 
# url address
while True:
  url = input("\nEnter UR: ")
  #url = "http://www.google.com"
  print("the IP address of {} is {}".format(url,resolveDNS(url.strip())))
  if url.upper() == "NONE":
  	break;
  RTT(url)
