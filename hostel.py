from month import DailyBazar, DailyMeal, Month

class Hostel:
    def __init__(self, name) -> None:
        self.name = name 
        self.members = []
        self.admins = []
        self.months_data = {}
    
    
    def add_daily_meal(self, member,day_number, month, year, meal_quantity):
        daily_meal_data = DailyMeal(member,day_number,meal_quantity)
        for key, value in self.months_data.items():
            if key == month+year:
                value.daily_meal.append({member:daily_meal_data})
                value.total_meal += meal_quantity
                print("Daily meal added")
                return
        print("Month sheet not found !")

    def add_daily_bazar(self, member,day_number, month, year, bazar_description, bazar_amount):
        daily_bazar_data = DailyBazar(member,day_number,bazar_description, bazar_amount)
        for key, value in self.months_data.items():
            if key == month+year:
                value.daily_bazar.append({member:daily_bazar_data})
                value.total_bazar += bazar_amount
                print("Daily bazar added")
                return
        print("Month sheet not found !")
            
    def view_single_member_month_data(self, member, month, year):
        month_year_key = f"{month}{year}"
        if month_year_key in self.months_data:
            this_month_data = self.months_data[month_year_key]
            total_meal = 0
            total_bazar = 0
            data = {str(day): {'meal': '-', 'bazar': '-' , 'bazar_description': '-'} for day in range(1, 32)}
            
            for daily_meal_data in this_month_data.daily_meal:
                if member in daily_meal_data:
                    day_number = str(daily_meal_data[member].day_number)
                    data[day_number]['meal'] = daily_meal_data[member].meal_quantity
                    total_meal += daily_meal_data[member].meal_quantity
            
            for daily_bazar_data in this_month_data.daily_bazar:
                if member in daily_bazar_data:
                    day_number = str(daily_bazar_data[member].day_number)
                    data[day_number]['bazar'] = daily_bazar_data[member].bazar_amount
                    total_bazar += daily_bazar_data[member].bazar_amount
                    data[day_number]['bazar_description'] = daily_bazar_data[member].bazar_description
            
            print(f"\n\t------- Monthly Data of Month: {month}, Year: {year} of {member.name} -------")
            print("\tDate\tMeal\tBazar\tBazar Description")
            print('\t---------------------------------------------')

            for day, values in data.items():
                print(f"\t{day}\t{values['meal']}\t{values['bazar']} BDT\t{values['bazar_description']}")

            print("\n\tYour total meal qunatity of this month: ", total_meal)
            print("\tYour total Bazar amount of this month: ", total_bazar, "BDT")
            print('------------------------------------------------------------------------')


        else:
            print(f"Sorry! Month: {month} & Year: {year} of data not found ")


    def view_all_member_month_data(self, month, year):
        month_year_key = f"{month}{year}"
        if month_year_key in self.months_data:
            this_month_data = self.months_data[month_year_key]
            try: 
                meal_rate =  this_month_data.total_bazar / this_month_data.total_meal
            except(ZeroDivisionError):
                meal_rate = "There is no meal"

            meal_data = {str(day): [] for day in range(1, 32)}
            for daily_meal_data in this_month_data.daily_meal:
                for daily_meal_obj in daily_meal_data.values():
                    day_number = daily_meal_obj.day_number
                    meal_data[day_number].append(daily_meal_obj)

            
            meal_array = [['-' for _ in range(len(self.members)+1)] for _ in range(31)]
            # Set the first column values to 1 through 31
            for i in range(31):
                meal_array[i][0] = i + 1
            

           
            for key, value in meal_data.items():
                for mem in self.members:
                    for x in value:
                        if mem == x.member:
                            meal_array[int(key)-1][self.members.index(mem)+1] = x.meal_quantity
                      
    
            print("\n\t------- All Member's Meal -------")
            print("\tDate", end="")
            for mem in self.members:
                print(f"\t{mem.name}" , end="")
            print("")
            print('\t---------------------------------------------')

            for row in meal_array:
                for col in row:
                    print(f"\t{col}", end="")
                print("")


            bazar_array = [['-' for _ in range(len(self.members)+1)] for _ in range(31)]
            for i in range(31):
                bazar_array[i][0] = i + 1
            bazar_data = {str(day): [] for day in range(1, 32)}
            for daily_bazar_data in this_month_data.daily_bazar:
                for daily_bazar_obj in daily_bazar_data.values():
                    day_number = daily_bazar_obj.day_number
                    bazar_data[day_number].append(daily_bazar_obj)
            
            for key, value in bazar_data.items():
                for mem in self.members:
                    for x in value:
                        if mem == x.member:
                            bazar_array[int(key)-1][self.members.index(mem)+1] = x.bazar_amount

            print("\n\t------- All Member's Bazar -------")
            print("\tDate", end="")
            for mem in self.members:
                print(f"\t{mem.name}" , end="")
            print("")
            print('\t---------------------------------------------')

            for row in bazar_array:
                for col in row:
                    print(f"\t{col}", end="")
                print("")

            total_meal = this_month_data.total_meal
            total_bazar = this_month_data.total_bazar
            meal_rate = total_bazar / total_meal

            print(f"\n\t Total Meal Of This Month is : {total_meal}")
            print(f"\n\t Total Bazar Of This Month is : {total_meal} BDT")
            print(f"Per Meal Rate is: {meal_rate} BDT")
            print('------------------------------------------------------------------------')
            

        else:
            print(f"Sorry! Month: {month} & Year: {year} of data not found ")

        print('\n------------------------------------------------------------------------')
        




    #Admin Activities

    def add_month(self, month_name,year):
        month = Month(month_name,year)
        # month_obj = {month_name+year : month}
        self.months_data[month_name+year] = month


    def add_admin(self, member):
        for mem in self.admins:
            if mem.name == member.name and mem.phone == member.phone:
                print(f"Name: {member.name} and Phone: {member.phone} this admin is already exit, try another!!!")
                return
        self.admins.append(member)
        print(f"Name: {member.name} and Phone: {member.phone} this admin added successfully !!!")




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
        print("\n------- All Member List -------\n")
        print("Name\tPhone\t\tEmail")
        print("-------------------------------------------------------")
        for member in self.members:
            print(f"{member.name}\t{member.phone}\t{member.email}")


 