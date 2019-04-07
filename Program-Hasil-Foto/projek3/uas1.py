def uas1 () :
            from texttable import Texttable
            import datetime
            table = Texttable (max_width=300)
            x = datetime.datetime.now()
            no = 0
            nama = []
            nim = []
            seminar = []
            kelas = []
            nilai_uts = []
            bulanan =[]
            kas = []
            admin = []
            print ('\n\t\tKategori Pembayaran UAS')
            print('---------------------------------------------------------------')
            jab =(int(input("Masukkan jumlah mata kuliah yang akan dibayar untuk UTS     : ")))
            nilai_uas=jab*50000
            bul = (int(input('Masukkan jumlah bulan yang dibayar                          : ')))
            bulanan=bul*500000
            ka=(int(input('Masukkan jumlah kas yang dibayar                            : ')))
            kas=ka*20000
            sem=(int(input('Masukkan jumlah seminar yang akan dibayar                   : ' )))
            
            seminar=sem*100000
            admin=5000
            print('\n')
            no +=1
            for i in range (no) :
                akhir = nilai_uas+ bulanan+ kas+ admin + seminar
                total = akhir +admin
                table.set_cols_dtype(['i','t','t','t','a','a','a','a','a','a','t'])
                table.add_rows([['No','Nama','NIM','Kelas','Biaya UAS','Biaya SPP','Seminar','KAS','Admin','Total Bayar','Tanggal Transaksi'],
                                [i+1,nama,nim,kelas,nilai_uas,
                                 bulanan,seminar,kas,admin,akhir,x]])             
            print (table.draw())       


uas1()
