class rumah_makan:

    def DaftarMenu():
        print("Daftar Menu")
        print("makanan dan minuman ")
        print("1. Bakso (Rp.10000)")
        print("2. soto (Rp.15000)")
        print("3.  gorengan(Rp.1000)")
        print("4. ingkung (Rp.55000)")
        print("5. es lemon (Rp.6000)")
        print("6.es teh (Rp 4.000)")
    def struk(A,B,C,D):
        import datetime
        print("")
        print("==================")
        print("======Struk=======")
        print(f"===Nama      : {B}")
        print("===Beli      :")
        for item in A:
            print(f"              - {item}")
        print(f"===Tagihan   : Rp.{C}")
        print(f"===Uang      : Rp.{D}")
        print(f"===Waktu Pemesanan: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
        print("==================")


while True:
    print("Selamat Datang di Rumah Makan Kami")
    rumah_makan.DaftarMenu()
    print("==================================")
    nama = input("Masukan nama anda: ")
    THarga = 0
    Belanjaan = []
    while True:
        rumah_makan.DaftarMenu()
        Menu = int(input("Pilih menu (1-5) atau (0) untuk mengakhiri pembelian : "))
        if Menu == 0:
            break
        if Menu in [1, 2, 3, 4, 5, 6]:
            menu_harga = {
                1: ('Bakso', 10000),
                2: ('soto', 15000),
                3: ('gorengan', 1000),
                4: ('ingkung', 15000),
                5: ('es lemon', 6000),
                6: ('es teh ', 4000)
            }
            if Menu in menu_harga:
                menu, harga = menu_harga[Menu]
                inputJumlah = int(input("Masukkan jumlah : "))
                subtotal = harga * inputJumlah
                THarga += subtotal
                Belanjaan.append(f"{inputJumlah} {menu} (Rp.{subtotal})")
            else:
                print("Menu tidak valid, silakan pilih kembali.")
        else:
            print("Masukan tidak valid, silakan masukkan angka (1-5) atau (0).")
    uang = int(input("Masukkan jumlah uang yang diberikan: "))
    kembalian = uang - THarga
    rumah_makan.struk(Belanjaan,nama,THarga,uang,)
    lanjut = input("Apakah ada pelanggan berikutnya? (ya/tidak) ")
    if lanjut.lower() != 'ya':
        break
     
