"""
PRAKTIKUM 1 (Implementasi Metode Bolzano)
Komputasi Numerik D
Kelompok 10 :
- Rizky Alifiyah Rahma (5025211208)
- Muhammad Naufal Fawwaz Ramadhan (5025211223)

Cara penggunaan :
1. Clone Git ini
2. Jalankan Praaktikum 1 Komnum_Kelompok 10.py
3. Masukkan persamaan
4. Masukkan angka pembulatan dan taraf error
5. Masukkan x1 dan x2 sebagai nilai awal
6. Menampilkan hasil 10 kali iterasi, tekan enter jika ingin iterasi berlanjut 
"""

import os
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

_x = np.zeros(1001)
_y = np.zeros(1001)
_xmid = []
_ymid = []

# Clear Screen
def clear():
    if os.name == "nt":
        os.system('cls')
        pass
    else:
        os.system('clear')
        
# Pesan Error
def error():
    print("Persamaan salah")

# Menghitung Persamaan
def f(x,p):
    return (eval(p))

# Merubah bentuk persamaan
def persamaan(pers):
    n = 1
    while ((pers.find("^")) == 1):
        n = n + 1
        pers = pers.replace("x^%d"%(n), "pow(x,%d)"%(n))
    return pers

# Menggambar grafik
def grafik(x3,fx3):
    plt.grid()
    print("\nHasil : ",x3,fx3)
    plt.title(print("Grafik Persamaan :"))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x3,fx3,'ro')
    plt.show()
    

# Metode Bolzano
def bolzano(persp):
    n = 0
    p = persamaan(persp)
    
    clear()
    print("Metode Bolzano")
    print("Persamaan, %s"%(persp))
    print()
    print("(Berapa angka dibelakang koma. Masukkan 2 jika tidak yakin)")
    ro = int(input("Pembulatan : "))
    print("(Ingin mendekati nilai berapa. Masukkan 0 jika tidak yakin)")
    err = float(input("Masukkan Error : "))
    
    while True:
        print()
        x1 = float(input("Masukkan X1 : "))
        x2 = float(input("Masukkan X2 : "))
        fx1 = round(f(x1,p), ro)
        fx2 = round(f(x2,p), ro)
        

        print()
        print("Nilai dari, F(%d) = %f " % (x1,fx1))
        print("Nilai dari, F(%d) = %f " % (x2,fx2))
        print()

        s = int(x1)
        r = int(x2)
        for i in range(s,r+1):
            _x[i] = i
            _y[i] = round(f(i,p), 2)
        # print(_x)
        # print(_y)
        plt.plot(_x,_y,'b')
        # os.system("pause")
        
        check = fx1*fx2
        if check < 0:
            print("Sudah memenuhi syarat. f(%d)*f(%d) < 0 || %5.2f < 0"%(x1,x2,check))
            break
        else:
            print("Belum memenuhi syarat. f(%d)*f(%d) >= 0 || %5.2f >= 0"%(x1,x2,check))

        
    
    print()
    # Output akan berbentuk tabel
    print("X1 = %d , X2 = %d, Error = %.6f"% (x1,x2,err))
    print("__________________________________________________________")
    print("  n          x              f(x)              error    ")
    print("__________________________________________________________")
    
    # Inisialisasi
    cektemp = random.randint(1,100)
    
    while True:
        # Counter Iteraso
        n = n + 1
        
        x3 = round(((x1 + x2)/2),ro)
        fx3 = round(f(x3,p),ro)
        _xmid.append(x3)
        _ymid.append(fx3)
        
        print("%3d|\t%.8f\t%10.8f %12.0f" % (n,x3,fx3,fx3))
        
        
        if abs(fx3) <= 0 or abs(fx3) == cektemp :
            print("________________")
            print("Akar Persamaan, %.36f"%(x3))
            print("Atau ~ %.4f"%(round(x3,4)))
            print("Error, %.4f"%(round(fx3,4)))
            print()
        
        if f(x1,p)*f(x3,p) > 0:
            x1 = x3
        else:
            x2 = x3

        cektemp = abs(fx3)
        
        if n%10 == 0:
            # print(_xmid,_ymid)
            grafik(_xmid,_ymid)
            os.system("pause")
            input("Lanjut? Tekan enter.")
            
# Input persamaan
if __name__ == '__main__':
    #Inisialisasi Variable
    pil2 = 'y'

    if( (len(sys.argv)>2)): #Error Usage
        error()
        exit()

    elif(len(sys.argv)==2): #jika Menggnuakan Argument
        pil3 = 'y'
        pers = str(sys.argv[1])
        if((sys.argv[1].find('x')) == -1):
            error()
            print('\nNo Variable or using other than x')
            exit()

    else:
        pil3 = 'n'

    clear()
    while(pil2 == 'y' or pil2 == 'Y'):
        if (pil3 == 'n' or pil3 == 'N'):
            print("ex. x^3 + 2*x^2 - 4*x - 4")
            pers = str(input("Masukkan Persamaan : "))
            pers = pers.lower()
        print()

        #Pemilihan Metode Numerik
        bolzano(pers)
