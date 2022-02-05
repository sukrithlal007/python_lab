import csv
with open('83hc.txt') as inf:
 content = csv.DictReader(inf)

 print("playername")

 for row in content:
   print(row["PlayerName"])
    
