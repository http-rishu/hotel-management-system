import tkinter as tk
from tkinter import messagebox
import random
import datetime

# Global List Declaration 
name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []

# Global Variable Declaration
i = 0

# Room and Menu Information
room_info_text = """STANDARD NON-AC
Room amenities include: 1 Double Bed, Television, Telephone,
Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and
an attached washroom with hot/cold water.

STANDARD AC
Room amenities include: 1 Double Bed, Television, Telephone,
Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and
an attached washroom with hot/cold water + Window/Split AC.

3-Bed NON-AC
Room amenities include: 1 Double Bed + 1 Single Bed, Television,
Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1
Side table, Balcony with an Accent table with 2 Chair and an
attached washroom with hot/cold water.

3-Bed AC
Room amenities include: 1 Double Bed + 1 Single Bed, Television,
Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa,
1 Side table, Balcony with an Accent table with 2 Chair and an
attached washroom with hot/cold water + Window/Split AC."""

menu_info_text = """BEVERAGES                     MAIN COURSE
1 Regular Tea 20.00        16 Shahi Paneer 110.00
2 Masala Tea 25.00        17 Kadai Paneer 110.00
3 Coffee 25.00            18 Handi Paneer 120.00
4 Cold Drink 25.00        19 Palak Paneer 120.00
5 Bread Butter 30.00      20 Chilli Paneer 140.00
6 Bread Jam 30.00         21 Matar Mushroom 140.00
7 Veg. Sandwich 50.00     22 Mix Veg 140.00
8 Veg. Toast Sandwich 50.00 23 Jeera Aloo 140.00
9 Cheese Toast Sandwich 70.00 24 Malai Kofta 140.00
10 Grilled Sandwich 70.00  25 Aloo Matar 140.00

SOUPS                        ROTI
11 Tomato Soup 110.00      29 Plain Roti 15.00
12 Hot & Sour 110.00       30 Butter Roti 15.00
13 Veg. Noodle Soup 110.00 31 Tandoori Roti 20.00
14 Sweet Corn 110.00       32 Butter Naan 20.00
15 Veg. Munchow 110.00

SOUTH INDIAN                RICE
26 Plain Dosa 100.00       33 Plain Rice 90.00
27 Onion Dosa 110.00       34 Jeera Rice 90.00
28 Masala Dosa 130.00      35 Veg Pulao 110.00
36 Peas Pulao 110.00

FAST FOOD                   DAL
37 Veg. Burger 50.00       37 Dal Fry 110.00
38 Veg. Pizza 90.00        38 Dal Makhani 120.00
39 Cheese Pizza 110.00
40 Paneer Pizza 110.00
41 Veg. Patties 50.00
"""

# Home Function
def Home():
    global root
    root = tk.Tk()
    root.title("Hotel RAGA")
    root.geometry("600x400")
    root.configure(bg="#F0F8FF")  # Set background color

    main_frame = tk.Frame(root, bg="#F0F8FF")
    main_frame.pack(fill="both", expand=True)

    tk.Label(main_frame, text="HOTEL MANAGEMENT SYSTEM", font=("Helvetica", 20, "bold"), bg="#4682B4", fg="white", padx=20, pady=20).pack(fill="x")

    buttons_frame = tk.Frame(main_frame, bg="#F0F8FF")
    buttons_frame.pack(pady=30)

    # Customizing buttons with colors and font
    button_styles = {
        "font": ("Helvetica", 12),
        "bg": "#87CEEB",
        "fg": "white",
        "activebackground": "#4682B4",
        "activeforeground": "white",
        "width": 20,
        "height": 2,
        "bd": 0,
    }

    tk.Button(buttons_frame, text="1 Booking", command=Booking, **button_styles).pack(pady=10)
    tk.Button(buttons_frame, text="2 Rooms Info", command=Rooms_Info, **button_styles).pack(pady=10)
    tk.Button(buttons_frame, text="3 Room Service(Menu Card)", command=ask_customer_id, **button_styles).pack(pady=10)
    tk.Button(buttons_frame, text="4 Payment", command=Payment, **button_styles).pack(pady=10)
    tk.Button(buttons_frame, text="5 Record", command=Record, **button_styles).pack(pady=10)
    tk.Button(buttons_frame, text="6 Edit Room Info", command=Edit_Room_Info, **button_styles).pack(pady=10)
    tk.Button(buttons_frame, text="7 Edit Menu", command=Edit_Menu, **button_styles).pack(pady=10)
    tk.Button(buttons_frame, text="0 Exit", command=root.quit, bg="#FF4500", fg="white", width=20, height=2, bd=0).pack(pady=10)

    root.mainloop()

# Function to check date validity
def date(c):
    try:
        datetime.datetime(c[2], c[1], c[0])
    except ValueError:
        return False
    return True

# Booking Function
def Booking():
    def submit_booking():
        global i

        n = name_entry.get()
        p1 = phno_entry.get()
        a = address_entry.get()
        cii = checkin_entry.get()
        coo = checkout_entry.get()
        room_choice = room_var.get()

        if not (n and p1 and a):
            messagebox.showerror("Error", "Name, Phone No. & Address cannot be empty!")
            return

        ci = [int(x) for x in cii.split('/')]
        co = [int(x) for x in coo.split('/')]

        if not date(ci) or not date(co) or datetime.datetime(ci[2], ci[1], ci[0]) >= datetime.datetime(co[2], co[1], co[0]):
            messagebox.showerror("Error", "Invalid Check-In or Check-Out date")
            return

        name.append(n)
        phno.append(p1)
        add.append(a)
        checkin.append(cii)
        checkout.append(coo)
        day.append((datetime.datetime(co[2], co[1], co[0]) - datetime.datetime(ci[2], ci[1], ci[0])).days)

        if room_choice == "1":
            room.append('Standard Non-AC')
            price.append(3500)
        elif room_choice == "2":
            room.append('Standard AC')
            price.append(4000)
        elif room_choice == "3":
            room.append('3-Bed Non-AC')
            price.append(4500)
        elif room_choice == "4":
            room.append('3-Bed AC')
            price.append(5000)
        else:
            messagebox.showerror("Error", "Invalid room choice")
            return

        rn = random.randrange(40) + 300
        cid = random.randrange(40) + 10
        while rn in roomno or cid in custid:
            rn = random.randrange(60) + 300
            cid = random.randrange(60) + 10

        roomno.append(rn)
        custid.append(cid)
        rc.append(0)
        p.append(0)

        i += 1
        messagebox.showinfo("Success", f"Room Booked Successfully\nRoom No: {rn}\nCustomer Id: {cid}")

    booking_window = tk.Toplevel(root)
    booking_window.title("Booking")
    booking_window.geometry("500x500")

    booking_frame = tk.Frame(booking_window, bg="#F0F8FF")
    booking_frame.pack(fill="both", expand=True)

    tk.Label(booking_frame, text="Name", bg="#F0F8FF").pack(pady=5)
    name_entry = tk.Entry(booking_frame)
    name_entry.pack()

    tk.Label(booking_frame, text="Phone No.", bg="#F0F8FF").pack(pady=5)
    phno_entry = tk.Entry(booking_frame)
    phno_entry.pack()

    tk.Label(booking_frame, text="Address", bg="#F0F8FF").pack(pady=5)
    address_entry = tk.Entry(booking_frame)
    address_entry.pack()

    tk.Label(booking_frame, text="Check-In (dd/mm/yyyy)", bg="#F0F8FF").pack(pady=5)
    checkin_entry = tk.Entry(booking_frame)
    checkin_entry.pack()

    tk.Label(booking_frame, text="Check-Out (dd/mm/yyyy)", bg="#F0F8FF").pack(pady=5)
    checkout_entry = tk.Entry(booking_frame)
    checkout_entry.pack()

    tk.Label(booking_frame, text="Room Type", bg="#F0F8FF").pack(pady=5)
    room_var = tk.StringVar()
    room_options = ["1", "2", "3", "4"]
    room_menu = tk.OptionMenu(booking_frame, room_var, *room_options)
    room_menu.pack()

    submit_button = tk.Button(booking_frame, text="Submit", command=submit_booking, bg="#4682B4", fg="white", width=20, height=2, bd=0)
    submit_button.pack(pady=20)

# Rooms Info Function
def Rooms_Info():
    room_info_window = tk.Toplevel(root)
    room_info_window.title("Rooms Info")
    room_info_window.geometry("500x500")

    tk.Label(room_info_window, text=room_info_text, font=("Helvetica", 12), justify="left").pack(pady=20)

# Ask Customer ID Function
def ask_customer_id():
    ask_id_window = tk.Toplevel(root)
    ask_id_window.title("Enter Customer ID")
    ask_id_window.geometry("300x150")

    tk.Label(ask_id_window, text="Enter Customer ID:").pack(pady=10)
    customer_id_entry = tk.Entry(ask_id_window)
    customer_id_entry.pack()

    tk.Button(ask_id_window, text="Submit", command=lambda: room_service(customer_id_entry.get()), bg="#4682B4", fg="white").pack(pady=20)

# Room Service Function
def room_service(cust_id):
    if cust_id not in custid:
        messagebox.showerror("Error", "Invalid Customer ID")
        return

    room_service_window = tk.Toplevel(root)
    room_service_window.title("Room Service (Menu Card)")
    room_service_window.geometry("500x500")

    tk.Label(room_service_window, text=menu_info_text, font=("Helvetica", 12), justify="left").pack(pady=20)

# Payment Function
def Payment():
    def submit_payment():
        cust_id = cust_id_entry.get()

        if cust_id not in custid:
            messagebox.showerror("Error", "Invalid Customer ID")
            return

        index = custid.index(cust_id)
        total_payment = price[index] * day[index]

        messagebox.showinfo("Payment", f"Total Payment for Customer ID {cust_id} is {total_payment}")

    payment_window = tk.Toplevel(root)
    payment_window.title("Payment")
    payment_window.geometry("300x200")

    tk.Label(payment_window, text="Enter Customer ID:").pack(pady=10)
    cust_id_entry = tk.Entry(payment_window)
    cust_id_entry.pack()

    submit_button = tk.Button(payment_window, text="Submit", command=submit_payment, bg="#4682B4", fg="white", width=20, height=2, bd=0)
    submit_button.pack(pady=20)

# Record Function
def Record():
    record_window = tk.Toplevel(root)
    record_window.title("Record")
    record_window.geometry("500x500")

    for idx in range(i):
        record_text = f"Name: {name[idx]}, Phone: {phno[idx]}, Address: {add[idx]}, Check-In: {checkin[idx]}, Check-Out: {checkout[idx]}, Room: {room[idx]}, Price: {price[idx]}, Room No: {roomno[idx]}, Customer ID: {custid[idx]}"
        tk.Label(record_window, text=record_text, font=("Helvetica", 12), justify="left").pack(pady=10)

# Edit Room Info Function
def Edit_Room_Info():
    def save_room_info():
        global room_info_text
        room_info_text = room_info_text_entry.get("1.0", "end-1c")
        edit_room_info_window.destroy()

    edit_room_info_window = tk.Toplevel(root)
    edit_room_info_window.title("Edit Room Info")
    edit_room_info_window.geometry("500x500")

    room_info_text_entry = tk.Text(edit_room_info_window, font=("Helvetica", 12))
    room_info_text_entry.pack(pady=20)
    room_info_text_entry.insert("1.0", room_info_text)

    save_button = tk.Button(edit_room_info_window, text="Save", command=save_room_info, bg="#4682B4", fg="white", width=20, height=2, bd=0)
    save_button.pack(pady=20)

# Edit Menu Function
def Edit_Menu():
    def save_menu_info():
        global menu_info_text
        menu_info_text = menu_info_text_entry.get("1.0", "end-1c")
        edit_menu_window.destroy()

    edit_menu_window = tk.Toplevel(root)
    edit_menu_window.title("Edit Menu")
    edit_menu_window.geometry("500x500")

    menu_info_text_entry = tk.Text(edit_menu_window, font=("Helvetica", 12))
    menu_info_text_entry.pack(pady=20)
    menu_info_text_entry.insert("1.0", menu_info_text)

    save_button = tk.Button(edit_menu_window, text="Save", command=save_menu_info, bg="#4682B4", fg="white", width=20, height=2, bd=0)
    save_button.pack(pady=20)

# Run the Home function to start the application
Home()
