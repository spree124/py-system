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
    "ver": "Shows the version for this PC."
}

user1 = "Admin"
user1code = "1234"
systemuser = "SYSTEM"
syscode = str(random.randint(1000, 9999))

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
    elif im == systemuser:
        im1 = input("Password:")
        while im1 != syscode:
            print("Incorrect. Try again.")
            im1 = input("Password:")
        print("Welcome, System User")
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
            print("Logging out...")
            logged_in = False  # Set the logged_in flag to False
        elif command == "shutdown":
            print("Shutting down...")
            time.sleep(random.randint(2, 5))
            break
        elif command == "whoami":
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
          elif command == "ver"
              print("py-system ver 0.1 beta")
        
        else:
            print("Unknown command. Type 'help' for a list of commands.")
