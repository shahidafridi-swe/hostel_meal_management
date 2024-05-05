
class DailyMeal:
    def __init__(self, member, day_number, meal_quantity) -> None:
        self.member = member
        self.day_number = day_number
        self.meal_quantity = meal_quantity

class DailyBazar:
    def __init__(self, member, day_number, bazar_description, bazar_amount) -> None:
        self.member = member
        self.day_number = day_number
        self.bazar_description = bazar_description
        self.bazar_amount = bazar_amount


class Month:
    def __init__(self, name,year) -> None:
        self.name = name
        self.year = year 
        self.total_meal = 0
        self.total_bazar = 0
        self.meal_rate = 0
        self.days = []
        self.daily_meal = {}
        self.daily_bazar = {}

class Hostel:
    def __init__(self, name) -> None:
        self.name = name 
        self.members = []
        self.months_data = {}
    
    
    def add_daily_meal(self, member,day_number, month, year, meal_quantity):
        daily_meal_data = DailyMeal(member,day_number,meal_quantity)
        for key, value in self.months_data.items():
            if key == month+year:
                value.daily_meal.append({member:daily_meal_data})
                print("Daily meal added")
                return
        print("Month sheet not found !")

    def add_daily_meal(self, member,day_number, month, year, bazar_description, bazar_amount):
        daily_bazar_data = DailyBazar(member,day_number,bazar_description, bazar_amount)
        for key, value in self.months_data.items():
            if key == month+year:
                value.daily_meal.append({member:daily_bazar_data})
                print("Daily bazar added")
                return
        print("Month sheet not found !")
            
    
    def single_member_month_data(self, member, month, year):
        result = {}
        for key, value in self.months_data.items():
            if key == month+year:
                for k,v in value.daily_meal.items():
                    if k == 



    #Admin Activities

    def add_month(self, month_name,year):
        month = Month(month_name,year)
        month_obj = {month_name+year : month}
        self.months_data.append(month_obj)


    def add_member(self, member):
        for mem in self.members:
            if mem.name == member.name and mem.phone == member.phone:
                print(f"Name: {member.name} and Phone: {member.phone} this member is already exit, try another!!!")
                return
        self.members.append(member)
        print(f"Name: {member.name} and Phone: {member.phone} this member added successfully !!!")


    def find_member(self, member_name, member_phone):
        for mem in self.members:
            if mem.name == member_name and mem.phone == member_phone:
                return mem
        return None

    def update_member(self, member_name, member_phone):
        member = self.find_member(member_name,member_phone)    

        if member:
            print("Your selected member's current value:\n")
            print("Name\tPhone\tEmail")
            print("-------------------------------------------------------")

            print(f"{member.name}\t{member.phone}\t{member.email}")

            name = input('Enter the updated name: ')
            phone = input('Enter the updated phone: ')
            email = input('Enter the updated email: ')

            member.name = name
            member.phone = phone
            member.email = email

            print(f"Name: {member.name}, Phone: {member.phone}, Email: {member.email} updated successfully !")
        else:
            print("Member not found !!!")
    
    def delete_member(self, member_name, member_phone):
        member = self.find_member(member_name, member_phone)
        if member:
            self.members.remove(member)
            print("Member deleted successfully !!!")
        else:
            print("Member not found to delete !!!")
    
    def view_all_members(self):
        print("All Member List: \n")
        print("Name\tPhone\tEmail")
        print("-------------------------------------------------------")
        for member in self.members:
            print(f"{member.name}\t{member.phone}\t{member.email}")

