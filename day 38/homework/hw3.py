def get_first_letter_position(name):
    first_letter = name[0].lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.index(first_letter) + 1  # ანბანზე მდებარეობა 1-დან იწყება

# შეკითხვა მომხმარებლისთვის
name = input("თქვენი სახელი: ")
print(f"{name}ის პირველი ასო '{name[0]}' არის {get_first_letter_position(name)}-ე ადგილას ანბანში.")
