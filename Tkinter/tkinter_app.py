from tkinter import Tk, filedialog  # Import Tkinter modules for GUI and file dialog functionality

# Create the main Tkinter window instance
root = Tk()

# Hide the root window (we only want the file dialog to appear)
root.withdraw()

# Open a file dialog to select a file and store the file path
file_path = filedialog.askopenfilename()

# Print the selected file path to the console
print(file_path)
