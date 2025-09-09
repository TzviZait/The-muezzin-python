#
#
#
#
# from pymongo import MongoClient
# from gridfs import GridFSBucket
# from bson.objectid import ObjectId # Import ObjectId for querying by _id
#
# # Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['audio_database']
#
# # Create a GridFS bucket
# fs_bucket = GridFSBucket(db)
#
# # Retrieve the audio file (replace with the actual file_id or filename)
# # Option 1: Retrieve by _id
# # file_id_to_retrieve = ObjectId('your_uploaded_file_id')
# # download_stream = fs_bucket.open_download_stream(file_id_to_retrieve)
#
# # Option 2: Retrieve by filename
# filename_to_retrieve = 'download (1).wav 2454330'
# download_stream = fs_bucket.open_download_stream_by_name(filename_to_retrieve)
#
# # Save the retrieved audio to a local file
# output_file_path = 'retrieved_audio.mp3'
# with open(output_file_path, 'wb') as f:
#     f.write(download_stream.read())
#     print(f"Audio file downloaded to: {output_file_path}")
#
# client.close()

from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('mongodb://localhost:27017/')
db = client.your_database_name
collection = db.your_collection_name

# Find documents
cursor = collection.find({})

# Convert BSON documents to JSON string
json_data = dumps(cursor, indent=2)

print(json_data)