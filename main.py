from customer import Customer
from loan_utils import loan_matcher

if __name__ == '__main__':
    customer_data = Customer("Erikaya", "123.456.789-10", 29, "BH", 3000)
    result = loan_matcher(customer_data)
    print(result)