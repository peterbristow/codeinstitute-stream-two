import pymongo
def mongo_connect():
   try:
       conn = pymongo.MongoClient()
       print "Mongo is connected!"
       return conn
   except pymongo.errors.ConnectionFailure, e:
       print "Could not connect to MongoDB: %s" % e

conn = mongo_connect()
db = conn['twitter_stream']
print db  # Database(MongoClient('localhost', 27017), u'twitter_stream')