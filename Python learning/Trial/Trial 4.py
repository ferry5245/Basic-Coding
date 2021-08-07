A=eval(input('Masukkan Nilai A : '))
B=eval(input('Masukkan Nilai B : '))
C=eval(input('Masukkan Nilai C : '))
D=eval(input('Masukkan Nilai D : '))

TEMP=A
A=B
TEMP1=C
C=TEMP
TEMP=D
D=TEMP1
B=TEMP

print('A = %d\nB = %d\nC = %d\nD = %d'%(A,B,C,D))
