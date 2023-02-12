from cryptography.hazmat.primitives.asymmetric import rsa
def generateKeys():
 private = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
 )
 public = private.public_key()
 return private, public

if __name__ == '__main__':
    pr, pu = generateKeys()
    print(pr)
    print(pu)