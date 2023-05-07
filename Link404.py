import requests #Send get or post request to the server
import subprocess # Execute system commands
import os


def scan_links(domainName):
 subprocess.call(f"python3 photon.py -u http://{domainName} -l 3",shell=True)
 os.chdir(domainName)
 try:
  with open("external.txt","r") as data:
   links = data.read().split()
 except:
  print("File not found")
  return None
 return links

def broken(list):
 for url in list:
  status_code = requests.get(url).status_code
  if status_code == 404:
   print(f"[+] Link: {url} is vulnerable")
  else:
   pass

a = scan_links(input("Enter a domain name: "))
b = broken(a)
