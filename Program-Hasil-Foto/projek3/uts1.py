def uts1 () :
    from texttable import Texttable
    
    table = Texttable ()
    jawab = "y"
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
    nama.append(input("Masukkan Nama : "))
    nim.append(int(input("Masukkan NIM : ")))
    kelas.append(input('Kelas : '))
    while (jawab =="y") :
        
        print('\n')
        print ('Pembayaran UTS')
        jab =(int(input("Masukkan jumlah mata kuliah yang akan dibayar untuk UTS     : ")))
        nilai_uts.append(jab*50000)
        nilai_uas.append('000000')
        bul = (int(input('Masukkan jumlah bulan yang dibayar : ')))
        bulanan.append(bul*500000)
        ka=int(input('Masukkan jumlah kas yang dibayar: '))
        kas.append(ka*20000)
        sem=int(input('Masukkan jumlah seminar yang akan dibayar :' ))
        seminar.append(sem*100000)
        admin.append('5000')
        jawab = input("Ingin membayar lagi (y/t)?")
        print('\n')
        no +=1
    for i in range (no) :
        sm= int(seminar[i])
        ka = int (kas[i])
        uts = int (nilai_uts[i])
        bln = int (bulanan[i])
        uas = int(nilai_uas[i])
        akhir = (uts)+ (bln)+ (ka)+ (5000) + (sm)
        table.add_rows([['No','Nama','NIM','Kelas','Biaya UAS','Biaya UTS','Biaya SPP Bulanan','Biaya Seminar','Biaya KAS','Biaya Admin','Total Pembayaran'],
                        [i+1,nama[i],nim,kelas[i],nilai_uas[i],
                         nilai_uts[i],bulanan[i],seminar[i],kas[i],admin[i],akhir]])

                  
    print (table.draw())


uts1()




