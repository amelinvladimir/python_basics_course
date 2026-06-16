# Пример типичного использования

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine(self)

    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")

    class Engine:
        def __init__(self, car):
            self.status = "Off"
            self.car = car

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "Off"
            print("Engine stopped")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()