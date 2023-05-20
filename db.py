from pymongo import MongoClient
from pymongo.errors import WriteError
from datetime import datetime


def add_user(username, password):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')

    # Specify the database and collection
    db = client['chatbot']
    collection = db['chat']
    
    # Check if the username already exists
    existing_user = collection.find_one({"username": username})

    success = False
    error = None

    if existing_user:
        error = "Username already exists"
    else:
        # Get the current time
        current_time = datetime.now()

        # Create the document to be inserted
        user_data = {
            "username": username,
            "password": password,
            "timestamp": current_time
        }

        try:
            # Insert the data
            result = collection.insert_one(user_data)
            # Check if the insertion was successful
            if result.acknowledged:
                success = True
                error = f"Insertion successful, document ID: {result.inserted_id}"
            else:
                error = "Insertion failed"

        except WriteError as e:
            error = f"Insertion failed:{e}"

    # Close the MongoDB connection
    client.close()

    return success, error


def check_credentials(username, password):
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        
        # Specify the database and collection
        db = client['chatbot']
        collection = db['chat']
        
        # Query the user document
        user = collection.find_one({"username": username, "password": password})
        
        # Close the MongoDB connection
        client.close()
        
        return user
    except: 
        print("access mongo db failed")
        return None


def add_chat_record(question, answer, username):
    success = False
    msg = ""
    
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        
        # Specify the database and collection
        db = client['chatbot']
        collection = db['chat']
        
        # Check if the username exists
        existing_user = collection.find_one({"username": username})
        if existing_user is None:
            msg = "Username does not exist"
            return success, msg
        
        # Get the current timestamp
        timestamp = datetime.now()
        
        # Prepare the data to be inserted
        chat_data = {
            "question": question,
            "answer": answer,
            "timestamp": timestamp,
            "username": username
        }
        
        # Insert the data
        insert_result = collection.insert_one(chat_data)
        
        if insert_result.acknowledged:
            success = True
            msg = "Record inserted successfully, document ID: " + str(insert_result.inserted_id)
        else:
            msg = "Record insertion failed"
        
        # Close the MongoDB connection
        client.close()
    
    except Exception as e:
        msg = "Record insertion failed: " + str(e)
    
    return success, msg

def get_user_chat_records(username):
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')

        # Specify the database and collection
        db = client['chatbot']
        collection = db['chat']

        # Query the chat records for the specified user and sort by time in ascending order
        chat_records = collection.find({"username": username}).sort("timestamp", 1)

        # Return the chat records
        records = list(chat_records)

        # Close the MongoDB connection
        client.close()

        return records

    except Exception as e:
        print("Error retrieving chat records:", str(e))
        return []


if __name__ == '__main__':
    success, error = add_user("sillylord", "12345")
    print(success, error)

    user = check_credentials("sillylord", "12345")
    print(user)

    # success, msg = add_chat_record("nihao2",  "hi", "sillylord")
    # print(success, msg)

    chat_records = get_user_chat_records("sillylord")
    if chat_records:
        for record in chat_records:
            print(record)
