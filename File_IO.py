# Write a Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns.

# allows users to select a file
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw() # otherwise, the tk window is kept open

file_path = filedialog.askopenfilename() # returns just a string pointing to the file

with open(file_path) as data_file: # this is where the actual IO is done
    
    for line in data_file:

        line = line.replace(',', ' ')
        line = line.rstrip()
        print(line[:11], line[12:16].strip())
