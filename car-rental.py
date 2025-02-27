class Vehicle:
  def __init__(self, brand, model, year, rental_price_per_day):
    self.brand = brand
    self.model = model
    self.year = year
    self.rental_price_per_day = rental_price_per_day

  def display_info(self):
    print(f"{self.brand} {self.model}, Year: {self.year}, Rental price: {self.rental_price_per_day}$ /day")

  def calculate_rental_cost(self, days):
    return self.rental_price_per_day * days
  
class Car(Vehicle):
  def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
    super().__init__(brand, model, year, rental_price_per_day)
    self.seating_capacity = seating_capacity

  def display_info(self):
    print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental price: {self.get_rental_price()}$ /day")

class Bike(Vehicle):
  def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
    super().__init__(brand, model, year, rental_price_per_day)
    self.engine_capacity = engine_capacity

  def display_info(self):
    print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental price: {self.get_rental_price()}$ /day")