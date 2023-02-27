# Programmers Names:
# Mariam Alomari.
# Sharifa Alsadah.
# Hana Saleh.
# Razan Alogaiel.
# Reema Aljumaia.

# Instructor: Hussain Alattas.
# ------------------------------------

# importing libraries
from tkinter import filedialog, messagebox as mbox, Button, Label, Frame, Tk, mainloop
from PIL import Image, ImageTk


class handler():
    """Class for opening, encrypting and decrypting images"""

    # supported extensions
    img_ext = r"*.jpg *.png *.tiff *.jpeg *.gif"

    def init(self):
        self.filename = ""
        self.filename1 = ""

    def open_f(self):
        """To fetch the image file name"""
        f_types = [('image files', self.img_ext)]

        # open file dialog box
        self.filename = filedialog.askopenfilename(filetypes=f_types)
        self.filename1 = self.filename

    def encrypt(self):
        """Method to encrypt image"""
        global img

        # get file name
        self.open_f()
        # open the image file
        img = Image.open(self.filename)
        # resize the image
        img_resized = img.resize((400, 200))
        # create a photo image out of the resized image
        img = ImageTk.PhotoImage(img_resized)
        # create a button with the image
        img_button = Button(Window, image=img)
        img_button.place(x=290, y=220)


        En_file = open(self.filename, 'rb')
        # read the image file
        En_image = En_file.read()
        En_file.close()
        # convert image to byte array to apply the Encryption algorithm
        En_image = bytearray(En_image)

        key = 255
        # encrypt the image
        for index, values in enumerate(En_image):
            # xor to get encrypted values
            En_image[index] = values ^ key

        En_file = open(self.filename, 'wb')
        # save the image
        En_file.write(En_image)
        # success message, bg parameter is for specifying the background color,fg parameter is for specifying the font color
        text = Label(Window, text='The Image has been Encrypted Successfully!!', font=("times", 20, "bold"), bg='tan',
                     fg='maroon')
        text.place(x=300, y=460)
        En_file.close()

    def decrypt(self):
        """Method to decrypt an image"""
        self.open_f()
        De_file = open(self.filename1, 'rb')
        # read image file
        De_image = De_file.read()
        De_image = bytearray(De_image)

        key = 255
        for index, values in enumerate(De_image):
            # xor again to decrypt
            De_image[index] = values ^ key

        De_file = open(self.filename1, 'wb')
        # save the decrypted image
        De_file.write(De_image)
        # success message, bg parameter is for specifying the background color,fg parameter is for specifying the font color
        text = Label(Window, text='The Image has been Decrypted Successfully!!', font=("times", 20, "bold"), bg='tan',
                     fg='maroon')
        text.place(x=300, y=460)
        De_file.close()

    def exit(self):
        """Method to create exit window dialog"""
        if mbox.askokcancel("Exit", "Do you want to exit?"):
            Window.destroy()


try:

    # Creating Window
    Window = Tk()
    # set the title of the window
    Window.title("Image Encryption Decryption")
    # setting the geometry of the window which takes a string width x height
    Window.geometry("1000x600")
    # set the background color
    Window.config(bg="navajowhite")

    # Creating Image Frame
    frame = Frame(Window, width=450, height=250, bg='tan')
    frame.place(x=270, y=200)

    # Creating The Label
    main_label = Label(text="Image Encryption\nDecryption", font=("times", 40, "bold"), fg="maroon", bg="navajowhite")
    main_label.place(x=330, y=70)

    # Creating All Buttons
    a = handler()
    # Encryption button will call encrypt() method
    En_button = Button(Window, text='Encrypt', width=20, font=("times", 20, "bold"), highlightbackground="tan",
                       fg="maroon", command=lambda: a.encrypt())
    En_button.place(x=30, y=70)
    # Decryption button will call decrypt() method
    De_button = Button(Window, text='Decrypt', width=20, font=("times", 20, "bold"), highlightbackground="tan",
                       fg="maroon", command=lambda: a.decrypt())
    De_button.place(x=700, y=70)
    # Exit button will call exit() method
    exit_button = Button(Window, text="EXIT", command=a.exit, font=("Arial", 20), bg="red", highlightbackground="tan",
                         fg="maroon", borderwidth=3, relief="raised")
    exit_button.place(x=450, y=500)
    # mainloop() tells Python to run the Tkinter event loop. This method listens for events, such as button clicks
    mainloop()

except Exception as e:
    print('Error caught : ', e)
