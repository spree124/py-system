logged_in = False  # Define logged_in as a global variable
import pygame as p
import vlc
import random
import time
import os

commands = {
    "video": None,
    "help": "Displays available commands.",
    "logout": "Logs out of the system.",
    "shutdown": "Shuts down the system.",
    "whoami": "Shows what user you are logged on as and the computer name for the user.",
    "lock": "Locks your PC.",
    "ver": "Shows the version for this PC.",
    "githubprofile": "Shows my GitHub profile.",
    "music": "Plays music.",
    "calc": "It's a calculator. Nothing special."
}

user1 = "Admin"
user1code = "1234"
systemuser = "SYSTEM"
syscode = str(random.randint(1000, 9999))
shelluser = "shell"
shellcode = "dea"

def login():
    global logged_in
    print("Log on to Windows")
    im = input("Username:")

    if im == user1:
        im1 = input("Password:")
        while im1 != user1code:
            print("Incorrect. Try again.")
            im1 = input("Password:")
        print("Welcome")
        logged_in = True
        time.sleep(random.randint(2, 8))
    elif im == systemuser:
        im1 = input("Password:")
        while im1 != syscode:
            print("Incorrect. Try again.")
            im1 = input("Password:")
        print("Welcome, System User")
        logged_in = True
    elif im == shelluser:

        print("this user is meant to run shell without using an account")
        logged_in = True
    else:
        print("Invalid username. Please try again.")
    return im  # Return the username

# Main loop
while True:
    if not logged_in:
        username = login()  # Call the login function and store the returned username

    if logged_in:
        command = input("You are in Desktop. Type any command or type 'list' for list of commands ")

        if command == "list":
            print("Available commands:")
            for key, value in commands.items():
                print(f"  {key}: {value}")
        elif command == "help":
            print(commands["help"])
        elif command == "video":
            video_path = input("Enter the video path: ")
            commands["video"] = vlc.MediaPlayer(video_path)
            commands["video"].play()
            # Wait for playback to finish
            while commands["video"].get_state() != vlc.State.Ended:
                time.sleep(1)
            # Stop playback and release the media player
            commands["video"].stop()
            commands["video"].release()
        elif command == "logout":
            if username == shelluser:
                print("Going back to LogonUI...")
            else:    
                print("Logging out...")
            logged_in = False  # Set the logged_in flag to False
        elif command == "shutdown":
            print("Shutting down...")
            time.sleep(random.randint(2, 5))
            break
        elif command == "whoami":
            if username == shelluser:
                print(f"LogonUI\\{username}")
            else:    
                print(f"py-system\\{username}")
        elif command == "lock":
            print("Locking...")
            time.sleep(1)
            logged_in = False
            print(f"This computer has been locked by py-system\\{username}.")
            print(f"Type {username}'s password to unlock.")
            lockcode = input("Password:")
            if lockcode != user1code:
                while lockcode != user1code:
                    lockcode = input("Password:")
                    if lockcode == user1code:
                        print("py-system unlocked.")
                        logged_in = True
           
            else:
                print("py-system unlocked.")
                logged_in = True
        elif command == "ver":
            print("py-system ver 0.1 beta")
        elif command == "githubprofile":
            print(f"https://github.com/spree124")
        elif command == "music":
           path = input("Path to music file: ")
           p.init()
           p.mixer.init()
           p.mixer.music.load(path)
           start_time = time.time()
           p.mixer.music.play()
           pdf = input("type stop to stop")
           if pdf.lower() == "stop":
                end_time = time.time()
                p.mixer.music.pause()
                playback_time = end_time - start_time

                # Calculate minutes and seconds
                minutes = int(playback_time // 60)
                seconds = int(playback_time % 60)

                # Format the output
                playback_time_str = f"{minutes:02d}:{seconds:02d}"
            
                print(f"ya listened for {playback_time_str}")
        elif command == "calc":
            o = input("do addition? (y/n) ")
            if o == "y":
                value1 = int(input("num1: "))
                value2 = int(input("num2: "))
                print(value1+value2)
            else:
                o = input("do subtraction? (y/n) ")
                if o == "y":
                    value1 = int(input("num1: "))
                    value2 = int(input("num2: "))
                    print(value1-value2)
                else:
                    o = input("do multiplication? (y/n) ")
                    if o == "y":
                        value1 = int(input("num1: "))
                        value2 = int(input("num2: "))
                        print(value1*value2)
                    else:
                        o = input("do division? (y/n) ")
                        if o == "y":
                            value1 = int(input("num1: "))
                            value2 = int(input("num2: "))
                            print(float(value1/value2))
        else:
            print("Unknown command. Type 'help' for a list of commands.")
