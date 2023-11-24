
def caesar_encrypt(shift, message):
    encrypted_message = ''
    for i in message:
        # char = i
        # si la chaine possède un espace on le remet juste, print(ord(" ")) ---> 32 donc ceci peut poser problème
        if i == ' ':
            encrypted_message += i
        else:
            # chr() transforme de chiffres UNICODE en ASCII et ord() fait l'inverse
            # le modulo permet de rester dans la plage des 26 lettres de l'alphabet mais ne représente pas un vrai décalage de x 
            # comme on pourrait le faire avec une string contenant deux fois l'alphabet
            # Sur internet j'ai lu que le chiffrement de césar utilisait le décalage et le module
            # ce qui crée le fait que le décalage n'est pas linéaire.
            # Nous pourrions resoudre cet exercice avec décalage linéaire en utilisant par exemple une string avec l'alphabet doublé
            # mais cette méthode ne reproduirait pas le chiffrement de César standard
            if i.isupper():
                encrypted_message += chr((ord(i) + shift - 64) % 26 + 65)
            else:
                encrypted_message +=  chr((ord(i) + shift - 96) % 26 + 97)
    return encrypted_message
        
test = "Hello la Plateforme"
print(test)
encrypted_message = caesar_encrypt(5,test)
print(encrypted_message)
