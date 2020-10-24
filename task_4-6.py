class Warehouse:
    items_dict = []
    count = 0

    @staticmethod
    def inventory_receipt(self):
        Warehouse.count += 1
        Warehouse.items_dict.append((Warehouse.count, {'name': self.name, "quantity": self.quantity,
                                                       'price': self.price, "brand": self.brand}))

    @staticmethod
    def inventory_transfer(self, write_off_qty, item_id):
        x = [i for i in Warehouse.items_dict if item_id in i][0]
        if write_off_qty == Warehouse.items_dict[Warehouse.items_dict.index(x)][1]['quantity']:
            Warehouse.items_dict.pop(Warehouse.items_dict.index(x))
        else:
            Warehouse.items_dict[Warehouse.items_dict.index(x)][1]['quantity'] -= write_off_qty

    @staticmethod
    def inventory_write_off(self, item_id):
        import datetime
        x = self.purchase_date.split('/')
        d = datetime.date(int(x[2]), int(x[1]), int(x[0]))
        if datetime.date.today().year - d.year == self.durability_in_years:
            y = [i for i in Warehouse.items_dict if item_id in i][0]
            Warehouse.items_dict.pop(Warehouse.items_dict.index(y))
        else:
            print("You can't write off this inventory yet. Its useful life is not over yet")


class OfficeEquipment(Warehouse):
    def __init__(self, name, quantity, price, purchase_date, durability_in_years, brand):
        super().__init__()
        self.name = name
        self.quantity = quantity
        self.price = price
        self.purchase_date = purchase_date
        self.durability_in_years = durability_in_years
        self.brand = brand


class Printer(OfficeEquipment):
    def __init__(self, name, quantity, price, purchase_date, durability_in_years, brand, is_laser=True, is_color=False):
        super().__init__(name, quantity, price, purchase_date, durability_in_years, brand)
        self.is_laser = is_laser
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, name, quantity, price, purchase_date, durability_in_years, brand, scanner_type, sensor_type):
        super().__init__(name, quantity, price, purchase_date, durability_in_years, brand)
        self.scanner_type = scanner_type
        self.sensor_type = sensor_type


class Xerox(OfficeEquipment):
    def __init__(self, name, quantity, price, purchase_date, durability_in_years, brand, copies_num_per_cycle):
        super().__init__(name, quantity, price, purchase_date, durability_in_years, brand)
        self.copies_num_cycle = copies_num_per_cycle


printer_1 = Printer('printer', 30, 50000, '24/10/2020', 5, 'HP')
scanner_1 = Scanner('scanner', 20, 40000, '08/11/2019', 6, 'EPSON', 'slide-scanner', 'CCD')
xerox_1 = Xerox('xerox', 5, 15000, '10/09/2010', 10, 'Xerox', 999)
printer_1.inventory_receipt(printer_1)
print(Warehouse.items_dict)
scanner_1.inventory_receipt(scanner_1)
xerox_1.inventory_receipt(xerox_1)
print(Warehouse.items_dict)
printer_1.inventory_transfer(printer_1, 15, 1)
print(Warehouse.items_dict)
scanner_1.inventory_transfer(scanner_1, 20, 2)
print(Warehouse.items_dict)
xerox_1.inventory_write_off(xerox_1, 3)
print(Warehouse.items_dict)
printer_1.inventory_write_off(printer_1, 1)
printer_2 = Printer('printer', 20, 60000, '25/10/2020', 5, 'Xerox')
printer_2.inventory_receipt(printer_2)
scanner_2 = Scanner('scanner', 10, 20000, '08/11/2020', 7, 'EPSON', 'slide-scanner', 'CCD')
scanner_2.inventory_receipt(scanner_2)
xerox_2 = Xerox('xerox', 5, 15000, '24/10/2020', 10, 'Xerox', 999)
xerox_2.inventory_receipt(xerox_2)
print(Warehouse.items_dict)
scanner_2.inventory_transfer(scanner_2, 10, 5)
print(Warehouse.items_dict)
