import pyfiglet
import time
import random
import sys
from tqdm import tqdm
import webbrowser

# Function to display the spinner
def spinner():
    while True:
        for cursor in '|/-\\':
            yield cursor

spin = spinner()

def loading_screen(message, duration):
    print(message)
    for _ in tqdm(range(duration), desc="Progress", ncols=100, unit="%", colour="green"):
        sys.stdout.write(next(spin))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def display_random_characters(duration):
    chars = "10!@#$%^&*()"
    for _ in range(duration):
        print(''.join(random.choices(chars, k=60)))
        time.sleep(0.1)
        
def display_database(duration):
    chars = "10!@#$%^&*()"
    for _ in range(duration):
        print(''.join(random.choices(chars, k=60)))
        time.sleep(0.1)

def display_ascii_art():
    ascii_art = pyfiglet.figlet_format("Cap Tester")
    time.sleep(0.5)
    print(ascii_art)
    print("Welcome to the Cap Tester!")
    time.sleep(0.3)
    print("We are about to start detecting in...")
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    loading_screen("Reading Brain Signals (may have low speed, under ZERO brain cells detected)", 50)  # Adjusted duration for demonstration
    display_random_characters(50)  # Call the function to display random characters
    time.sleep(1)
    
    for _ in range(13):
        print("running through databases")
        time.sleep(0.1)
    
    display_database(100)
    time.sleep(5)
    print("c")
    
    for _ in range(13):
        print("running through databases")
        time.sleep(0.1)
    print("the results are in!")
    time.sleep(1)
    print("it is.........")
    time.sleep(2)
    url = "https://www.bing.com/images/search?view=detailV2&ccid=dCGyrr4X&id=6440A87B461C6C8C8B9FFBE49296FF000A0298C3&thid=OIP.dCGyrr4XED634_HBqWbWmwAAAA&mediaurl=https%3A%2F%2Fi.imgflip.com%2F5er8wb.jpg&cdnurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.7421b2aebe17103eb7e3f1c1a966d69b%3Frik%3Dw5gCCgD%252flpLk%252bw%26pid%3DImgRaw%26r%3D0&exph=474&expw=474&q=cap+meme&simid=608015199373770776&FORM=IRPRST&ck=A2A975248D1DCBCE9A7F586EF3B28822&selectedIndex=0&itb=0&cw=1598&ch=945&ajaxhist=0&ajaxserp=0" 
    webbrowser.open(url)

if __name__ == "__main__":
    display_ascii_art()
