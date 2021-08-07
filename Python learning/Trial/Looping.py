#i=5
#while(i>0):
#    print(i)
#    i-=1

#x=1
#genap=0
#ganjil=0
#while(x<=10):
#    if(x%2==0):
#        genap=genap+x
#    else:
#        ganjil=ganjil+x
#    x+=1
#print("Jumlah Ganjil adalah %d"%ganjil)
#print("Jumlah Genap adalah %d"%genap)

a=["January","February","March","April","May","June","July","August","September","October","November","Desember"]
for i in range(0,len(a),2):
    print(a[i])

b=0
while(b<3):
    print("B = ",b)
    c=0
    while(c<b):
        print("C = ",c)
        c+=1
    b+=1