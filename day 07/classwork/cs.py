first_number = float(input("შეიყვანეთ პირველი რიცხვი: "))
second_number = float(input("შეიყვანეთ მეორე რიცხვი: "))

# მათემატიკური ოპერაციები
sum_result = first_number + second_number
difference_result = first_number - second_number
product_result = first_number * second_number
quotient_result = first_number / second_number if second_number != 0 else "ნული არ შეიძლება იყოს დივიზორი"

# შედეგების დაბეჭდვა
print(f"ჯამი: {sum_result}")
print(f"სხვაობა: {difference_result}")
print(f"პროდუქტი: {product_result}")
print(f"გატანა: {quotient_result}") 

 
