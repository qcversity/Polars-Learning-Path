# Environment Setup

It is essential to setup a proper environment for separate projects to avoid package conflicts. And since we are going to learn about a new Python framework `Polars`, it is considered best practive to create a dedicated virtual environment for this course. 

I will illustrate in this setup file how to setup this environment on both Windows and Unix-Based system such as Linux and Mac OS using Anaconda distribution package manager `conda`.


## Why Virtual Environment

If you are new to virtual environment you might wonder what that is and bother using it. Here is a simple definition and why we need to create a virtual environment for this course:
> A virtual environment in Python is like a separate, isolated workspace for your Python projects. It keeps each project's libraries and settings separate, preventing them from interfering with each other.

Here is even a simplified defintion
> Different projects may require different versions of libraries, and conflicts can arise if they share the same environment. Virtual environments allow you to manage project-specific dependencies without interfering with each other.

In essence, creating a distinct environment in Python ensures compatibility, reproducibility, and easy sharing of projects without conflicts or issues when others use your code on their systems.

## Creating Virtual Environment 

To create a virtual environment we will be using command-line interfaces like the Windows Command Prompt for Windows and the terminal for Unix-based systems such as Linux and Mac OS throughout this course, as they are preferable for working with these tools. Familiarity with CLI tools, whether built-in or third-party, is encouraged.


## Create Virtual Environment Using `conda` Package Manager

In this second section, we will be creating a virtual environment using `conda`, a popular package manager in the Python ecosystem. In fact using `conda` is recommended for beginners; 

### Installing Mamba

If you don't have mamba installed, you can download and install it from the official [Miniforge](https://github.com/conda-forge/miniforge)  distribution. 

### Creating a New Virtual Environment:

`mamba` package manager can be used from Windows Command prompt (or Anaconda prompt). While you will keep using the **terminal** for Linux and Mac OS. 

- To create a new virtual environment named `plenv`, launch your command line interface (CLI),  and run the following command:

```bash
mamba create --name plenv
```


### Activating the Virtual Environment

- You can activate the virtual environment `plenv` using the following command: 

```bash
mamba activate plenv
```


### Installing Packages in the Virtual Environment

With your `plenv` virtual environment active, we can install the Python packages `pandas`, `polars`, `numpy` and `pyarrow` like this:

```bash
mamba install numpy pandas polars pyarrow
```

### Using Virtual Environments with Jupyter Notebooks

Ensure that you have already activated your virtual environment as discussed above before proceeding with these steps. We will explain to install Jupyter lab and configure the kernel in the newly created `conda` environment` step by step. From your virtual environment directory, follow these steps: 


1. **Install Jupyter Lab:** You can install `Jupyter lab` in the active virtual environment `plenv` using this command:

```bash
mamba install -c conda-forge jupyterlab
```


- **Install `ipykernel`:**  This allows you to create a custom kernel specific to your virtual environment. 

```bash
mamba install -c anaconda ipykernel
```

- **Add the kernel and the needed components for IPython:**

```bash
python -m ipython kernel install --user --name="Plenv"
```

- **Launch jupyter notebook (or Jupyter lab):** You can launch a notebook from this environment using the command:

```bash
jupyter lab
```

### Deactivating the Virtual Environment

To deactivate the virtual environment and return to your base Python installation, use the following command:

```bash
mamba deactivate
```


### Removing the Virtual Environment

If you no longer need the virtual environment, you can remove it using the following command:

```bash
mamba remove --name myenv --all
```

By following the previous steps, you can ensure a well-structured, isolated environment for your Python projects and streamline the process of working with the different Python frameworks such as Polars. Happy coding!

## Conclusion

In this environment setup guide, we have established the importance of creating a dedicated virtual environment for Python projects. The significance of this step becomes evident when you start handling real world data science projects as well we Programming projects. 

