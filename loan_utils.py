from loan import Loan

def loan_matcher(customer):
    loans = []

    #empréstimo pessoal
    loans.append(Loan("personal", 4))

    #empréstimo com garantia
    #sim***
    if customer.income <= 3000 and customer.age < 30 and customer.location == 'SP':
        loans.append(Loan("collaterelized", 3))
    
    #sim**
    elif customer.income > 3000 and customer.income < 5000 and customer.location == 'SP':
        loans.append(Loan("collateralized", 3))
    
    #sim***
    elif customer.income >= 5000 and customer.age < 30:
        loans.append(Loan("collateralized", 3))

    #empréstimo consignado
    if customer.income >= 5000:
        loans.append(Loan("payroll", 2))

    result = {
        "customer": customer.name,
        "loans": [{"type": Loan.loan_type, "taxes": Loan.loan_taxe} for Loan in loans]
    }

    return result