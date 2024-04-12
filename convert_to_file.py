class Convert:
    def save_response_to_file(cls, response_bytes, file_path):
        with open(file_path, 'wb') as file:
            file.write(response_bytes)
