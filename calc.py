import time
import sys
import random
from tqdm import tqdm
import pyfiglet
from colorama import Fore, Style, init
import logging

# Initialize colorama
init(autoreset=True)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Function to display the spinner
def spinner(custom_message="Loading... Please wait."):
    while True:
        for cursor in '|/-\\':
            yield cursor

spin = spinner()

def simulate_library_install(library_name, source):
    delay = random.uniform(0, 1)
    print(f"Installing {library_name} from {source}... ", end="")
    for _ in tqdm(range(int(delay * 100)), desc="Progress", ncols=100, unit="%", colour="white"):
        time.sleep(delay / 100)
    print(f"{Fore.GREEN}Done!")
    return delay

def loading_process():
    total_delay = 0
    print("Loading... Please wait.")
    libraries = [
        ("tqdm", "PyPI"),
        ("pyfiglet", "PyPI"),
        ("colorama", "PyPI")
    ]
    
    for lib, src in libraries:
        total_delay += simulate_library_install(lib, src)
        
    return total_delay

def display_ascii_art():
    ascii_art = pyfiglet.figlet_format("Calculator")
    print(Fore.GREEN + ascii_art)
    print("made by Joseph Rivera")
    print("dedicated to my mom because she recently said she likes algebra")

# Define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main function
def main():
    logging.info("Program started.")
    
    total_loading_time = loading_process()
    spinner_time = total_loading_time
    print(f"\nTotal loading time: {spinner_time:.2f} seconds")
    
    display_ascii_art()
    
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. reload imports")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error! Division by zero.":
                    print(result)
                    logging.error("Attempted division by zero.")
                else:
                    print(f"{num1} / {num2} = {result}")

        elif choice == '5':
            loading_process()

        else:
            print("Invalid Input")
            logging.warning("Invalid operation choice.")
        
        next_calculation = input("Let's do another calculation? (y/n): ")
        if next_calculation.lower() != 'y':
            break

    logging.info("Program ended.")

if __name__ == "__main__":
    main()
