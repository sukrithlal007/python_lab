import csv
with open('83hc.txt') as inf:
 content = csv.reader(inf, delimiter=',')

 line_count = 0

 for row in content:

   if line_count == 0:

     print(f'Column names are {", ".join(row)}')

     line_count += 1

   else:

     print(f'\t{row[0]} ,{row[1]},{row[2]},{row[3]}.')
     line_count += 1
