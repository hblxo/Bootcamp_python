# # Python program showing
# # file management using
# # context manager

# class FileManager():
# 	def __init__(self, filename, mode):
# 		self.filename = filename
# 		self.mode = mode
# 		self.file = None

# 	def __enter__(self):
# 		self.file = open(self.filename, self.mode)
# 		return self.file

# 	def __exit__(self, exc_type, exc_value, exc_traceback):
# 		self.file.close()

# # loading a file
# with FileManager('test.txt', 'w') as f:
# 	f.write('Test')

# print(f.closed)

# It's the context manager that will help you handle this task.

# Implement a CsvReader class that opens, reads, and parses a csv file. In order to create a context manager the class will need a few built-in methods: __init__, __enter__ and __exit__. It's mandatory to close the file at the end of the procedure.


class CsvReader():
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.sep = sep
        self.header = None
        self.headerFlag = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.filename = filename
        self.file = None
        self.data = []
        # print('------ Enter init method ------')

    def __enter__(self):
        # print('------ Enter enter method ------')
        try:
            self.file = open(self.filename)
            if self.headerFlag:
                self.header = self.file.readline().split(self.sep)
                self.skip_top += 1
            with open(self.filename) as my_file:
                lines_count = (sum(1 for _ in my_file))
            row = 0
            for i in range(self.skip_top, lines_count - self.skip_bottom):
                line = list(
                    filter(None, self.file.readline().strip().split(self.sep)))
                if row == 0:
                    row = len(line)
                assert row == len(line)
                self.data.append(line)
        except (OSError, IOError) as e:
            print(e)
        except:
            print("ERROR")
            return None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('------ Enter exit method ------')
        self.file.close()

    def getdata(self):
        # print('------ Enter getdata method ------')
        return self.data

    def getheader(self):
        # print('------ Enter getheader method ------')
        return self.header
# Usually the separator in csv files is the ,, but we want to be able to change this parameter. You can also tell the class to skip lines at the top and the bottom, and also to keep the first line as a header if header is True.

# The file shouldn't be corrupted (line with too many elements), if it's corrupted return None. You have to handle the case file not found.

# You will have to also implement 2 methods: getdata() and getheader()
