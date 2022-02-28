import csv
import numpy as np
import datetime as dt
products=["drive","forsage","extrime","1+1","family","one+12","all-world","no-limit","wild","auto-car"]
categories=["web","phone"]
types=["tariff","add-on"]
recurrent=["regular","once"]
with open("D:\\new\\product.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",")
    file_writer.writerow(["id","имя", "категория", "тип","оплата",
    "цена-звонок", "цена-смс","цена-интернет", "кол-звонок", "кол-смс", "кол-интернет"])
    for i in range(np.random.randint(1,10, size=1)[0]):
        mas=["","", "", "","","","","","","",""]
        mas[0]=i

        product=np.random.randint(0,len(products), size=1)[0]
        mas[1]=product
        
        if products[product]=="1+1" or products[product]=="family" or products[product]=="one+12":
            mas[2]=categories[0]
        else:
            mas[2]=categories[1]
        if products[product]=="drive" or products[product]=="forsage" or products[product]=="extrime":
            mas[3]=types[1]
        else:
            mas[3]=types[0]
        if products[product]=="forsage" or products[product]=="extrime":
            mas[4]=recurrent[1]
        else:
            mas[4]=recurrent[0]
        if mas[2]=="web":
            mas[5]="null"
            mas[6]="null"
            if mas[3]=="add-on":
                mas[7]=np.random.randint(200,300, size=1)[0]
            else:
                mas[7]=np.random.randint(400,500, size=1)[0]
            mas[8]="null"
            mas[9]="null"
            mas[10]=np.random.randint(20,40, size=1)[0]
        else:
            if mas[3]=="add-on":
                mas[5]=np.random.randint(10,20, size=1)[0]
                mas[6]=np.random.randint(0,20-mas[5]+1, size=1)[0]
            else:
                mas[5]=np.random.randint(40,50, size=1)[0]
                mas[5]=np.random.randint(10,20, size=1)[0]
            mas[7]="null"
            mas[8]=np.random.randint(20,40, size=1)[0]
            mas[9]=np.random.randint(10,40, size=1)[0]
            mas[10]=np.random.randint(10,20, size=1)[0]

        products.remove(products[product])

        file_writer.writerow(mas)
