import csv
class Items:
    pay_rate = 0.8  # after Applying 20% discount
    all = []

    def __init__(self, name: str, price: int, quantity: int):

        # For Running Validation
        assert price >= 0, f"Price {price} must be larger than 0"
        assert quantity >= 0, f"Quantity {quantity} must be larger than 0"

        self._name = name
        self.price = price
        self.quantity = quantity

        # Actions Running For All Instances
        Items.all.append(self)

    @property
    def name(self):  # from now on the attribute of name will be read only only
        return self.__name

    @name.setter  # This is Make the private attributes can be accessed eventhoght It is private
    def name(self, value):
        if (len(value)) >= 10:
            raise Exception("The Name Is Too Long")
        self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def calculate_discount_price(self):
        return self.price * self.pay_rate

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self._name}','{self.price}','{self.quantity}')"

    @classmethod  # This is Decorator to allow me access the instances
    def instintiate_from_csv(cls):
        with open('Items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Items(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),

            )

    @staticmethod
    def is_integer(num):
        # we will count the floats that are point to zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @property
    def read_only_item(self):
        return "AAA"

    # this is abstract That prevent access to unneccessary Information
    def __connect(self, smpt_server=0):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone
        We Have {self._name} {self.quantity} Times
        Regardes, Youssef Saeed Thabet
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect("you")
        self.__prepare_body()
        self.__send()


class Phone(Items):
    def __init__(self, name, price, quantity, broken_phones=0):
        self.broken_phones = broken_phones
        # Items.__init__(self,name,price,quantity) # Calling The super Function
        super().__init__(name, price, quantity)  # calling The  Parent Class


Phone1 = Phone("Redmi 12c", 5000.0, 100.0)
Item1 = Items("Phones", 5000, 500)
print(Phone1.calculate_total_price())
print(Items.all)
print(Phone.all)
print(Item1.read_only_item)
Item1.name = "Realme"
print(Item1.name)
print(Items.all)

print(Phone1.send_email())


# Item1.read_only_item = "BBB" You Can not change The read only value
item1 = Items("Phone", 100, 500)
item2 = Items("Computer Screen",200,500)
item2.pay_rate = 0.5

print(item1.calculate_discount_price())
print(item2.calculate_discount_price())
print(Items.all)

# for i in Items.all:
#     print(list[i.name,i.price])
# print(Items.__dict__) # all the attribute for class level
# print(item1.__dict__) # alll the attribute for instance level

Items.instintiate_from_csv()
print(Items.all)
# print(Items.is_integer(7.0))
#---------------------------------------------------------------------------
# Abstarction in OOP
from abc import ABC, abstractmethod
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    
    @abstractmethod
    def print_details(self):
        pass    
    def accelerate(self):
        print("Speed Up")
    def stop(self):
        print("Stop the Car")
class Nisssan(Car):
    def print_details(self):
        print("The Brand For The Car is ",self.brand)
        print("The model For The Car is ",self.model)
        print("The Year For The Car is ",self.year)
car1 = Nisssan("SUV","ALto","2024")
car1.print_details()
car1.accelerate()
#--------------------------------------------------------------
