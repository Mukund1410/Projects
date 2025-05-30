from user_management import register_user, login_user
from admin_management import add_room, view_rooms,view_customers,remove_customer
from customer_management import view_available_rooms, book_room, checkout_room, view_active_bookings, view_booking_history

def main():
    print("Welcome to the Hotel Management System")
    print("1. Login")
    print("2. Register")

    choice = input("Enter choice: ")

    if choice == "2":
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        register_user(name, email, password, "customer")

    email = input("\nEnter email: ")
    password = input("Enter password: ")
    user = login_user(email, password)

    if user:
        user_id, name, role = user
        print(f"\nLogin successful! Welcome, {name}.")

        if role == "admin":
            while True:
                print("\nAdmin Menu")
                print("1. Add Room")
                print("2. View Rooms")
                print("3. Remove a User")  # Add this in Admin Menu
                print("4. Logout")
                choice = input("Enter choice: ")
                if choice == "1":
                    room_type = input("Enter room type: ")
                    price = 1000 if room_type.lower() == "single" else 2500 if room_type.lower() == "double" else 5000
                    add_room(room_type, price)
                elif choice == "2":
                    view_rooms()
                elif choice == "3":
                    customers = view_customers()
                    if not customers:
                        print("No customers found.")
                    else:
                        print("\nCustomer List:")
                        for cust in customers:
                            print(f"ID: {cust[0]} | Name: {cust[1]} | Email: {cust[2]}")

                        try:
                            user_id = int(input("Enter the ID of the customer to remove (or 0 to cancel): "))
                            if user_id != 0:
                                remove_customer(user_id)
                                print("Customer removed successfully.")
                        except ValueError:
                            print("Invalid ID input.")
                elif choice == "4":
                    print("Logging out...")
                    break
        elif role == "customer":
            while True:
                print("\nCustomer Menu")
                print("1. View Available Rooms")
                print("2. Book a Room")
                print("3. View Active Bookings")
                print("4. View Booking History")
                print("5. Check Out")
                print("6. Logout")
                choice = input("Enter choice: ")
                if choice == "1":
                    view_available_rooms()
                elif choice == "2":
                    book_room(user_id)
                elif choice == "5":
                    checkout_room(user_id)
                elif choice == "3":
                    view_active_bookings(user_id)
                elif choice == "4":
                    view_booking_history(user_id)
                elif choice == "6":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice.")
    else:
        print("Invalid email or password!")

if __name__ == "__main__":
    main()
