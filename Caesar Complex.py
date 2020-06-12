import string

### DO NOT MODIFY THIS FUNCTION ###
def read_word_list(file_name):
    '''
    file_name (str): the name of the file containing the list of words
    to load.
    
    Returns: a set of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    try:
        in_file = open(file_name, 'r') # in_file: file
        line = in_file.readline()      # line: str
        word_list = line.split()       # word_list: list of str
        in_file.close()
    except IOError:
        print("Unable to read:", file_name)
        word_list = []
    return frozenset(word_list)       # creates an immutable set.

### DO NOT MODIFY THIS FUNCTION ###
def read_message_string(file_name):
    """
    Returns: a possibly profound message in encrypted text.
    """
    try:
        in_file = open(file_name, "r")
        message = str(in_file.read())
        in_file.close()
    except IOError:
        print("Unable to read: ", file_name)
        message = ""
    return message

# IMPLEMENT THIS FUNCTION
def create_shift_table(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
        
    shift (int): the amount by which to shift every letter of the 
    alphabet, 0 <= shift < N_LETTERS. If shift is less than zero or
    greater than or equal to N_LETTERS, this function must raise a
    ValueError() exception.

    Returns: a dictionary mapping a letter (str) to another
             letter (str), for all lower and upper case letters.
    '''
    # YOUR CODE HERE
    if shift < 0:
        raise ValueError()
    elif shift >=26:
        raise ValueError()
    
    letters = string.ascii_lowercase
    letters_shifted = (letters * 2)[shift : shift + 26]
    letters = letters + letters.upper()
    letters_shifted = letters_shifted + letters_shifted.upper()

    shift_dict = {}

    for i in range(52):
        shift_dict[letters[i]] = letters_shifted[i]
        
    return shift_dict    
        
### IMPLEMENT THIS FUNCTION
def apply_shift(original_text, shift):
    '''
    Applies the Caesar Cipher to original_text with the input shift.
    Creates a new string that is original_text shifted down the
    alphabet by some number of characters determined by the input shift        
    shift (int): the shift with which to encrypt the message.
    0 <= shift < N_LETTERS

    Returns: the message text (str) in which every character is shifted
             down the alphabet by the input shift
    '''
    # YOUR CODE HERE
    new_msg = []
    for i in original_text:
        if i not in create_shift_table(shift).keys():
            new_msg.append(i)
            continue
        else:
            new_msg.append(create_shift_table(shift)[i])
    return ''.join(new_msg)
                                                     
### DO NOT MODIFY THIS FUNCTION ###
def encrypt_message(original_text, shift):
    '''
    Used to encrypt the message using the given shift value.
        
    Returns: The encrypted string.
    '''
    return apply_shift(original_text, shift)

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation
        
    word (str): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word('bat')
    True
    >>> is_word('asdf')
    False
    '''
    garbage = " !@#$%^&*()-_+={}[]|\:;'<>?,./\""
    return word.strip(garbage).lower() in VALID_WORDS

### IMPLEMENT THIS FUNCTION ###
def decrypt_message(cipher_text):
    '''
    Decrypt cipher_text by trying every possible shift value
    and find the "best" one. We will define "best" as the shift that
    creates the maximum number of real words when we use apply_shift(shift)
    on the text. If s is the original shift value used to encrypt
    the message, then we would expect N_LETTERS - s to be the best shift value 
    for decrypting it.

    Note: if multiple shifts are equally good such that they all create 
    the maximum number of words, you may choose any of those shifts (and 
    their corresponding decrypted messages) to return

    Returns: a tuple of the best shift value used to decrypt the message
    and the decrypted message text using that shift value.
    '''
    # YOUR CODE HERE
    best_shift = None
    best_words = 0
    message = ""

    for x in range(26):
        decode_text = apply_shift(cipher_text, x)
        words = decode_text.split()
        real_words = sum([is_word(a) for a in words])
        if real_words > best_words:
            best_shift = x
            best_words = real_words
            message = decode_text

    return (best_shift, message)

# DO NOT CHANGE ANY CODE AFTER THIS LINE!!

N_LETTERS = len(string.ascii_lowercase)
VALID_WORDS = read_word_list('words.txt')

# Unit test - verify that create_shift_table is properly implemented.

message = "Hello, World!"
print("*** create_shift_table:", end=" ")
try:
    x = create_shift_table(-1)
except ValueError:
    pass
else:
    assert False # create_shift_table allowed shift < 0
try:
    x = create_shift_table(N_LETTERS)
except ValueError:
    pass
else:
    assert False # create_shift_table allowed shift >= N_LETTERS

n_errors = 0
for i in range(N_LETTERS):
    table = create_shift_table(i)
    assert len(table) == N_LETTERS * 2
    for key in table:
        alt = table[key]
        if key.isupper():
            base = ord('A')
        elif key.islower():
            base = ord('a')
        org = chr(((ord(key) - base) + i) % N_LETTERS + base)
        if alt != org:
            n_errors += 1

if n_errors != 0:
    print("FAILED")
else:
    print("PASSED")
assert n_errors == 0

# Unit test - verify that apply_shift is properly implemented.
print("*** apply_shift:", end=' ')
result = apply_shift(message, 1)
if result != 'Ifmmp, Xpsme!':
    print("FAILED")
else:
    print("PASSED")

# Test encryption.

plaintext = 'Python is pretty useful.'
expected = 'Ravjqp ku rtgvva wughwn.'
print('Expected Output:', expected, end=' ')
print('Actual Output:', encrypt_message(plaintext, 2))
assert expected == encrypt_message(plaintext, 2)

# Test decryption.

ciphertext = "Kdssb Vxpphu, L krsh!"
expected = (23, 'Happy Summer, I hope!')
print('Expected Output:', expected, end = ' ')
print('Actual Output:', decrypt_message(ciphertext))
assert expected == decrypt_message(ciphertext)

# Actually try to decode the message.

ciphertext = read_message_string("message.txt")
result = decrypt_message(ciphertext)
print("Best shift:", result[0])
print(result[1])
