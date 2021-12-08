class FileReader:
    
    def __init__(self, file_name):
         self.file = file_name
         
    def read(self):
        try:
            with open(self.file, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            text = " "
        return text


def main():
    reader = FileReader("some_file.txt")
    text = reader.read()
    print(text)


if __name__ == "__main__":
    main()