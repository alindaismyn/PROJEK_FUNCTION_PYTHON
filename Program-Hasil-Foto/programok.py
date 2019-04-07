from projek2.kalkulatortab import kalkulator
from projek1.nilai import nilai
from projek1.gaji import gaji
from projek3.pembayaranku import main
import getpass
def menu() :
    print('\n')
    print( "----- SILAHKAN MEMILIH PROGRAM YANG TERSEDIA  -----")
    from texttable import Texttable
    table = Texttable ()
    table.add_rows([['NO','NAMA PROGRAM'],['1','PROGRAM GAJI KARYAWAN'], ['2','PROGRAM PENILAIAN MAHASISWA'],
                    ['3','PROGRAM KALKULATOR SEDERHANA'],['4','PROGRAM PEMBAYARAN KAMPUS PB'],['5','EXIT']])

    print(table.draw())
    pilih = int(input("Silahkan Masukkan Pilihan Anda : "))
    if pilih == 1:
        gaji()
        tanya()
    elif pilih == 2:
        nilai()
        tanya()
    elif pilih == 3 :
        kalkulator()
        tanya()
    elif pilih == 4:
        main()
        tanya()
    elif pilih == 5 :
        exit
        print('Thank You Using My Program')
    else:

        print("Eror, Pilihan Anda Tidak Ditemukan. Pilih 1-3")
        tanya()
        
       
def tanya ():
     tanya = input("Kembali Me Menu Utama (y/t)? ")
     if tanya == "y":
         menu()
     elif tanya == "t":
        exit
     else:
         print ("Terima Kasih Atas Kunjungan Anda")

  
print('\tWelcome to Sanna Setia Program')
print('===================================================') 
           
def login():
    
    print (' \nSilahkan Login Dahulu')
    print('---------------------------------------------------') 
    username = (input("Masukkan Username Anda : "))
    password = getpass.getpass("Masukkan Password Anda : ")
    if  (username == 'ikhsan' and password == '1234') : 
             print ('\nYeahhhhh, Succesfully Login ')
             print('---------------------------------------------------') 
             menu()
             exit
             
    else :
             print('\nPassword dan Usernameis not detected')
             
             
             login()
             exit                 

                               
login()
        



