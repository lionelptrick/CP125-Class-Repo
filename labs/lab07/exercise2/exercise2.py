def withdraw(accounts, card_number, amount):
    # TODO: Your code here
    if card_number not in accounts:
        return "Card Not Found"
    
    balance = accounts[card_number]

    if balance < amount:
        return "Insufficient Funds"
    
    accounts[card_number] = balance - amount

    return float(accounts[card_number])

    pass

accounts = {
    "4111-1111": 500.00,
    "4222-2222": 80.00,
}
print(withdraw(accounts, "4111-1111", 200.00))
print(withdraw(accounts, "4222-2222", 100.00))
print(withdraw(accounts, "9999-0000", 50.00))
