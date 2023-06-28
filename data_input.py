# Set up imports
from tkinter import *


class analyse:

  def __init__(self):
    # Set up GUI frame
    self.scan_frame = Frame(padx=10, pady=10)
    self.scan_frame.grid()

    # Set up GUI heading
    self.scan_heading = Label(self.anal_frame,
                              text="Bias Scanner",
                              font=("Arial", "16", "bold"))

    self.scan_heading.grid(row=0)

    # Set up instructions
    instructions = "Please enter your data in the format of two percentages that are equal to 100%"
    self.scan_instructions = Label(self.scan_frame,
                                   text=instructions,
                                   wrap=250,
                                   width=40,
                                   justify="left")

    self.scan_instructions.grid(row=1)

# **** Main Routine ****

  root = Tk()
  root.title("Bias Scanner")
  analyse()
  root.mainloop()
