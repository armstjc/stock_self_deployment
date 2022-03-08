import os

def useCurrentWorkingDirecotry():
    path = os.getcwd() ## Gets the current directory
    os.chdir(path)
    print(f"{path} is the curent working directory.")

def changeCurrentWorkingDirectory(new_directory=f"D:\Stocks"):
    os.chdir(new_directory)
    print(f"{new_directory} is the curent working directory.")