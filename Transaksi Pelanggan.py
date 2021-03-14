total = 0
command = 'y'
i = 0
karakter = []
while True:
    if command == 'y':
        jumlah_barang = int(input('Entrikan jumlah barang yang dibeli: '))
        harga_barang = int(input('Entrikan harga satuan barang: '))
        total += jumlah_barang * harga_barang
    elif command == 't':
        print("Total pembayaran: Rp ",'{:,}'. format(total))

        for item in karakter:
            print("Karakter salah indeks ke {} adalah {} ". format(i,item))
            i += 1
        break
    else:
        karakter.append(command)
    command = input('Apakah ada lagi item barang yang akan dientrikan atau tidak? [y]/[t] ')