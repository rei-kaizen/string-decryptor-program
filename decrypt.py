from tkinter import *

#define a class to decrypt string
class Decryptor:
    #define a method for decrypting a string
    def decrypt(self, encrypted_string):
        """Prompts the user for an encrypted string then replaces the sumbols
        to their corresponding letters to generate the decrypted string."""
        #replace all the encrypted characters
        #ask for string to be decrypted
        # encrypted_string = input("Enter a string to decrypt: ")
        decrypted_string = encrypted_string.replace('*', 'a') \
                                            .replace('&', 'e') \
                                            .replace('#', 'i') \
                                            .replace('+', 'o') \
                                            .replace('!', 'u')        
        return decrypted_string
    
#display the output
#print("The plain text: " +  Decryptor().decrypt()) 
   
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

        self.root.mainloop()

Interface()