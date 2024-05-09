def apt_search1(city: str, max_rent: int, min_beds: int, pets_allowed: bool = False):
    if pets_allowed:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} '
              f'bedroom apartments that allow pets, all within a budget of ${max_rent} per month.')
    else:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} '
              f'bedroom apartments, all within a budget of ${max_rent} per month.')

# Allows pets
apt_search1('Detroit', 1000, 3, True)
# Does not allow pets
apt_search1('Chicago', 3000, 1)
print()


def apt_search2(city: str, max_rent: int, min_beds: int = 2, pets_allowed: bool = False):
    if min_beds and pets_allowed:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} '
              f'bedroom apartments that allow pets, all within a budget of ${max_rent} per month.')
    else:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} '
              f'bedroom apartments, all within a budget of ${max_rent} per month.')

# Both omitted
apt_search2('Dallas', 1000)
# Just min_beds
apt_search2('NYC', 1000000, 5)
# Just pets_allowed
apt_search2('Seattle', 500, pets_allowed=True)
print()

user_number = int(input('Enter a number >> '))
user_text = str(input('Enter some words >> '))
print()

# Write a lambda function that adds 100 to any given number
plus_one_hundred = lambda x: float(x + 100)
final_total = plus_one_hundred(user_number)
print(f'This is your number + 100: {final_total}')

# Write a lambda function that squares any given number
square_num = lambda x: int(x ** 2)
final_total = square_num(user_number)
print(f'This is your number squared: {final_total}')

# Write a lambda function that concatenates “- “ before any string
concatenate = lambda y: '- ' + y
final_words = concatenate(user_text)
print(final_words)

# Write a lambda function that divides any number by 3
divide_by_three = lambda x: float(x / 3)
final_total = divide_by_three(user_number)
print(f'This is your number divided by 3: {final_total}')
