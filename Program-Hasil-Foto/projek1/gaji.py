def gaji() :
    print('\n')
    print ('\n\t PROGRAM GAJI KARYAWAN ','\n')
    from texttable import Texttable
        
    table = Texttable (max_width=300)
    jawab = "y"
    no = 0
    nama =[]
    jabatan_kamu = []
    gaji_pokok = []
   
    while (jawab == 'y') :
        nama.append(input("Masukkan Nama: "))
        jab = input ("Jabatan      : ")
        jabatan_kamu.append(jab)
        if (jab == 'Programmer'):
            gaji_pokok.append(500000)
           
        elif (jab =='Direktur') :
            gaji_pokok.append(10000)
            
        elif (jab =='Operator') :
            gaji_pokok.append(10000)
            
        else :
            
            break
            
            gaji_pokok.append(00000)
           
        no +=1
        jawab = input (" \n Tambah lagi ? ")
    for i in range (no) :
   
        table.add_rows ([['No','Nama','Jabatan','Gaji'], [i+1,nama[i],jabatan_kamu[i],gaji_pokok[i]]])

    print (table.draw())


   

