import csv
import numpy as np
import datetime as dt
firstName=["Антенор","Бенжамин","Джованни","Лусиан","Карлос","Матеус",
   "Иван","Алексей","Андрей","Виктор"]
lastName=["Алварис","Гарсия","Фернандес","Родригес","Гонсалес","Менандес",
   "Силва","Донских","Кузнецов","Санчес"]
gender=["ж","м"]
agreeForPromo=["yes","no"]
autopayCard=["yes","no"]
email=["gmail.com","yandex.ru"]
status=["yes","no"]
category=["Business","physical"]
city=["Sao-Paulo","Rio","Brasilia","Salvador","Fortalesa"]
language=["portuguese","russian"]
with open("D:\\new.first.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",")
    file_writer.writerow(["id","имя", "фамилия", "дата рождения","пол",
                          "промо-согласие","карта", "email","телефон",
                          "статус", "категория","since","место рождения", "язык",
                          "окончание"])
    for i in range(100):
        mas=["","", "", "","","","", "","","", "","", "","",""]
        rand10=np.random.randint(0,10, size=12)
        rand2=np.random.randint(0,2, size=6)
        rand65=np.random.randint(65,98, size=np.random.randint(3,10, size=1)[0])
        oldDate=dt.date(np.random.randint(1900,2008, size=1)[0],
                        np.random.randint(1,12, size=1)[0],
                        np.random.randint(1,29, size=1)[0])
        curYear=oldDate.year
        if curYear>=1980:
            newDate=dt.date(np.random.randint(curYear+10,2019, size=1)[0],
                        np.random.randint(1,12, size=1)[0],
                        np.random.randint(1,29, size=1)[0])
        else:
            newDate=dt.date(np.random.randint(1990,2019, size=1)[0],
                        np.random.randint(1,12, size=1)[0],
                        np.random.randint(1,29, size=1)[0])
        termDate=dt.date(np.random.randint(newDate.year+1,2022, size=1)[0],
                         np.random.randint(1,12, size=1)[0],
                         np.random.randint(1,29, size=1)[0])
        mas[0]=i
        mas[1]=firstName[rand10[0]]
        mas[2]=firstName[rand10[1]]
        mas[3]=oldDate.strftime("%Y/%m/%d")
        mas[4]=gender[rand2[0]]
        mas[5]=agreeForPromo[rand2[1]]
        mas[6]=autopayCard[rand2[2]]
        for j in rand65:
            mas[7]+=str(j)
        mas[7]+="@"+email[rand2[3]]
        mas[8]+="8-9"+str(rand10[2])+str(rand10[3])+"-"+str(rand10[4])+str(rand10[5])+str(rand10[6])+"-"
        str(rand10[7])+str(rand10[8])+"-"+str(rand10[9])+str(rand10[10])
        mas[9]=status[rand2[4]]
        mas[10]=category[rand2[5]]
        mas[11]=newDate.strftime("%Y/%m/%d")
        index=np.random.randint(1,12, size=1)[0]
        if index==0:
            mas[12]=city[4]
        elif index==1 or index==2:
            mas[12]=city[3]
        elif index>=3 or index<=5:
            mas[12]=city[2]
        elif index>=6 or index<=9:
            mas[12]=city[1]
        else:
            mas[12]=city[0]
        mas[13]=language[int(rand10[11]/9)]
        mas[14]=termDate.strftime("%Y/%m/%d")
        file_writer.writerow(mas)
