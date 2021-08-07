hari=input("Masukkan Hari : ")
tgl=int(input("Masukkan Tanggal : "))
merah=input("Tanggal Merah (Ya/Tidak)? ")

if((hari=="Jumat" or hari=="Jum'at") and tgl==1):
    print("Batik!")
elif(merah=="Ya"):
    print("Bebas!")
elif(hari=="Jumat" or hari=="Jum'at"):
    print("Olah Raga!")

else:
    print("Putih!")