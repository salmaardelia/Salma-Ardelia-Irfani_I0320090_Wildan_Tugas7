#Soal 1

str = "Biodata"
str_1 = str.center(25, '-')
print(str_1)
Nama = (input('Masukkan nama Anda: '))
Namaa = Nama.upper()
Tempatlahir = (input('Masukkan tempat lahir Anda: '))
Tempat_lahir = Tempatlahir.capitalize()
Tanggallahir = (input('Masukkan tanggal lahir Anda: '))
Jeniskelamin = (input('Masukkan jenis kelamin Anda: '))
Jeniskelamin1 = Jeniskelamin.capitalize()
Sosmed = (input('Masukkan username instagram Anda: '))
Sos_med = Sosmed.lower()

print('Nama: ', Namaa)
print('Tempat lahir: ', Tempat_lahir)
print('Tanggal lahir: ', Tanggallahir)
print('Jenis kelamin: ', Jeniskelamin)
print('Sosmed: ', Sos_med)