import dns.resolver
import sys

#name = 'iana.org'
if len(sys.argv) != 2: 
    print (f"Correct usage: script, domain-name")
    exit() 

# takes the first argument from command prompt as IP address 
name = str(sys.argv[1]) 

for qtype in 'A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA':
    answer = dns.resolver.resolve(name,qtype, raise_on_no_answer=False)
    if answer.rrset is not None:
        print(answer.rrset)