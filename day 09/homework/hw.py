# 2. დროში მოგზაურობის პროგრამა

# მომხმარებლის ასაკის, ამჟამინდელი წლის და დროში მოგზაურობის ასაკის მოთხოვნა
current_age = int(input("რამდენი წლის ხარ ამჟამად? "))
current_year = int(input("რომელია ამჟამინდელი წელი? "))
time_travel_years = int(input("რამდენი წლით გსურთ დროში მოგზაურობა? "))

# გამოთვლა
future_year = current_year + time_travel_years
future_age = current_age + time_travel_years

# შედეგების დაბეჭდვა
print(f"თქვენი დროში მოგზაურობის შემდეგ იქნება {future_year} წელი და თქვენ იქნებით {future_age} წლის.")