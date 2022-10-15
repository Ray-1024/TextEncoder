from tkinter import *
from tkinter import ttk
from random import choice


root = Tk()
root.title("Переводчик")
tin = Text(root, width = 35,height =15)
tout = Text(root, width = 35,height = 15)

def copytext():
	s=tout.get("1.0",END)[:-1]
	r=Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(s)
	r.update()
	r.destroy()
def to_code():
	global tin,tout
	s=tin.get("1.0",END)[:-1]
	tout.delete("1.0",END)
	ans=''
	ch="0123456789"
	ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	abc="abcdefghijklmnopqrstuvwxyz"
	r_ABC="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
	r_abc="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
	zn="~`!@#+*/$%^&*()-+;:?,><'|"
	alf=' '+ch+ABC+abc+r_ABC+r_abc+zn
	e,d=0,0
	for i in s:
		tmp=''
		ind = alf.find(i)
		d,e=ind//10,ind%10
		while d>0:
			tmp+=choice(ABC+abc+r_ABC+r_abc)
			d-=1
		while e>0:
			tmp+=choice(ch)
			e-=1
		tmp+=choice(zn)
		ans+=tmp
	tout.insert("1.0",ans)


def code_to():
	global tin,tout
	s=tout.get("1.0",END)[:-1]
	tin.delete("1.0",END)
	ans=''
	ch="0123456789"
	ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	abc="abcdefghijklmnopqrstuvwxyz"
	r_ABC="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
	r_abc="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
	zn="~`!@#+*/$%^&*()-+;:?,><'|"
	alf=' '+ch+ABC+abc+r_ABC+r_abc+zn
	e,d=0,0
	for i in s:
		if i in (ABC+abc+r_ABC+r_abc):
			d+=1
		elif i in ch:
			e+=1
		else:
			ans+=alf[d*10+e]
			d,e=0,0
	tin.insert("1.0",ans)


lab1= Label(root,text="Нормальнай текст")
lab2= Label(root,text="Зашифрованный текст")
coding = Button(root,text="Закодировать",command=to_code)
decoding = Button(root,text="Декодировать",command = code_to)
coping = Button(root,text="Скопировать зашифрованный текст",command=copytext)

lab1.grid(row=0,column = 0)
lab2.grid(row=0,column = 1)
tin.grid(row = 1,column = 0)
tout.grid(row = 1,column = 1)
coding.grid(row = 2,column = 0)
decoding.grid(row= 2,column = 1)
coping.grid(row = 3,column = 1)

root.mainloop()
