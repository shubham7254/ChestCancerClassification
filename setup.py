# Import the setuptools module to help with packaging the Python project
import setuptools

# Read the contents of the README file to use as the long description for the package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the current version of the project
__version__ = "0.0.0"

# Define metadata for the project
REPO_NAME = "ChestCancerClassification"  # Name of the GitHub repository
AUTHOR_USER_NAME = "shubham7254"                      # Your GitHub username
SRC_REPO = "cnnClassifier"                         # Name of the source code folder (Python package name)
AUTHOR_EMAIL = "shubham.jagtap2000@gmail.com"      # Your contact email

# Call the setup() function to define the package details
setuptools.setup(
    name=SRC_REPO,                    # This is the package name (used for pip install)
    version=__version__,              # Package version
    author=AUTHOR_USER_NAME,          # Author name
    author_email=AUTHOR_EMAIL,        # Author email
    description="A small python package for CNN app",  # Short description
    long_description=long_description,                  # Long description from README.md
    long_description_content="text/markdown",           # Format of long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # GitHub repo URL
    project_urls={                             # Additional project-related URLs
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
)