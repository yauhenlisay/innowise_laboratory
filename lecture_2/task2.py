from datetime import datetime

def generate_profile(age):
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    else:
        return "Adult"

user_name = input("Enter your full name: ")
birth_year = int(input("Enter your birth year: "))

current_year = datetime.now().year
current_age = current_year - birth_year

hobbies = []

while True:
    hobby_input = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby_input.lower() == "stop":
        break
    hobbies.append(hobby_input)

life_stage = generate_profile(current_age)

user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

print("\n---")
print("Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")
if not hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(hobbies)}):")
    for hobby in hobbies:
        print(f"- {hobby}")
print("---")