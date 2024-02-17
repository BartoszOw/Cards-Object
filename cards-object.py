
# Podstawowa klasa Wizytówki

class Card:
    def __init__(self, name, sec_name, company, job, mail):
        self.name = name
        self.sec_name = sec_name
        self.company = company
        self.job = job
        self.mail = mail

        self._name_length = 0
        self._sec_name_length = 0

    def __str__(self):
        return f'{self.name} {self.sec_name} {self.mail}'
    
    def contact(self):
        return f"Kontaktuje się z {self.name} {self.sec_name} {self.job} {self.mail}"

    def name_length(self):
        self._name_length += len(self.name)
        self._sec_name_length += len(self.sec_name)
        return self._name_length, self._sec_name_length
    

# Dziedziczenie - Bazowa Wizytowka

class BaseContact(Card):
    def __init__(self, phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone_number = phone_number

    def contact(self):
        return f"Wybieram numer +48 {self.phone_number} i dzwonie do {self.name} {self.sec_name}"

    def label_length(self):
        super().name_length()
        return self._name_length, self._sec_name_length

    
# Dziedziczenie - Firmowa Wizytowka
    
class BusinessContact(BaseContact):
    def __init__(self, job_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_phone = job_phone

    def contact(self):
        return f"Wybieram numer +48 {self.job_phone} i dzwonie do {self.name} {self.sec_name}"

    def label_length(self):
        super().label_length()
        return self._name_length, self._sec_name_length

# Wyniki wybierania numerów telefonu

first_person = BaseContact(name='Aga', sec_name='Bąk', company='AGG', job='sekretarka', mail='agabak@gmail.com', phone_number='505050219')
print(first_person.contact())
print(first_person.label_length())
first_person = BusinessContact(name='Aga', sec_name='Bąk', company='AGG', job='sekretarka', mail='agabak@gmail.com', job_phone='450230105', phone_number='505050129')
print(first_person.contact())
print(first_person.label_length())





sec_person = Card(name='Bart', sec_name='Kot', company='AKA', job='kierowca', mail='barton@gmail.com')
third_person = Card(name='Fran', sec_name='Pies', company='MILO', job='ochroniarz', mail='franpies@gmail.com')
fourth_person = Card(name='Geralt', sec_name='Król', company='GENO', job='sprzatacz', mail='geralt@gmail.com')
fifth_person = Card(name='Jacob', sec_name='Bek', company='BANO', job='szef', mail='jcb@gmail.com')

card_list = [first_person, sec_person, third_person, fourth_person, fifth_person]

# Posortowane Po "imionach, nazwiskach i mailach" instancje

by_name = sorted(card_list, key=lambda card: card.name)
by_sec_name = sorted(card_list,key=lambda card: card.sec_name)
by_mail = sorted(card_list, key=lambda card: card.mail)


#for i in by_sec_name:
#    print(i.name, i.sec_name, i.mail)








