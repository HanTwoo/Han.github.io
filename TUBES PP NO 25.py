with open('Tubes pp smst 1.txt', 'r') as f:
    text = f.read().split('\n')

daftar_buku = []
for data in text:
    line = data.split()
    data = {}
    data['ISBN'] = line[0]
    data['stock'] = int(line[1])
    data['total_dipinjam'] = sum([int(value) for value in line[2:]])
    daftar_buku.append(data)

def terbanyak():
    dipinjam_terbanyak = sorted(daftar_buku, key=lambda d: d['total_dipinjam'], reverse=True)
    print('ISBN buku dengan total peminjaman terbanyak adalah buku {} dengan peminjaman sebanyak {} buku.'.format(dipinjam_terbanyak[0]['ISBN'], dipinjam_terbanyak[0]['total_dipinjam']))

def report():
    for dict in daftar_buku:
        print("Rata-rata peminjaman buku {} dalam seminggu adalah {}".format(dict['ISBN'], round(dict['total_dipinjam']/6, 2)))
def main():
    print('SYEHAN FARIZ GUSTOMO | 1301210530 | IF-45-09')

    print('''
    1) Lihat ISBN buku yang paling banyak dipinjam
    2) Lihat rata-rata peminjaman buku setiap minggu
    ''')

    pilihan = int(input('Pilihan: '))
    if pilihan == 1:
        terbanyak()
    elif pilihan == 2:
        report()
    else:
        print('Pilihan tidak tersedia')
        main()

main()