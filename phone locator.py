import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone

number=input("Enter your phone number:")
ch= phonenumbers.parse(number,"CH")
print("Country- ",geocoder.description_for_number(ch,"en"))

from phonenumbers import carrier

servn=phonenumbers.parse(number,"RO")
print("ISP- ",carrier.name_for_number(servn,"en"))

timezo=timezone.time_zones_for_number(ch)

print(timezo)