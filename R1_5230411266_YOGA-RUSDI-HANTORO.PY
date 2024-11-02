from datetime import datetime

class Pegawai:
    def __init__(self, NIK, nama, alamat):
        self.NIK = NIK
        self.nama = nama
        self.alamat = alamat

    def tampilkan_info(self):
        return f"NIK: {self.NIK}, Nama: {self.nama}, Alamat: {self.alamat}"

class Produk:
    def __init__(self, kode_produk, nama_produk, jenis, jumlah, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis = jenis
        self.jumlah = jumlah
        self.harga = harga

    def tampilkan_info(self):
        return f"Kode: {self.kode_produk}, Nama: {self.nama_produk}, Jenis: {self.jenis}, Jumlah: {self.jumlah}, Harga: Rp{self.harga:,}"

    def get_jenis(self):
        return "Produk Umum"

class Snack(Produk):
    def __init__(self, kode_produk, nama_produk, jumlah, harga, berat, expired_date):
        super().__init__(kode_produk, nama_produk, "Snack", jumlah, harga)
        self.berat = berat
        self.expired_date = expired_date

    def tampilkan_info(self): 
        return f"{super().tampilkan_info()}, Berat: {self.berat}g, Expired: {self.expired_date}"

    def get_jenis(self):  
        return "Snack/Cemilan"

class Makanan(Produk):
    def __init__(self, kode_produk, nama_produk, jumlah, harga, porsi, waktu_masak):
        super().__init__(kode_produk, nama_produk, "Makanan", jumlah, harga)
        self.porsi = porsi
        self.waktu_masak = waktu_masak  

    def tampilkan_info(self):  
        return f"{super().tampilkan_info()}, Porsi: {self.porsi} orang, Waktu Masak: {self.waktu_masak} menit"

    def get_jenis(self):  
        return "Makanan Berat"

class Minuman(Produk):
    def __init__(self, kode_produk, nama_produk, jumlah, harga, volume, is_dingin):
        super().__init__(kode_produk, nama_produk, "Minuman", jumlah, harga)
        self.volume = volume  # dalam ml
        self.is_dingin = is_dingin

    def tampilkan_info(self):  # override
        status_dingin = "Dingin" if self.is_dingin else "Normal"
        return f"{super().tampilkan_info()}, Volume: {self.volume}ml, Suhu: {status_dingin}"

    def get_jenis(self):  # override
        return "Minuman"

class Struk:
    def __init__(self, no_transaksi, pegawai):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai
        self.tanggal = datetime.now()
        self.items = []
        self.total = 0

    def tambah_item(self, produk, jumlah_beli):
        if jumlah_beli <= produk.jumlah:
            subtotal = jumlah_beli * produk.harga
            self.items.append({
                'produk': produk,
                'jumlah_beli': jumlah_beli,
                'subtotal': subtotal
            })
            self.total += subtotal
            produk.jumlah -= jumlah_beli  
            return True
        return False

    def cetak_struk(self):
        print("\n" + "="*60)
        print(f"{'STRUK PEMBELIAN':^60}")
        print("="*60)
        print(f"No Transaksi : {self.no_transaksi}")
        print(f"Tanggal      : {self.tanggal.strftime('%d-%m-%Y %H:%M:%S')}")
        print(f"Kasir        : {self.pegawai.nama}")
        print("-"*60)
        print(f"{'Nama Produk':<25}{'Jumlah':>8}{'Harga':>12}{'Subtotal':>15}")
        print("-"*60)
        
        for item in self.items:
            produk = item['produk']
            print(f"{produk.nama_produk:<25}{item['jumlah_beli']:>8}Rp{produk.harga:>10,}Rp{item['subtotal']:>13,}")
        
        print("-"*60)
        print(f"Total{'':>45}Rp{self.total:>13,}")
        print("="*60)
        print(f"{'Terima Kasih Atas Kunjungan Anda':^60}")
        print("="*60)

class ManajemenToko:
    def __init__(self):
        self.pegawai_list = []
        self.produk_list = []
        self.no_transaksi = 1

    def is_nik_exist(self, NIK):
        return any(pegawai.NIK == NIK for pegawai in self.pegawai_list)

    def is_kode_exist(self, kode_produk):
        return any(produk.kode_produk == kode_produk for produk in self.produk_list)

    def tambah_pegawai(self, pegawai):
        if self.is_nik_exist(pegawai.NIK):
            print("NIK sudah terdaftar. Silakan gunakan NIK lain.")
            return False
        self.pegawai_list.append(pegawai)
        print("Pegawai berhasil ditambahkan.")
        return True

    def tambah_produk(self):
        print("\nPilih jenis produk:")
        print("1. Snack")
        print("2. Makanan")
        print("3. Minuman")
        
        pilihan = input_string("Masukkan pilihan: ")
        kode = input_string("Masukkan Kode Produk: ")
        
        if self.is_kode_exist(kode):
            print("Kode produk sudah ada. Silakan gunakan kode lain.")
            return

        nama = input_string("Masukkan Nama Produk: ")
        jumlah = input_integer("Masukkan Jumlah: ")
        harga = input_integer("Masukkan Harga: ")

        if pilihan == "1":
            berat = input_integer("Masukkan Berat (gram): ")
            expired = input_string("Masukkan Tanggal Kadaluarsa (DD-MM-YYYY): ")
            produk = Snack(kode, nama, jumlah, harga, berat, expired)
        elif pilihan == "2":
            porsi = input_integer("Masukkan Jumlah Porsi: ")
            waktu = input_integer("Masukkan Waktu Masak (menit): ")
            produk = Makanan(kode, nama, jumlah, harga, porsi, waktu)
        elif pilihan == "3":
            volume = input_integer("Masukkan Volume (ml): ")
            is_dingin = input_string("Apakah minuman dingin? (y/n): ").lower() == 'y'
            produk = Minuman(kode, nama, jumlah, harga, volume, is_dingin)
        else:
            print("Pilihan tidak valid!")
            return

        self.produk_list.append(produk)
        print(f"{produk.get_jenis()} berhasil ditambahkan.")

    def hapus_pegawai(self, NIK):
        for pegawai in self.pegawai_list:
            if pegawai.NIK == NIK:
                self.pegawai_list.remove(pegawai)
                print(f"Pegawai dengan NIK {NIK} berhasil dihapus.")
                return True
        print(f"Pegawai dengan NIK {NIK} tidak ditemukan.")
        return False

    def hapus_produk(self, kode_produk):
        for produk in self.produk_list:
            if produk.kode_produk == kode_produk:
                self.produk_list.remove(produk)
                print(f"Produk dengan kode {kode_produk} berhasil dihapus.")
                return True
        print(f"Produk dengan kode {kode_produk} tidak ditemukan.")
        return False

    def tampilkan_pegawai(self):
        if not self.pegawai_list:
            print("\nBelum ada data pegawai.")
            return
        print("\nDaftar Pegawai:")
        print("-" * 80)
        for pegawai in self.pegawai_list:
            print(pegawai.tampilkan_info())
        print("-" * 80)

    def tampilkan_produk(self):
        if not self.produk_list:
            print("\nBelum ada data produk.")
            return
        print("\nDaftar Produk:")
        print("-" * 100)
        for produk in self.produk_list:
            print(produk.tampilkan_info())
        print("-" * 100)

    def buat_transaksi(self, nik_pegawai):
        # Cari pegawai berdasarkan NIK
        pegawai = next((p for p in self.pegawai_list if p.NIK == nik_pegawai), None)
        if not pegawai:
            print("Pegawai tidak ditemukan!")
            return
        
        # Buat struk baru
        struk = Struk(f"TRX{self.no_transaksi:04d}", pegawai)
        self.no_transaksi += 1

        while True:
            self.tampilkan_produk()
            print("\nKetik 'selesai' untuk mengakhiri transaksi")
            kode = input_string("Masukkan kode produk: ")
            
            if kode.lower() == "selesai":
                break

            produk = next((p for p in self.produk_list if p.kode_produk == kode), None)
            if not produk:
                print("Produk tidak ditemukan!")
                continue

            jumlah = input_integer("Masukkan jumlah beli: ")
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                continue

            if not struk.tambah_item(produk, jumlah):
                print(f"Stok tidak mencukupi! Stok {produk.nama_produk} tersisa: {produk.jumlah}")
                continue
            
            print(f"\n{produk.nama_produk} berhasil ditambahkan ke keranjang!")

        if struk.items:
            print("\nMemproses transaksi...")
            struk.cetak_struk()
        else:
            print("\nTransaksi dibatalkan karena tidak ada item yang dibeli.")

def input_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input tidak boleh kosong!")

def input_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Mohon masukkan angka yang valid!")

def tambah_data_awal(manager):
  
    pegawai_data = [
        Pegawai("P001", "farhan kebab", "Jl. Merdeka No. 123"),
        Pegawai("P002", "Siti munaro", "Jl. Sudirman No. 45"),
        Pegawai("P003", "Budi setiawan", "Jl. Gatot Subroto No. 67")
    ]

   
    snack_data = [
        Snack("S001", "Chitato negro", 50, 8000, 75, "31-12-2024"),
        Snack("S002", "Pocky black paper", 40, 12000, 45, "30-06-2024"),
        Snack("S003", "ambatuoreo", 60, 10000, 133, "15-08-2024")
    ]

    
    makanan_data = [
        Makanan("M001", "Nasi Goreng cumi hitam pak kris", 20, 15000, 1, 15),
        Makanan("M002", "Mie Goreng", 25, 12000, 1, 10),
        Makanan("M003", "Ayam Bakar", 15, 25000, 1, 20)
    ]


    minuman_data = [
        Minuman("D001", "krim kocok ilham", 100, 5000, 250, True),
        Minuman("D002", "Kopi", 50, 8000, 200, False),
        Minuman("D003", "Jus Alpukat", 30, 15000, 350, True)
    ]

    print("\nMenambahkan data awal...")
    
 
    print("\nMenambahkan data pegawai:")
    for pegawai in pegawai_data:
        if not manager.is_nik_exist(pegawai.NIK):
            manager.pegawai_list.append(pegawai)
            print(f"Pegawai {pegawai.nama} berhasil ditambahkan")
        else:
            print(f"Pegawai dengan NIK {pegawai.NIK} sudah ada")

    
    print("\nMenambahkan data produk:")
    for produk in snack_data + makanan_data + minuman_data:
        if not manager.is_kode_exist(produk.kode_produk):
            manager.produk_list.append(produk)
            print(f"{produk.get_jenis()} {produk.nama_produk} berhasil ditambahkan")
        else:
            print(f"Produk dengan kode {produk.kode_produk} sudah ada")

    print("\nData awal berhasil ditambahkan!")

def main():
    manager = ManajemenToko()
    
    
    tambah_data_awal(manager)
    
    while True:
        print("\n=== SISTEM MANAJEMEN TOKO ===")
        print("1. Menu Pegawai")
        print("2. Menu Produk")
        print("3. Menu Transaksi")
        print("0. Keluar")
        print("=" * 28)

        menu_utama = input_string("Pilih Menu: ")

        if menu_utama == "1":
            while True:
                print("\n=== MENU PEGAWAI ===")
                print("1. Tambah Pegawai")
                print("2. Tampilkan Pegawai")
                print("3. Hapus Pegawai")
                print("0. Kembali ke Menu Utama")
                print("=" * 20)

                pilihan = input_string("Pilih Menu Pegawai: ")

                if pilihan == "1":
                    NIK = input_string("Masukkan NIK: ")
                    nama = input_string("Masukkan Nama: ")
                    alamat = input_string("Masukkan Alamat: ")
                    pegawai = Pegawai(NIK, nama, alamat)
                    manager.tambah_pegawai(pegawai)
                elif pilihan == "2":
                    manager.tampilkan_pegawai()
                elif pilihan == "3":
                    NIK = input_string("Masukkan NIK pegawai yang akan dihapus: ")
                    manager.hapus_pegawai(NIK)
                elif pilihan == "0":
                    break
                else:
                    print("Pilihan tidak valid!")

        elif menu_utama == "2":
            while True:
                print("\n=== MENU PRODUK ===")
                print("1. Tambah Produk")
                print("2. Tampilkan Produk")
                print("3. Hapus Produk")
                print("0. Kembali ke Menu Utama")
                print("=" * 19)

                pilihan = input_string("Pilih Menu Produk: ")

                if pilihan == "1":
                    manager.tambah_produk()
                elif pilihan == "2":
                    manager.tampilkan_produk()
                elif pilihan == "3":
                    kode = input_string("Masukkan Kode produk yang akan dihapus: ")
                    manager.hapus_produk(kode)
                elif pilihan == "0":
                    break
                else:
                    print("Pilihan tidak valid!")

        elif menu_utama == "3":
            while True:
                print("\n=== MENU TRANSAKSI ===")
                print("1. Buat Transaksi Baru")
                print("2. Tampilkan Produk")
                print("3. Tampilkan Pegawai")
                print("4. Cetak Struk Terakhir")
                print("0. Kembali ke Menu Utama")
                print("=" * 21)

                pilihan = input_string("Pilih Menu Transaksi: ")

                if pilihan == "1":
                    if not manager.pegawai_list:
                        print("Belum ada pegawai yang terdaftar!")
                        continue
                    if not manager.produk_list:
                        print("Belum ada produk yang tersedia!")
                        continue
                        
                    manager.tampilkan_pegawai()
                    nik = input_string("Masukkan NIK pegawai: ")
                    struk_baru = manager.buat_transaksi(nik)
                    if struk_baru:
                        manager.struk_terakhir = struk_baru  

                elif pilihan == "2":
                    manager.tampilkan_produk()
                elif pilihan == "3":
                    manager.tampilkan_pegawai()
                elif pilihan == "4":
                    if hasattr(manager, 'struk_terakhir') and manager.struk_terakhir:
                        print("\nMencetak struk terakhir...")
                        manager.struk_terakhir.cetak_struk()
                    else:
                        print("Belum ada transaksi yang dilakukan!")
                elif pilihan == "0":
                    break
                else:
                    print("Pilihan tidak valid!")

        elif menu_utama == "0":
            print("\nTerima kasih telah menggunakan sistem ini!")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()

