filename = 'x.txt'
file = open(filename, mode='r') # 'r' is to read
text = file.read()
print(text)
file.close()