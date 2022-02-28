import csv
import numpy as np
import datetime as dt
status=["yes","no"]
products=["drive","forsage","extrime","1+1","all-world","one+12","no-limit","wild","auto","family"]
customers=[i for i in range(100)]
distChanel=["web","phyzi"]
with open("D:\\new.instance.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",")
    file_writer.writerow(["id","id-customer", "id-product", "since","окончание",
    "статус", "канал распр"])
    for i in range(np.random.randint(1,10, size=1)[0]):
        mas=["","", "", "","","",""]
        rand2=np.random.randint(0,2, size=2)
        activDate=dt.date(np.random.randint(1990,2019, size=1)[0],
                        np.random.randint(1,12, size=1)[0],
                        np.random.randint(1,29, size=1)[0])
        termDate=dt.date(np.random.randint(activDate.year+1,2019, size=1)[0],
                        np.random.randint(1,12, size=1)[0],
                        np.random.randint(1,29, size=1)[0])
        mas[0]=i

        customer=np.random.randint(0,len(customers), size=1)[0]
        mas[1]=customer
        customers.remove(customers[customer])

        product=np.random.randint(0,len(products), size=1)[0]
        mas[2]=product
        products.remove(products[product])
        
        mas[3]=activDate.strftime("%Y/%m/%d")
        mas[4]=termDate.strftime("%Y/%m/%d")
        mas[5]=status[rand2[0]]
        mas[6]=distChanel[rand2[1]]
        file_writer.writerow(mas)