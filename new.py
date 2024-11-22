import tkinter
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("WaterMarking App")

        self.container = tk.Frame(self, height=400, width=600)
        self.container.grid(column=0, row=0, padx=30, pady=30)

        self.container.columnconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.frames = None
        # for F in (MainPage, SidePage):
        #     frame = F(self.container, self)
        #     self.frames[F] = frame
        #     frame.grid(column=1, row=1)

        self.show_frame(MainPage)

    def show_frame(self, cont):
        new_frame = cont(self.container, self)
        if self.frames is not None:
            self.frames.destroy()
        self.frames = new_frame
        self.frames.pack()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self, text="Watermark your photos!")
        title_label.grid(column=1, row=0, padx=10, pady=10)

        switch = tk.Button(self, text="Get Started", command=lambda: controller.show_frame(SidePage))
        switch.grid(row=1, column=1, padx=10, pady=10)

class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        switch = tk.Button(self, text="Get Started", command=lambda: controller.show_frame(MainPage))
        switch.grid(column=0, row=0, padx=10, pady=10)

        title_label = tk.Label(self, text="Upload Here!")
        title_label.grid(column=1, row=0, columnspan=2, padx=10, pady=10)

        self.upload = tk.Button(self, text="Upload Photo", command=self.open_image)
        self.upload.grid(column=3, row=0, padx=10, pady=10)


    def open_image(self):
        self.file1 = filedialog.askopenfilename()
        self.file_image = Image.open(self.file1)
        self.file_image = self.file_image.resize((500, 300))
        self.photo = ImageTk.PhotoImage(self.file_image)

        self.label = tk.Label(self, image=self.photo)
        self.label.grid(column= 1, row= 1, columnspan=2)
        # self.canvas.create_image(100, 100, image=self.photo)
        self.label.image = self.photo

        self.text = tk.Label(self, text="Text:")
        self.text.grid(column=1, row=3, padx=5, pady=5, sticky="EW")
        self.text_box = tk.Entry(self, width=35, fg="grey")
        self.text_box.grid(column=2, row=3, sticky="EW")
        self.text_box.focus()

        self.color = tk.Label(self, text="Text Color:")
        self.color.grid(column=1, row=4, padx=5, pady=5, sticky="EW")


        colors = ['Red', 'Green', 'Yellow', 'Black', 'White',
                 'Blue', 'Purple']
        self.var = tk.StringVar()

        self.var.set("Black")
        self.color_box = tk.OptionMenu(self, self.var, *colors)
        self.color_box.grid(column=2, row=4, sticky="EW")

        self.size = tk.Label(self, text="Font_Size:")
        self.size.grid(column=1, row=5, padx=5, pady=5, sticky="EW")
        self.size_box= tk.Scale(self, from_=0, to=100, orient='horizontal')
        self.size_box.grid(column=2, row=5, sticky="EW")

        self.save_button = tk.Button(self, text="Save Changes", command= self.dict_print)
        self.save_button.grid(column=1, row=8, columnspan=2, padx=5, pady=5, sticky="EW")


    def dict_print(self):

        my_image = Image.open(self.file1)
        my_image = my_image.resize((500, 300))
        width, height = my_image.size

        size_of_font = int(self.size_box.get())
        text_font = ImageFont.truetype("arial.ttf", size_of_font)
        text_to_add = self.text_box.get()
        color_to_add = self.var.get()

        edit_image = ImageDraw.Draw(my_image)
        edit_image.text((int(width) /2, (int(height)/2 )), text_to_add, fill=color_to_add, font=text_font)

        my_image.save("new_image.png")

        self.text_box.delete(0, tk.END)
        self.text_box.insert(0, "Saving File...")

        self.label.after(2000, self.show_pic)


    def show_pic(self):
        global aspen
        # self.label.destroy()

        aspen = tk.PhotoImage(file="new_image.png")
        # self.label = tk.Label(self, image=aspen)
        # self.label.grid(column=1, row=1, columnspan=2)
        self.label.config(image=aspen)
        self.label.image = aspen
        self.text_box.delete(0, tk.END)
        self.var.set("Black")
        self.label.update()
        self.size_box.set(0)


window = windows()
window.mainloop()
