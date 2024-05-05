class User:
    def __init__(self, name, phone, password, email) -> None:
        self.name = name
        self.phone = phone
        self.password = password
        self.email = email


class Admin(User):
    def __init__(self, name, phone, password, email) -> None:
        super().__init__(name, phone, password, email)

    def add_member(self, hostel, member):
        hostel.add_meber(member)

    def update_member(self, hostel, member_name, member_phone):
        hostel.update_member(member_name,member_phone)

    def delete_member(self, hostel, member_name, member_phone):
        hostel.delete_member(member_name,member_phone)

    def add_month(self, hostel, month, year):
        hostel.add_month(month,year)


class Member(User):
    def __init__(self, name, phone, password, email) -> None:
        super().__init__(name, phone, password, email)

    def add_daily_meal(self, hostel, date, month, year, meal_quantity):
        hostel.add_daily_meal(self, date, month, year, meal_quantity)
    
    def add_daily_bazar(self, hostel, date, month, year,bazar_description, amount):
        hostel.add_daily_bazar(self, date, month, year,bazar_description, amount)
    
    def view_my_month_data(self,hostel,month,year):
        hostel.single_member_month_data(self,month,year)
        
        






            

        


    
        

        