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
        self.__total_meal = 0
        self.__total_bazar = 0
        self.meal_rate = 0
        self.days = [] 
        self.daily_meal = []
        self.daily_bazar = []

    @property
    def total_meal(self):
        return self.__total_meal

    @total_meal.setter
    def total_meal(self, value):
        self.__total_meal = value
   
    @property
    def total_bazar(self):
        return self.__total_bazar

    @total_bazar.setter
    def total_bazar(self, value):
        self.__total_bazar = value
