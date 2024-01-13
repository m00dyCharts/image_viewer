import customtkinter
from tkinter import filedialog
from PIL import Image, ImageTk

def directory_selection():
    directory_path = filedialog.askdirectory(initialdir='/home/matt',
                                             title = 'Select directory')
    directory_selection_entry.insert(0, str(directory_path))

def next_image():
    print(directory_selection_entry.get())
    image_label.configure(image = image_list[2])

def previous_image():
    print(directory_selection_entry.get())
    image_label.configure(image = image_list[0])

app = customtkinter.CTk()
app.title("TRADU")

image_list = [ImageTk.PhotoImage(Image.open("/home/matt/Downloads/trading/CL1!_2023-12-26_13-50-51.png")), ImageTk.PhotoImage(Image.open("/home/matt/Downloads/trading/ES1!_2023-12-10_12-19-41.png")), ImageTk.PhotoImage(Image.open("/home/matt/Downloads/trading/ESZ2023_2023-12-05_21-16-30.png"))]

image_frame = customtkinter.CTkFrame(app, width = 350, height = 250)
image_frame.grid(row = 0, column = 0, columnspan = 2, sticky = 'NSEW')

directory_selection_frame = customtkinter.CTkFrame(app, width = 250, height = 50)
directory_selection_frame.grid(row = 1, column = 0, columnspan = 1, sticky = 'SW')

image_controls_frame = customtkinter.CTkFrame(app, width = 100, height = 50)
image_controls_frame.grid(row = 1, column = 1, columnspan = 1, sticky = 'SE')

image_label = customtkinter.CTkLabel(image_frame, image=image_list[1], bg_color='red', fg_color='transparent')
image_label.grid(padx = 14, pady = 14, row = 0, column = 0, columnspan = 1, sticky = 'NSEW')

directory_selection_button = customtkinter.CTkButton(directory_selection_frame, text="Change Directory", command=directory_selection)
directory_selection_button.grid(row = 0, column = 0)

directory_selection_entry = customtkinter.CTkEntry(directory_selection_frame, placeholder_text="Change Directory")  
directory_selection_entry.grid(row = 0, column = 1, padx = 2)  

previous_image_button = customtkinter.CTkButton(image_controls_frame, text=" << ", command=previous_image, width = 25)
previous_image_button.grid(padx = 4, sticky = 'E', row = 0, column = 0)

next_image_button = customtkinter.CTkButton(image_controls_frame, text=" >> ", command=next_image, width = 25)
next_image_button.grid(sticky = 'E', row = 0, column = 1)

app.columnconfigure(0, weight = 1)
app.rowconfigure(0, weight = 1)

app.mainloop()
