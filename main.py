from hostel import Hostel
from month import DailyBazar, DailyMeal, Month
from users import Member, Admin
import datetime

x = datetime.datetime.now()


ash = Hostel("Ayman Super Hostel")

ranju_vai = Member("Ranju","01535798094", "1234", "ranju@email.com")
maruf_vai = Member("Maruf", "01770787848", "1234","maruf@gmail.com")
afridi = Member("Afridi","01704805886", "1234", "shahid@gmail.com")
kalin = Member('Kalin', "01912345678", "1234", "kalin@gmail.com")
nirob = Member("Nirob", "01770787881", "1234", "nirob@gmail.com")
mahin = Member("Mahin", "01712345678","1234", "mahin@gmail.com")

admin = Admin("Admin", "01558988666","1234", "admin@gmail.com")

ash.add_admin(admin)

admin.add_member(ash, ranju_vai)
admin.add_member(ash, maruf_vai)
admin.add_member(ash, afridi)
admin.add_member(ash, kalin)
admin.add_member(ash, nirob)
admin.add_member(ash, mahin)

admin.view_all_members(ash)
admin.add_month(ash,"5","2024")


nirob.add_daily_meal(ash, "13","5","2024",3)
nirob.add_daily_meal(ash, "12","5","2024",2)

afridi.add_daily_meal(ash, "13","5","2024",3)
afridi.add_daily_meal(ash, "11","5","2024",3)
afridi.add_daily_meal(ash, "12","5","2024",2)
# print(ash.months_data['52024'].total_bazar)

afridi.add_daily_bazar(ash,'20', "5",'2024',"meat", 550)
# print(ash.months_data['52024'].total_bazar)

# afridi.view_all_member_month_data(ash,'5','2024')

# afridi.view_single_member_month_data(ash, "5","2024")

# print(ash.months_data["52024"].daily_meal[0][afridi].day_number)
# print(ash.months_data["52024"].daily_meal[0][afridi].meal_quantity)

currentUser = None

while True:
    print(f"\n\t Welcome to {ash.name}")
    print("----------------------------------------------------------")
    print("\nAre Admin or Member ?")
    print("Press 1 : for admin")
    print("Press 2 : for member")
    print("Press 0 : for end the program")
    opUser = input("\n\tPlease enter here : ")

    if opUser == '0':
        print("Thank you for staying with us.")
        break
    
    #Admin UI
    elif opUser == '1':
        phone = input("\tEnter Your Phone Number: ")
        password = input("\tEnter the password: ")

        for admin in ash.admins:
            if admin.phone == phone and admin.password == password:
                currentUser = admin
                break
        if not currentUser:
            print("Invalid information, Try Again !!!")
        else:
            while True:
                print("\nHello Admin...")
                print("\nOptions:")
                print("\t 1. Add Member")
                print("\t 2. Delete Member")
                print("\t 3. View All Member")
                print("\t 4. View All Data of a Month")
                print("\t 5. Add a Month")
                print("\t 0. Log Out")

                op = input("\nPlease enter your choice: ")

                if op == '1':
                    name = input("Enter the name: ")
                    email = input("Enter the email: ")
                    password = input("Enter the password: ")
                    phone = input("Enter the phone: ")
                    member = Member(name, phone, password, email)
                    currentUser.add_member(ash, member)
                
                elif op == '2':
                    name = input("Enter the name: ")
                    phone = input("Enter the phone: ")
                    currentUser.delete_member(ash,name, phone)
                
                elif op == '3':
                    currentUser.view_all_members(ash) 

                elif op == '4':
                    month = input("Enter the Month No ( 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 ): ")
                    year = input("Enter the Year No ( Example: 2024 ): ")
                    currentUser.view_all_member_month_data(ash,month, year)
                
                elif op == '5':
                    month = input("Enter the Month No ( 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 ): ")
                    year = input("Enter the Year No ( Example: 2024 ): ")
                    currentUser.add_month(ash,month, year)
                
                elif op == '0':
                    currentUser = None
                    break
                    
                else:
                    print("\t !!! Invalid Input !!!")

    elif opUser == '2':
        while True:
            print("\nHello Member...")
            print("Press 1 : for Login")
            print("Press 0 : for Main Menu")
            opLR = input("\n\tPlease enter here : ")
            
            if opLR == '0':
                break

            elif opLR == '1': #login
                phone = input("\nEnter Your Phone Number: ")
                password = input("Enter your password: ")
                for mem in ash.members:
                    if mem.phone == phone and mem.password == password:
                        currentUser = mem
                        break
                if not currentUser:
                    print('\n\tUser not found !!!')
                
                else:
                    while True:
                        print(f"\nHello {currentUser.name} !!!")
                        print("Options:")
                        print("\t 1. Add Daily Meal")
                        print("\t 2. Update Daily Meal")
                        print("\t 3. Add Daily Bazar")
                        print("\t 4. Update Daily Bazar")
                        print("\t 5. View Your All Data of A Month")
                        print("\t 6. View All Member's Data of A Month")
                        print("\t 0. Log Out")

                        op = input("\nPlease enter your choice: ")

                        if op == '1':
                            print("!!! Don't use 0 before single digit number !!!")
                            day = input("Enter the Date: ")
                            month = input('Enter the month No: ')
                            year = input("Enter the Year: ")
                            meal_quantity = int(input("Enter Your Today's Meal Quantity: "))
                            currentUser.add_daily_meal( ash, day, month, year, meal_quantity)

                        elif op == '5':
                            print("!!! Don't use 0 before single digit number !!!")
                            month = input('Enter the month No: ')
                            year = input("Enter the Year: ")
                            currentUser.view_my_month_data(ash, month, year)
                        
                        elif op == '6':
                            print("!!! Don't use 0 before single digit number !!!")
                            month = input('Enter the month No: ')
                            year = input("Enter the Year: ")
                            currentUser. view_all_member_month_data(ash, month, year)


                        elif op == '0':
                            currentUser = None
                            break   
                        else:
                            print("\t !!! Invalid Input !!!")