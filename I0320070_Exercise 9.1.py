import sys

#mendefinisikan array konstan
HARI = ('Minggu','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu')

def main():
    #meminta user memasukkan no hari
    nohari = int(input("Masukkkan nomor hari [1..7]: "))

    if (nohari < 1) or (nohari > 7):
        print("tidak ada hari ke-%s" % nohari)
        sys.exit(1)

    print("Hari ke-%d adalah %s" % (nohari, HARI[nohari-1]))

if __name__ == "__main__":
    main()