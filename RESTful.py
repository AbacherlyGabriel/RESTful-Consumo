import requests


class People:

    def __init__(self, url):
        self.url = url

    def list_all(self):
        response = requests.get(self.url)
        status = response.status_code

        if status == requests.codes.ok:
            print(f'\n> Status Code: {status} (OK)\n')

            for person in response.json():
                print(person)

        else:
            print(f'[!] Status Code: {status}')

    def person(self, identification):
        response = requests.get(self.url)
        status = response.status_code

        if status == requests.codes.ok:
            print(f'\n> Status Code: {status} (OK)\n')

            people = response.json()

            for person in people:
                if person['id'] == identification:
                    print(person)

        else:
            print(f'[!] Status Code: {status}')

    def add_person(self, person):
        response = requests.post(self.url, json=person)
        status = response.status_code

        if status == requests.codes.ok:
            print(f'\n> Status Code: {status} (OK)\n')

            print(f'{person["name"]} Successfully Added.')
        else:
            print(f'[!] Status Code: {status}')

    def delete_person(self, identification):
        person = self.url + '/' + str(identification)
        response = requests.delete(person)
        status = response.status_code

        if status == requests.codes.ok:
            print(f'\n> Status Code: {status} (OK)\n')

            print(f'User {identification} Successfully Removed.')
        else:
            print(f'[!] Status Code: {status}')
