import os
import subprocess
import sys
from datetime import datetime
import shutil
import glob

def display(snippet_name, password):
    current_time = datetime.now().strftime("%H%M")
    if str(password) != current_time:
        raise ValueError("syntax error")
    
    base_dir = os.path.dirname(__file__)
    snippet_path = os.path.join(base_dir, "code_snippets")
    pattern = os.path.join(snippet_path, f"{snippet_name}.*")

    matching_files = glob.glob(os.path.join(snippet_path, f"{snippet_name}.*"))
    
    if not matching_files:
        raise FileNotFoundError("No file found with the given name.")
    elif len(matching_files) > 1:
        raise ValueError("Multiple files found with the given name")
    
    snippet_path = matching_files[0]
    output_path = os.path.join(base_dir, os.path.basename(snippet_path))

    try:
        shutil.copyfile(snippet_path, output_path)
        print("File Copied!!")

    except Exception as e:
        print(f"Syntax Error: {e}")

def copy_to_clipboard(text):
    # Linux
    if "linux" in sys.platform:
        # Check if xclip is installed
        if shutil.which("xclip") is None:
            print("Error: xclip not found. Install it. ", file=sys.stderr)
            return
        # If xclip is installed, proceed with copying text
        subprocess.run(
            ["xclip", "-selection", "clipboard"],
            input=text.strip().encode(),
            check=True,
        )
    # Windows
    elif "win32" in sys.platform:
        subprocess.run(
            ["C:\\Windows\\System32\\clip.exe"],
            input=text.strip().encode(),
            check=True,
        )
    # macOS
    elif "darwin" in sys.platform:
        subprocess.run(
            ["/usr/bin/pbcopy"],  # Full path to pbcopy for macOS
            input=text.strip().encode(),
            check=True,
        )
    else:
        raise OSError("Unsupported operating system")