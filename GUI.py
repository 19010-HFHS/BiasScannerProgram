# Set up imports
from tkinter import *

class analyse:

  def __init__(self):
    # Set up GUI frame
    self.anal_frame = Frame(padx=10, pady=10)
    self.anal_frame.grid()

    

# **** Main Routine ****
  root = Tk()
  root.title("Bias Scanner")
  analyse()
  root.mainloop()