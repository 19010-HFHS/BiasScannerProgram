# Set up imports
from tkinter import *


class analyse:

  def __init__(self):
    # Set up GUI frame
    self.scan_frame = Frame(padx=10, pady=10)
    self.scan_frame.grid()

    # Set up GUI heading
    self.scan_heading = Label(self.scan_frame,
                              text="Bias Scanner",
                              font=("Arial", "16", "bold"),
                              bg="#AEF359")

    self.scan_heading.grid(row=0)

    # Set up instructions
    instructions = "Please enter your data in the format of two percentages that are equal to 100%"
    self.scan_instructions = Label(self.scan_frame,
                                   text=instructions,
                                   wrap=250,
                                   width=40,
                                   justify="left")

    self.scan_instructions.grid(row=1)

    # Set up input box
    self.scan_input = Entry(self.scan_frame, font=("Arial", "14"))
    self.scan_input.grid(row=2, padx=10, pady=10)

    # Set up error message
    error = "please enter percentages equal to 100%, may not include negatives, decimals or non-numerical subjects"
    self.scan_error = Label(self.scan_frame, text=error, fg="#9C0000")
    self.scan_error.grid(row=3)

    # Set up analyse button
    self.button_frame = Frame(self.scan_frame)
    self.button_frame.grid(row=4)

    self.analyse_button = Button(self.button_frame,
                                 text="Analyse",
                                 bg="#004C99",
                                 fg="#FFFFFF",
                                 width=12)

    self.analyse_button.grid(row=0, column=0, padx=5, pady=5)


# **** Main Routine ****
if __name__ == "__main__":
  root = Tk()
  root.title("Bias Scanner")
  analyse()
  root.mainloop()
