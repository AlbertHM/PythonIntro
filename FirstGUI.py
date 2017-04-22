#Intro to GUI and Object Oriented Programming

from tkinter import *

class Idleclicker:
	def __init__(self,a=1): #Behaviour yang pertama kali berjalan, menciptakan object itu sendiri
		self.a=a              #Dalam class ini, object memiliki properti a, yang memiliki default 0 dan dapat di generate(itu dibawah)
		window = Tk()
		self.label = Label(window, text = self.a)
		btTambah = Button(window, text = 'nambah', bg = 'blue', command=self.nambah)  #Deklarasi tombol dan pencatutan fungsi kepada tombol
		btKurang = Button(window, text = 'ngurang', bg = 'red', command=self.ngurang)
		self.label.pack()     #Menaruh label kedalam form
		btTambah.pack()
		btKurang.pack()
		window.mainloop()
	def ngurang(self):      #Behaviour yang berjalan ketika tombol tambah diklik
		self.a-=1             #Properti a dikurangi 1
		self.label['text']=str(int(self.label['text'])-1)
		return 0
	def nambah(self):
		self.a+=1
		self.label['text']=str(int(self.label['text'])+1)
		return 0
	
ok = Idleclicker(a=4) #ok adalah object yang cetakannya(class) adalah Idleclicker dengan properti a=4
