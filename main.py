from controllers.controller_menu import MenuController

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    menu_controller = MenuController()
    while True:
        clear_screen()
        print ("=" * 29)
        print ("[", " SELAMAT DATANG DI RESTO ", "]")
        print ("=" * 29)
        print ("""
1. Tampilkan Menu
2. Buat Pesanan
3. Lihat Pesanan
4. Checkout
5. Keluar           
            """)
        try:
            pilihan = int(input("Pilih Opsi (1-5): "))
            if pilihan == 1:
                menu_controller.tampilkan_menu()  # Tampilkan Menu
            elif pilihan == 2:
                pass  # Buat Pesanan
            elif pilihan == 3:
                pass  # Lihat Pesanan
            elif pilihan == 4:
                pass  # Checkout
            elif pilihan == 5:
                print("Terima kasih telah berkunjung!")
                break
            else:
                print("Pilihan tidak ada dalam daftar, silakan coba lagi.")
                
        except ValueError:
            print("Masukkan dengan format angka !")
            
        input("Tekan Enter untuk melanjutkan...")
        

if __name__ == "__main__":
    main()