from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url infromation 
uri="mongodb+srv://jayant:12345@cluster0.i1cl5jk.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connect to server
client= MongoClient(uri)

#create a database name and collection name 
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

df=pd.read_csv("C:\Users\91941\Downloads\sensorproject\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)
json_record=list(json.loads(df.T.to_json()).values())
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)