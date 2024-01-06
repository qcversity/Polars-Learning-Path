"""
This module has a set of functions to be used in the polars learning path.
"""

import importlib
import subprocess
import sys
import re

from importlib.metadata import version, PackageNotFoundError


def get_pip_version():
    result = subprocess.run([sys.executable, '-m', 'pip', '--version'],
                            capture_output=True, text=True)
    
    match = re.search(r'pip (\d+\.\d+\.\d+)', result.stdout)
    return match.group(1) if match else None


def update_pip():
    current_version = get_pip_version()
    if current_version is None:
        print("Unable to determine the current version of pip.")
        return

    # Get the latest version of pip from pypi
    latest_version = subprocess.run([sys.executable, '-m', 'pip', 'index', 'versions', 'pip'],
                                    capture_output=True, text=True).stdout.split()[-1]

    if current_version == latest_version:
        print("pip is already up-to-date.")
    else:
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'],
                stdout=subprocess.DEVNULL,  
                stderr=subprocess.DEVNULL   
            )
            print(f"pip has been successfully updated from {current_version} to {latest_version}.")
        except subprocess.CalledProcessError:
            print("Failed to update pip.")
            

def install_faker():
    """
    Installs the Faker package if it is not already installed in the current Python environment.
    
    This function first checks if the Faker package is available in the current Python environment.
    If Faker is already installed, it prints a message with the installed version.
    If Faker is not installed, it proceeds to install the package using pip.
    
    Exceptions:
        - Catches `importlib.metadata.PackageNotFoundError` if Faker is not installed.
        - May raise exceptions related to subprocess execution or pip installation failures.
    
    Requires:
        - `importlib.metadata` (standard library in Python 3.8 and later; for earlier versions, install `importlib-metadata` package).
        - `subprocess` module for executing the pip install command.
    """

    try:
        # Check if Faker is already installed
        faker_version = version("Faker")
        print(f"Faker is already installed. Version: {faker_version}")
        
    except PackageNotFoundError:
        print("Faker is not installed. Installing Faker...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "Faker"])
        print("Faker has been successfully installed.")


