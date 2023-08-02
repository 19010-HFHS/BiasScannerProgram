# Set up imports
from tkinter import *

# Set up lists
all_input = []
gender = ""
ethnicity = ""
major_percentage = ""
minor_percentage = ""


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
    instructions = "Please enter the author's gender, ethnicity, and the subject of research for their major percentage and minor percentage, press Analyse after each input"
    self.scan_instructions = Label(self.scan_frame,
                                   text=instructions,
                                   wrap=250,
                                   width=40,
                                   justify="center")

    self.scan_instructions.grid(row=1)

    # Set up input box
    self.scan_input = Entry(self.scan_frame, font=("Arial", "14"))
    self.scan_input.grid(row=3, column=0, padx=10, pady=10)

    # Set up error message
    self.scan_output = Label(self.scan_frame, text="", wrap=250, fg="#9C0000")
    self.scan_output.grid(row=5)

    # Set up analyse button
    self.button_frame = Frame(self.scan_frame)
    self.button_frame.grid(row=4)

    self.analyse_button = Button(self.button_frame,
                                 text="Analyse",
                                 bg="#2A9DF4",
                                 fg="#FFFFFF",
                                 width=12,
                                 command=lambda: self.analysis())

    self.analyse_button.grid(row=0, column=0, padx=5, pady=5)

  def valid_check(self):
    # Defines error message
    has_error = "no"
    error = "Invalid Format: please enter please enter the authors gender and ethnicity, as well as the subject of research for their major and minor percentage"

    # Sets has error format function so that entry box and labels can be correctly formatted by formatting function
    try:
      float(self.scan_input.get())
      has_error = "yes"

    except ValueError:
      has_error = "no"

    if has_error == "yes":
      self.var_has_error.set("yes")
      self.var_feedback.set(error)
      return "invalid"

    else:
      pass

  def analysis(self):
    to_analyse = self.valid_check()
    answer = ""

    # Run analysis
    if self.valid_check() != "invalid":
      # Replace once analysis code is complete
      response = self.scan_input.get()
      all_input.append(response)
      self.scan_input.delete(0, END)
      if len(all_input) == 4:
        match = "False"
        gender = all_input[0]
        ethnicity = all_input[1]
        major_percentage = all_input[2]
        minor_percentage = all_input[3]

        if gender.lower() == major_percentage.lower() or ethnicity.lower(
        ) == major_percentage.lower():
          answer = "Possible Confirmation Bias detected!!!\n Possible Selection Bias detected!!!\n Possible Observer Bias detected!!!\n Before you use this data, you should confirm that it was collected fairly, and take it with a grain of salt."
          match = "True"

        if gender.lower() == minor_percentage.lower() or ethnicity.lower(
        ) == minor_percentage.lower():
          answer = "Possible Confirmation Bias detected!!!\n Possible Selection Bias detected!!!\n Possible Observer Bias detected!!!\n Before you use this data, you should confirm that it was collected fairly, and take it with a grain of salt."
          match = "True"

        elif match == "False":
          answer = "No match detected. However, it is very difficult to perfectly pin down bias. It is advised that you take all information and data with a grain of salt."

    # if valid check returns invalid set feedback to no
    if to_analyse == "invalid":
      # Red text, Pink entry box
      self.scan_output.config(fg="#9C0000")
      self.scan_input.config(bg="#F8CECC")
      self.scan_output.config(text=self.var_feedback.get())

    else:
      output = (all_input, answer)
      self.scan_output.config(fg="#CC7722")
      self.scan_input.config(bg="#FFFFFF")
      self.scan_output.config(text=output)


# **** Main Routine ****
if __name__ == "__main__":
  root = Tk()
  root.title("Bias Scanner")
  analyse()
  root.mainloop()
