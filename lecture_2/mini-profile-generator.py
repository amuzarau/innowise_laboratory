import json
from datetime import datetime
from colorama import Fore, Style


def get_age():
    """Ask user for birth year and calculate current age."""
    try:
        birth_year = int(input("Enter your birth year (e.g., 1990): "))
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a valid year." + Style.RESET_ALL)
        return get_age()
    current_year = datetime.now().year
    return current_year - birth_year


def get_user_hobbies():
    """Collect hobby list until user types 'stop'."""
    hobbies = []
    while True:
        user_input = input("Enter a favorite hobby or type 'stop' to finish: ")
        if user_input.lower() == "stop":
            break
        hobbies.append(user_input)
    return hobbies


def generate_profile(age):
    '''
    Determines the user's "life stage" based on their age.

    Args:
        age (int): The age of the user.

    Returns:
        str: One of "Child", "Teenager", or "Adult" depending on the age.
    '''
    if age <= 12:
        return "Child"
    elif 12 < age < 20:
        return "Teenager"
    else:
        return "Adult"


def print_summary(profile):
    """Print a formatted summary of the user's profile."""

    print(Fore.GREEN + "Profile summary:" + Style.RESET_ALL)
    print(f"Name: {profile['name']}")
    print(f"Age: {profile['age']}")
    print(f"Life Stage: {profile['stage']}")

    hobbies = profile["hobbies"]
    if hobbies:
        print(f"Favorite Hobbies ({len(hobbies)}):")
        for hobby in hobbies:
            print(f"- {hobby}")
    else:
        print("You didn't mention any hobbies.")


def save_to_json(profile, filename="user_profile.json"):
    """Save user profile to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=4)
    print(f"\nProfile saved to {filename}")


# ------MAIN PROGRAM------
def main():
    user_name = input("Enter your full name: ")
    age = get_age()
    hobbies = get_user_hobbies()
    life_stage = generate_profile(age)

    user_profile = {
        "name": user_name,
        "age": age,
        "stage": life_stage,
        "hobbies": hobbies,
    }

    print_summary(user_profile)
    save_to_json(user_profile)


# Run the program
if __name__ == "__main__":
    main()
