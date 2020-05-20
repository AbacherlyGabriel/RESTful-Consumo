from RESTful import People


def main():
    response = People('http://ec2-18-231-63-74.sa-east-1.compute.amazonaws.com:8080/person')

    # response.list_all()

    # response.person(101)

    # response.add_person({'id': 999, 'name': 'Test', 'lastName': 'Testing', 'email': 'test@usp.br'})
    # response.list_all()

    response.delete_person(999)
    response.list_all()


if __name__ == '__main__':
    main()
