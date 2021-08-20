class Customer(object):
    def __init__(self, name):
        self.name = name
        self.rentals = []
    
    def add_rental(self, arg):
        self.rentals.append(arg)

    def get_name(self):
        return self.name

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental Record for " + self.get_name() + "\n"

        for element in self.rentals:
            this_amount = 0
            each = element

            # determine amounts for each line

            if each.getMovie().getPriceCode() == Movie.REGULAR:
                total_amount += 2
                if each.getDaysRented() > 2:
                    this_amount += (each.getDaysRented() - 2) * 1.5
            elif each.getMovie().getPriceCode() == Movie.NEW_RELEASE:
                    total_amount += each.getDaysRented() * 3
            elif each.getMovie().getPriceCode() ==  Movie.CHILDRENS:
                    total_amount += 1.5
                    if (each.getDaysRented() > 3):
                        this_amount += (each.getDaysRented() - 3) * 1.5
            

            frequent_renter_points += 1

            if each.getMovie().getPriceCode() == Movie.NEW_RELEASE and each.getDaysRented() > 1:
                frequent_renter_points += 1

            result += "\t" + each.getMovie().getTitle() + "\t" +  str(this_amount) + "\n"
            total_amount += this_amount

        result = result + "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"
        return result


class Movie(object):
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self,  title, priceCode):
        self.title = title
        self.priceCode = priceCode

    def getPriceCode(self):
        return self.priceCode

    def setPriceCode(self, arg):
        self.priceCode = arg

    def getTitle (self):
        return self.title


class Rental(object):
    def __init__(self, movie, daysRented):
        self.movie = movie
        self.daysRented = daysRented
    
    def getDaysRented(self):
        return self.daysRented
    
    def getMovie(self):
        return self.movie
