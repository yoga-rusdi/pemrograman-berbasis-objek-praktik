class Deliver:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}")

class manage_deliver:
    def __init__(self):
        self.deliver_list = []
        self.order = []  

    def add_deliver(self, deliver):
        self.deliver_list.append(deliver)

    def display_deliver(self):
        for deliver in self.deliver_list:
            deliver.display()
    
    def set_order(self, order):
        self.order = order
    
    def add_order(self, order):
        self.order.append(order)

    def display_order(self):
        for order in self.order:
            print(f"Order ID: {order.id}, Customer: {order.customer}, Deliver: {order.deliver}")

    def display_all_data(self):
       
        col_width = {
            'id': 5,
            'customer': 15,
            'deliver': 15,
            'information': 20,
            'date': 12,
            'address': 25
        }
        
        # Membuat header tabel
        header = f"| {'ID':^{col_width['id']}} | {'Customer':^{col_width['customer']}} | {'Deliver':^{col_width['deliver']}} | {'Informasi':^{col_width['information']}} | {'Tanggal':^{col_width['date']}} | {'Alamat':^{col_width['address']}} |"
        separator = '-' * len(header)
        
        print(separator)
        print(header)
        print(separator)
        
 
        for order in self.order:
            row = f"| {order.id:<{col_width['id']}} | {order.customer:<{col_width['customer']}} | {order.deliver:<{col_width['deliver']}} | {order.information:<{col_width['information']}} | {order.date:<{col_width['date']}} | {order.address:<{col_width['address']}} |"
            print(row)
        
        print(separator)

class order:
    def __init__(self, id, customer, deliver, information, date, address):
        self.id = id
        self.customer = customer
        self.deliver = deliver
        self.information = information
        self.date = date
        self.address = address

def input_string(prompt):
    while True:
        value = input(prompt)
        if value.strip():  # Memastikan input tidak kosong atau hanya spasi
            return value
        print("Input tidak boleh kosong. Silakan coba lagi.")

def input_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

manager = manage_deliver()

while True:
    print("\nMenu")
    print("1. Add Deliver")
    print("2. Display Deliver")
    print("3. Set Order")
    print("4. Display Order")
    print("5. Tampilkan Semua Data")
    print("0. Exit")

    pilihan = input_string("Masukan pilihan: ")

    if pilihan == "1":
        id = input_integer("Masukan ID: ")
        name = input_string("Masukan Name: ")
        deliver_obj = Deliver(id, name)
        manager.add_deliver(deliver_obj) 
    elif pilihan == "2":
        manager.display_deliver() 
    elif pilihan == "3":
        id = input_integer("Masukan ID: ")
        customer = input_string("Masukan Customer: ")
        deliver = input_string("Masukan Deliver: ")
        information = input_string("Masukan Informasi: ")
        date = input_string("Masukan Tanggal: ")
        address = input_string("Masukan Alamat: ")
        order_obj = order(id, customer, deliver, information, date, address)
        
        manager.add_order(order_obj)  
    elif pilihan == "4":
        manager.display_order() 
    elif pilihan == "5":
        manager.display_all_data()
    elif pilihan == "0":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
