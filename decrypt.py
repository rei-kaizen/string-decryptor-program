#define a class to decrypt string
class Decryptor:
    #define a method for decrypting a string
    def decrypt(self):
        """Prompts the user for an encrypted string then replaces the sumbols
        to their corresponding letters to generate the decrypted string."""
        #ask for string to be decrypted
        encrypted_string = input("Enter a string to decrypt: ")
        #replace all the encrypted characters
        decrypted_string = encrypted_string.replace('*', 'a') \
                                            .replace('&', 'e') \
                                            .replace('#', 'i') \
                                            .replace('+', 'o') \
                                            .replace('!', 'u')        
        return decrypted_string
    
instance = Decryptor()
#display the output
print("The plain text: " +  instance.decrypt())
