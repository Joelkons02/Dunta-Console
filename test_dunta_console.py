#!/usr/bin/python3
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
my_model.name = "My First Model"
my_model.my_number = 89

# Print string representation of the BaseModel instance
print(my_model)

# Save the BaseModel instance to the file storage
storage.new(my_model)
storage.save()

# Print string representation of the BaseModel instance after saving
print(my_model)

# Convert the BaseModel instance to a dictionary
my_model_json = my_model.to_dict()

# Print the JSON representation of the BaseModel instance
print(my_model_json)

print("JSON of my_model:")
# Print each key-value pair in the JSON representation
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
