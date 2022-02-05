import re

f = open("hcn.txt",'r')

text = f.readlines()

f.close()

k1 = re.compile(r"explain")
k2 = re.compile(r"^\d{2}-[a-zA-Z]{3}-\d{4}$")
k3 = re.compile(r"^[6-9[0-9]{9}")
k4 = re.compile(r"^.{8,}$")
print("Line containing word explain")
for line in text:
    if k1.search(line):
       print(line)
print("Line containing date")
for line in text:
    if k2.search(line):
       print(line)
print("Line containing phone no")
for line in text:
    if k3.search(line):
       print(line)
print("Line containing words having characters greater than 8")
for line in text:
    if k4.search(line):
       print(line)
    
       
    
       
