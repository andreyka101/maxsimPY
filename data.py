# метод open(файл , режим) используется для открытия файлов
# метод read() считывает содержимое файла в строку (используется для чтения)
dataRead = open("file.txt","r").read()
# "w" режим для записи все режимы ниже
dataWrite = open("file.txt","w")
sTr = ""
for i in dataRead:
    if (i=="5"):
        i = "0"
    sTr += i


# метод write() используется для перезаписи файла
dataWrite.write(sTr)
# метод close() закрывает файл (этот метод нельзя вызывать если файл открыт в режиме чтения - "r")
dataWrite.close()






# Режим	Обозначение
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись



# урок 2 ----------------

# read = open("C:/Games/sel.txt",'r').read()
# print(read)



