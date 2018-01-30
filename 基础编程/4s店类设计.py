class CarStore(object):
    def order(self,car_type):
        if car_type=='索纳塔':
            return Suonata()
        elif car_type=='名图':
            return Mingtu()

    

class Car(object):
    def msice(self):
        print('音乐响起')
    def move(self):
        print('可以开走')

class Suonata(Car):
    pass

class Mingtu(Car):
    pass


car_store=CarStore()

car=car_store.order('索纳塔')
car.move()
car.msice()