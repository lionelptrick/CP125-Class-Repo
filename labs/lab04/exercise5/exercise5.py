
def find_momentum_days(prices):
    if len(prices) < 2:
        return []

    changes = []
    for i in range(1, len(changes)):
        return True
    
    pass


# Test
prices = [100, 102, 105, 107, 106, 108, 112, 114]

result = find_momentum_days(prices)
print(f"Momentum days: {result}")  # Expected: [2, 5, 6]
