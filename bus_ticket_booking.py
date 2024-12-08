import json

# File to store data
DATABASE_FILE = "bus_booking.json"

def load_data():
    try:
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"buses": [], "bookings": []}

def save_data(data):
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_bus(data):
    print("\n-- Add Bus --")
    bus_id = input("Enter Bus ID: ")
    route = input("Enter Route (e.g., CityA-CityB): ")
    date = input("Enter Date (YYYY-MM-DD): ")
    time = input("Enter Time (HH:MM): ")
    seats = int(input("Enter Total Seats: "))

    data["buses"].append({
        "bus_id": bus_id,
        "route": route,
        "date": date,
        "time": time,
        "seats": seats
    })
    save_data(data)
    print("Bus added successfully!")

def view_buses(data):
    print("\n-- Available Buses --")
    if not data["buses"]:
        print("No buses available.")
    else:
        for bus in data["buses"]:
            print(f"Bus ID: {bus['bus_id']}, Route: {bus['route']}, Date: {bus['date']}, "
                  f"Time: {bus['time']}, Seats: {bus['seats']}")

def book_ticket(data):
    print("\n-- Book Ticket --")
    user_name = input("Enter Your Name: ")
    bus_id = input("Enter Bus ID: ")
    seats = int(input("Enter Number of Seats: "))

    for bus in data["buses"]:
        if bus["bus_id"] == bus_id:
            if bus["seats"] >= seats:
                bus["seats"] -= seats
                booking_id = len(data["bookings"]) + 1
                data["bookings"].append({
                    "booking_id": booking_id,
                    "user_name": user_name,
                    "bus_id": bus_id,
                    "seats": seats
                })
                save_data(data)
                print(f"Booking confirmed! Booking ID: {booking_id}")
                return
            else:
                print("Not enough seats available.")
                return
    print("Bus ID not found.")

def cancel_booking(data):
    print("\n-- Cancel Booking --")
    booking_id = int(input("Enter Booking ID: "))
    for booking in data["bookings"]:
        if booking["booking_id"] == booking_id:
            for bus in data["buses"]:
                if bus["bus_id"] == booking["bus_id"]:
                    bus["seats"] += booking["seats"]
                    data["bookings"].remove(booking)
                    save_data(data)
                    print("Booking canceled successfully!")
                    return
    print("Booking ID not found.")

def view_bookings(data):
    print("\n-- View All Bookings --")
    if not data["bookings"]:
        print("No bookings available.")
    else:
        for booking in data["bookings"]:
            print(f"Booking ID: {booking['booking_id']}, User: {booking['user_name']}, "
                  f"Bus ID: {booking['bus_id']}, Seats: {booking['seats']}")

def main():
    data = load_data()
    while True:
        print("\n-- Bus Ticket Booking System --")
        print("1. Add Bus")
        print("2. View Buses")
        print("3. Book Ticket")
        print("4. Cancel Booking")
        print("5. View All Bookings")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_bus(data)
        elif choice == "2":
            view_buses(data)
        elif choice == "3":
            book_ticket(data)
        elif choice == "4":
            cancel_booking(data)
        elif choice == "5":
            view_bookings(data)
        elif choice == "6":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
