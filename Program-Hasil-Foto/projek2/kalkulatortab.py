def kalkulator () :
    def add(x, y):
       return x + y

    # This function subtracts two numbers 
    def subtract(x, y):
       return x - y

    # This function multiplies two numbers
    def multiply(x, y):
       return x * y

    # This function divides two numbers
    def divide(x, y):
       return x / y

    print ('\tProgram Kalkulator Sederhana')
    print ('=============================================')
    print ('1. Penjumlahan')
    print ('2. Pengurangan')
    print ('3. Perkalian')
    print ('4. Pembagian')
    print ('=============================================')
    print ('Silahkan pilih program yang diinginkan (1-4)')
    print (' ')

    pil = input ('Masukkan pilihan Anda : ')
    if pil == '1':
        from texttable import Texttable
        jawab = 'y'
        no=0
        nama =[]
        nu = []
        num=[]
        hasil =[]
        table=Texttable(max_width=300)
        while (jawab=='y'):
            num1 = (int(input("\nSilahkan masukkan nomor pertama : ")))
            num.append(num1)
            num2 = (int(input("Silahkan masukkan nomor kedua   : ")))
            nu.append(num2)
           
            jawab = input("\nTambah data [y/n]?")
            no+=1
    
        for i in range (no) :
            a= int (num[i])
            b = int (nu[i])
            akhir= (a+b)
            table.set_cols_dtype(['i','t','t','t'])
            table.add_rows([['No','Bilangan A','Bilangan B','Hasil A+B'],[i+1,num[i],nu[i],akhir]])
            table.set_cols_align(['c','l','l','l'])
        print (table.draw())
        tanya ()
        
    elif pil == '2':
            from texttable import Texttable
            jawab = 'y'
            no=0
            nama =[]
            nu = []
            num=[]
            hasil =[]
            table=Texttable()
            while (jawab=='y'):
                num1 = (int(input("\nSilahkan masukkan nomor pertama : ")))
                num.append(num1)
                num2 = (int(input("Silahkan masukkan nomor kedua   : ")))
                nu.append(num2)
               
                jawab = input("\nTambah data [y/n]?")
                no+=1
        
            for i in range (no) :
                a= int (num[i])
                b = int (nu[i])
                akhir= (a-b)
                table.set_cols_dtype(['i','t','t','t'])
                table.add_rows([['No','Bilangan A','Bilangan B','Hasil A-B'],[i+1,num[i],nu[i],akhir]])
                table.set_cols_align(['c','l','l','l'])
            print (table.draw())
            tanya ()
        
    
    elif pil == '3':
            from texttable import Texttable
            jawab = 'y'
            no=0
            nama =[]
            nu = []
            num=[]
            hasil =[]
            table=Texttable()
            while (jawab=='y'):
                num1 = (int(input("\nSilahkan masukkan nomor pertama : ")))
                num.append(num1)
                num2 = (int(input("Silahkan masukkan nomor kedua   : ")))
                nu.append(num2)
               
                jawab = input("\nTambah data [y/n]?")
                no+=1
        
            for i in range (no) :
                a= int (num[i])
                b = int (nu[i])
                akhir= (a*b)
                table.set_cols_dtype(['i','t','t','t'])
                table.add_rows([['No','Bilangan A','Bilangan B','Hasil A*B'],[i+1,num[i],nu[i],akhir]])
                table.set_cols_align(['c','l','l','l'])
            print (table.draw())
            tanya ()
        
    
    elif pil == '4':
            from texttable import Texttable
            jawab = 'y'
            no=0
            nama =[]
            nu = []
            num=[]
            hasil =[]
            table=Texttable()
            while (jawab=='y'):
                num1 = (int(input("\nSilahkan masukkan nomor pertama : ")))
                num.append(num1)
                num2 = (int(input("Silahkan masukkan nomor kedua   : ")))
                nu.append(num2)
               
                jawab = input("\nTambah data [y/n]?")
                no+=1
        
            for i in range (no) :
                a= int (num[i])
                b = int (nu[i])
                akhir= (a/b)
                table.set_cols_dtype(['i','t','t','t'])
                table.add_rows([['No','Bilangan A','Bilangan B','Hasil A/B'],[i+1,num[i],nu[i],akhir]])
                table.set_cols_align(['c','l','l','l'])
            print (table.draw())
            tanya ()
        
        
    else:
        exit
        print("\nEror, Nomor yang Anda masukkan tidak tersedia")
        tanya ()




def tanya () :
    r = input ('\nApakah Anda ingin mengulang (y/t)? ')
    if r == 'y':
        kalkulator ()
    elif r == 't':
        print ('\nTerima kasih kawan ')
    else :
        print ('\nMaaf,input yang Anda masukkan salah')
        print ('\nSilahkan ulangi lagi')
        tanya ()





