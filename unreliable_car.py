from car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            distance = 0
            return distance

        # if random_number >= self.reliability:
        #     distance = 0
        # driven = super().drive(distance)
        # return driven
