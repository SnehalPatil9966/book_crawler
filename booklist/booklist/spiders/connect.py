from pymongo import MongoClient
 
# Connect to the local MongoDB instance
client = MongoClient('localhost', 27017)
 
# Create a new database
db = client['sample_database']
 
# Create a new collection
collection = db['sample_collection']
 
# Sample data to be inserted
sample_data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]
 
# Insert the sample data into the collection
collection.insert_many(sample_data)
 
print("Sample data inserted successfully!")