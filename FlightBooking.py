import random,re,time


class booking:
    Ecomomy = 'Economy'
    Business = 'Business'

class Seat:
    def __init__(self, row_number):
        self.row_number = row_number
    def __str__(self):
        return '{}'.format(self.row_number)

class SeatingArea:
    def __init__(self, booking_class, start_row, row_count, seats_row):
        self.booking_class = booking_class
        self.start_row = start_row
        self.seat_count = row_count * seats_row
        self.window_seat = row_count * 2
        self.other_seats = self.seat_count - self.window_seat





 def main():
    print '** Welcome to flight booking system **'
    while True:
        response = raw_input('Do you want to book a ticket now? ')
        match = re.search('yes|y', response, re.I)
        if not match:
            print 'Thanks for using flight booking system'
            break

        print 'Total number of seats available in Business and economy class is: '

        name = raw_input('What is passenger name: ')

        class_response = raw_input('which class you prefer? ')
        match = re.search('business|economy', class_response, re.I)
        if not match:
            print 'Thanks for using flight booking system, I am not able to understand your input'
            break

        seat_response = raw_input('Do you have window or Aisle preferance? ')
        match = re.search('window|aisle', seat_response, re.I)
        if not match:
            print 'Thanks for using flight booking system, I am not able to understand your input'
            break

        print 'Thanks, I am booking class {}, {} seat, waiting for 2 sec'.format(class_response, seat_response)
        time.sleep(2)

        print 'Passenger {} has seat number {} and bookingId {}'.format(name, 1, 1)
    if __name__ == '__main__':
        main()





