#в примере рассматривается поле 78*52 !!!!!!!!!



#вот соотношение белых пикселей цифры (рассматривается как картинка) к чёрным (её фону)
'''
всего пикселей - 3600
0 - 1279 пикселей (35,52%) #595959
1 - 685  пикселей (19,02%) #303030
2 - 1047 пикселей (29,08%) #4a4a4a
3 - 1036 пикселей (28,77%) #4a4a4a
4 - 1166 пикселей (32,38%) #525252
5 - 1067 пикселей (29,63%) #4d4d4d
6 - 1301 пикселей (36,13%) #5c5c5c
7 - 804  пикселей (22,33%) #383838
8 - 1430 пикселей (39,72%) #666666
9 - 1285 пикселей (35,69%) #5c5c5c
'''





#открытие окна и импорт модулей
import tkinter as tk

window = tk.Tk()
window.title("Number Pattern")

canvas = tk.Canvas(window, width=780, height=780)
canvas.grid(row=0, column=0)



#открываем файл с числом
import os
current_file = os.path.realpath(__file__)
to_open = os.path.dirname(current_file)
to_open = to_open.replace("\\", "/")
print(to_open)
file = open(to_open+"/Pi.txt", "r")
content = file.read()



#обязательные переменные
x=0
y=0
sx=0
cnt=0

#Дефолтные значения цветов цифр (было определено соотношением белых пикселей в цифре к фону)
one="#303030"
two="#4a4a4a"
three="#4a4a4a"
four="#525252"
five="#4d4d4d"
six="#5c5c5c"
seven="#383838"
eight="#666666"
nine="#5c5c5c"
zero="#595959"

#выбор режима восприятия цифр
print("хотите ли вы, чтобы цифры 1 и 7 выделялись почти чёрным цветом?\nда/нет   1/0 (ничего не пишите для следующей опции)")
inp=input()
if inp=="да" or inp=="1" or inp=="ДА": #режим выделения цифр 1 и 7 (если на них посмотреть издалека, то они заметно отличаются от остальных чисел)
    one="#242424"
    seven="#0c0c0c"
if inp=="":
    print("хотите ли вы перейти в режим рисования? (чем больше число, тем оно светлее)\nда/нет   1/0")
    inp=input()
    if inp=="да" or inp=="1" or inp=="ДА": #режим рисования
        zero="#000000"
        one="#1a1a1a"
        two="#333333"
        three="#4d4d4d"
        four="#666666"
        five="#808080"
        six="#999999"
        seven="#b3b3b3"
        eight="#cccccc"
        nine="#e5e5e5"




###  ОСНОВНОЙ ЦИКЛ СОЗДАНИЯ ПИКСЕЛЕЙ  ###

for rx in range(4056): #в range(...) задать количество всех знаков в файле (или сколько из них вы хотите использовать) (по умолчанию: 4056)
    
    cnt+=1

    if rx%78==0: #rx%...==0 тут задать кол-во рядов, через которое будет делаться сдвиг по "y" (по умолчанию: 78)
        y+=10 #все цифры 10 (далее в коде) значат корень кол-ва реальных пикселей в больших пикселях
        x=0
        srx=rx
    else:
        x=(rx-srx)*10 # <- десятка, и всё дальше, где x+..., y+... тоже значит квадрат кол-ва пикселей в одном гигантском пикселе (что отбражается на экране)

    #if content[cnt-1]=="\n": #программа ИГНОРИРУЕТ знаки энтер
    #    cnt+=1
    if content[cnt-1]=="0":
        canvas.create_rectangle(x, y, x+10, y+10, fill=zero,outline=zero)
    if content[cnt-1]=="1":
        canvas.create_rectangle(x, y, x+10, y+10, fill=one,outline=one)
    if content[cnt-1]=="2":
        canvas.create_rectangle(x, y, x+10, y+10, fill=two,outline=two)
    if content[cnt-1]=="3":
        canvas.create_rectangle(x, y, x+10, y+10, fill=three,outline=three)
    if content[cnt-1]=="4":
        canvas.create_rectangle(x, y, x+10, y+10, fill=four,outline=four)
    if content[cnt-1]=="5":
        canvas.create_rectangle(x, y, x+10, y+10, fill=five,outline=five)
    if content[cnt-1]=="6":
        canvas.create_rectangle(x, y, x+10, y+10, fill=six,outline=six)
    if content[cnt-1]=="7":
        canvas.create_rectangle(x, y, x+10, y+10, fill=seven,outline=seven)
    if content[cnt-1]=="8":
        canvas.create_rectangle(x, y, x+10, y+10, fill=eight,outline=eight)
    if content[cnt-1]=="9":
        canvas.create_rectangle(x, y, x+10, y+10, fill=nine,outline=nine)
    if content[cnt-1]=="\n":
        cnt+=1




#закрыте файла с числом (обязательно)
file.close()



#конец цикла окна (обязательно)
window.mainloop()