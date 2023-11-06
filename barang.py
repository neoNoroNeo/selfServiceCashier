class Barang:
    def __init__(self, nama_customer,nama_item, jumlah_item, harga_item, total_harga, own_boool):
        self.nama_customer = nama_customer
        self.nama_item = nama_item
        self.jumlah_item = jumlah_item
        self.harga_item = harga_item
        self.total_harga = total_harga
        self.own_boool = own_boool
        #use own bool in each method
    
    def transaction(self):
        self.own_boool == False
        while self.own_boool == False:

            self.nama_customer = input("Masukkan namamu: ")
            self.nama_item = input("Masukkan nama item: ")
            
            # Using while to ensure that user is inputting the right format
            boool = False
            while boool == False:
                try:
                    str_jumlah_item = input("Masukkan jumlah item: ")
                    #convert str input to int
                    self.harga_item = int(str_jumlah_item)
                    boool = True
                except ValueError:
                    print("Anda tidak memasukkan angka. Ulangi kembali")
            
            boool = False
            while boool == False:
                try:
                    str_harga_item = input("Masukkan harga item: ")
                    #convert str input to int
                    self.jumlah_item = int(str_harga_item)
                    boool = True
                except ValueError:
                    print("Anda tidak memasukkan angka. Ulangi kembali")
                    
            self.total_harga = self.harga_item * self.jumlah_item

            print(f'Nama Customer: {self.nama_customer}')
            print(f'Nama Item: {self.nama_item}')
            print(f'Jumlah Item: {self.jumlah_item}')
            print(f'Nama Customer: {self.nama_customer}')
            print(f'Total Harga: {self.total_harga}')

            ownbool = False
            while ownbool == False:
                print("Apakah pilihan kalian sudah benar? Y/N")
                pilihan = input()

                if pilihan == 'Y':
                    self.own_boool = True
                    ownbool = True
                elif pilihan == 'N':
                    ownbool = True
                else:
                    print('Mohon masukkan kembali inputnya')
    

    def check_transaction(self):
        print(self.nama_customer)
        print(self.nama_item)
        print(self.jumlah_item)
        print(self.harga_item)
        print(self.total_harga)

    def update_nama_item(self, nama_item_baru):
        nama_item_baru = input("Masukkan nama customer: ")
        print(f"Nama customer telah dirubah dari {self.nama_item} menjadi {nama_item_baru}")
        self.nama_item = nama_item_baru

    def update_jumlah_item(self, jumlah_item_baru):
        jumlah_item_baru = input("Masukkan nama customer: ")
        print(f"Nama customer telah dirubah dari {self.jumlah_item} menjadi {jumlah_item_baru}")
        self.jumlah_item = jumlah_item_baru
        self.total_harga = self.jumlah_item * self.harga_item
        print(f'Total harga terbaru anda adalah: {self.total_harga}')

    def update_harga_item(self, harga_item_baru):
        harga_item_baru = input("Masukkan nama customer: ")
        print(f"Nama customer telah dirubah dari {self.harga_item} menjadi {harga_item_baru}")
        self.harga_item = harga_item_baru
        self.total_harga = self.jumlah_item * self.harga_item
        print(f'Total harga terbaru anda adalah: {self.total_harga}')

    def transit_variabel(self):
        nama_customer = self.nama_customer
        nama_item = self.nama_item
        jumlah_item = self.jumlah_item
        harga_item = self.harga_item
        total_harga = self.total_harga
        return nama_customer, nama_item, jumlah_item, harga_item, total_harga