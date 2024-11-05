Desafio de Código
A proposta da aplicação que vamos desenvolver em conjunto é disponibilizar a uma pessoa as modalidades de empréstimo as quais ela tem acesso de acordo com algumas variáveis.

Devemos prover os seguintes modelos de empréstimo:

Empréstimo pessoal. Taxa de juros: 4%
Empréstimo com garantia. Taxa de juros: 3%
Consignado. Taxa de juros: 2%
Abaixo seguem as regras de negócio relacionadas a concessão de empréstimo de acordo com o perfil da pessoa:

Empréstimo pessoal	Empréstimo c/ garantia	Consignado
Salário <= 3000	Sim	Sim***	Não
Salário > 3000 e < 5000	Sim	Sim**	Não
Salário => 5000	Sim	Sim*	Sim

* Clientes com menos de 30 anos
** Clientes que residem em SP
*** Clientes com menos de 30 anos que residem em SP
Utilização da aplicação:
A aplicação deve receber como entrada essas informações:

input
{
  "customer": {
    "name": "Erikaya",
    "cpf": "123.456.789-10",
    "age": 29,
    "location": "BH",
    "income": 3000
  }
}
Para fins de simplicidade, considere que vamos sempre receber os dados corretos (tipos e formatos)

E deve responder essas informações:

output
{
  "customer": "Erikaya",
  "loans": [
    {
      "type": "personal",
      "taxes": 1
    }
  ]
}
