from task_11 import Dessert

class JellyBean(Dessert):
    def __int__(self, name, calories, flavor=None):
        super().__init__(name, calories)
        self.flavor = flavor

    @property
    def flavor(self):
        return self.flavor

    @flavor.setter
    def flavor(self, new_flavor):
        self.flavor = new_flavor
        