from shoewear_inventory.database import initialize_database
from shoewear_inventory.cli.menu import display_brand_menu, display_product_menu


def main():
    initialize_database()
    while True:
        print("\n === ShoeWear Inventory System ===")
        print("1. Manage Brands")
        print("2. Manage Products")
        print("3. Exit")
        choice = input("Select option: ")

        if choice == "1":
            display_brand_menu()
        elif choice == "2":
            display_product_menu()
        elif choice == "3":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid option.")


if __name__ == "__main__":
    main()