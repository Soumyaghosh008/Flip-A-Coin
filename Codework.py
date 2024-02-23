import random

def coin_flip():
    # Generate a random number (0 or 1)
    result = random.randint(0, 1)

    # Map the result to 'Heads' or 'Tails'
    if result == 0:
        return 'Heads'
    else:
        return 'Tails'

# Test the coin flip function
flip_result = coin_flip()
print(f"The coin landed on: {flip_result}")