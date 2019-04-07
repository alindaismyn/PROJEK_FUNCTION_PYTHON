from texttable import Texttable
import datetime
def bayarku():
    table= Texttable (max_width=700)
    no=0
    nama=[]
    nim=[]
    kelas=[]
    bayar_spp =[]
    bayar_sppp =[]
    bayar_bulan=[]
    bayar_seminar=[]
    bayar_kas=[]
    admin=[]
    x = datetime.datetime.now()
    jawab2 = "y"
    while(jawab2 == "y"):
        
        print ("\n\t\t\t PEMBAYARAN KAMPUS PELITA BANGSA")
        print ("="*78) 
        nama=(input("\nMasukan Nama  : "))
        nim=(input("Masukan NIM   : "))
        kelas=(input("Masukan Kelas : "))
        pili = (input("\nApakah Anda ingin membayar biaya UTS/UAS (y/t) ? "))
        if pili =='y':
            print ("\nSilahkan Pilih Jalur Pembayaran : ")
            print ("1. Pembayaran UTS")
            print ("2. Pembayaran UAS")
            print (("-"*55))
            jawab = 'y'
            while(jawab == 'y'):
                pilih = (input("Masukkan pilihan Anda : "))
                if   pilih == '1':
                    spp =int(input("Masukkan jumlah mata kuliah UTS yang ingin dibayar : "))
                    bayar_spp= 50000*spp
                    jawab = 't'
                    print (("-"*55))
                    pil = (input("\nApakah Anda ingin membayar biaya bulanan (y/t) ? "))
                    if pil == 'y':
                        bulanan = int(input("Masukkan jumlah bulan yang ingin dibayar           : "))
                        bayar_bulan=500000*bulanan
                        print (("-"*55))
                    else :
                        bulanan= ''
                        bayar_bulan=0

                                  
                    pil = (input("\nApakah Anda ingin membayar biaya seminar (y/t) ? "))
                    if  pil == 'y':
                        seminar =int(input("Masukkan jumlah seminar yang ingin dibayar         : "))
                        bayar_seminar= 100000*seminar
                        print (("-"*55))
                    else :
                        seminar = ''
                        bayar_seminar=0
                           
                    pil = (input("\nApakah Anda ingin membayar biaya kas     (y/t) ? "))
                    if  pil == 'y':
                        kas = int(input("Masukkan jumlah kas yang ingin dibayar             : "))
                        bayar_kas= 20000*kas
                        print (("-"*55))
                    else :
                        kas = ''
                        bayar_kas=0
                    print('\nSilahkan Klik Enter Untuk Melihat Detail Pembayaran'),input('')
                    admin=5000
                    bayar_sppp=0
                    no=+1
                           
                    for i in range(no):
                        baba  = bayar_spp+bayar_bulan+bayar_seminar+bayar_kas
                        total = baba+admin
                        table.set_cols_dtype(['i','t','t','t','t','t','t','t','t','t','t','t'])
                        table.add_rows([['NO','NAMA','NIM','KELAS','BIAYA UTS','BIAYA UAS','SPP BULAN','BIAYA SEMINAR','KAS','ADMIN','TOTAL','TANGGAL TRANSAKSI'],
                                    [i+1,nama,nim,kelas,bayar_spp,bayar_sppp,bayar_bulan,bayar_seminar,bayar_kas,admin,total,x]])
                        print (("-"*78))
                        print ('\n"Slip Pembayaran Kampus Pelita Bangsa"'); print("")
                        print (table.draw())

                else :
                                 print('Anda tidak akan dikenakan biaya UTS')
                                 bayar_spp= ''
                                 bayar_spp= 0
                                 jawab = 't'
                             
                     
                     
                if pilih == '2':
                    sppp =int(input("Masukkan jumlah mata kuliah UAS yang ingin dibayar  : "))
                    bayar_sppp= 50000*sppp
                    jawab = 't'
                    print (("-"*55))
                    pil = (input("\nApakah Anda ingin membayar biaya bulanan (y/t) ? "))
                    if pil == 'y':
                        bulanan = int(input("Masukkan jumlah bulan yang ingin dibayar           : "))
                        bayar_bulan=500000*bulanan
                        print (("-"*55))
                    else :
                        bulanan= ''
                        bayar_bulan=0

                                  
                    pil = (input("\nApakah Anda ingin membayar biaya seminar (y/t) ? "))
                    if  pil == 'y':
                        seminar =int(input("Masukkan jumlah seminar yang ingin dibayar         : "))
                        bayar_seminar= 100000*seminar
                        print (("-"*55))
                    else :
                        seminar = ''
                        bayar_seminar=0
                           
                    pil = (input("\nApakah Anda ingin membayar biaya kas     (y/t) ? "))
                    if  pil == 'y':
                        kas = int(input("Masukkan jumlah kas yang ingin dibayar             : "))
                        bayar_kas= 20000*kas
                        print (("-"*55))
                    else :
                        kas = ''
                        bayar_kas=0
                    print('\nSilahkan Klik Enter Untuk Melihat Detail Pembayaran'),input('')
                    admin=5000
                    bayar_spp=0
                    no=+1
                           
                    for i in range(no):
                        babaa = bayar_sppp+bayar_bulan+bayar_seminar+bayar_kas
                        total = babaa+admin
                        table.set_cols_dtype(['i','t','t','t','t','t','t','t','t','t','t','t'])
                        table.add_rows([['NO','NAMA','NIM','KELAS','BIAYA UTS','BIAYA UAS','SPP BULAN','BIAYA SEMINAR','KAS','ADMIN','TOTAL','TANGGAL TRANSAKSI'],
                                    [i+1,nama,nim,kelas,bayar_spp,bayar_sppp,bayar_bulan,bayar_seminar,bayar_kas,admin,total,x]])
                        print (("-"*78))
                        print ('\n"Slip Pembayaran Kampus Pelita Bangsa"'); print("")
                        print (table.draw())
                else :
                     print('Anda tidak akan dikenakan biaya UAS')
                     bayar_sppp=''
                     bayar_sppp= 0
                     jawab = 't'   
               
               
        else:
              bayar_sppp=0
              bayar_spp = 0
   
        
        jawab2 = input("\nIngin Menambah Data Pembayaran (y/t)? ") ; print("")

bayarku()
