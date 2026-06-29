def load_text_document(path):

    with open(path, "r") as file:
        return file.read()