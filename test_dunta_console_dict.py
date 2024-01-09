#!/usr/bin/python3
from console import DuntaCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

# Initialize FileStorage
storage = FileStorage()
storage.reload()

# Create an instance of the DuntaCommand class
dunta_cmd = DuntaCommand()

# Create a new BaseModel instance
my_model = BaseModel()

# Set attributes for the BaseModel instance
my_model.name = "My_First_Model"
my_model.my_number = 89

# Print the ID of the BaseModel instance
print(my_model.id)

# Print string representation of the BaseModel instance
print(my_model)

# Print the type of created_at attribute
print(type(my_model.created_at))

print("--")

# Convert the BaseModel instance to a dictionary
my_model_json = my_model.to_dict()

# Print the JSON representation of the BaseModel instance
print(my_model_json)

print("JSON of my_model:")
# Print each key-value pair in the JSON representation
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")

# Create a new BaseModel instance using the dictionary
my_new_model = BaseModel(**my_model_json)

# Print the ID of the new BaseModel instance
print(my_new_model.id)

# Print string representation of the new BaseModel instance
print(my_new_model)

# Print the type of created_at attribute of the new instance
print(type(my_new_model.created_at))

print("--")

# Check if the two instances are the same
print(my_model is my_new_model)
