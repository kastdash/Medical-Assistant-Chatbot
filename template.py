# Importing necessary libraries
import os
from pathlib import Path
import logging 

# Logging configuration string
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)

# List of files - 
# _init_.py is an initializer, that turns the src folder into a module
# from which functions may be imported. The src folder contains a helper function,
# prompt function, setup, and application
files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists.")

