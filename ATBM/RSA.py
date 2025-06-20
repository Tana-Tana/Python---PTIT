from Crypto.Util import number  

def generate_keypair(bits):  
    p = number.getPrime(bits)  
    q = number.getPrime(bits)  
    n = p * q  
    phi = (p - 1) * (q - 1)  
    
    e = 65537  
    d = pow(e, -1, phi)  
    
    return (e, n), (d, n)  

def encrypt(public_key, plaintext):  
    e, n = public_key  
    plaintext = plaintext % n  
    ciphertext = pow(plaintext, e, n)  
    return ciphertext  

def decrypt(private_key, ciphertext):  
    d, n = private_key  
    plaintext = pow(ciphertext, d, n)  
    return plaintext  

# Sử dụng  
public_key, private_key = generate_keypair(1024)  
message = 42  
encrypted_msg = encrypt(public_key, message)  
decrypted_msg = decrypt(private_key, encrypted_msg)  

print(f"Message: {message}")  
print(f"Encrypted: {encrypted_msg}")  
print(f"Decrypted: {decrypted_msg}")