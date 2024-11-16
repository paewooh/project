# main.py

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":    
    content1 = read_file('file1.txt')
    content2 = read_file('file2.txt')
    
    print(f"Содержимое файла 1: {content1}")
    print(f"Содержимое файла 2: {content2}")