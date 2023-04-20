#define a class to decrypt string
class Decryptor:
    #define a method for decrypting a string
    def decrypt(self):
        #ask for string to be decrypted
        encrypted_string = input("Enter a string to decrypt: ")

        return encrypted_string
    
#create an instance of the class    
instance = Decryptor()
#to get the user input and return it
instance.decrypt()

