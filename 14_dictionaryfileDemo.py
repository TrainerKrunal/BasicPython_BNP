import csv
employees=[{"name":"john","dept":"hr","salary":500000},
           {"name":"krunal","dept":"hr","salary":600000},
           {"name":"sanjay","dept":"hr","salary":700000}]


fields = list(employees[0].keys())
csvfile = open("empdata.csv","w",newline="")
obj = csv.DictWriter(csvfile,fieldnames=fields)
obj.writeheader()
obj.writerows(employees)
csvfile.close()

csvfile = open("empdata.csv","r",newline="")
obj = csv.DictReader(csvfile)
for field in obj.fieldnames:
    print(field,end="\t")
print()
for item in obj:
    print("\t".join(item.values()))
csvfile.close()
