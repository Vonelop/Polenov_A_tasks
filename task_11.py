class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        self.name = new_name

    @property
    def calories(self):
        return self.calories

    @calories.setter
    def calories(self, new_calories):
        self.calories = new_calories

    def is_healthy(self):
        if self.calories < 200:
            return True

    def is_delicious(self):
        if self.name != None:
            return True

