# POO

class Hotel:
    def __init__(self, max_number_guests, free_parking_spaces):
        self.max_number_guests = max_number_guests
        self.free_parking_spaces = free_parking_spaces
        self.guests = 0

    def add_guests(self, guests):
        self.guests += guests

    def checkout(self, guests):
        self.guests -= guests

    def total_ocupation(self):
        return self.guests

def run():
    my_hotel = Hotel(50, 10)
    print('''
    * * * * * * * * * * * * *
           HOTEL MATUS
    * * * * * * * * * * * * *
    ''')

    print(f'Maximum number of guests: {my_hotel.max_number_guests}')
    print(f'Number of free parking spaces: {my_hotel.free_parking_spaces}')

    guests_number = int(input('\nAdd the number of guests: '))
    my_hotel.add_guests(guests_number)

    people_exits = int(input('Number of people exits: '))
    my_hotel.checkout(people_exits)

    print(f'Total occupancy: {my_hotel.total_ocupation()}')



if __name__ == '__main__':
    run()