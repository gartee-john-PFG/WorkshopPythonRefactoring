from approvaltests.approvals import verify
from approvaltests.combination_approvals import verify_all_combinations
from customer import Customer, Movie, Rental

def test_what_does_customer_statement_do():
    cust = Customer("Test Customer")
    movie = Movie("Star Wars", Movie.REGULAR)
    rental = Rental(movie,2)
    cust.add_rental(rental)

    result = cust.statement()
    
    verify(result)