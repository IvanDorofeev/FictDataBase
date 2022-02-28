import csv
import numpy as np
import datetime as dt
products=[]
instancesActiv=[]
instancesTerm=[]
types=["calls","sms"]
direction=["исход","вход"]
roaming=["yes","no"]
custCall=[i for i in range(100)]
custCalled=[i for i in range(100)]
with open("D:\\new\\event.csv", mode="w", encoding='utf-8') as w_file:
    with open("D:\\new\\instance.csv", encoding='utf-8') as r1_file:
        with open("D:\\new\\product.csv", encoding='utf-8') as r2_file:
            file_writer = csv.writer(w_file, delimiter = ",")
            file_reader1 = csv.reader(r1_file, delimiter = ",")
            file_reader2 = csv.reader(r2_file, delimiter = ",")
            file_writer.writerow(["id","id-instance", "дата", "цена","длительность",
            "кол-смс", "всего","тип","direct", "роуминг","from", "to"])
            inDate=[]
            teDate=[]
            curProduct=[]

            for row in file_reader1:
                inDate=row[3].split("/")
                teDate=row[4].split("/")
                curProduct.append(row[2])
                instancesActiv.append(int(newDate[0]))
                instancesActiv.append(int(newDate[1]))
                instancesActiv.append(int(newDate[2]))
                instancesTerm.append(int(teDate[0]))
                instancesTerm.append(int(teDate[1]))
                instancesTerm.append(int(teDate[2]))

            for row in file_reader2:
                products.append(row[1])
                products.append(row[5])
                products.append(row[6])
                products.append(row[7])

            for i in range(np.random.randint(5,20, size=1)[0]):
                mas=["","", "", "","","","", "", "","","",""]

                rand2=np.random.randint(0,2, size=2)
                rand100=np.random.randint(1,100, size=2)[0]
                mas[0]=i

                mas[1]=np.random.randint(0,10, size=1)[0]

                activDate=dt.date(np.random.randint(instancesActiv[mas[1]*3],instancesTerm[mas[1]*3]+1, size=1)[0],
                                np.random.randint(instancesActiv[mas[1]*3+1],13, size=1)[0],
                                np.random.randint(instancesActiv[mas[1]*3+2],29, size=1)[0])
                mas[2]=activDate.strftime("%Y/%m/%d")

                if products[products.index(curProduct[mas[1]])+1]=="null":
                    mas[7]="web"
                    duration=np.random.randint(1,10, size=1)[0]/100
                    mas[3]=duration*products[products.index(curProduct[mas[1]])+3]
                    mas[4]="null"
                    mas[5]="null"
                    mas[6]=duration
                else:
                    mas[7]=types[int(np.random.randint(1,10, size=1)[0]/8)]
                    if mas[7]=="call":
                        mas[3]=(np.random.randint(1,10, size=1)[0]/100)*products[products.index(curProduct[mas[1]])+1]
                        mas[4]=np.random.randint(1,3600, size=1)[0]
                        mas[5]="null"
                        mas[6]=mas[4]
                    else:
                        mas[3]=(np.random.randint(1,30, size=1)[0])*products[products.index(curProduct[mas[1]])+2]
                        mas[4]="null"
                        mas[5]=np.random.randint(1,7, size=1)[0]
                        mas[6]=mas[5]
                
                products.remove(products[product])
                mas[8]=direction[rand2[0]]
                mas[9]=roaming[rand2[1]]
                mas[10]=custCall[rand100[0]]
                mas[11]=custCall[rand100[1]]
                if rand100[0]==rand100[1]:
                    mas[11]=custCall[rand100[1]+1]
                file_writer.writerow(mas)
