# A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple
# projects with different dependencies and packages without conflicts

# python -m venv myenv        # Create a virtual environment

# source myenv/bin/activate   # Activate the virtual environment (Linux/macOS)

# myenv\Scripts\activate.bat  # Activate the virtual environment (Windows)

# Once the virtual environment is activated, any packages that you install using pip will be installed in the virtual environment, 
# rather than in the global Python environment. This allows you to have a separate set of packages for each project, without affecting
# the packages installed in the global environment.

# deactivate     # Deactivate the virtual environment


# To create a requirements.txt file, you can use the pip freeze command, which outputs a list of installed packages and their versions.

# pip freeze > requirements.txt   # Output the list of installed packages and their versions to a file

# To install the packages listed in the requirements.txt file, you can use the pip install command with the -r flag:

# pip install -r requirements.txt     # Install the packages listed in the requirements.txt file