from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
def generateKeys():
 private = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
 )
 public = private.public_key()
 return private, public

def signMessage(message, private):
    message = bytes(str(message), 'utf-8') #Converting string message to bytes
    signature = private.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
    )
    return signature

def verification(message, sign, public):
    message = bytes(str(message), 'utf-8')
    try:
        public.verify(
        sign,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
    except:
        print('Error executing public key')
        return False

    

if __name__ == '__main__':
    private, public = generateKeys()
    #print(private)
    #print(public)
    message = "Hello I am Mayank Sharma"
    sign = signMessage(message, private)
    #print(sign)
    check = verification(message, sign, public)
    if check == True:
        print('Message is correct')
    else:
        print('Message is incorrect')