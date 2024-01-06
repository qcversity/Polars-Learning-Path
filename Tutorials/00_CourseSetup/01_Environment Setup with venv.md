# Environment Setup

It is essential to setup a proper environment for separate projects to avoid package conflicts. And since we are going to learn about a new Python framework `Polars`, it is considered best practive to create a dedicated virtual environment for this course. 

I will illustrate in this setup file how to setup this environment on both Windows and Unix-Based system such as Linux and Mac OS using Python native tool `venv`.


## Why Virtual Environment

If you are new to virtual environment you might wonder what that is and bother using it. Here is a simple definition and why we need to create a virtual environment for this course:
> A virtual environment in Python is like a separate, isolated workspace for your Python projects. It keeps each project's libraries and settings separate, preventing them from interfering with each other.

Here is even a simplified defintion
> Different projects may require different versions of libraries, and conflicts can arise if they share the same environment. Virtual environments allow you to manage project-specific dependencies without interfering with each other.

In essence, creating a distinct environment in Python ensures compatibility, reproducibility, and easy sharing of projects without conflicts or issues when others use your code on their systems.

## Creating Virtual Environment 

To create a virtual environment we will be using command-line interfaces like the Windows Command Prompt for Windows and the terminal for Unix-based systems such as Linux and Mac OS throughout this course, as they are preferable for working with these tools. Familiarity with CLI tools, whether built-in or third-party, is encouraged.


### Create Virtual Environment Using `venv`

1. To create a virtual environment in a given directory, you would run the following command:

```bash
python -m venv /path/to/directory
```
for example you would like to create a project named `plenv` (this folder will be the name of your environment) in your documents folder, you would run:

1. **Linux and Mac OS:**  To create a virtual environment in the "Documents" directory on Linux and Mac OS, you can use the following command:

```bash
python -m venv ~/Documents/plenv
```


2. **Windows:** Assuming Python is in the system's search path, you can create a virtual environment in the "Documents" directory on Windows with this command:

```bash
python -m venv C:\Users\YourUsername\Documents\plenv
```

You can inspect the contents of the created directory. Here is an example from Mac OS:

```bash
tree -L 2 ~/Documents/plenv

/Users/trainer/Documents/plenv
├── bin
│   ├── Activate.ps1
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── pip
│   ├── pip3
│   ├── pip3.11
│   ├── python -> /usr/local/anaconda3/bin/python
│   ├── python3 -> python
│   └── python3.11 -> python
├── include
│   └── python3.11
├── lib
│   └── python3.11
└── pyvenv.cfg
```

for windows you can use the `dir` command. 

### Activating the Virtual Environment:

After creating the virtual environment, you can activate it using the appropriate command based on your system and shell:

1. Linux Based Systems:
    - Bash shell: `source ~/Documents/plenv/bin/activate`
    - Csh shell: `source ~/Documents/plenv/bin/activate.csh`
    - Fish shell: `source ~/Documents/plenv/bin/activate.fish`
2. Windows:
    - Command Prompt: `C:\Users\YourUsername\Documents\plenv\bin\activate.bat`
    - Powershell: `C:\Users\YourUsername\Documents\plenv\bin\activate.ps1`



3. **Using the virtual environment**

Once you’ve activated the new virtual environment, you can start using it. Here are few steps you may to do:

1. Upgrading `pip` Python package manager. Use this command on any system:

```bash
python -m pip install -U pip
```

2. **Install the packages you need:** To install the necessary packages for your project, you have two options:

    - **Manual Installation:** In this course, we require `polars`, `pandas`, `numpy`, and `pyarrow` as a starting point. You can install them individually or all at once using the following command:

```bash
pip install polars pandas numpy pyarrow
```

 - **Using a Requirements File:** This method involves a text file typically named `requirements.txt`, which lists the required libraries along with their versions. This way is the preferred one for large projects. You can install all the dependencies listed in this file with a single command:
  
```bash
pip install -r requirements.txt
```

### Using Virtual Environments with Jupyter Notebooks

Ensure that you have already activated your virtual environment before proceeding with these steps. If you have Jupyter installed system-wide, Then you can skip the first step; otherwise, from your virtual environment directory, follow these steps: 


1. **Install Jupyter Lab (if not already installed system-wide):** If you don't have Jupyter Lab installed system-wide, you can install it in your virtual environment with this command:

```bash
pip install jupyterlab
```

- **Install `ipykernel`:**  This allows you to create a custom kernel specific to your virtual environment. 

```bash
pip install ipykernel
```

- **Add the kernel and the needed components for IPython:**

```bash
ipython kernel install --user --name="Plenv"
```

- **Launch jupyter notebook (or Jupyter lab):** You can launch a notebook from this environment using the command:

```bash
jupyter notebook 
# or 
jupyter lab
```


### Deactivating the Virtual Environment

To deactivate the virtual environment you can terminate the session by usign the `deactivate` command directly from the command prompt or terminal.

Note that exiting the command line tool will also deactivate the virtual environment.


### Removing the Virtual Environment

If you decide you no longer need to virtual environment, you can just delete it like any other folder.
Virtual environments are self-contained. When you no longer need the virtual environment, you can just delete its directory. Just make sure you first close any running copies of Python that use the virtual environment.

1. Delete the Virtual environment on Linux-Based systems

```bash
rm -rf ~/Documents/plenv
```

2. Delete the Virtual environment on Windows systm:

```bash
rd /S  C:\Users\YourUsername\Documents\plenv
```

By following the previous steps, you can ensure a well-structured, isolated environment for your Python projects and streamline the process of working with the different Python frameworks such as Polars. Happy coding!

## Conclusion

In this environment setup guide, we have established the importance of creating a dedicated virtual environment for Python projects. The significance of this step becomes evident when you start handling real world data science projects as well we Programming projects. 



