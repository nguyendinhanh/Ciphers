/*********************************
*
*  Project Name: One Time, One Time
*  Description: Ciphers and deciphers messages with its specific key with a process called one time pad.
*  Date: February 16, 2018  
*  Authors: Anh Nguyen
*
**********************************/
#include <stdio.h>

#define MAXLENGTH 2048

//Prototypes:
int readIn(unsigned char text[]);
int tile(unsigned char key[], int keyLength, int messageLength);
void convert(unsigned char key[], int keyLength);
unsigned char rotate (unsigned char character, int count);
int bits(unsigned char character);
void cipherMessage(unsigned char key[], unsigned char message[], unsigned char cipher[], int messageLength);
void print(unsigned char text[], int length);


int main()
{
	//Creates arrays for the message, key and, cipher with maximal length defines.
	unsigned char message[MAXLENGTH];
	unsigned char key[MAXLENGTH];
	unsigned char cipher[MAXLENGTH];
	
	//Reads in the message and stores the length of the recorded message in the message array.
	int messageLength = readIn(message);
	//Reads in the key and stores the length of the recorded key in the key array.
	int keyLength = readIn(key);
	//Uses the tile function to expand key so key length matches the message length.
	keyLength = tile(key, keyLength, messageLength);
	
	//Converts the key into the new more secure key.
	convert(key, keyLength);
	//Ciphers the message with key obtained above.
	cipherMessage(key, message, cipher, messageLength);
	//Prints the ciphered message.
	print(cipher, messageLength);
}

//Reads in characters  until the delimitor or EOF is hit. Should the input be longer then maximum length the rest of the characters is simply ignored.
int readIn(unsigned char text[]) 
{
	//Setting the length to 0.
	int length = 0;
	//Gets the first character from the input.
	int character = getchar();				
	//Loop runs while character is not delimitor or EOF.
	while(character != 255 && character != EOF) {
		//Only if the maximum length is not exceeded the read in character is stored in the array.
		if (length < MAXLENGTH) {
			text[length] = character;	
			//The length is incremented
			++length;
		}
		//Get the next character from the input.
		character = getchar();
	}
	//Return the length of the read in message.
	return length;
}

//Expand and repeat the key to match the length of the message.
int tile(unsigned char text[], int keyLength, int messageLength)
{
	int index;
	//Set the initial index to the key length which is the beginning of the new repeated key.
	//Loop which runs until the new key has the length of the message.	
	for (index = keyLength; index < messageLength; ++index) {
		//Put the repeated characters into the key.
		text[index] = text[index % keyLength];
	}
	//Return the new key length which should match the message length now.
	return index;
}

//Converts the key into the new harder to crack key.
void convert(unsigned char key[], int keyLength) 
{
	//Initialize sum to the last itme in the key.
	int sum = key[keyLength - 1] % keyLength;
	int i;
	//Create the first element in the new key.
	key[0] = rotate(key[0] ^ key[sum], bits(key[keyLength - 1]));
	//Update the new running sum.
	sum = (sum + key[0]) % keyLength;
	//Loops from the second character in the key to the last one.
	for (i = 1; i < keyLength; ++i) {
		//Rotates the XORed key by the value returned in the bits function and updates the key character.
		key[i] = rotate((key[i] ^ key[sum]), bits(key[i - 1]));
		//Update the new running sum.
		sum = (sum + key[i]) % keyLength;
	}
}

//Rotate the bits in a character by a specific count.
unsigned char rotate (unsigned char character, int count) 
{
	int i, pad;
	//Loop count time to rotate the last seven bits of the character.
	for (i = 0; i < count; ++i) {
		pad = 0;
		//If the last bit is odd then the seventh one has to be changed to a one. A pad is create which has a one at the 7th bit.
		if ((character & 1) == 1)
			pad = (1 << 6) ;
		//Shift the character by one to the right.
		character >>= 1;
		//OR the pad to take care of the 7th bit.
		character |= pad;
	}
	//Return the new character.
	return character;
}

//Gets the ammount of one bits in a character.
int bits(unsigned char character) 
{
	//Counter starts at 0.
	int counter = 0;
	int i;
	//Loops eight times to look at every bit in the character.
	for (i = 0; i < 8; ++i) {
		//If the last bit in the character is a one the counter is incremented.
		if ((character & 1) == 1) 
			++counter;
		//The character is shifted to the right by one.
		character >>= 1;
	}
	//The amount of bits in the character is returned.
	return counter;
}

//Ciphers the message with the new key and stores the encrypted characters in the cipher array.
void cipherMessage(unsigned char key[], unsigned char message[], unsigned char cipher[], int messageLength)
{
	int i;
	//Loops through the whole message and XORs the message and key at each location.
	for (i = 0; i < messageLength; ++i)
		cipher[i] = message[i] ^ key[i];
}

//Prints out the charcters in the array.
void print(unsigned char text[], int length) 
{
	int i;
	for (i = 0; i < length; ++i) 
		putchar(text[i]);
}
