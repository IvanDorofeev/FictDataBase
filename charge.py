import csv
import numpy as np
import datetime as dt
status=["yes","no"]
products=[]
instances=[]
distChanel=["web","phyzi"]
with open("D:\\new\\charge.csv", mode="w", encoding='utf-8') as w_file:
    with open("D:\\new\\instance.csv", encoding='utf-8') as r_file:
        with open("D:\\new\\product.csv", encoding='utf-8') as r2_file:
            file_writer = csv.writer(w_file, delimiter = ",")
            file_writer.writerow(["id","id-instance", "id-product", "count","дата",
            "цена", "тип"])
            file_reader = csv.reader(r_file, delimiter = ",")
            file_reader2 = csv.reader(r2_file, delimiter = ",")
            curproducts=[]
            for row in file_reader:
                instances.append(row[3].split("/"))
                instances.append(row[4].split("/"))
                curproducts.append(row[2])

            for row in file_reader2:
                    products.append(row[1])
                    products.append(row[5])
                    products.append(row[6])
                    products.append(row[7])

            for i in range(np.random.randint(1,10, size=1)[0]):
                mas=["","", "", "","","",""]

                mas[0]=i
                mas[1]=np.random.randint(0,10, size=1)[0]

                activDate=dt.date(np.random.randint(int(instances[mas[1]*2][0]),int(instances[mas[1]*2+1][0]), size=1)[0],
                                np.random.randint(int(instances[mas[1]*2][1]),int(instances[mas[1]*2+1][1]), size=1)[0],
                                np.random.randint(int(instances[mas[1]][2]),int(instances[mas[1]+1][2]), size=1)[0])

                mas[3]=activDate.strftime("%Y/%m/%d")
                if products[mas[1]*4]!="forsage" and products[mas[1]*4]!="extrime":
                    if products[mas[1]*4+1]!="null":
                        mas[4]=str(5*int(products[mas[1]*4+2])+5*int(products[mas[1]*4+1]))
                    else:
                        mas[4]=products[mas[1]*4+3]
                else:
                    mas[4]="ok"
                if curproducts[mas[1]]=="forsage" or curproducts[mas[1]]=="extrime":
                    mas[5]="once"
                    mas[2]="0"
                else:
                    mas[5]="charge"
                    mas[2]="1"
                file_writer.writerow(mas)
