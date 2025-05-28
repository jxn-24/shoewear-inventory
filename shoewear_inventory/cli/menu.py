from shoewear_inventory.models.base import SessionLocal
from shoewear_inventory.models.brand import Brand
from shoewear_inventory.models.product import Product


def display_brand_menu():
    while True:
        print("\n=== Brand Menu ===")
        print("1. Create Brand")
        print("2. Delete Brand")
        print("3. View All Brands")
        print("4. Find Brand by Name")
        print("5. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            name = input("Enter brand name: ")
            try:
                Brand.create(name)
                print("✅ Brand created.")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            try:
                bid = int(input("Enter brand ID: "))
                Brand.delete(bid)
                print("✅ Brand deleted.")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "3":
            brands = Brand.get_all()
            for b in brands:
                print(f"{b.id}. {b.name}")

        elif choice == "4":
            name = input("Search brand by name: ")
            results = Brand.find_by_name(name)
            for b in results:
                print(f"{b.id}. {b.name}")

        elif choice == "5":
            break

        else:
            print("⚠️ Invalid option.")


def display_product_menu():
    while True:
        print("\n=== Product Menu ===")
        print("1. Create Product")
        print("2. Delete Product")
        print("3. View All Products")
        print("4. View Products by Attribute")
        print("5. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            name = input("Name: ")
            image_url = input("Image URL (optional): ")
            desc = input("Description (optional): ")
            price = input("Price: ")
            brand_id = input("Brand ID: ")
            try:
                Product.create(name, image_url, desc, float(price), int(brand_id))
                print("✅ Product created.")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            pid = input("Enter product ID: ")
            try:
                Product.delete(int(pid))
                print("✅ Product deleted.")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "3":
            products = Product.get_all()
            for p in products:
                print(f"{p.id}: {p.name} | ${p.price} | From: {p.brand.name}")

        elif choice == "4":
            attr = input("Search by (name/price/brand): ")
            val = input("Enter search term: ")
            try:
                results = Product.find_by_attribute(attr, val)
                for p in results:
                    print(f"{p.id}: {p.name} | ${p.price} | From: {p.brand.name}")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "5":
            break

        else:
            print("⚠️ Invalid option.")