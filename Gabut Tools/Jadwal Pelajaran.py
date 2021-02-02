
from datetime import *
now = datetime.now()
hari_ini = now.strftime("%A")
tanggal = date.today()


class main:
	def __init__(self, jadwal):
		senin = """BK
		Bahasa Indonesia
		PAI"""
		
		selasa = """Matematika
		PKN"""
		
		rabu = """IPA
		PJOK"""
		
		kamis = """IPS
		SBK"""
		
		jumat = """Bahasa Inggris
		Prakarya"""
		
		sabtu = """Libur Cuy, Istirahat Dulu Lah ^_^"""
		
		minggu = """Libur Cuy, Istirahat Dulu Lah ^_^"""
		
		if jadwal == "Monday":
			jadwal = senin
			hari = "Senin"
		elif jadwal == "Tuesday":
			jadwal = selasa
			hari = "Selasa"
		elif jadwal == "Wednesday":
			jadwal = rabu
			hari = "Rabu"
		elif jadwal == "Thursday":
			jadwal = kamis
			hari = "Kamis"
		elif jadwal == "Friday":
			jadwal = jumat
			hari = "Jum'at"
		elif jadwal == "Saturday":
			jadwal = sabtu
			hari = "Sabtu"
		elif jadwal == "Sunday":
			jadwal = minggu
			hari = "Minggu"
		
		self.jadwal = jadwal
		self.hari = hari
	
	def tampilkan(self):
		hasil = {}
		hasil['hari'] = self.hari
		hasil['jadwal'] = self.jadwal
		return hasil

def home():
	h = "\033[92m"
	p = "\033[0m"
	a = main(str(hari_ini))
	b = a.tampilkan()
	print("Tanggal: " + h + str(tanggal) + p)
	print("Hari: " + h + b['hari'] + p)
	print("\nJadwal Pelajaran:")
	for s in b['jadwal'].replace('\t', '').splitlines():
		print("- " + s)

home()
