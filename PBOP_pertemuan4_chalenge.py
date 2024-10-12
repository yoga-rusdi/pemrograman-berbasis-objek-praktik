class Debitur:
    def __init__(self, nama, ktp, jumlah_pinjaman):
        self.nama = nama
        self.ktp = ktp
        self.jumlah_pinjaman = jumlah_pinjaman
        self.angsuran_pokok = jumlah_pinjaman / 12
        self.angsuran_bulanan = self.angsuran_pokok + (jumlah_pinjaman * 0.05)
        self.bunga = jumlah_pinjaman * 0.05
        self.angsuran_total = self.angsuran_bulanan * 12

    def __str__(self):
        return f"Nama: {self.nama}, KTP: {self.ktp}, Jumlah Pinjaman: {self.jumlah_pinjaman}, Angsuran Pokok: {self.angsuran_pokok}, Angsuran Bulanan: {self.angsuran_bulanan}, Bunga: {self.bunga}, Angsuran Total: {self.angsuran_total}"

class ManageDebitur:
    def __init__(self):
        self.debiturs = {}

    def input_debitur(self):
        
        try:
            nama = input("Masukkan nama debitur: ")
            while not nama:
                print("Nama tidak boleh kosong!")
                nama = input("Masukkan nama debitur: ")
            
        except ValueError:
                print("Input tidak valid.masukan dengan benar.")

        try:

            ktp = input("Masukkan KTP debitur: ")
            while not ktp:
                print("KTP tidak boleh kosong!")
                ktp = input("Masukkan KTP debitur: ")
        except ValueError:
                print("Input tidak valid. Pastikan ktp  adalah angka.")
        try:
            jumlah_pinjaman = float(input("Masukkan jumlah pinjaman: "))
            while jumlah_pinjaman <= 0:
                print("Jumlah pinjaman harus lebih besar dari 0!")
                jumlah_pinjaman = float(input("Masukkan jumlah pinjaman: "))
        except ValueError:
                print("Input tidak valid. Pastikan Jumlah Pinjam adalah angka.")

        
        debitur = Debitur(nama, ktp, jumlah_pinjaman)

        
        self.debiturs[ktp] = debitur

        print("Debitur berhasil ditambahkan!")

    def display_debiturs(self):
        
        print("Debitur Information:")
        print("=" * 60)
        print("| KTP | Nama | Jumlah Pinjaman | Angsuran Pokok | Angsuran Bulanan | Bunga | Angsuran Total |")
        print("=" * 60)
        for ktp, debitur in self.debiturs.items():
            print(f"| {ktp} | {debitur.nama} | {debitur.jumlah_pinjaman} | {debitur.angsuran_pokok} | {debitur.angsuran_bulanan} | {debitur.bunga} | {debitur.angsuran_total} |")
        print("=" * 60)

    def delete_debitur(self):
        
        ktp = input("Masukkan KTP debitur yang akan dihapus: ")
        if ktp in self.debiturs:
            del self.debiturs[ktp]
            print("Debitur berhasil dihapus!")
        else:
            print("Debitur tidak ditemukan!")

def main():
    manage_debitur = ManageDebitur()

    while True:
        print("Menu:")
        print("1. Input Debitur")
        print("2. Display Debiturs")
        print("3. Delete Debitur")
        print("4. Exit")
        choice = input("Masukkan pilihan: ")

        if choice == "1":
            manage_debitur.input_debitur()
        elif choice == "2":
            manage_debitur.display_debiturs()
        elif choice == "3":
            manage_debitur.delete_debitur()
        elif choice == "4":
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()