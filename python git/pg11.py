names=(input('enter the name'))
count=[x for  x in names.split()if  x.lower().startswith('a')]
print(len(count))
