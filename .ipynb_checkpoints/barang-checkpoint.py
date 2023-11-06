class Barang:
    def __init__(self, nama_customer,nama_item, jumlah_item, harga_item):
        self.nama_customer = nama_customer
        self.nama_item = nama_item
        self.jumlah_item = jumlah_item
        self.harga_item = harga_item
    
    def transaction(self):
        self.nama_customer = input("Masukkan namamu: ")
        self.nama_item = input("Masukkan nama item: ")
        self.jumlah_item = input("Masukkan jumlah item: ")
        self.harga_item = input("Masukkan harga item: ")
    
    def check_transaction(self):
        print(self.nama_customer)
        print(self.nama_item)
        print(self.jumlah_item)
        print(self.harga_item)