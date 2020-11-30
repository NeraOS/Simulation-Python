def py(file):
    exec('import '+str(file))
def check(x):
    if x =='help':
        print("""Список комманд:
help - справка по коммандам
explorer - открыть проводник
py(<имя файла>) - выполнение python кода
""")
    elif x =='explorer':
        import explorer
    else:
        try:
            print(eval(x))
        except Exception:
            try:
                eval(x)
            except Exception:
                print('Ошибки:\n',Exception)
def normal():
    x = str(input('))'))
    check(x)
def protected():
    x = str(input('))'))
    check(x)
print("""NeraOS
Для получения справки введите help
""")
f = open('config.ini','r')#считываем данные
mode = f.read()
status = True
if mode == 1:
    while status == True:
        normal() #Стандартный режим
else:
    while status == True:
        protected()#Безопасный режим
