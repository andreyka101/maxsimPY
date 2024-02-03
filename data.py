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
# file = open("B:/del.txt",'w')
# file.write("00000")
# file.close()
# rd = open("B:/del.txt","r").read()
# print(rd)


# урок 3 ----------------

# with - закроет файл автоматически при завершении блока
# with open("B:/del.txt",'w') as file:
#     file.write(input())

# rd = open("B:/del.txt","r").read()
# print(rd)


# with - также его можно использовать для чтения файла
# with open("B:/del.txt",'r') as file:
#     fileRead = file.read()
# метод .rstrip() убирает в конце строки пробелы
#     print(fileRead.rstrip())


with open("B:/del.txt",'r') as file:
    # метод .readlines() каждую строку txt файла превращает в элемент массива
    # он возвращает массив
    fileRead = file.readlines()
    print(fileRead)
    checkForIndentation = True
    fileARR = []
    for i in fileRead:
        if (i == '  ' or i == "\n"):
            checkForIndentation = False
        if(checkForIndentation):
            fileARR.append(i)
    print(fileARR)


# домашнее задание урока 3
# номер 1
# создайте менеджер пользователей
# . программа должна работать до тех пор пока не не будет введено exit или ex
# . если ввести new - создаётся новый пользователь он должен хранить имя и пароль (если ввести существующие имя то программа просит его изменить)
# . если ввести del - удаляется пользователь его имя и пароль
# все пользователи должны сохраняются на txt файл
