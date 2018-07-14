# importing module
from pymongo import MongoClient

# creation of MongoClient
client = MongoClient()

# Connect with the portnumber and host
client = MongoClient('localhost', 27017)

# Access database
mydatabase = client['mydb']

# Access collection of the database
mycollection = mydatabase['customers']

# dictionary to be added in the database
rec = {
    'first_name':'Allu_Vidyasagar',
    'last_name':'Allu',
}

# inserting the data in the database
recd = mydatabase.mycollection.insert_one(rec)
print(recd)

for i in mydatabase.mycollection.find():
    print(i)