from src.generator import (
    get_all_episodes,
    find_episodes_by_theme,
    find_episodes_by_character
)
from src.display import display_episodes, display_message, display_error, format_episode

def main_menu():
    print("\n Bob's Burgers Episode Generator ")
    print("1. Find episodes by theme")
    print("2. Find episodes by character")
    print("3. Get a completely random episode")
    print("4. Exit")
    print("                               ")

def get_user_choice(prompt: str, valid_choices: list = None) -> str:
    while True:
        choice = input(prompt).strip()
        if valid_choices and choice not in valid_choices:
            display_error(f"Invalid choice. Please enter onr of: {', '.join(valid_choices)}")
        else:
            return choice

def run_app():
    display_message("Bob Burger?")

    while True:
        show_main_menu()
        choice = get_user_choice("Enter your choice (1-4): ", ['1', '2', '3', '4'])

        if choice == '1':
            theme = input("Enter a theme to search for: ").strip()
            if theme:
                matching_episodes = find_episodes_by_theme(theme)
                display_episodes(matching_episodes, f"Episodes featuring '{theme}'")
            else:
                display_error("Theme cannot be empty.")

        elif choice == '2':
            character = input("Enter a character name to search for: ").strip()
            if character:
                matching