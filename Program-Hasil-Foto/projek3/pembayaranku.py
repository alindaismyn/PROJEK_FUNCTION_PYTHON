def main () :
    print('\n')
    print ('\n\t PROGRAM PEMBAYARAN KAMPUS PELITA BANGSA ','\n')
    from texttable import Texttable
    table = Texttable (max_width=300)
    no = 0
    nama = []
    nim = []
    seminar = []
    kelas = []
    nilai_uas = []
    nilai_uts = []
    bulanan =[]
    kas = []
    admin = []
    nama.append(input("Masukkan Nama    : "))
    nim.append(int(input("Masukkan NIM     : ")))
    kelas.append(input('Kelas            : '))
    print('\n')
    print ('\n\t\tJalur Pembayaran Mahasiswa')
    print('===============================================================')
    print('1. Pembayaran UTS')
    print('2. Pembayaran UAS')
    print('===============================================================')
    pilih = int (input ('Masukkan pilihan Anda : '))
    if  pilih == 1 :
            print('\n')
            print ('\n\t\tKategori: Pembayaran UTS')
            print('---------------------------------------------------------------')
            jab =(int(input("Masukkan jumlah mata kuliah yang akan dibayar untuk UTS     : ")))
            nilai_uts.append(jab*50000)
            bul = (int(input('Masukkan jumlah bulan yang dibayar                          : ')))
            bulanan.append(bul*500000)
            ka=int(input('Masukkan jumlah kas yang dibayar                            : '))
            kas.append(ka*20000)
            sem=int(input('Masukkan jumlah seminar yang akan dibayar                   : ' ))
            seminar.append(sem*100000)
            admin.append('5000')
            print('\n')
            no +=1
            for i in range (no) :
                sm= int(seminar[i])
                ka = int (kas[i])
                uts = int (nilai_uts[i])
                bln = int (bulanan[i])
                akhir = (uts)+ (bln)+ (ka)+ (5000) + (sm)
                table.set_cols_dtype(['i','t','t','t','a','a','a','a','a','a'])
                table.add_rows([['No','Nama','NIM','Kelas','Biaya UTS','Biaya SPP','Seminar','KAS','Admin','Total'],
                                [i+1,nama[i],nim[i],kelas[i],nilai_uts[i],
                                 bulanan[i],seminar[i],kas[i],admin[i],akhir]])

                          
            print (table.draw())
            tanya()
    elif pilih == 2 :
            print ('\n\t\tKategori Pembayaran UAS')
            print('---------------------------------------------------------------')
            jab =(int(input("Masukkan jumlah mata kuliah yang akan dibayar untuk UTS     : ")))
            nilai_uas.append(jab*50000)
            bul = (int(input('Masukkan jumlah bulan yang dibayar                          : ')))
            bulanan.append(bul*500000)
            ka=int(input('Masukkan jumlah kas yang dibayar                            : '))
            kas.append(ka*20000)
            sem=int(input('Masukkan jumlah seminar yang akan dibayar                   : ' ))
            seminar.append(sem*100000)
            admin.append('5000')
            print('\n')
            no +=1
            for i in range (no) :
                sm= int(seminar[i])
                ka = int (kas[i])
                bln = int (bulanan[i])
                uas = int(nilai_uas[i])
                akhir = (uas)+ (bln)+ (ka)+ (5000) + (sm)
                table.set_cols_dtype(['i','t','t','t','a','a','a','a','a','a'])
                table.add_rows([['No','Nama','NIM','Kelas','Biaya UAS','Biaya SPP','Seminar','KAS','Admin','Total'],
                                [i+1,nama[i],nim[i],kelas[i],nilai_uas[i],
                                 bulanan[i],seminar[i],kas[i],admin[i],akhir]])             
            print (table.draw())
            tanya()


    else :
            print ( "PROGRAM ERORRRRR")
            tanya()
            
    


def tanya ():
     tanya = input("Ingin Membayar Lagi (y/t)? ")
     if tanya == "y":
         main()
     elif tanya == "t":
        print('\n Terima Kasih Guys')
        exit
     else:
         print ("Terima Kasih Atas Kunjungan Anda")








