import csv
import os

CAR_TYPES = {'Car': 'car', 'Truck': 'truck', 'SpecMachine': 'spec_machine'}

class CarBase:
    def __init__(self, brand=None, photo_file_name=None, carrying=None):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        root, extention = os.path.splitext(self.photo_file_name)
        if extention == '.jpeg' or '.jpg' or '.png' or '.gif':
            return extention
        else:
            return False
        

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = CAR_TYPES['Car']
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = CAR_TYPES['Truck']
        self.body_width = 0
        self.body_height = 0
        self.body_length = 0
        self.body_volume = 0
      
        if body_whl:
            self.get_body_parameters(body_whl)      
        
    def get_body_parameters(self, body_whl):
        try:
            length, width, height = map(float, body_whl.split("x"))
        except ValueError:
            length ,width, height = [0, 0, 0]
            
        self.body_width = width
        self.body_height = height
        self.body_length = length
        self.body_volume = width * height * length      
        
    def get_body_volume(self):
        return self.body_volume
        

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = CAR_TYPES['SpecMachine']
        self.extra = extra
        


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
            if car_type == 'car' and photo_file_name and brand and carrying and passenger_seats_count:            
                car = Car(brand=brand, photo_file_name=photo_file_name, carrying=carrying, passenger_seats_count=passenger_seats_count)
                car_list.append(car)
            if car_type == 'truck' and photo_file_name and brand and carrying:
                truck = Truck(brand=brand, photo_file_name=photo_file_name, carrying=carrying, body_whl=body_whl)
                car_list.append(truck)
            if car_type == 'spec_machine' and photo_file_name and brand and carrying  and extra:
                spec_machine = SpecMachine(brand=brand, photo_file_name=photo_file_name, carrying=carrying, extra=extra)
                car_list.append(spec_machine)
    return car_list
