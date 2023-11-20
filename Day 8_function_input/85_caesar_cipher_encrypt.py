alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower() # text = "Hello"
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

cipher_text = ""
def encrypt(text, shift):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    # 인덱스를 찾고 shift number를 더해서 새로운 index의 string을 출력해주기
    for i in list(text): # ["h", "e", "l", "l", "o"]
        if i in alphabet:
            encoded_index = alphabet.index(i) + shift
            # variable[number]은 index [number]에 해당하는 값을 찾는 것, variable = a.index("b")은 a list의 "b" index number를 찾는 것
            encoded_text = alphabet[encoded_index]
    global cipher_text
    cipher_text += encoded_text
    print(f"The encoded text is {cipher_text}")

    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    # alphabet list item들을 복사한다. index는 첫 item의 값만 반환하기에.

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

encrypt(text, shift)



# Answer

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text: # ["h", "e", "l", "l", "o"]
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")