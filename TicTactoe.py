#MainGameEngineUp4.py
'''
Info
Titik kiri atas adalah 0,0 untuk memudahkan indexing di list
'''


####Albert Harazaki Mendrofa
####1506672496
####DDP Ekstensi-01


import tkinter
import tkinter.messagebox
import tkinter.scrolledtext
from tkinter import colorchooser
import datetime

#display engine#
kotak=[]
line=[]
row=[]
#main game engine#
statuskotak=[]
templist=[] #'tuk memasukkan list kedalam status kotak per kolom

class frontpage(tkinter.Tk):
	def __init__(self,parent):
		self.lanjut=0
		self.color=['SystemButtonFace','SystemButtonFace']
		tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.resizable(width=False, height=False)
		'''Creating'''
		#Window
		labeljudul = tkinter.Label(self, text = 'Conquer the line!',bg='Red',fg='white')
		frameutama = tkinter.Frame(self)
		
		frametampilan = tkinter.Frame(frameutama,relief='groove', borderwidth=3)
		frameplayer = tkinter.Frame(frameutama, relief='groove', borderwidth=3)
		framepreset = tkinter.Frame(frameutama, relief='groove', borderwidth=3)
		subframepreset = tkinter.Frame(framepreset)
		framestart = tkinter.Frame(frameutama)
		#FramePlayer
		label1 = tkinter.Label(frameplayer, text = 'Nickname Player 1       :')
		label2 = tkinter.Label(frameplayer, text = 'Nickname Player 2       :')
		label3 = tkinter.Label(frameplayer, text = 'Jumlah Baris 	        :')
		label4 = tkinter.Label(frameplayer, text = 'Jumlah Kolom \t        :')
		label5 = tkinter.Label(frameplayer, text = 'Jumlah petak menang :')
		
		self.p1name = tkinter.StringVar()
		entry1 = tkinter.Entry(frameplayer, width=10, textvariable = self.p1name)
		self.p2name = tkinter.StringVar()
		entry2 = tkinter.Entry(frameplayer, width=10, textvariable = self.p2name)
		self.baris = tkinter.IntVar()
		entry3 = tkinter.Entry(frameplayer, width=5, textvariable = self.baris)
		self.kolom = tkinter.IntVar()
		entry4 = tkinter.Entry(frameplayer, width=5, textvariable = self.kolom)
		self.ptkmng = tkinter.IntVar()
		entry5 = tkinter.Entry(frameplayer, width=5, textvariable = self.ptkmng)
		
		#FrameTampilan
		frameteks = tkinter.Frame(frametampilan)
		self.cek1var = tkinter.IntVar()
		cek1 = tkinter.Checkbutton(frametampilan, text = 'Text pada button', variable=self.cek1var, command = lambda: self.cekbutton(0))
		cek1.select()
		labelft1 = tkinter.Label(frameteks, text = 'P1 :')
		self.p1teks = tkinter.StringVar()
		entryft1 = tkinter.Entry(frameteks, width = 3, textvariable = self.p1teks)
		self.p1teks.set('')
		labelft2 = tkinter.Label(frameteks, text = 'P2 :')
		self.p2teks = tkinter.StringVar()
		entryft2 = tkinter.Entry(frameteks, width = 3, textvariable = self.p2teks)
		self.p2teks.set('')
		
		self.cek2var = tkinter.IntVar()
		cek2 = tkinter.Checkbutton(frametampilan, text = 'Background Button',variable=self.cek2var, command = lambda: self.cekbutton(1))
		cek2.select()
		btnwarna1 = tkinter.Button(frametampilan, text = 'Warna Button P1', command=lambda:self.pilihwarna(0)) #entahmengapa, tapi butuh lambda biar kagak langsung muncul
		btnwarna2 = tkinter.Button(frametampilan, text = 'Warna Button P2', command=lambda:self.pilihwarna(1))
		#Frame Preset
		labelp1 = tkinter.Label(framepreset, text = 'Preset Permainan')
		btnrefresh = tkinter.Button(framepreset, text = 'Refresh', command=self.refresh)
		self.btnp1 = tkinter.Button(subframepreset, height=3, width=5)
		self.btnp2 = tkinter.Button(subframepreset, height=3, width=5)
		
		#FrameStart
		buttonStart = tkinter.Button(framestart, text = 'Start',width=10,command=self.start)
		buttonExit = tkinter.Button(framestart, text = 'Exit', width=10, command=self.exit)
		
		'''Packing'''
		#FrameWindow
		labeljudul.pack(fill='x')
		frameutama.pack()
		#~FrameUtama
		frameplayer.grid(row=1, column=1)
		frametampilan.grid(row=1, column=2)
		framepreset.grid(row=2, column=1)
		framestart.grid(row=2, column=2)
		#~FrameUtama~FramePlayer
		label1.grid(row=1,column=1,sticky='w')
		entry1.grid(row=1, column=2)
		label2.grid(row=2,column=1,sticky='w')
		entry2.grid(row=2, column=2)
		label3.grid(row=3,column=1,sticky='w')
		entry3.grid(row=3, column=2, sticky='w')
		label4.grid(row=4,column=1,sticky='w')
		entry4.grid(row=4, column=2, sticky='w')
		label5.grid(row=5,column=1)
		entry5.grid(row=5, column=2, sticky='w')
		#~FrameUtama~FramaTampilan
		cek1.pack(anchor='w')
		frameteks.pack()
		labelft1.grid(row=1, column=1, sticky='w')
		entryft1.grid(row=1, column=2, sticky='w')
		labelft2.grid(row=2, column=1, sticky='w')
		entryft2.grid(row=2, column=2, sticky='w')
		cek2.pack()
		btnwarna1.pack()
		btnwarna2.pack()
		#~FrameUtama~FramePreset
		labelp1.grid(row=1,column=1)
		btnrefresh.grid(row=2, column=1)
		subframepreset.grid(row=1, column=2, rowspan=2)	
		self.btnp1.pack(side='left',padx=5)
		self.btnp2.pack(side='right',padx=5)
		#~FrameUtama~FrameStart
		buttonStart.pack(pady=5)
		buttonExit.pack()
		
		'''Finishing'''
		entry1.focus_set()
		
	def pilihwarna(self,player):
		metadata= colorchooser.askcolor()[1]
		if metadata:
			self.color[player]= metadata
			if not player:
				self.btnp1['bg']=self.color[player]
			else:
				self.btnp2['bg']=self.color[player]
	
	def cekbutton(self, no):
		if not no: #cek1
			if self.cek1var.get():
				self.btnp1['text']=self.p1teks.get()
				self.btnp2['text']=self.p2teks.get()
			else:
				self.btnp1['text'], self.btnp2['text'] = '',''
		else:
			if self.cek2var.get():
				self.btnp1['bg']=self.color[0]
				self.btnp2['bg']=self.color[1]
			else:
				self.btnp1['bg']='SystemButtonFace'
				self.btnp2['bg']='SystemButtonFace'
	
	def refresh(self):
		if self.cek1var.get():
			self.btnp1['text']=self.p1teks.get()
			self.btnp2['text']=self.p2teks.get()
		else:
			self.btnp1['text'], self.btnp2['text'] = '',''
			
		if self.cek2var.get():
			self.btnp1['bg']=self.color[0]
			self.btnp2['bg']=self.color[1]
		else:
			self.btnp1['bg']='SystemButtonFace'
			self.btnp2['bg']='SystemButtonFace'
	
	def start(self):
		m = self.baris.get()
		n = self.kolom.get()
		k = self.ptkmng.get()
		if not self.p1name.get():
			return tkinter.messagebox.showwarning('what??','Nick player1 masih kosong')
		if not self.p2name.get():
			return tkinter.messagebox.showwarning('what??','Nick player2 masih kosong')
		try:	
			if m<0 or n<0:
				9/0
			if m<2 or n<2:
				return tkinter.messagebox.showwarning('what??','Kecil amat dah ukuran boxnya, ukuran minimal 2 x 2')
			if k<2:
				return tkinter.messagebox.showwarning('What??','Jumlah petak menang paling sedikit adalah 2')
			if (k > m) and (k > n):
				return tkinter.messagebox.showwarning('What??','Jumlah petak menang paling banyak adalah jumlah kolom atau baris(Nb: yang paling besar jumlahnya)')
		except:
			return tkinter.messagebox.showwarning('what??','Box baris, kolom dan petak menang harus diisi integer positif')
		if self.cek1var.get()==0 and self.cek2var.get()==0:
			return tkinter.messagebox.showwarning('what??','Permainan harus menggunakan sebuah pembeda, baik itu teks ataupun warna. Anda belum memilih')
		self.lanjut=1
		self.destroy()
		
	def exit(self):
		if tkinter.messagebox.askokcancel('Exit?','Anda ingin keluar?'):
			self.lanjut=0
			self.destroy()
			
class MainEngine(tkinter.Tk):
	def __init__(self,parent,baris,kolom,ptkmng,warnap1,warnap2,teksp1,teksp2,p1,p2):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.baris = baris
		self.kolom = kolom
		self.ptkmng = ptkmng
		self.warnap1 = warnap1
		self.warnap2 = warnap2
		self.teksp1 = teksp1
		self.teksp2 = teksp2
		self.namap1 = p1
		self.namap2 = p2
		self.lanjut = False
		self.turn = 0
		
		self.giliranP=1 #player 1 = 1
		
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~Bagian Atas~~~~~~~~~~~~~~~~~~~~~~~~~~~#
		frameatas = tkinter.Frame(self,bg='cyan')
		frameatas.pack(fill='x')
		self.btnp1 = tkinter.Button(frameatas,text='Player 1\n{}'.format(self.namap1),width=7,height=3)
		self.captatas = tkinter.Label(frameatas, text='Selamat Bermain!',width=(6*(self.kolom-2)))
		self.btnp2 = tkinter.Button(frameatas,text='Player 2\n{}'.format(self.namap2),width=7,height=3)
		self.btnp1.pack(side='left')
		self.captatas.pack(side='left')
		self.btnp2.pack(side='right')
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
		
		self.mainframe = tkinter.Frame(self)
		self.mainframe.pack()
		
		framebawah = tkinter.Frame(self)
		framebawah.pack()
		btnHt = tkinter.Button(framebawah,text='History Permainan',command=self.historymain)
		btnRe = tkinter.Button(framebawah, text = 'Reset Permainan',command=self.reset)
		btnHt.pack()
		btnRe.pack()
		
		for baris in range (0,self.baris):
			row=[]
			templist=[]
			
			for kolom in range (0,self.kolom):
				row.append(self.initialize(baris, kolom))
				row[kolom].grid(column=kolom, row=baris)
				templist.append(0)
				
			statuskotak.append(templist)
			line.append(row)
	
	def initialize(self,baris,kolom):
		self.grid()
		
		return tkinter.Button(self.mainframe,bg='SystemButtonFace',height=3,width=5, command=lambda b=baris, k=kolom: self.OnButtonClick(b,k))
		
	def OnButtonClick(self,b,k):
		global statuskotak
		global line
		if self.giliranP==1 and statuskotak[b][k]==0:
			line[b][k]['text']=self.teksp1
			line[b][k]['bg']=self.warnap1
			self.captatas['text']='Giliran ~~~~>'
			self.cekmenangutama(b,k,self.ptkmng,self.giliranP)
			statuskotak[b][k]=1
			self.giliranP=2
		elif self.giliranP==2 and statuskotak[b][k]==0:
			line[b][k]['text']=self.teksp2
			line[b][k]['bg']=self.warnap2
			self.captatas['text']='<~~~~ Giliran'
			self.cekmenangutama(b,k,self.ptkmng,self.giliranP)
			statuskotak[b][k]=2
			self.giliranP=1
		else:
			tkinter.messagebox.showwarning('what??','really m8?')
			self.turn-=1
		self.turn+=1
		#Draw check
		penuh = True
		rahasia=[]
		for n in statuskotak:
			for i in n:
				rahasia.append(i)
		if 0 in rahasia:
			penuh = False
			
		if penuh:
			self.captatas['text']='Permainan Seri'
			stp=open("History Permainan.txt","a+")
			stp.write('====================\n')
			stp.write("Tanggal Main : "+datetime.datetime.now().strftime("%d/%m/%y")+"\n")
			stp.write('Nama pemain 1 : {}\n'.format(self.namap1))
			stp.write('Nama pemain 2 : {}\n'.format(self.namap2))
			stp.write('Pemenang : N/A Permainan Seri\n')
			stp.write('Jumlah giliran : {}\n\n'.format(self.turn+1))
			stp.close
			for n in line:
				for b in n:
					b['state']='disabled'
		print(statuskotak)
		
	def cekmenangutama(self,posisibaris,posisikolom,ptkmng,player):
		def cekmenangsebagian(faktorbaris,faktorkolom,posisibaris,posisikolom,ptkmng,player):
			cek=1
			for n in range (1,ptkmng):
				print((posisibaris - (n*faktorbaris)) < 0)
				print((posisikolom - (n*faktorkolom)) < 0)
				if ((posisibaris - (n*faktorbaris)) < 0) or ((posisikolom - (n*faktorkolom)) < 0):
					print('masuk1')
					break
				else:
					try:
						u=statuskotak[posisibaris - n*faktorbaris][posisikolom - n*faktorkolom]
					except IndexError:
						break
					if u == player :
						cek+=1
						continue
					else: #kalau bukan petak dia, langsung stop
						break
			print(cek)
			print('********')
			if cek<ptkmng:
				for n in range (1,ptkmng):
				#if over, using try and except
					try:
						u=statuskotak[posisibaris + n*faktorbaris][posisikolom + n*faktorkolom]
					except IndexError:
						break
					if u == player :
						cek+=1
						if cek==ptkmng:
							break
						continue
					else:
						break
				print(cek)
			return cek
		print('------------------------')
		print(posisibaris,'++++',posisikolom)
		a = cekmenangsebagian(1,1,posisibaris,posisikolom,ptkmng,player)
		b = cekmenangsebagian(1,0,posisibaris,posisikolom,ptkmng,player)
		c = cekmenangsebagian(1,-1,posisibaris,posisikolom,ptkmng,player)
		d = cekmenangsebagian(0,1,posisibaris,posisikolom,ptkmng,player)
		print('------------------------')
		if a==ptkmng or b==ptkmng or c==ptkmng or d==ptkmng:
			if self.giliranP==1:
				namapemenang=self.namap1
			else:
				namapemenang=self.namap2
			for n in line:
				for b in n:
					b['state']='disabled'
			self.captatas['text']='{} memenangkan permainan!'.format(namapemenang)
			stp=open("History Permainan.txt","a+")
			stp.write('====================\n')
			stp.write("Tanggal Main : "+datetime.datetime.now().strftime("%d/%m/%y")+"\n")
			stp.write('Nama pemain 1 : {}\n'.format(self.namap1))
			stp.write('Nama pemain 2 : {}\n'.format(self.namap2))
			stp.write('Pemenang : {}\n'.format(namapemenang))
			stp.write('Jumlah giliran : {}\n\n'.format(self.turn+1))
			stp.close
			
			return tkinter.messagebox.showwarning('WIN!','Selamat!!!\n{} memangkan permainan!\nJumlah Giliran :{}'.format(namapemenang,self.turn+1))
	
	def historymain(self):
		try:
			file=open("History Permainan.txt","r")
		except:
			file=open("History Permainan.txt","w")
			file.close
			file=open("History Permainan.txt","r")
		file.seek(0)
		a = tkinter.Tk()
		b = tkinter.scrolledtext.ScrolledText(a,width = 25, height = 20)
		c = file.read()
		if not c:
			c = 'Belum ada history permainan'
		file.close
		b.insert(tkinter.INSERT,c)
		b.pack(fill='both')
		a.title('Conquer the line!')
		a.mainloop()
	
	def reset(self):
		global statuskotak
		global line
		
		statuskotak=[]
		line = []
		
		self.lanjut = True
		self.destroy()
		
if __name__ == '__main__':
	frontapp = frontpage(None)
	frontapp.title('Conquer the line!')
	frontapp.mainloop()
	while frontapp.lanjut:
		app = MainEngine(None,frontapp.baris.get(),frontapp.kolom.get(),frontapp.ptkmng.get(),frontapp.color[0],frontapp.color[1],frontapp.p1teks.get(),frontapp.p2teks.get(),frontapp.p1name.get(),frontapp.p2name.get())
		app.title('Conquer the line!')
		app.mainloop()
		if not app.lanjut:
			break
