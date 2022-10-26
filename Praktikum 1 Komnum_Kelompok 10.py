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
4. Masukkan x1 dan x2 sebagai nilai awal
5. Menampilkan hasil 10 kali iterasi
"""

import os, random, sys
# from sy import Symbol, Derivative

def clear():
    if os.name == "nt":
        os.system('cls')
        pass
    else:
        os.system('clear')
        
def error():
    print("Persamaan salah")
    
def f(x,p):
    return (eval(p))

def persamaan(pers):
    n = 1
    while ((pers.find("^")) == 1):
        n = n + 1
        pers = pers.replace("x^%d"%(n), "pow(x,%d)"%(n))
    return pers
    
def bolzano(persp):
    n = 0
    p = persamaan(persp)
    
    clear()
    print("Metode Bolzano")
    print("Persamaan, %s"%(persp))
    print()
    
    while True:
        print()
        x1 = float(input("Masukkan X1 : "))
        x2 = float(input("Masukkan X2 : "))
        fx1 = round(f(x1,p), 2)
        fx2 = round(f(x2,p), 2)
        
        print()
        print("Nilai dari, F(%d) = %f " % (x1,fx1))
        print("Nilai dari, F(%d) = %f " % (x2,fx2))
        print()
        
        check = fx1*fx2
        if check < 0:
            print("Sudah memenuhi syarat. f(%d)*f(%d) < 0 || %5.2f < 0"%(x1,x2,check))
            break
        else:
            print("Belum memenuhi syarat. f(%d)*f(%d) >= 0 || %5.2f >= 0"%(x1,x2,check))
    
    print()
    #Mempersiapkan output berupa tabel
    print("X1 = %d , X2 = %d"% (x1,x2))
    print("________________________________________")
    print("  n           x              f(x)       ")
    print("________________________________________")
    
    cektemp = random.randint(1,100)
    
    while True:
        n = n + 1
        x3 = round(((x1 + x2)/2),2)
        fx3 = round(f(x3,p),2)
        
        print("%3d|\t%.8f\t%10.8f" % (n,x3,fx3))
        
        if abs(fx3) <= 0 or abs(fx3) == cektemp :
            print("________________")
            print("Akar Persamaan, %.36f"%(x3))
            print("Atau ~ %.4f"%(round(x3,4)))
            print()
        
        if f(x1,p)*f(x3,p) > 0:
            x1 = x3
        else:
            x2 = x3

        cektemp = abs(fx3)
        
        if n%10 == 0:
        	input("Lanjut? Tekan enter.")
    

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

        # print()
        # pil2 = input("Ulang ? (y/n) : ")
        # if (pil2 =='y' or pil2 == 'Y'):
        # 	pil3 = input("Ulang dengan Persamaan yang sama ? (y/n) : ")
        #     clear()
        # else:
        #     exit()