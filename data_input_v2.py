# Set up imports
from tkinter import *


class analyse:

  def __init__(self):

    # Sets up feedback format function
    self.var_feedback = StringVar()
    self.var_feedback.set("")

    # Sets up has error format function
    self.var_has_error = StringVar()
    self.var_has_error.set("no")
    
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
    self.scan_error = Label(self.scan_frame, text="", fg="#9C0000")
    self.scan_error.grid(row=3)

    # Set up analyse button
    self.button_frame = Frame(self.scan_frame)
    self.button_frame.grid(row=4)

    self.analyse_button = Button(self.button_frame,
                                 text="Analyse",
                                 bg="#2A9DF4",
                                 fg="#FFFFFF",
                                 width=12)

    self.analyse_button.grid(row=0, column=0, padx=5, pady=5)

  def valid_check(self, max_value):
    # Defines error message
    has_error = "no"
    error = "please enter percentages equal to {}%, may not include negatives, decimals or non-numerical subjects".format(max_value)

    # Checks that the user enters a valid number
    response = self.temp_entry.get()
    try:
      response = int(response)
      # Checks if value is above maximum
      if response > max_value:
        has_error = "yes"

      # Sets has error format function so that entry box and labels can be correctly formatted by formatting function
      if has_error == "yes":
        self.var_has_error.set("yes")
        self.var_feedback.set(error)
        return "invalid"
      else:
        return response
      
  
# **** Main Routine ****

  root = Tk()
  root.title("Bias Scanner")
  analyse()
  root.mainloop()
