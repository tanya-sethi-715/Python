from datetime import datetime

class CarRental:
    def __init__(self, available_cars):
        self.available_cars = available_cars
        self.rental_records = {}

    def display_available_cars(self):
        print("Available Cars:")
        for car, stock in self.available_cars.items():
            print(f"{car}: {stock} available")

    def rent_hourly(self, car, num_cars, rental_time):
        if car in self.available_cars and self.available_cars[car] >= num_cars and num_cars > 0:
            self.available_cars[car] -= num_cars
            self.rental_records[car] = (num_cars, rental_time, 'hourly')
            print(f"{num_cars} {car} rented hourly at {rental_time}.")
        else:
            print("Sorry, requested number of cars not available.")

    def rent_daily(self, car, num_cars, rental_time):
        if car in self.available_cars and self.available_cars[car] >= num_cars and num_cars > 0:
            self.available_cars[car] -= num_cars
            self.rental_records[car] = (num_cars, rental_time, 'daily')
            print(f"{num_cars} {car} rented daily at {rental_time}.")
        else:
            print("Sorry, requested number of cars not available.")

    def rent_weekly(self, car, num_cars, rental_time):
        if car in self.available_cars and self.available_cars[car] >= num_cars and num_cars > 0:
            self.available_cars[car] -= num_cars
            self.rental_records[car] = (num_cars, rental_time, 'weekly')
            print(f"{num_cars} {car} rented weekly at {rental_time}.")
        else:
            print("Sorry, requested number of cars not available.")

    def return_cars(self, car, rental_time):
        if car in self.rental_records:
            num_cars, rent_start, rental_mode = self.rental_records[car]
            del self.rental_records[car]
            self.available_cars[car] += num_cars
            rental_end = datetime.now()
            rental_period = rental_end - rent_start
            total_bill = 0
            if rental_mode == 'hourly':
                total_bill = num_cars * rental_period.seconds / 3600 * 10
            elif rental_mode == 'daily':
                total_bill = num_cars * rental_period.days * 40
            elif rental_mode == 'weekly':
                total_bill = num_cars * rental_period.days / 7 * 150
            print(f"{num_cars} {car} returned. Total bill: ${total_bill}")
        else:
            print("Car not rented or already returned.")

class Customer:
    def request_cars(self, car_rental):
        car_rental.display_available_cars()
        car = input("Enter the car you want to rent: ")
        num_cars = int(input("Enter the number of cars you want to rent: "))
        rental_mode = input("Enter the rental mode (hourly/daily/weekly): ")
        rental_time = datetime.now()
        if rental_mode == 'hourly':
            car_rental.rent_hourly(car, num_cars, rental_time)
        elif rental_mode == 'daily':
            car_rental.rent_daily(car, num_cars, rental_time)
        elif rental_mode == 'weekly':
            car_rental.rent_weekly(car, num_cars, rental_time)
        else:
            print("Invalid rental mode.")

    def return_cars(self, car_rental):
        car = input("Enter the car you want to return: ")
        return_time = datetime.now()
        car_rental.return_cars(car, return_time)

def main():
    available_cars = {'Toyota Camry': 5, 'Honda Accord': 3, 'Ford Mustang': 2}
    car_rental = CarRental(available_cars)
    customer = Customer()

    while True:
        print("\n1. Display available cars\n2. Rent a car\n3. Return a car\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            car_rental.display_available_cars()
        elif choice == '2':
            customer.request_cars(car_rental)
        elif choice == '3':
            customer.return_cars(car_rental)
        elif choice == '4':
            print("Thank you for using our car rental service!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
