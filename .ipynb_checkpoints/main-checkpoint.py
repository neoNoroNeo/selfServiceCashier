import barang

print("Selamat datang di self-service cashier. Masukkan angka yang ingin dilakukan olehmu")

print("1. Masukkan transaksi baru")
print("2. Update nama item")
print("3. Update jumlah item")
print("4. Update harga item")
print("5. Hapus item")
print("6. Cek Transaksi")
print("7. Keluar dari Transaksi")

inputAngka = input()

options = {
    '1': "Masukkan transaksi baru",
    '2': "Update nama item",
    '3': "Update jumlah item",
    '4': "Update harga item",
    '5': "Hapus item",
    '6': "Cek Transaksi",
    '7': "Keluar dari Transaksi"
}

selected_option = options.get(inputAngka)
selected_option = int(selected_option)

if selected_option == 1:
    print(f"Option {inputAngka}: {selected_option}")
    barang_1.transaction()
else:
    print("Input tidak valid")