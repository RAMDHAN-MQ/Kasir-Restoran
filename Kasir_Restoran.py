nama_akun = 'ramdhan'
sandi = 'ram1234'

print('Masukkan data pembeli')
nama = input('Nama = ')
alamat = input('Alamat = ')
nomorHP = str(input('Nomor HP = '))

while True:
    while True:
        print('Silahkan Login')
        username = input('username = ')
        password = input('password = ')
        if username == nama_akun and password == sandi:
            print('Login Berhasil')
            break
        else:
            print('username / password salah')
    keranjang_pesanan = {}
    total = 0

    while True:
        print('\nSILAHKAN PILIH MENU DIBAWAH INI')
        menu = {    
            "Nasi Goreng": 15000,
            "Mie Ayam": 12000,
            "Ayam Goreng": 10000,
            "Soda Gembira": 13000,
            "Es Teh": 5000,
            "Es Jeruk": 6000,
        }
        for i in menu:
            print(f'{i}  \t: Rp {menu[i]}')
        pesanan = input('Pilih menu = ')
        jumlah_pesanan = int(input(f'{pesanan} Berapa = '))

        keranjang_pesanan[pesanan] = keranjang_pesanan.get(pesanan,0) + jumlah_pesanan
        total += (menu[pesanan] * jumlah_pesanan)

        pilih = int(input('\nDaftar pilihan \n1.Makan ditempat \n2.Take away \n3.Pesan lagi \npilih menu (1/2/3) = '))
        if pilih == 1:
            reservasi = f'\nNama = {nama} \nNomor HP = {nomorHP}\nAlamat = {alamat}'
            member = input('member(y/n) = ')
            if member == 'y':
                if total >= 300000 and total < 500000:
                    diskon = 0.02
                    total = total - (total * 0.02)
                elif total >= 500000:
                    diskon = 0.03
                    total = total - (total * 0.03)
                else:
                    diskon = 0
            else:
                if total >= 650000:
                    diskon = 0.025
                    total = total - (total * 0.025)
                else:
                    diskon = 0

            voucher = int(input('Pilih Voucher \n1. Gratis Rp.30.000,- \n2. Gratis Es Teh \n3. Tidak ada voucher \nPilih (1/2/3) = '))
            if voucher == 1:
                total = total - 30000
                total = int(total)
                print(f'total = Rp {total}')
                bayar = (int(input('Bayar = ')))
                kembalian = bayar - total
                print(f'\n===================\nRESTORAN RAMDHAN \n=================== {reservasi}\n===================')
                for pesanan,jumlah_pesanan in keranjang_pesanan.items():
                    print(f'{jumlah_pesanan} {pesanan} = Rp {menu[pesanan] * jumlah_pesanan}')
                print(f'===================\nDiskon = {diskon * 100} %\nVoucher = Gratis Rp 30.000\nBayar = Rp {bayar}\nTotal = Rp {total}\nKembalian = Rp {kembalian}\n===================')
                break

            elif voucher == 2:
                print(f'total = Rp {total}')
                total = int(total)
                bayar = (int(input('Bayar = ')))
                kembalian = bayar - total
                print(f'\n===================\nRESTORAN RAMDHAN \n=================== {reservasi}\n===================')
                for pesanan,jumlah_pesanan in keranjang_pesanan.items():
                    print(f'{jumlah_pesanan} {pesanan} = Rp {menu[pesanan] * jumlah_pesanan}')
                print(f'Bonus = 1 Es Teh \n===================\nDiskon = {diskon * 100} %\nBayar = Rp {bayar}\nTotal = Rp {total}\nKembalian = Rp {kembalian}\n===================')
                break

            else:
                print(f'total = Rp {total}')
                total = int(total)
                bayar = (int(input('Bayar = ')))
                kembalian = bayar - total
                print(f'\n===================\nRESTORAN RAMDHAN \n=================== {reservasi}\n===================')
                for pesanan,jumlah_pesanan in keranjang_pesanan.items():
                    print(f'{jumlah_pesanan} {pesanan} = Rp {menu[pesanan] * jumlah_pesanan}')
                print(f'===================\nDiskon = {diskon * 100} %\nBayar = Rp {bayar}\nTotal = Rp {total}\nKembalian = Rp {kembalian}\n===================')
                break
        
        elif pilih == 2:
            ongkir = 5000
            jarak = float(input('Jarak (KM) = '))

            member = input('member(y/n) = ')
            if member == 'y':
                if total >= 300000 and total < 500000:
                    diskon = 0.02
                    total = total - (total * 0.02) + (jarak * 5000)
                elif total >= 500000:
                    diskon = 0.03
                    total = total - (total * 0.03) + (jarak * 5000)
                else:
                    diskon = 0
                    total = total + (jarak * 5000)
            else:
                if total >= 650000:
                    diskon = 0.025
                    total = total - (total * 0.025) + (jarak * 5000)
                else:
                    diskon = 0
                    total = total + (jarak * 5000)

            print(f'total = Rp {total}')
            total = int(total)
            bayar = (int(input('Bayar = ')))
            kembalian = bayar - total
            print(f'\n===================\nRESTORAN RAMDHAN \n===================')
            for pesanan,jumlah_pesanan in keranjang_pesanan.items():
                print(f'{jumlah_pesanan} {pesanan} = Rp {menu[pesanan] * jumlah_pesanan}')
            print(f'===================\nDiskon = {diskon * 100} %\nJarak(KM) = {jarak} Rp {jarak * 5000}\nBayar = Rp {bayar}\nTotal = Rp {total}\nKembalian = Rp {kembalian}\n===================')
            break

        elif pilih == 3:
            print('pesan lagi')
    break