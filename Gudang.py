#Albert HM
#1506672496
#DDP Ekstensi 01

import json
importir_file='datagudang.json'

print('Sistem Gudang Pak Yaya\n\
[1]Lihat Gudang\n\
[2]Tambah Barang\n\
[3]Update Persediaan Barang\n\
[4]Cuci Gudang\n\
[5]Keluar\n')

def lihatGudang(file):
	l=1
	if file:
		for n in file:
			print('[{}] {} ada {} dari {}. Hargannya {}.'.format(l,n,file[n]['jumlah'],file[n]['nama_pemasok'],file[n]['harga']))
			l+=1
	else:
		print('Tidak ada barang digudang')
	return 0

def tambahBarang(file):
	wout=''
	b=input('Silahkan masukkan input dengan format <barang> <harga> <pemasok>(ex: gula 1500 "CV Semut Setia")\n')
	try:
		if b.count(' ')>=2 and b.count('"')==2 :
			b=b.split(' ',2)
			int(b[1])
			if b[0] in file:
				wout='Barang sudah ada'
			else:
				file[b[0].lower()]={"jumlah":0,"nama_pemasok":b[-1].strip('"'),"harga":b[1]}
				wout='1 barang baru berhasil disimpan.'
			#print(file)
		else:
			9/0
	except:
		print('Input yang anda masukkan tidak sesuai dengan format')
	return wout,file

def updateBarang(file):
	wout=''
	b=input('Silahkan masukkan input dengan format <barang> <stok>\n')
	try:
		if b.count(' ')==1 and b.split(' ')[1]:
			b=b.split(' ')
			b[1]=int(b[1])
			if b[0] in file:
				if file[b[0]]['jumlah'] + b[1] >= 0:
					file[b[0]]['jumlah'] += b[1]			
					wout='Stok {} sekarang {}'.format(b[0],file[b[0]]['jumlah'])
				else:
					wout = 'Stok gula hanya {}, tidak bisa dikurangi {}.'.format(file[b[0]]['jumlah'],abs(b[1]))
			else:
				wout='Barang tidak ditemukan'
		else:
			wout='Input yang anda masukkan tidak sesuai'
	except:
		wout='Harap masukkan jumlah stok dengan benar'
	return wout,file

def cuciGudang(file):
	terhapus=[]
	wout=''
	for a in file:
		if (file[a]['jumlah']) == 0:
			terhapus.append(a)
	if len(terhapus) != 0:
		for penghapus in terhapus:
			del file[penghapus]
	if len(terhapus)==0:
		print('Gudang tidak perlu dicuci!')
	elif len(terhapus)==1:
		wout= '{} tidak ada lagi digudang'.format(terhapus[0])
	else:
		wout=('{} dan {} tidak ada lagi digudang'.format(', '.join(terhapus[:-1]),terhapus[-1]))
	return wout, file

while True:	
	dicti={}
	with open(importir_file,'r') as input_file:
		dicti=json.load(input_file)
	a=input('Pilihan : ')
	if a=='1':
		lihatGudang(dicti)
		continue
	elif a=='2':
		final=tambahBarang(dicti)
	elif a=='3':
		final=updateBarang(dicti)
	elif a=='4':
		final=cuciGudang(dicti)
	elif a=='5':
		print('Ingat pesan Pak Yaya, gudang harus rapi seperti baris program python!!!')
		break
	else:
		print('Input tidak sesuai, harap masukkan sesuai dengan pilihan yang tersedia')
		continue
	print(final[0])
	with open(importir_file,'w') as output_file:
			json.dump(final[1],output_file)
