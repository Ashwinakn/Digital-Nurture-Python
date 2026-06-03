def read_file():
        file = open("file.txt","r")
        content= file.read()
        print("Content inside file.txt:",content)
        file.close()
read_file()
