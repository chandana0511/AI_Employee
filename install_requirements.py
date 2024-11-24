import os

def install_packages():
    packages = [
        "pandas==2.0.1",
        "numpy==1.24.2",
        "scikit-learn==1.2.2",
        "matplotlib==3.7.1",
        "seaborn==0.12.2",
        "openpyxl==3.1.2",
        "argparse==1.4.0",
        "nltk==3.8.1",
        "spacy==3.5.0",
        "pytest==7.4.0",
        "tabulate==0.9.0"
    ]
    
    for package in packages:
        os.system(f"pip install {package}")

if __name__ == "__main__":
    install_packages()
