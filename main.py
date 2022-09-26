class Perpustakaan:
    def __init__(self, listbuku):
        self.bukus = listbuku

    def bukuyangTersedia(self):
        print(f"\n{len(self.bukus)} Buku Yang Tersedia: ")
        for buku in self.bukus:
            print(" - " + buku)
        print("\n")

    def meminjamBuku(self, name, namabuku):
        if namabuku not in self.bukus:
            print(
                f"{namabuku} Buku Tidak tersedia Mungkin Sedang di Pinjam Orang lain, Tunggu Sampai Dia Mengembalikan.\n")
        else:
            track.append({name: namabuku})
            print("Pesan  : Terima kasih Jaga Buku Dengan Baik dan Kembalikan Tepat Waktu.\n")
            self.bukus.remove(namabuku)

    def mengembalikanBuku(self, namabuku):
        print("Buku Sudah di Kembalikan : Terima Kasih! \n")
        self.bukus.append(namabuku)

    def donasiBuku(self, namabuku):
        print("Buku Donasi : Terima kasih.\n")
        self.bukus.append(namabuku)


class Murid():
    def requestBook(self):
        print("Apakah Kamu akan meminjam buku!")
        self.buku = input("Masukkan : ")
        return self.buku

    def mengembalikanBuku(self):
        print("Apakah Kamu Akan Mengembalikan Buku!")
        name = input("Masukkan Nama Anda : ")
        self.buku = input("Masukkan Nama Buku Yang Akan di Kembalikan : ")
        if {name: self.buku} in track:
            track.remove({name: self.buku})
        return self.buku

    def donasiBuku(self):
        print("Okay! Kamu akan Donasi Buku !")
        self.buku = input("Masukkan nama Buku Yang Akan DiDonasikan : ")
        return self.buku


if __name__ == "__main__":

    UMMPerpustakaan = Perpustakaan(
        ["vistas", "invention", "rich&poor", "indian", "macroeconomics", "microeconomics"])
    murid = Murid()
    track = []

    print("\t\t\t\t\t\t\t♦♦♦♦♦♦♦ Selamat datang di Perpustakaan UMM ♦♦♦♦♦♦♦\n")
    print(
        """Pilih Apa yang akan kamu lakukan :-\n1. List Semua buku \n2. Meminjam Buku\n3. Mengembalikan Buku \n4. Donasi Buku \n5. Melacak Buku \n6. Keluar dari Perpustakaan\n""")

    while (True):
        # print(track)
        try:
            usr_response = int(input("Masukkan Pilihan mu : "))

            if usr_response == 1:
                UMMPerpustakaan.bukuyangTersedia()
            elif usr_response == 2:
                UMMPerpustakaan.meminjamBuku(
                    input("Masukkan Nama Kamu : "), murid.requestBook())
            elif usr_response == 3:
                UMMPerpustakaan.mengembalikanBuku(murid.mengembalikanBuku())
            elif usr_response == 4:
                UMMPerpustakaan.donasiBuku(murid.donasiBuku())
            elif usr_response == 5:
                for i in track:
                    for key, value in i.items():
                        holder = key
                        buku = value
                        print(f"{buku} Buku sudah di ambil/di pinjam oleh  {holder}.")
                print("\n")
                if len(track) == 0:
                    print("Tidak ada buku yang di keluarkan !. \n")

            elif usr_response == 6:
                print("Terima Kasih ! \n")
                exit()
            else:
                print("Inputan Salah! \n")
        except Exception as e:
            print(f"{e}---> Inputan Salah! \n")
