import json


# with open("data/sample.txt", "r") as file:   #Use "with" Automatically closes file.
#     content = file.read()
#     print(content)

# with open("data/output.txt", "w") as file:
#     file.write("This is a sample text file created for demonstration purposes.")  #for writing to a file. "w" mode will overwrite existing content,   while "a" mode will append to the file instead of overwriting it.

def write_json(data, file_path):

    with open(file_path, "w") as file:

        json.dump(data, file, indent=4)

def read_json(file_path):

    with open(file_path, "r") as file:

        return json.load(file)