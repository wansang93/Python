class Car:
    color = None
    speed = 0

    def up_speed(self, value):
        self.speed += value
    
    def down_speed(self, value):
        self.speed -= value

my_value = 0

car1 = Car()
car2 = Car()


car1.color = 'red'
car1.speed = 50

car1.up_speed(50)

print(car1.speed)
print(car1)