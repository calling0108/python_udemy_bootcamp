alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

# def caesar(text, shift, direction):
#     caesar_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         if direction == "encode":
#             new_position = position + shift
#         elif direction == "decode":
#             new_position = position - shift
#         caesar_text += alphabet[new_position]
#     print(f"The {direction}d text is {caesar_text}")


# #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(text, shift, direction)


# Answer

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1 # for 문 내에 있으면 shift_amount = -1, 1, -1, 1, -1로 5번 연산하게 됨.
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")

caesar(start_text = text, shift_amount = shift, cipher_direction = direction)