from plyer import notification
import datetime
import matplotlib.pyplot as plt


class ElectronicStore:
    def __init__(self):
        self.iphone = {"Iphone 15 Pro Max": 149000, "Iphone 15": 80000, "Iphone 14 Pro Max": 110000, "Iphone 14": 59000}
        self.samsung = {"Galaxy S24 Ultra": 140000, "Galaxy S24": 80000, "Galaxy S23 Ultra": 109999,
                        "Galaxy S23": 69000}
        self.google = {"Google Pixel 8 Pro": 106999, "Google Pixel 8": 75999, "Google Pixel 7": 47000,
                       "Google Pixel 6a": 43999}
        self.realme = {"Realme 10": 19999, "Realme 9i": 17000, "Realme Narzo 30": 15000}

        self.iphone_quantity = {"Iphone 15 Pro Max": 30, "Iphone 15": 50, "Iphone 14 Pro Max": 35, "Iphone 14": 60}
        self.samsung_quantity = {"Galaxy S24 Ultra": 25, "Galaxy S24": 40, "Galaxy S23 Ultra": 35, "Galaxy S23": 50}
        self.google_quantity = {"Google Pixel 8 Pro": 40, "Google Pixel 8": 32, "Google Pixel 7": 29,
                                "Google Pixel 6a": 44}
        self.realme_quantity = {"Realme 10": 50, "Realme 9i": 49, "Realme Narzo 30": 67}

        self.dict2 = {}
        self.list1 = []
        self.sales_data = {}

    def add_item(self, company_dict):
        phone_name = input("Enter Mobile Name : ")
        phone_cost = int(input("Enter Mobile Price : "))
        if phone_name not in company_dict.keys():
            company_dict[phone_name] = phone_cost
            print("Added Successfully")
        else:
            print("The entered Mobile Name is already present in our data")

    def remove_item(self, company_dict):
        phone_name = input("Enter Mobile Name that has to be removed : ")
        if phone_name in company_dict.keys():
            del company_dict[phone_name]
            print("Deleted Successfully")
        else:
            print("Entered Mobile Name is not present in our data.\nTRY AGAIN")

    def modify_item(self, company_dict):
        phone_name = input("Enter Mobile Name whose price you want to change : ")
        if phone_name in company_dict:
            phone_price = int(input("Enter Mobile Price that needs to be modify : "))
            company_dict[phone_name] = phone_price
            print("Modified Successfully")
        else:
            print(
                "The entered Mobile Name is not already present in our data.\nSO CANNOT MODIFY ANYTHING.\nTRY AGAIN !")

    def purchase(self, company, company_quantity):
        total = 0
        product_name = input("Enter Mobile Name or Product Name that you would like to purchase : ")
        if product_name in company.keys():
            quantity = int(input("Enter how many Mobile Phone would you like to purchase : "))
            if quantity > company_quantity[product_name]:
                print("Not enough quantity we only have", company_quantity[product_name], "quantity available")
            elif quantity < 0:
                print("Quantity can never be negative")
            else:
                company_quantity[product_name] -= quantity
                self.dict2[product_name] = quantity
                total = company[product_name] * quantity
                self.list1.append(total)
                # Update sales data
                if company == self.iphone:
                    company_name = "iPhone"
                elif company == self.samsung:
                    company_name = "Samsung"
                elif company == self.google:
                    company_name = "Google"
                elif company == self.realme:
                    company_name = "Realme"

                if company_name in self.sales_data:
                    self.sales_data[company_name] += total
                else:
                    self.sales_data[company_name] = total
        else:
            print("Entered product name is not in our data")

    def bill(self, customer):
        total_bill = sum(self.list1)
        pay = str(total_bill)
        date = datetime.datetime.now()
        print()
        print("BILL".center(150, "."))
        print("Name : ", customer)
        print("Date of Purchase : ", date)
        print()
        print("_" * 100)
        print("Mobile Phone".ljust(30, " "), "Quantity Purchased".ljust(20, " "), "Price per Mobile".ljust(20, " "),
              "Total Price".ljust(20, " "))
        print("_" * 100)
        for key, value in self.dict2.items():
            price_per_mobile = 0
            if key in self.iphone:
                price_per_mobile = self.iphone[key]
            elif key in self.samsung:
                price_per_mobile = self.samsung[key]
            elif key in self.google:
                price_per_mobile = self.google[key]
            elif key in self.realme:
                price_per_mobile = self.realme[key]
            total_price = price_per_mobile * value
            print(str(key).ljust(40, " "), str(value).ljust(15, " "), str(price_per_mobile).ljust(20, " "),
                  str(total_price).ljust(20, " "))
        print("_" * 100)
        print("Total Amount to be Paid = ", pay.ljust(70, " "))
        print("_" * 100)
        print("\n")
        return total_bill

    def notify_me(self, title, message, total_amount):
        notification.notify(
            title=title,
            message=message.replace("[amount]", str(total_amount)),
            app_icon="C:\\Users\\naman\\Downloads\\icon.ico",
            timeout=10
        )

    def staff_operations(self):
        staff = ["Yogesh", "Tilak", "Karan", "Arun", "Sunil", "Kapil"]
        pas = "Staff123"
        staff_name = input("Enter Username : ")
        password = input("Enter staff password : ")

        if staff_name in staff and password == pas:
            while True:
                print("""Which task will you like to perform-
                \t1.Add an item
                \t2.Remove an item
                \t3.Modify the item
                \t4.View
                \t5.View Sales Data
                \t6.Exit""")
                print("\n")
                ch = int(input("Enter the choice of operation you want to perform : "))
                if ch == 1:
                    print("""Under which Mobile Company you want to add -
                    \t1.Iphone
                    \t2.Samsung
                    \t3.Google
                    \t4.Realme""")
                    m = int(input("Enter your choice : "))
                    if m == 1:
                        self.add_item(self.iphone)
                    elif m == 2:
                        self.add_item(self.samsung)
                    elif m == 3:
                        self.add_item(self.google)
                    elif m == 4:
                        self.add_item(self.realme)
                    else:
                        print("WRONG CHOICE ENTERED.\nTRY AGAIN!")

                elif ch == 2:
                    print("""Under which Mobile Company you want to delete a Certain Mobile Model -
                    \t1.Iphone
                    \t2.Samsung
                    \t3.Google
                    \t4.Realme""")
                    m = int(input("Enter your choice : "))
                    if m == 1:
                        self.remove_item(self.iphone)
                    elif m == 2:
                        self.remove_item(self.samsung)
                    elif m == 3:
                        self.remove_item(self.google)
                    elif m == 4:
                        self.remove_item(self.realme)

                    else:
                        print("WRONG CHOICE ENTERED.\nTRY AGAIN!")

                elif ch == 3:
                    print("""Under which Mobile Company you want to modify a Certain Mobile Model -
                    \t1.Iphone
                    \t2.Samsung
                    \t3.Google
                    \t4.Realme""")
                    m = int(input("Enter your choice : "))
                    if m == 1:
                        self.modify_item(self.iphone)
                    elif m == 2:
                        self.modify_item(self.samsung)
                    elif m == 3:
                        self.modify_item(self.google)
                    elif m == 4:
                        self.modify_item(self.realme)
                    else:
                        print("WRONG CHOICE ENTERED.\nTRY AGAIN!")

                elif ch == 4:
                    print("""Which Company Mobile you want to see-
                    \t1.Iphone
                    \t2.Samsung
                    \t3.Google
                    \t4.RealMe""")
                    m = int(input("Enter your choice : "))
                    if m == 1:
                        self.display_company(self.iphone)
                    elif m == 2:
                        self.display_company(self.samsung)
                    elif m == 3:
                        self.display_company(self.google)
                    elif m == 4:
                        self.display_company(self.realme)
                    else:
                        print("WRONG CHOICE ENTERED.\nTRY AGAIN!")

                elif ch == 5:
                    self.view_sales_data()

                elif ch == 6:
                    break
                else:
                    print("Invalid choice entered")

        else:
            print("Wrong Username or Password is entered\nTRY AGAIN !\n")

    def customer_operations(self):
        while True:
            print("Welcome SIR/MA'AM")
            print("""What would you like to do-
            \t1.Ready to make a purchase
            \t2.Exit""")
            cho = int(input("Enter your choice : "))
            if cho == 1:
                while True:
                    print("""What would you like to do-
                    \t1.Purchase
                    \t2.Exit""")
                    ch = int(input("Enter Choice : "))
                    print()
                    if ch == 1:
                        while True:
                            print("""Which Company Mobile you would like to purchase-
                            \t1.Iphone
                            \t2.Samsung
                            \t3.Google
                            \t4.Realme
                            \t5.Exit""")
                            c = int(input("Enter your Choice : "))
                            print()
                            if c == 1:
                                self.display_company(self.iphone)
                                self.purchase(self.iphone, self.iphone_quantity)
                            elif c == 2:
                                self.display_company(self.samsung)
                                self.purchase(self.samsung, self.samsung_quantity)
                            elif c == 3:
                                self.display_company(self.google)
                                self.purchase(self.google, self.google_quantity)
                            elif c == 4:
                                self.display_company(self.realme)
                                self.purchase(self.realme, self.realme_quantity)
                            elif c == 5:
                                break
                            else:
                                print("Invalid Choice Entered")

                    elif ch == 2:
                        break
                    else:
                        print("Invalid Choice Entered")
                name = input("Enter your name : ")
                total_amount = self.bill(name)
                self.notify_me("Dear " + name,
                               """You have purchased mobile phones valued at Rs. [amount] from our electronic store.\nTHANK YOU. HAVE A NICE DAY""",
                               total_amount)

            elif cho == 2:
                break
            else:
                print("Invalid Choice Entered")

    def display_company(self, company_dict):
        print(" ")
        print("_" * 45)
        print("Phone Name".ljust(30, " "), "Phone Price".ljust(30, " "))
        print("_" * 45)
        for key, value in company_dict.items():
            print(str(key).ljust(30, " "), str(value).ljust(30, " "))
        print("_" * 45)
        print("\n")

    def view_sales_data(self):
        if self.sales_data:
            companies = list(self.sales_data.keys())
            sales_values = list(self.sales_data.values())
            plt.figure(figsize=(8, 5))  # Adjust figure size here
            plt.bar(companies, sales_values, color='skyblue')
            plt.xlabel('Mobile Companies')
            plt.ylabel('Total Sales (Rs)')
            plt.title('Total Sales by Company')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--')  # Change grid style
            plt.tight_layout()  # Adjust layout for better spacing
            plt.show()

            plt.figure(figsize=(8, 5))
            companies = ['iPhone', 'Samsung', 'Google', 'Realme']
            quantities = [sum(self.iphone_quantity.values()), sum(self.samsung_quantity.values()),
                          sum(self.google_quantity.values()), sum(self.realme_quantity.values())]
            plt.bar(companies, quantities, color='lightgreen')
            plt.xlabel('Mobile Companies')
            plt.ylabel('Total Quantity Available')
            plt.title('Total Quantity of Mobile Phones Available by Company')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--')
            plt.tight_layout()
            plt.show()
        else:
            print("No sales data available.")


# Instantiate and start the electronic store
store = ElectronicStore()
while True:
    print("Welcome to our Electronic Store")
    print("""Are you :-
    \t1.Staff
    \t2.Customer
    \t3.Exit""")
    person = int(input("Enter the above : "))
    print()
    if person == 1:
        store.staff_operations()
    elif person == 2:
        store.customer_operations()
    elif person == 3:
        break
    else:
        print("Please enter a valid option.")