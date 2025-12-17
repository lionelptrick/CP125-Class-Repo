# Lab 02 Exercise 9: Level Up Calculator
# Write your code below:

def calculate_xp_required(current_level):
    """Return XP needed to level up (level * 100)."""
    # TODO: Implement this function
    return current_level * 100
    
def can_level_up(xp_remaining, xp_required):
    """Return True if xp_remaining >= xp_required."""
    # TODO: Implement this function
    return xp_remaining >= xp_required
    
def simulate_leveling(total_xp):
    level = 1
    xp_remaining = total_xp
    xp_required = calculate_xp_required(current_level)

    while can_level_up(xp_remaining, xp_required):
        xp_required = calculate_xp_required(current_level)
        xp_remaining = calculate_xp_required(current_level)
        current_level =+ 1

    return current_level, xp_remaining
# Test your code here
print("Testing Level Up Calculator...")
