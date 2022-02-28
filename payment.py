import csv
import numpy as np
import datetime as dt
customers=[]
distChanel=["web","phyzi"]
with open("D:\\new\\payment.csv", mode="w", encoding='utf-8') as w_file:
    with open("D:\\new\\customer.csv", encoding='utf-8') as r_file:
        file_writer = csv.writer(w_file, delimiter = ",")
        file_writer.writerow(["id","id-customer", "метод", "дата","количество"])
        file_reader = csv.reader(r_file, delimiter = ",")
        for row in file_reader:
            customers.append(row[3].split("/"))
            customers.append(row[11].split("/"))
        for i in range(np.random.randint(1,10, size=1)[0]):
            mas=["","", "", "",""]

            mas[0]=i
            mas[1]=np.random.randint(0,100, size=1)[0]

            activDate=dt.date(np.random.randint(int(customers[mas[1]*2][0]),int(customers[mas[1]*2+1][0]), size=1)[0],
                            np.random.randint(int(customers[mas[1]*2][1]),int(customers[mas[1]*2+1][1]), size=1)[0],
                            np.random.randint(int(customers[mas[1]][2]),int(customers[mas[1]+1][2]), size=1)[0])

            mas[2]=distChanel[np.random.randint(0,2, size=1)[0]]
            mas[3]=activDate.strftime("%Y/%m/%d")
            mas[4]=np.random.randint(100,400, size=1)[0]
            file_writer.writerow(mas)
