import csv

products=[(1,"mobile",25000,10),(2,"laptop",35000,1),(3,"pen",25,10)]
csvfile = open("data.csv","w",newline="")
obj = csv.writer(csvfile)
for item in products:
    obj.writerow(item) #writes a data row by row
csvfile.close()


 
csvfile = open("data1.csv","w",newline="")
obj = csv.writer(csvfile)
obj.writerows(products) #writes collection 
csvfile.close()

csvfile = open("data.csv",newline="")
obj=csv.reader(csvfile)
for row in obj:
    print(row)
csvfile.close()
