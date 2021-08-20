# from approvaltests.approvals import verify
from approvaltests.combination_approvals import verify_all_combinations
from customer import Customer, Movie, Rental

def test_what_does_customer_statement_do():
    customer_name = ["Test Customer"]
    movie_name = ["Star Wars"]
    price_code = [Movie.REGULAR, Movie.CHILDRENS, Movie.NEW_RELEASE]
    days_rented = [2, 3, 4]

    # result = make_statement(customer_name, movie_name, price_code)
    
    # verify(result)
    verify_all_combinations(make_statement,[customer_name, movie_name, price_code, days_rented])

def make_statement(customer_name, movie_name, price_code, days_rented):
    cust = Customer(customer_name)
    movie = Movie(movie_name, price_code)
    rental = Rental(movie, days_rented)
    cust.add_rental(rental)

    result = cust.statement()
    return result