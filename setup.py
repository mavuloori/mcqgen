from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Manohara',
    author_email='mavmanohar@gmail.com',
    install_required=['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
    )
