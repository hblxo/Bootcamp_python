
from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('resources/good.csv', header=True) as file:
        if file == None:
            print("File is corrupted")
        data = file.getdata()
        header = file.getheader()
        # print(data)


if __name__ == "__main__":
    with CsvReader('resources/bad.csv') as file:
        if file == None:
            print("File is corrupted")
