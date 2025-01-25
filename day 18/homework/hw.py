def bank_system():
 
    balance = 1000  
    print("სალამი! ბანკის სისტემაში შედიხართ.")
    
    while True:
        print("\nაირჩიეთ მოქმედება:")
        print("1. შეამოწმეთ ანგარიშის ბალანსი")
        print("2. დაამატეთ თანხა")
        print("3. გამოიტანეთ თანხა")
        print("4. დატოვეთ სისტემა")
        
        action = int(input("თქვენი არჩევანი: "))
        
        if action == 1:
            print(f"თქვენი მიმდინარე ბალანსი არის: {balance} ლარი")
        
        elif action == 2:
            deposit_amount = float(input("კომპანიისთვის თანხის რაოდენობა: "))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"თქვენ წარმატებით დაამატეთ {deposit_amount} ლარი. ახლანდელი ბალანსი: {balance} ლარი")
            else:
                print("გთხოვთ, შეიყვანოთ დადებითი თანხა!")
        
        elif action == 3:
            withdrawal_amount = float(input("კომპანიისთვის თანხის რაოდენობა გამოსატანად: "))
            if withdrawal_amount > balance:
                print("მონაცემი არ არის საკმარისი თანხის გამოტანისთვის!")
            elif withdrawal_amount > 0:
                balance -= withdrawal_amount
                print(f"თქვენ წარმატებით გამოიტანეთ {withdrawal_amount} ლარი. ახლანდელი ბალანსი: {balance} ლარი")
            else:
                print("გთხოვთ, შეიყვანოთ დადებითი თანხა!")
        
        elif action == 4:
            print("თქვენ დატოვეთ სისტემა. გმადლობთ, რომ გამოგიყენეთ ჩვენი ბანკის სერვისი!")
            break
        
        else:
            print("არასწორი არჩევანი. გთხოვთ, აირჩიოთ მოქმედება ახალი.")

bank_system()
