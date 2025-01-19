import random
import time
import sys
from tqdm import tqdm

def spinner():
    while True:
        for cursor in ['/', '-', '\\', '|', '*', '+', '#', '%', '$', '@']:
            yield cursor

spin = spinner()

def loading_screen(message, duration):
    print(message)
    for _ in tqdm(range(duration), desc="Progress", ncols=100, unit="%", colour="green"):
        sys.stdout.write(next(spin))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def generate_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def generate_coordinates():
    return f"{random.uniform(-90, 90):.6f}, {random.uniform(-180, 180):.6f}"

def generate_password():
    devices = ["computer", "laptop", "phone", "mother"]
    device = random.choice(devices)
    password = ''
    for _ in range(3, 15):
        char = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        password += char
        print(f"Password: {password}", end='\r')
        time.sleep(0.1)
    return f"{device} password: {password}"

def display_random_characters(duration):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    for _ in range(duration):
        print(''.join(random.choices(chars, k=100)))
        time.sleep(0.1)

def main():
    while True:
        target = input("Who do you want to hack? ")
        loading_screen("Finding IP address", random.randint(1, 20))
        print(f"IP address: {generate_ip()}")
        
        loading_screen("Finding coordinates", random.randint(1, 20))
        print(f"Coordinates: {generate_coordinates()}")
        
        loading_screen("Finding password", random.randint(1, 20))
        print(generate_password())
        
        loading_screen("encrypting Information", random.randint(1, 30))
        display_random_characters(10)
        
        print("Hacking complete!")
        print("Do you want to hack again? (y/else)")
        response = input().lower()
        if response != "y":
            break

if __name__ == "__main__":
    main()
