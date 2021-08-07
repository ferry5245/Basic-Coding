blj=int(input("Masukkan Total Belanja : "))
mem=input("Apakah anda adalah member (Ya/Tidak)? ")
disc=int(0)
if(mem=="Ya"):
    disc += 5
if(blj>=500000 and blj<=1000000):
    disc += 2
elif(blj>1000000):
    disc += 3

if not(disc==0):
    print(f"Selamat, anda mendapatkan diskon {disc}%")
else:
    print("Maaf, anda tidak mendapatkan diskon")