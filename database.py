import pymongo
mydb=pymongo.MongoClient("mongo://localhost:27017")
mytb=mydb["sdb"]
mycol1=mytb["details"]
mydict1={'reg':1,"name":"nikitha"}
x=mycol1.insert_one(mydict1)