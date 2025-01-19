import pyfiglet
import random
import time
import sys
from tqdm import tqdm

# Function to display the spinner
def spinner(custom_message="Loading Chars"):
    while True:
        for cursor in '|/-\\':
            yield cursor

spin = spinner()

def simulate_task(task_name, duration, update_interval=0.5):
    print(f"{task_name}... ", end="")
    for _ in tqdm(range(int(duration / update_interval)), desc="Progress", ncols=100, unit="%", colour="green"):
        sys.stdout.write(next(spin))
        sys.stdout.flush()
        time.sleep(update_interval)
        sys.stdout.write('\b')
    print("Done!")

# Display the ASCII art
logo = pyfiglet.figlet_format("HomeStuck")
print(logo)

# Simulate an initial loading screen
simulate_task("Loading initial setup", 8.848, 0.00005)

# Section contents
section_content = {
    1: ("Homestuck is an Internet fiction series created by American author and artist Andrew Hussie. "
        "The fourth and best-known of Hussie's four MS Paint Adventures, it originally ran from April 13, 2009, "
        "to April 13, 2016. Though normally described as a webcomic, and partly constituted by a series of single panel pages, "
        "Homestuck also relied heavily on Flash animations and instant message logs to convey its story, along with occasional use of browser games.\n\n"
        "Its plot centers on a group of teens who trigger the inevitable destruction of Earth by installing the beta version of an upcoming PC game, Sburb. "
        "The teens soon come into contact with a group of Internet trolls who are revealed to be horned aliens, and these trolls work with the kids to create a new universe "
        "by completing the game. It has been noted for its complex and nonlinear plot, considerable length at over 8,000 pages and 800,000 words, and intensely devoted fan community.\n\n"
        "The success of Homestuck has resulted in numerous related projects and sequels, including the Hiveswap series of adventure games."
    ),
    2: ("In 2009, on thirteen-year-old John Egbert's birthday, he receives a beta copy of an upcoming computer game, Sburb. "
        "Upon installing the game on his computer, he triggers a real life meteor storm, as a massive meteor approaches him, with a countdown slowly ticking down to when it will collide with his house. "
        "John survives only by being transported to a place called 'the Medium'. John's friends, Rose Lalonde, Dave Strider, and Jade Harley join him in the game along with their guardians, "
        "and they learn that playing the game has inadvertently triggered the destruction of Earth and that they must beat Sburb to create a new universe.\n\n"
        "John and his friends are attacked by a ruthless villain known as Jack Noir while exploring the medium. As this is ongoing, John and his friends are also harassed by a group of twelve Internet trolls "
        "whose own session of Sburb was a failure that they blame the kids for. Among them, Karkat Vantas, Kanaya Maryam, Terezi Pyrope, and Vriska Serket each develop a relationship with the four humans, "
        "and the trolls are revealed to be an alien species simply called 'trolls'. The narrative shifts to a side story arc about the trolls and the specific sequence of events that led this group to play their own session of the game. "
        "The group and troll society as a whole is manipulated by the enigmatic Doc Scratch, who serves an even more mysterious master. The trolls win their session and a new universe – the universe the kids inhabit – is created. "
        "Before they can claim their prize, they are attacked by Jack Noir and forced into hiding, where they begin to troll the kids via a chat program.\n\n"
        "Each of the twelve trolls is associated with a Western zodiac sign and a color.\n"
        "Returning to the present, the two species cooperate to salvage the kids' game session. However, Vriska sabotages key events which results in the kids' accidentally empowering Jack Noir from a simple adversary to a seemingly-invincible monster. "
        "Rising tensions among the trolls eventually boil over, and some begin to attack and kill others; almost half the group (including Vriska) dies before Karkat manages to restore order. From Doc Scratch, the kids learn about a game mechanism called the 'Scratch' "
        "that allows the humans to reset their session to escape Jack but will also inadvertently summon Lord English, Doc Scratch's master who seeks dominion over all of reality.\n\n"
        "Executing the Scratch resets the kids' universe, and versions of themselves become guardians to a new group of players, who are versions of their own ancestors. As a result, John's late grandmother, Jane Crocker, is fifteen years old and the protagonist of the new arc. "
        "She leads her three friends Roxy Lalonde, Dirk Strider, and Jake English – the mother, brother, and grandfather of Rose, Dave, and Jade, respectively – through their own session of the game, while the original humans and surviving trolls journey through dimensions to the new post-Scratch session over the course of three years.\n\n"
        "The post-Scratch version of Earth quickly becomes dominated by the Condesce, the sinister former troll empress now in service to Lord English. In lieu of trolls, the four post-Scratch kids interact online with two alien cherubs, the siblings Calliope and Caliborn. "
        "While Calliope becomes a fast friend of the group, Caliborn resents their camaraderie, and is highly antagonistic towards them. After the post-Scratch kids enter their session, the two cherubs play their own version of Sburb in a session that sees Caliborn cheating to win by having his sister assassinated.\n\n"
        "When finally uniting in the new session, the kids and trolls enact a plan to create a new universe and to defeat Lord English, the Condesce, and Jack Noir; the latter of whom escaped from the original doomed session. John Egbert develops new powers allowing him to retcon previous events within the Homestuck narrative. "
        "In the ensuing conflict, only John, Roxy, Dirk, and one of the trolls, Terezi, survive. With Terezi's guidance, John retcons key events in the narrative, most notably Vriska's death, setting up a timeline with a clear path to victory. "
        "In the retconned narrative, the kids and trolls defeat their enemies in a giant battle and create the new universe. The comic ends with Lord English fighting an army led by Vriska, Caliborn becoming Lord English after gaining unconditional immortality, "
        "and the remaining living heroes about to enter their newly created universe."
    ),
    3: ("While nominally a webcomic, Homestuck consists of a combination of static images, animated GIFs, and instant message logs. Generally, pages included a single panel, and navigational links to successive pages are phrased similarly to commands in interactive fiction games. "
        "Additionally, unlike previous works from Andrew Hussie which exclusively relied on GIF images for animation, Homestuck introduced complex animations and browser games made with Adobe Flash, many involving contributions from fan artists. "
        "According to academic Kevin Veale of Massey University, Homestuck used these various methods of engagement to manipulate its readers' experiences in order to tell a multilayered non-linear story.\n\n"
        "The basic premise of Sburb has been described as similar to games like The Sims, Spore, and EarthBound. As in Hussie's prior webcomic Problem Sleuth, the adventure is characterized by time travel, mystery, a complex fictional universe, and frequent references to pop culture and previous adventures. "
        "Changes from previous stories include an emphasis on contemporary society, such as online gaming and Internet culture, which contrasts with the historical settings of MS Paint Adventures comics Bard Quest and Problem Sleuth.\n\n"
        "Hussie first launched an early version of Homestuck, the Homestuck Beta, on April 10, 2009. The Homestuck Beta was published only three days after Problem Sleuth and ran until April 13, 2009.\n\n"
        "A recurring symbol throughout Homestuck is the spirograph.\n\n"
        "The initial style of the webcomic was developed to be advanced by fan contributions, with the fans deciding what actions the characters would take. "
        "Later, Hussie moved away from this style because the fan input method had grown 'too unwieldy and made it difficult... to tell a coherent story.' "
        "While Hussie now controlled the main plot of the story and the characters' actions, he still 'visited fan blogs and forums' to figure out small things to add into Homestuck. "
        "However, throughout its run, content within Homestuck would cease to be updated in several named pauses. The most infamous of these pauses was the result of Andrew Hussie taking a full year to solely focus on the production of Hiveswap in the gigapause.\n\n"
        "Cover of Homestuck Book 1\n"
        "On April 13, 2016, Hussie released the final chapter of the webcomic: a nine-minute-long animated short titled '[S] ACT 7'. Hussie stated that an ep