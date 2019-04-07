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
        num1 = int(input("\n\tSilahkan masukkan nomor pertama : "))
        num2 = int(input("\tSilahkan masukkan nomor kedua   : "))
        print('\n\tHasil dari ',num1,'+',num2,'=',add(num1,num2))
        tanya ()
    
    elif pil == '2':
        num1 = int(input("\n\tSilahkan masukkan nomor pertama : "))
        num2 = int(input("\tSilahkan masukkan nomor kedua   : "))
        print('\n\tHasil dari ',num1,'-',num2,'=',  subtract(num1,num2))
        tanya ()
    
    elif pil == '3':
        num1 = int(input("\n\tSilahkan masukkan nomor pertama : "))
        num2 = int(input("\tSilahkan masukkan nomor kedua   : "))
        print('\n\tHasil dari ',num1,'*',num2,'=', multiply(num1,num2))
        tanya ()
    
    elif pil == '4':
        num1 = int(input("\n\tSilahkan masukkan nomor pertama : "))
        num2 = int(input("\tSilahkan masukkan nomor kedua   : "))
        print('\n\tHasil dari ',num1,'/',num2,'=', divide(num1,num2))
        tanya ()
        
    else:
        exit
        print("\n\tEror, Nomor yang Anda masukkan tidak tersedia")
        tanya ()




def tanya () :
    r = input ('\n\tApakah Anda ingin mengulang (y/t)? ')
    if r == 'y':
        kalkulator ()
    elif r == 't':
        print ('\n\tTerima kasih ')
    else :
        print ('\n\tMaaf,input yang Anda masukkan salah')
        print ('\n\tSilahkan ulangi lagi')
        tanya ()




