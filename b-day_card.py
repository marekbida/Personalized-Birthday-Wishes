def calculate_age(birth_year):
    this_year = 2024
    age = this_year - birth_year
    return age

# user's input
boy_girl_name = input("Enter recipient's name: ")
year_of_birth = int(input("Enter year of birth: "))
personalized_text = input("Enter personalized message: ")
my_name = input("Enter sender's name: ")

# Calculating recipient's age
age = calculate_age(year_of_birth)

# Generating personalized text
b_day_card= "Dear {boy_girl_name},\n\nlets celebrate your {age} years of awesomeness!\nWishing you a day filled with joy and laughter as you turn {age}!\n{personalized_text}\nWith love and best wishes,\n{my_name}"

# Displaying the personalized text
print(b_day_card)