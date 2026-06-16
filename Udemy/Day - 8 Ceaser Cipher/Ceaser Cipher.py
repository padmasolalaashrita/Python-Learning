#Ceaser Cipher for encoding and decoding
direction = input("Type 'encode' to encrypt and 'decode' to decrypt your message.\n").lower()
text = input("Enter your message here.\n").lower()
shift = int(input("Enter the shift number.\n"))

def encode(text,shift):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = list(text)
    n = len(message)
    new_list = [] 

    for i in range(n):
        if message[i] in alphabets:
            pos = alphabets.index(message[i])
            new_pos = pos + shift
            if new_pos >= 26:
                new_pos = (pos + shift) % 26
            new_list.append(alphabets[new_pos])
        else:
            new_list.append(message[i])
            
    new_word = "".join(new_list)   
    
    return new_word


def decode(text, shift):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = list(text)
    n = len(message)
    new_list = [] 

    for i in range(n):
        if message[i] in alphabets:
            pos = alphabets.index(message[i])
            new_pos = (pos - shift)% 26
            new_list.append(alphabets[new_pos])
        else:
            new_list.append(message[i])
            
    new_word = "".join(new_list)   
    
    return new_word

if direction == "encode":
    print(encode(text,shift))
elif direction == "decode":
    print(decode(text,shift))

