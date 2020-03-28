import pymysql
import hashlib
import random
import time

banderaFirma = 1 

#Valores simulados
latitud = "19.721830"
longitud = "-101.185828"
valor = 24 

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='datos'
        )

        self.cursor = self.connection.cursor()
        print("Conexion exitosa")
    
    
    def firmaDigital(self):
        caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"
        cadena = ""

        for ciclo in range(1,20):
            cadena = cadena + random.choice(caracteres)
    
        sql="insert into clima (id,firma,utc,variable) values ('temperatura_01','{}','-6','temperatura')".format(cadena)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as b:
            print(b)
 
        print("firma creada con exito: "+cadena)    

    def updateData(self, lat, lon, val):
        hora=str(time.strftime("%H:%M:%S"))
        fecha=str(time.strftime("%d/%m/%y"))

        sql ="update clima set latitud='{}', longitud='{}', fecha='{}', hora='{}', valor={}  where id ='temperatura_01'".format(lat,lon,fecha,hora,val)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("actualizando datos")
        except Exception as b:
            print(b)

    def bandera(self):
        sql ='select * from clima'

        try:
            self.cursor.execute(sql)
            ban = self.cursor.fetchone()
            

            if ban[0] == 'temperatura_01':
                global banderaFirma
                banderaFirma = 0
               # print('ban = 0')
            else:
                banderaFirma = 0
                #print('ban = 1')
        except Exception as i:
            pass
    

dataBase = DataBase()  
dataBase.bandera()
while True:

    if banderaFirma == 1:
        dataBase.firmaDigital()
        banderaFirma = 0
    else:
        dataBase.updateData(latitud,longitud,valor)
    time.sleep(10)
