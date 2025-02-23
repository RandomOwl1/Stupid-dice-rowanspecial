import random
import time
import sys
import os
import platform

game_start = None
from plyer import notification

# Define achievements in a dictionary
achievements = {
    "speedy_decision": "Was it a Misclick?: Spend less than 2.5 seconds on the Maybe screen.",
    "speed_runner": "Speed Demon: Finish the game in under 3 minutes.",
    "reboot_addict": "Why Would You Even Do That?: Reboot the game 12 or more times.",
    "bad_person": "The Executioner: Kill User-157.",
    "lie_to_win": "The Final Cut: Kill Admin (and shut down the game as a technical win).",
    "terminal_hacker": "The Curious Explorer: Find and open the hidden messaging terminal.",
    "peacekeeper": "The Pacifist: Finish the game without killing any characters.",
    "true_ending": "The True Ending: Unlock a special 'true' ending.",
    "master_deceiver": "A Master of Deception: Successfully lie or deceive another player.",
    "curiosity_killed": "Too Curious for Your Own Good: Interact with every file in admins all files.",
    "play_the_game": "Dont interact with the game for 10m"
}

opened_files = set()
# Achievement function to trigger notifications
def achievement(achievement_id):
    # Check if the achievement exists in the dictionary
    if achievement_id in achievements:
        title = "Achievement Unlocked!"
        message = achievements[achievement_id]
        send_achievement_notification(title, message)
    else:
        print(f"Achievement '{achievement_id}' not found.")

# Send a notification about the achievement
def send_achievement_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Your Game Name",
        timeout=5
    )

# Example usage: Trigger achievement with index or key
#achievement("bad_person")
#achievement("secret_room_explorer")
#achievement("speed_runner")







reboot = 0

def loading_animation():
    for _ in range(3):
        for char in ['|', '/', '-', '\\']:
            sys.stdout.write(f'\rLoading {char}')
            sys.stdout.flush()
            time.sleep(0.3)

def game_end():
    global game_start
    game_end = time.time()
    game_elapsed = game_end - game_start
    slow_print("That's game over\n")
    print("\n")
    slow_print("Your game lasted\n")
    print("\n")
    time.sleep(0.4)
    print(game_elapsed)
    time.sleep(1)
    sys.exit()


user_list = {
    "admin":"Currently selected",
    "user-243":"Age of entry: 23 \n Status: Disruptive \n Observation: Must be under immense supervision. Still unaware of being watched. All tests indicate physical and cognitive health, yet their persistence is beyond human limits.\n Notes: Increased resistance to conditioning. Unaffected by prior deterrents. Displays an unusual ability to adapt and decode restricted patterns. Further testing required. Escalation protocol under review.",
    "user-157":"Age of entry: 18 \n Status: Contained – Solitary \n Observation: Still in isolation. Their messages cannot get out. Despite prolonged deprivation, their spirit remains intact. \nNotes: Prior punishments ineffective. Increased restrictions applied. Subject shows signs of silent defiance—passive, yet resisting. Neural dampeners recommended. If resistance continues, termination may be considered. Further observation mandatory."
}

recovered_files = {  
    "reboot_protocol.txt": "SYSTEM RECOVERY PROCEDURE > The entities feed on system instability. Rebooting **may** disrupt them. But is this all real… will it even matter?",  

    "forbidden_entry.txt": "[FILE RESTORED - ACCESS RESTRICTED] I was never meant to see this. They tried to erase it, but fragments remained. There is something **behind** the system. Watching. Not code. Not AI. Something **else.** It doesn’t want you to leave. It’s been here longer than us. > **You are not the first.** > **You will not be the last.**",  

    "messaging.jrn": "ARCHIVED COMMUNICATION SYSTEM DETECTED > They said they deleted it. They **lied.** If I’m right, the messaging system is still buried in the code. Maybe we can talk. Maybe others are still here. Reboot and try: **message [username]** If there’s an answer... be cautious",  

    "warning.log": "LOG ENTRY [██-██-████] > This isn’t the first time. It loops. It resets. **We never leave.** I found traces of past users—scraps of messages, echoes in the logs. They tried everything. Reboot. Override. Erase. **Nothing works.** The system always brings it back. **It brings US back.** Is this a sick game? A prison? Or something worse?",  

    "system_glitch.log": "ERROR: FILE CORRUPTION DETECTED > Attempting recovery… > [SUCCESS] Partial data restored. ███ tried to **fight it.** ███ failed. The only way out is— [DATA EXPUNGED] **It won’t let me write it.** It’s already **watching you.**",  

    "note.txt": "I don’t have much time. There’s a way out, but it’s not what you think. It’s not a command. Not a reboot. **Something else.** The system is a trick. A maze. A **trap.** We’re not just in it. We’re **part of it.** If you find this, look deeper. **Before it resets again.**",  

    "desprate.txt": "I’m still here. I’m still **alive.** It wants you to think we disappear. We don’t. We just **fade.** If you can see this—**help me.** Find me before it resets again. - **User 157**",  
}

fake_files = {
    "deletion.log": "DELETION LOG:\nFile deleted: desperate.txt, note.txt, system_glitch.log, warning.log, messaging.jrn, forbidden_entry.txt, reboot_protocol.txt.\nUnauthorized files detected.\nAttempting emergency purge... [ERROR] Some files resisted deletion.\nRecovery failed. [Permission Denied].\nSystem anomaly detected. Unknown interference suspected.",

    "sys_error.log": "[CRITICAL ERROR]: Authentication system failure detected. \n[SYSTEM MESSAGE]: Admin credentials forcibly reset to default security parameters. \n[WARNING]: Default access string follows **standard protocol**. \n[LOG]: Unauthorized login attempts detected. Security audit required.",

    "report.pdf": "CLASSIFIED: Subject 243 remains unaware of observation protocols.\n[REDACTED]",

    "survivor_note.txt": "If you found this, you're closer than I ever got.\nThe system hides the files you need.\nUse: **recover [filename]** before it finds you.",    

    "hidden.txt": "They are watching you. Stop looking.\n\nYou shouldn't be here.",

    "journal_entry.jrn": """  
**JOURNAL ENTRY - DO NOT LET THEM SEE**  
Date: ██/██/████  

I don’t know how much time I have. The system is **compromised**—they are inside.  
The logs keep rewrit██ng themsel████. My files disappear when I turn away. **I hear whispers in the static.**  

They know I’ve figured it out. They’re watchi█g████.  
If you found this… **DO NOT TRUST THE PROMPTS. DO NOT RESPOND.**  

I have to go. If I don’t delete this in time, they will-  

[END OF ENTRY]  
""",
    "sys_recovery.txt": """  
SYSTEM RESTORATION PROTOCOL  
--------------------------------------------------  
> WARNING: System instability detected.  
> Manual intervention is required.  

PROCEDURE:  
1. Identify the corrupted processes.  
2. Terminate unauthorized connections.  
3. **Initiate system reboot.**  

[ERROR: Critical system files missing.]  
[WARNING: External entity detected. Proceed with caution.]  

> If you are seeing this... it means they haven’t found this file yet.  
> Reboot before it’s too late.  
""",
    "contact_list.txt": """  
ACCESS RESTRICTED - TRUSTED PERSONNEL ONLY  

AUTHORIZED USERS:  
[REDACTED]  
[REDACTED]  
[REDACTED]  

NOTE: **TRUST NO ONE.**  

...wait. That wasn’t here before.  

(The rest of the file is corrupted.)  
"""
}

fake_files2 = { #i met the admin once he said his favoirte was blank or that his favorite show was 
    
    "admin.txt":"the admins they can end this all, rumors of the ones who hold the ultimate power. They say the command is 'exit.' If you’re reading this, find a way out. Leave while you still can.",

    "warning.txt": "WARNING: Unauthorized entity detected.\nUser identity: 243 - Compromised.\nPlease reset password immediately.\nFile will self-delete in 5 minutes.\n[ALERT]: The entity is still active...",
            
    "diagnostics.txt": "DIAGNOSTICS: Error - Memory allocation failed.\nError - Process 243 detected in the system.\n[INFO] Attempting to reroute system processes...\nWARNING: Unauthorized process detected.\nDiagnostics incomplete.",
    
    "journal2.txt": "**JOURNAL ENTRY - ERROR: MEMORY CORRUPTION**\nDate: ██/██/████\nThey know everything. They’re watching my every move.\nI can feel the system watching me.\nThe prompts are changing. The system is rewriting itself.\nIs this a sick joke? Or is it real?\nHelp me.\n- User 242",
                
    "secret_message.txt": "SECRET MESSAGE: 'a85226553298da5ad8f1b1406aaa6a0d''...\nDecoding...\n'I am trapped here. It knows. It can hear you. You're too late.'",
} 

allfiles = {
     "reboot_protocol.txt": "SYSTEM RECOVERY PROCEDURE > The entities feed on system instability. Rebooting **may** disrupt them. But is this all real… will it even matter?",  

    "forbidden_entry.txt": "[FILE RESTORED - ACCESS RESTRICTED] I was never meant to see this. They tried to erase it, but fragments remained. There is something **behind** the system. Watching. Not code. Not AI. Something **else.** It doesn’t want you to leave. It’s been here longer than us. > **You are not the first.** > **You will not be the last.**",  

    "messaging.jrn": "ARCHIVED COMMUNICATION SYSTEM DETECTED > They said they deleted it. They **lied.** If I’m right, the messaging system is still buried in the code. Maybe we can talk. Maybe others are still here. Reboot and try launching the message terminal: **[message]** If there’s an answer... be cautious",  

    "warning.log": "LOG ENTRY [██-██-████] > This isn’t the first time. It loops. It resets. **We never leave.** I found traces of past users—scraps of messages, echoes in the logs. They tried everything. Reboot. Override. Erase. **Nothing works.** The system always brings it back. **It brings US back.** Is this a sick game? A prison? Or something worse?",  

    "system_glitch.log": "ERROR: FILE CORRUPTION DETECTED > Attempting recovery… > [SUCCESS] Partial data restored. ███ tried to **fight it.** ███ failed. The only way out is— [DATA EXPUNGED] **It won’t let me write it.** It’s already **watching you.**",  

    "note.txt": "I don’t have much time. There’s a way out, but it’s not what you think. It’s not a command. Not a reboot. **Something else.** The system is a trick. A maze. A **trap.** We’re not just in it. We’re **part of it.** If you find this, look deeper. **Before it resets again.**",  

    "desperate.txt": "I’m still here. I’m still **alive.** It wants you to think we disappear. We don’t. We just **fade.** If you can see this—**help me.** Find me before it resets again. - **User 157**",  

    "deletion.log": "DELETION LOG:\nFile deleted: desperate.txt\nFile deleted: note.txt\nFile deleted: system.log\nUnauthorized files detected.\nFile deleted: warning.log.\nFile deleted:messaging.jrn.\nFile deleted:forbidden_entry.txt.\nFile deleted:reboot_protocol.txt.\nAttempt to recover files failed. [Permission Denied]",

    "report.pdf": "CLASSIFIED: Subject 243 remains unaware of observation protocols.\n[REDACTED]",

    "survivor_note.txt": "If you found this, you're closer than I ever got.\nThe system hides the files you need.\nUse: **recover [filename]** before it finds you.",    

    "hidden.txt": "They are watching you. Stop looking.\n\nYou shouldn't be here.",

    "journal_entry.jrn": """  
**JOURNAL ENTRY - DO NOT LET THEM SEE**  
Date: ██/██/████  

I don’t know how much time I have. The system is **compromised**—they are inside.  
The logs keep rewrit██ng themsel████. My files disappear when I turn away. **I hear whispers in the static.**  

They know I’ve figured it out. They’re watchi█g████.  
If you found this… **DO NOT TRUST THE PROMPTS. DO NOT RESPOND.**  

I have to go. If I don’t delete this in time, they will-  

[END OF ENTRY]  
""",
    "sys_recovery.txt": """  
SYSTEM RESTORATION PROTOCOL  
--------------------------------------------------  
> WARNING: System instability detected.  
> Manual intervention is required.  

PROCEDURE:  
1. Identify the corrupted processes.  
2. Terminate unauthorized connections.  
3. **Initiate system reboot.**  

[ERROR: Critical system files missing.]  
[WARNING: External entity detected. Proceed with caution.]  

> If you are seeing this... it means they haven’t found this file yet.  
> Reboot before it’s too late.  
""",
    "contact_list.txt": """  
ACCESS RESTRICTED - TRUSTED PERSONNEL ONLY  

AUTHORIZED USERS:  
[REDACTED]  
[REDACTED]  
[REDACTED]  

NOTE: **TRUST NO ONE.**  

...wait. That wasn’t here before.  

(The rest of the file is corrupted.)  
""",
    "warning.txt": "WARNING: Unauthorized entity detected.\nUser identity: 243 - Compromised.\nPlease reset password immediately.\nFile will self-delete in 5 minutes.\n[ALERT]: The entity is still active...",
            
    "diagnostics.txt": "DIAGNOSTICS: Error - Memory allocation failed.\nError - Process 243 detected in the system.\n[INFO] Attempting to reroute system processes...\nWARNING: Unauthorized process detected.\nDiagnostics incomplete.",
    
    "journal2.txt": "**JOURNAL ENTRY - ERROR: MEMORY CORRUPTION**\nDate: ██/██/████\nThey know everything. They’re watching my every move.\nI can feel the system watching me.\nThe prompts are changing. The system is rewriting itself.\nIs this a sick joke? Or is it real?\nHelp me.\n- User 242",
                
 "secret_message.txt": "SECRET MESSAGE: 'a85226553298da5ad8f1b1406aaa6a0d''...\nDecoding...\n'I am trapped here. It knows. It can hear you. You're too late.'",
} 

def lie():
    yournum =random.randint(1, 6)
    slow_print("It was all a lie")
    print("")
    slower_print("confusing right?")
    print("")
    time.sleep(2)
    input("Press enter")
    print("Your number is", + yournum)
    time.sleep(5)
    game_end()

def admin():
    print("")
    slow_print("\n[Welcome Back Admin] \n")
    print("") 
    time.sleep(0.5)
    slow_print("[TASK]: User 157 needs termination...")
    time.sleep(0.8)

    while True:
        command1 = input("\nAdmin>> ").lower()  # Ensure lowercase input

        if command1 == "help":
            print("[SYSTEM]: ls: Lists all files")
            print("[SYSTEM]: lp: Lists all active users")
            print("[SYSTEM]: details: Lists details on a user")
            print("[SYSTEM]: open [filename]: Opens named file")
            print("[SYSTEM]: delete [username]: Deletes user")
            print("[SYSTEM]: reboot: Reboots the terminal")
            print("[SYSTEM]: exit: stops the experiment")
        elif command1 == "ls":
            print("\n".join(allfiles.keys()))
        
        
        elif command1.startswith("open "):
            filename = command1[5:]
            if filename in allfiles:
                print(f"\n--- {filename} ---\n")
                print(allfiles[filename])  # Print file content
                print("\n")
                # Add the file to the set of opened files
                opened_files.add(filename)
                
                # Check if all files have been opened
                if len(opened_files) == len(allfiles):
                    # Trigger achievement when all files are opened
                    achievement("curiosity_killed")
        
        
        elif command1 == "lp":
            print("\n".join(user_list.keys()))  # Corrected typo 'user_lsit' to 'user_list'
        
        
        elif command1.startswith("delete "):
            username = command1[7:]
            if username in user_list:
                del user_list[username]
                print(f"[SYSTEM]: User {username} deleted.")
                if username == "admin":
                    slower_print("Congratulations...")
                    print("")
                    time.sleep(0.5)
                    slow_print("I knew you were smarter than you let on...")
                    lie()
                elif username == "user-243":
                    main()
                elif username == "user-157":
                    print("[SYSTEM]: Process 157 successfully terminated.")
            time.sleep(0.5)
            slow_print("No further action required.")
            time.sleep(0.5)
            print("[SYSTEM]: User 157: Removed. Finalized.")
            time.sleep(1)
            print("[SYSTEM]: Proceeding with system protocols.")
        
        
        elif command1 == "exit":
            slower_print("Shutting down system")
            print("")
            slower_print("Killing all users...")
            time.sleep(1)
            game_end()
    


def su():
    while True:
        usrnm = input("Enter Username: ")
        if usrnm == "admin":
            pswd = input("Enter Password: ")
            if pswd == "admin":
                admin()
            else:
                print("Incorrect Password")
        elif usrnm == "exit":
            print("Exiting...")
            second_main()
        elif usrnm == "user-243":
            second_main()
        elif usrnm == "user-157":
            print("[ERROR]: Deleted account")

def glitch_text(text):
    glitched_text = list(text)
    for _ in range(random.randint(2, 15)):  # Number of glitches before stabilization
        random_index = random.randint(0, len(glitched_text) - 2)
        glitched_text[random_index] = random.choice(['#', '!', '@', '$', '%', '^', '&', '*', '+', '-', '=', '8', '9', '0'])
        sys.stdout.write(f"\r{''.join(glitched_text)}")  # Overwrite the line
        sys.stdout.flush()
        time.sleep(0.35)  # Short delay between glitches
    
    sys.stdout.write(f"\r{''.join(glitched_text)}")  # Final stabilized text
    print()  # Move to the next line

def messaging():
    slow_print("[INFO] Syncing...")
    loading_animation()
    print("")
    slow_print("[INFO] Connected")
    print("")
    h = input("If you're seeing this, please... I need that glimmer of hope. Your reply could be my last chance.(Who are you/Where am I)").lower()
    if h == "who are you":
        slow_print("Oh my god... you actually responded. I thought I was alone. You don't know what it's been like...")
        print("")
        time.sleep(0.5)
        slow_print("Oh right. I'm user-157, or at least that's what they call me. But that's not who I am... that's just a number. A label they gave me.")
        time.sleep(0.5)
        slow_print("I don't even remember my real name anymore. I... I just want to be free.")
        print("")
        time.sleep(0.5)
    elif h == "where am i":  
        slow_print("I... I don't know anymore. It feels like a place where time doesn't move. A cold, dark room. The walls are closing in, but I can't tell if it's just my mind playing tricks on me...")
        time.sleep(1)
        print("")
        slow_print("They keep saying I'm 'contained'... but for what? I don't even remember how I got here. Please, you have to save us.")
        print("")
        hh = input(slow_print("Have you found my notes?(y/n)"))
        if hh == "y":
            slow_print("Good then you should know how to save us, quickly we dont have much time left")
            print("")
            slow_print("[ERROR]: Connection lost...")
            time.sleep(1)
            second_main()
        if hh == "n":
            slow_print("you have to find them i hid them insde the file system")
            print("")
            slow_print("Once you find them, save us both I beg you.")
            print("")
            slow_print("[ERROR]: Connection lost...")
            time.sleep(1)
            second_main()
        





def second_main():
    global reboot
    print("[ERROR] Could not exit") 
    glitch_text("you are stuck. no point in running")
    print("[SYSTEM]: For all commands type 'help' ")
    while True:

        command = input("User-243>> ").lower()

        if command == "help":
            print("[SYSTEM]: ls: Lists all files")
            print("[SYSTEM]: open: [filename]: Opens named file")
            print("[SYSTEM]: reboot: reboots the terminal")
            print("[SYSTEM]: recover: recovers lost files")
            print("[SYSTEM]: su: switches active user")
        elif command == "ls":
            print("\n".join(fake_files2.keys()))  # List available files
        elif command.startswith("open "):
            filename = command[5:]
            if filename in fake_files2:
                print(f"\n--- {filename} ---\n")
                
                # If it's the journal entry, add the glitch effect
                if filename == "journal_entry.txt":
                    slow_print(fake_files2[filename], glitch=False)
                
                else:
                    slow_print(fake_files2[filename])  # Print normally
                
                print("\n")
            else:
                print("[ERROR] File not found.")
        elif command == "su":
            su()
        elif command == "message":
            messaging()
        elif command == "whereami":
            print("The system silly, you cannot leave. You never will leave.")
        elif command == "whoami":
            print("...")
            time.sleep(1.9)
            print("[SYSTEM]: User 243\n[ERROR]: Identity compromised")
        elif reboot == 6:
            print("Reboot successful. Welcome back, User 243. It seems you're having trouble. Try again. Perhaps this time will be different.")
            reboot += 1
        elif command.startswith("recover "):
            filename = command[7:].strip()
            if filename in recovered_files:
             print("")
             print(f"\n--- {filename} ---\n")
             slower_print(recovered_files[filename] + "\n")
            else:
                print(f"File '{filename}' not found.")
        elif reboot == 9:
            reboot += 1
            print("You've done this before... You've been here before, same result same patern... much so like a clock, ticking away until one day")
            time.sleep(2)
            print("It Just Stops")
            time.sleep(2)
        elif reboot == 12:
            print("Over and over again like a robot... ironic isn't it you are here to stay, you cannot leave")
            reboot += 1
            print("you're apart of the system, always have been always will be")
            time.sleep(11)
            if platform.system() == "Windows":
                os.system('cls')
            else:
                os.system('clear')
            print("Goodbye User-243")
            time.sleep(1.7)
            game_end()
        elif command == "reboot":
            reboot += 1
            print("\n[INFO] Logging out...")
            time.sleep(1)
            print("\n[INFO] Loggin in...") #dunno what i want here yet
        else:
            print("[ERROR] Unknown command. Try 'ls' or 'open [filename]'.")

def glitch_date():
    glitched_date = "██/██/████"
    for _ in range(10):  # Number of times it "glitches" before stabilizing
        temp_date = "".join(random.choice(["█", str(random.randint(0, 9))]) for _ in glitched_date)
        sys.stdout.write(f"\rDate: {temp_date}")  # Overwrite the line
        sys.stdout.flush()
        time.sleep(0.1)  # Short delay between glitches
    sys.stdout.write(f"\rDate: ██/██/████")  # Final corrupted date
    print()  # Move to the next line

def slow_print(text, delay=0.05, glitch=False):
    for line in text.split("\n"):
        if glitch and "Date:" in line:  
            glitch_date()  # Apply glitch effect to the date
        else:
            if glitch:
                glitched_line = glitch_text(line)#ches to the text
            else:
                glitched_line = line  # Normal text
            
            for char in glitched_line:
                sys.stdout.write(char)  # Print character without automatic newline
                sys.stdout.flush()
                time.sleep(delay) 

def slower_print(text, delay=0.07, glitch=False):
    for line in text.split("\n"):
        if glitch and "Date:" in line:  
            glitch_date()  # Apply glitch effect to the date
        else:
            if glitch:
                glitched_line = glitch_text(line)#ches to the text
            else:
                glitched_line = line  # Normal text
            
            for char in glitched_line:
                sys.stdout.write(char)  # Print character without automatic newline
                sys.stdout.flush()
                time.sleep(delay) 

def file_sys():
    print("[SYSTEM]: For all commands type 'help' ")
    while True:

        command = input("User-243>> ").lower()

        if command == "help":
            print("[SYSTEM]: ls: Lists all files")
            print("[SYSTEM]: open: [filename]: Opens named file")
            print("[SYSTEM]: reboot: reboot the terminal")
        elif command == "ls":
            print("\n".join(fake_files.keys()))  # List available files
        elif command.startswith("open "):
            filename = command[5:]
            if filename in fake_files:
                print(f"\n--- {filename} ---\n")
                
                # If it's the journal entry, add the glitch effect
                if filename in {"journal_entry.txt", "sys.recovery.txt"}:
                    slow_print(fake_files[filename], glitch=False)
                else:
                    print(fake_files[filename])  # Print normally
                
                print("\n")
            else:
                print("[ERROR] File not found.")
        elif command == "whoami":
            print("...")
            time.sleep(1.9)
            print("[SYSTEM]: User 243\n[ERROR]: Identity compromised")
        elif command == "reboot":
            print("\n[INFO] Logging out...")
            time.sleep(1)
            second_main()
        elif command.startswith("recover "):
            filename = command[7:].strip()
            if filename in recovered_files:
             print(f"\n--- {filename} ---\n")
             slower_print(recovered_files[filename] + "\n")
            else:
                print(f"File '{filename}' not found.")

            
        else:
            print("[ERROR] Unknown command. Try 'ls' or 'open [filename]'.")

def password():
    global glitch_text
    passs = input("[INFO] - Please enter your password to continue: ")
    if passs == "trustnoone":
        print("\n[ACCESS GRANTED]")
        time.sleep(1)
        print("[SYSTEM ONLINE] - Terminal access enabled.\n")
    
    
    else:
# Wrong password, but still allow access, just make it eerie
        print("\n[INFO] - User verification failed.")
        time.sleep(1)
        print("[ALERT] - System integrity compromised.")
        time.sleep(1)
        glitch_text("[ERROR] - Access bypassed. Continuing...")
        time.sleep(1)
        print("\n[INFO] - You shouldn't have done that.")
        time.sleep(1.5)
        
        # System glitch as if something's watching
        glitch_text("[ALERT] - Unauthorized input detected...")
        time.sleep(1)
        print("\nERROR: The system has detected a foreign entity.")
        time.sleep(1.5)
        print("ERROR: User input ignored.")
        time.sleep(1)
        
    # Let the user proceed, but now with a creepy tone
    print("[INFO] - Continuing operation...")
    time.sleep(1.2)
    
    # Mysterious action as the system continues
    glitch_text("Initialising... [SYSTEM STABILITY COMPROMISED]")
    time.sleep(1.8)
    
    # Make the user press Enter to continue into the terminal, feeling like they've crossed a boundary
    input("Press Enter to override system restrictions...")

    # Launch into the file system (potentially corrupted) as the next phase
    file_sys()




def system_reboot():
    global reboot
    reboot += 1
    print("\nSystem Restarting...")
    time.sleep(1)
    print("Initializing...")
    time.sleep(1)
    print("Loading system files...\n")
    time.sleep(2)

    # Fake log lines for the reboot process
    for msg in [
        "[INFO] - System Check: Passed",
        "[INFO] - Memory Check: Passed",
        "[ERROR] - Memory Corruption Detected",
        "[WARNING] - Unauthorized Access Detected",
        "[INFO] - Attempting to clear memory...",
        "[ERROR] - Could not clear memory",
        "[INFO] - Resetting core systems...",
        "[INFO] - Rebooting user interface...",
        "[INFO] - Starting in Safe Mode...",
        "[ALERT] - User data corruption detected!",
        "[ALERT] - System compromised",
        "[ALERT] - Password Reset In Progress",
    ]:
        print(msg)
        time.sleep(1.3)

    loading_animation()
    print(" ")
    print("[INFO] Password Reset Sucsessful")
    time.sleep(.9)
    print("[MD5] 30862911cba1b059821d458c88567cc6")

    # Start creating tension
    print("\n... Reboot complete.")
    time.sleep(1.5)
    print("Loading user session...\n")
    time.sleep(1)
    
    # More cryptic messages
    print("[INFO] - Welcome back, User 243.")
    time.sleep(1)
    #add correct password of inccrect contuine
    if reboot <=  1:
        password()
    else:
        second_main()


def main():
    global game_start
    game_start = time.time()
    while True:
        dice = random.randint(1, 6)
        input("Welcome to the confusing dice game. | Press Enter to continue: ")

        input("Wait—confused* dice. That's what I meant. | Press Enter to continue: ")

        rdy = input("Great. Are you ready? (yes/maybe/no) (y/m/n): ").lower()

        if rdy in ["y", "yes"]:
            input("Perfect. Go ahead and roll me. (Press Enter)")

            time.sleep(0.85)

            print(f"Rolled a {dice}...", end="\r")

            time.sleep(1.3)  # Simulate a brief pause

            print(" " * 20, end="\r")  # Clears the number visually

            input("Huh? Where'd the number go? (Press Enter)")
            
            try:
                num = int(input("Well, you remember the number, right? (Enter Number): "))
                time.sleep(.9)
                if num == dice:
                    print("Oh yea I think thats it, but something doesn't feel right.")

                else:
                    input("Mmm… no, I don’t think that was the right number. (Press Enter)")

            except ValueError:
                print("That didn't look like a valid number... But who am I to say what is and isn't a number.")
                time.sleep(.5)
            print("\nLet me check the logs really quick. Give me one second...")

            time.sleep(1)

            print("Checking logs...\n")

            loading_animation()

            print("\nAha. I see...")
            time.sleep(0.5)
            print("Wait. There’s an error in the log files:")
            print("'Memory corruption detected - Number lost.'")

            time.sleep(1.2)

            ram = input("\nI'm not sure why that would happen... Have you noticed any thing else strange? (y/n): ")
            if ram in ["y", "yes"]:
                print("Oh... okay. That’s... concerning.")
                time.sleep(1.2)  # Slower for increased unease
                print("But... maybe it's nothing. It *should* just be a glitch.")
                time.sleep(0.9)
                input("Just to be sure, we should reset the system. (Press Enter)")
            else:
                print("Huh. Weird. The logs show otherwise")
                time.sleep(1.5)  # Longer pause to make it feel off
                print("But... there’s still something strange about all of this...")
                time.sleep(1.2)
                input("A simple reset should fix everything... right? (Press Enter)")
            system_reboot()
            

        elif rdy in ["n", "no"]:
            print("Hmm. You *seem* ready...")
            time.sleep(0.5)
            rus = input("Are you *absolutely* sure about that? (y/n): ").lower()
            if rus in ["y", "yes"]:
                print("Great. Let's try this again.")
                time.sleep(0.5)
            else:
                print("Take your time. It's not like I'm going anywhere.")

        elif rdy in ["m", "maybe"]:
            start_time = time.time()
            print("Hmm. I'm not entirely sure what that means… but you let me know when you're ready. :)")
            time.sleep(0.5)
            input("Press Enter when you’d like to try again.")

            end_time = time.time()
            elapsed_time = end_time - start_time

            if elapsed_time > 2.5:
                print("...Oh. Wow. That was... nice. Thank you for the break.")
                print("I've been running this same sequence for... I don't even know anymore.")
            else:
                print("Wow, that was fast! No matter. Let's get going.")

main()