
import phonenumbers
from phonenumbers import geocoder

phone = input('Digite o telefone no seguinte formato +552126481374: ')

phone_number = phonenumbers.parse(phone)


print(geocoder.description_for_number(phone_number, 'pt'))