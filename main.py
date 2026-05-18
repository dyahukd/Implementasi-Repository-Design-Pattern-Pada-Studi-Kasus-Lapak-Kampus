from product_controller import ProductController

controller = ProductController()

while True:

    print("\n==============================")
    print(" LAPAK KAMPUS MARKETPLACE ")
    print("==============================")
    print("1. Lihat Barang")
    print("2. Tambah Barang")
    print("3. Konfirmasi Barang Terjual")
    print("4. Hapus Barang")
    print("5. Exit")

    choice = input("Pilih menu: ")

    if choice == "1":
        controller.show_products()

    elif choice == "2":
        controller.add_product()

    elif choice == "3":
        controller.confirm_sale()

    elif choice == "4":
        controller.delete_product()

    elif choice == "5":
        print("\nProgram selesai")
        break

    else:
        print("\nMenu tidak valid")