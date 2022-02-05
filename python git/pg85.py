import csv

with open('temp.csv', mode='w') as outf:

 fieldnames = ['Name', 'Department', 'Birthday Month']

 content = csv.DictWriter(outf, fieldnames=fieldnames)

 content.writeheader()

 content.writerow({'Name': 'John', 'Department': 'Accounting', 'Birthday Month': 'November'})

 content.writerow({'Name': 'Amy', 'Department': 'IT', 'Birthday Month': 'March'})
data = csv.DictReader(open("temp.csv"))
print("CSV file as a dictionary:\n")
for row in data:
   print(row)
