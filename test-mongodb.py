from pymongo import MongoClient
client = MongoClient("mongodb+srv://chatbot_user:4kNWZXmTx6ZFxcSm@chatbotcluster.jgtommw.mongodb.net/?retryWrites=true&w=majority&appName=ChatbotCluster")
db = client["chatbot"]
db["test"].insert_one({"test": "connection successful"})
print(db["test"].find_one())