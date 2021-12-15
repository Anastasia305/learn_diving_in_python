# -*- coding: utf-8 -*-
import os
import tempfile

class File:
    def __init__(self, path_to_file):
        if os.path.exists(path_to_file):
            pass
        else:
            with open(f'{path_to_file}', 'w'):
                pass
        self.path_to_file = path_to_file
        self.current = 0

    def __str__(self):
        return self.path_to_file
    
    def __iter__(self):
        return self
    
    def __next__(self):
        with open(self.path_to_file, 'r', encoding='utf8') as file:
            file.seek(self.current)
            line = file.readline()

            if line:
                self.current = file.tell()
                return line
            else:
                self.current = 0
                raise StopIteration
    
    def __add__(self, obj):
        new_path_to_file = os.path.join(tempfile.gettempdir(), 'summary_file')
        text_from_added_file = obj.read()
        with open(self.path_to_file, 'r') as file:
            self.value = file.read()
        with open(new_path_to_file, 'w') as summary_file:
            summary_file.write(f'{self.value}' + f'{text_from_added_file}') 
        summary_file = File(new_path_to_file)
        return summary_file

    def read(self):
        with open(self.path_to_file, 'r') as file:
            text = file.read()
        return text
    
    def write(self, new_text):
        with open(self.path_to_file, 'w') as file:
            file.write(new_text)
        return(len(new_text))
            
if __name__ == "__maim__":    
    file_2 = File('file_2.txt')
    file_2.write('qwe')
    for line in file_2:
        print(ascii(line))    
