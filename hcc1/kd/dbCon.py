from pymongo import MongoClient
con=MongoClient('mongodb://localhost:27017/')
db=con['Conn']
col=db['data']
