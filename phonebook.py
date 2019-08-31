

class Contact:
    def __init__(self, firstname, lastname, telnumber, chosen=False, *args, **kwargs):
        self.firstname = firstname
        self.lastname = lastname
        self.telnumber = telnumber
        self.chosen = chosen
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        if not self.chosen:
            chosen_info = "нет"
        else:
            chosen_info = "да"

        additional_info = ''
        for item in self.args:
            additional_info += f"\n\t\t{item}"
        for k, v in self.kwargs.items():
            additional_info += f"\n\t\t{k}: {v}"

        return f"Имя: {self.firstname}\n" \
            f"Фамилия: {self.lastname}\n" \
            f"Телефон: {self.telnumber}\n" \
            f"В избранных: {chosen_info}\n" \
            f"Дополнительная информация:" \
            f"{additional_info}"


class PhoneBook:
    def __init__(self, namephonebook, list_contacts=[]):
        self.namephonebook = namephonebook
        self.list_contacts = list_contacts

    def display(self):
        for item in self.list_contacts:
            print(item)

    def add_contact(self, contact):
        self.list_contacts.append(contact)

    def del_contact(self, telnumber):
        contacts_for_delete = list(filter(lambda x: x.telnumber == telnumber, self.list_contacts))
        self.list_contacts.remove(contacts_for_delete[0])

    def search_chosen_contacts(self):
        return list(filter(lambda x: x.chosen, self.list_contacts))

    def search_contacts_by_names(self, firstname, lastname):
        return list(filter(lambda x: x.firstname == firstname and x.lastname == lastname, self.list_contacts))


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(jhon)
    alex = Contact('Alex', 'Smith', '+71234567810', chosen=True, telegram='@alex', email='alex@smith.com')
    print(alex)
    anna = Contact('Anna', 'Smith', '+71234567811', telegram='@anna', email='anna@smith.com')
    print(anna)
    my_pb = PhoneBook('my')
    my_pb.add_contact(jhon)
    my_pb.add_contact(alex)
    my_pb.add_contact(anna)
    print("\n\nКонтакты из телефонной книги\n")
    my_pb.display()
    print("\n\nПосле удаления контакта с номером +71234567810\n")
    my_pb.del_contact('+71234567809')
    my_pb.display()
    print("\n\nСписок избранных контактов:")
    for item in my_pb.search_chosen_contacts():
        print(item)
    print("\n\nПоиск по фамилии и имени:")
    for item in my_pb.search_contacts_by_names('Anna', 'Smith'):
        print(item)




