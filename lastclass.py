import requests
import json

# pip install requests
# pip install mysql-connector-python

def request_data(page_num):
    url = "https://app-vava-dtc-search-tr-prod.azurewebsites.net/search"

    body= {
        "pageNum": 1,
        "pageSize": 20,
        "filters": {
            "transmission": [],
            "fuelType": [],
            "driveType": [],
            "bodyType": [],
            "doorCount": [],
            "seatingCapacity": [],
            "carFeaturesCodes": [],
            "color": [],
            "locationCity": [],
            "tags": [],
            "hideBooked": True,
            "anyBooked": False
        }
    }

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.request("POST", url, data=json.dumps(body), headers=headers)
        data=json.loads(response.text)
        return data['items']
    except:
        print("algo ha fallado")
        return[]

#CLASE COCHE
class Coche():
    def __init__(self, vehicle):
            self.matricula= vehicle['plateNumber'].upper()
            self.make= vehicle['make'].upper()
            self.model= vehicle['model'].upper()
            self.trim= vehicle['trimLevel'].upper()
            self.price= float(vehicle['price'])
            self.km = int(vehicle.get("mileage", -100))
            self.year= int(vehicle['year'])

#CONEXION CON MYSQL
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="webdev"
)
mycursor=mydb.cursor()

#mycursor.execute("SELECT count (distinct matricula), avg(price) FROM Coches")
#result= mycursor.fetchall()
#print(result)

try:
    mycursor.execute ("""
        CREATE TABLE Coches (
            matricula VARCHAR(50),
            make VARCHAR(50),
            model VARCHAR(200),
            price INT,
            km INT,
            year INT
        )
    """)
    mydb.commit()
except:
    print("La tabla ya existe")


def insert_to_db(coche):
    mycursor.execute(f"""
        INSERT INTO Coches (matricuña, make, model, trim, price, km, year)
        VALUES('{coche.matricula}', '{coche.make}', '{coche.model}', '{coche.trim}', '{coche.price}', '{coche.km}', '{coche.year}')
    """)
    mydb.commit()

page=1
vehicles= request_data(1)

while len(vehicles)>0:
    print(page, len(vehicles))
    for vehicle_data in vehicles:
        coche= Coche(vehicle_data)
        #print(coche.matricula)
        insert_to_db(coche)

    page += 1
    vehicles = request_data(2)

