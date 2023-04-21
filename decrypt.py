from tkinter import *

#define a class to decrypt string
class Decryptor:
    #define a method for decrypting a string
    def decrypt(self, encrypted_string):
        """Prompts the user for an encrypted string then replaces the sumbols
        to their corresponding letters to generate the decrypted string."""
        #replace all the encrypted characters
        decrypted_string = encrypted_string.replace('*', 'a') \
                                            .replace('&', 'e') \
                                            .replace('#', 'i') \
                                            .replace('+', 'o') \
                                            .replace('!', 'u')        
        return decrypted_string
    
#build a GUI for the Decryptor 
class Interface:
    def __init__(self):
        """Initializes the interface window and runs the main loop."""
        self.root = Tk()
        self.root.geometry("590x370")
        self.root.title("String Decryptor")

        #set the frame for whole background appearance 
        whole_frame= Frame(self.root, width=590, height=370, relief=RIDGE, borderwidth=5, bg="#1c1c1c")
        whole_frame.place(x=0, y=0)

        #create text boxes for the input and output
        self.input_box = Text(whole_frame,  width=20, height=7, relief=RIDGE, borderwidth=5, font = ("verdana", 15), fg="white", bg="black")
        self.input_box.place(x=10, y=100)        
        self.output_box = Text(whole_frame,  width=20, height=7, relief=RIDGE, borderwidth=5, font = ("verdana", 15), fg="white", bg="black")
        self.output_box.place(x=300, y=100)
        
        #affix labels to their designated places
        Label(self.root, text="String Decryptor", font = ("Helvetica 20 bold"), fg="#2986cc", bg="#1c1c1c").pack(pady=10, padx=10)
        input_label = Label(self.root, text="Enter a string to decrypt", font = ("Helvetica 12 bold"), fg="gray", bg="#1c1c1c")
        input_label.place(x=13, y=70)
        output_label = Label(self.root, text="Decrypted Text", font = ("Helvetica 12 bold"), fg="gray", bg="#1c1c1c")
        output_label.place(x=305, y=70)

        #embed buttons for decrypt and reset methods
        decrypt_button = Button(whole_frame, text="Decrypt", relief=RIDGE, borderwidth=3, font = ("verdana 10 bold"), bg="#4676c9", fg="white", command=self.decrypt)
        decrypt_button.place(x=210, y=300)
        reset_button = Button(whole_frame, text="Reset", relief=RIDGE, borderwidth=3, font = ("verdana 10 bold"), bg="#4676c9", fg="white", command=self.reset)
        reset_button.place(x=300, y=300)

        #initialize Decryptor classr 
        self.string_decryptor = Decryptor()        
        self.root.mainloop()

    def decrypt(self):
        """Retrieve the text from the input box, strip any leading/trailing 
        whitespace, and pass it to the Decryptor instance to get the decrypted 
        string. Then, clear the output box to insert the decrypted string."""
        input_box = self.input_box.get("1.0", END).strip()
        output_box = self.string_decryptor.decrypt(input_box)
        self.output_box.delete("1.0", END)
        self.output_box.insert(END, output_box)

    def reset(self):
        """Clears the contents of input and output on its text boxes."""
        self.input_box.delete("1.0", END)
        self.output_box.delete("1.0", END)

Interface()
