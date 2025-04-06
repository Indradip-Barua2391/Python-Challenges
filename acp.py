import random
import string

def randPass(length):
    
    lowercases = string.ascii_lowercase
    uppercases = string.ascii_uppercase
    digits = string.digits
    punctuations = string.punctuation
    
    password = [random.choice(lowercases), random.choice(uppercases), random.choice(digits), random.choice
                (punctuations)]
    characters = lowercases + uppercases + digits + punctuations
    
    password = password + random.choice(characters, k = length - len(password))
    
    random.shuffle(password)
    
    return "".join(password)

passLength = random.randit(6,10)
password = randPass(passLength)

print(f"Password: {password}")
    