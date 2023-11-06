from barang import *
from database_test import *

barang_1 = Barang("", "", 0, 0, 0, False)

boool = False
while boool == False:

    print("Selamat datang di self-service cashier. Masukkan angka yang ingin dilakukan olehmu")

    print("1. Masukkan transaksi baru")
    print("2. Update nama item")
    print("3. Update jumlah item")
    print("4. Update harga item")
    print("5. Hapus item")
    print("6. Cek Transaksi")
    print("7. Save data kedalam Database")
    print("8. Keluar dari Transaksi")

    inputAngka = input()

    options = {
        '1': "Masukkan transaksi baru",
        '2': "Update nama item",
        '3': "Update jumlah item",
        '4': "Update harga item",
        '5': "Save data kedalam Database",
        '6': "Hapus item dari Database",
        '7': "Cek Transaksi",
        '8': "Keluar dari Transaksi"
    }

    selected_option = options.get(inputAngka)
    print(selected_option)

    if selected_option == "Masukkan transaksi baru":
        print(f"Option {inputAngka}: {selected_option}")
        barang_1.transaction()

        boool2 = False
        while boool2 == False:
            print("Anda ingin melanjutkan transaksi? Y/N")
            answer = input()
            if answer == 'Y':
                boool2 = True
            elif answer == 'N':
                boool = True
                boool2 = True
            else:
                print("Mohon masukkan ulang inputnya")

    elif selected_option == "Update nama item":
        print(f"Option {inputAngka}: {selected_option}")
        barang_1.update_nama_item
        
    elif selected_option == "Update jumlah item":
        print(f"Option {inputAngka}: {selected_option}")
        barang_1.update_jumlah_item

    elif selected_option == "Update harga item":
        print(f"Option {inputAngka}: {selected_option}")
        barang_1.update_harga_item

    elif selected_option == "Save data kedalam Database":
        nama_customer, nama_item, jumlah_item, harga_item, total_harga = barang_1.transit_variabel()
        print(nama_customer, nama_item, jumlah_item, harga_item, total_harga)

    elif selected_option == "Hapus item dari Database":
        print('Test')

    elif selected_option == "Cek Transaksi":
        print(f"Option {inputAngka}: {selected_option}")
        barang_1.check_transaction()

        boool2 = False
        while boool2 == False:
            print("Anda ingin melanjutkan transaksi? Y/N")
            answer = input()
            if answer == 'Y':
                boool2 = True
            elif answer == 'N':
                boool = True
                boool2 = True
            else:
                print("Mohon masukkan ulang inputnya")

    elif selected_option == "Keluar dari Transaksi":
        print("Terimakasih telah bertransaksi.")
        #Save barang1 disini kedalam database
        boool = True

    else:
        print("Input tidak valid")

close_cursor()