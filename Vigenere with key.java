import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintStream;
import java.math.BigInteger;
import java.util.Scanner;

public class Vigenere_with_key {

	public static String makekey(String input, String key)
	{
		int x = input.length(); 
	    for (int i = 0; ; i++) 
	    { 
	        if (x == i) 
	            i = 0; 
	        if (key.length() == input.length()) 
	            break; 
	        key+=(key.charAt(i)); 
	    } 
	    return key; 
	}
	
	static String encryptex(String input, String key) 
	{ 
	    String encryptex=""; 
	    for (int i = 0; i < input.length(); i++) 
	    { 
	        int x = (input.charAt(i) + key.charAt(i)) %26; 
	        x += 'A'; 
	        encryptex+=(char)(x); 
	    } 
	    return encryptex; 
	} 
	
	static String decryptex(String encryptex, String key) 
	{ 
	    String original=""; 
	  
	    for (int i = 0 ; i < encryptex.length() && i < key.length(); i++) 
	    {
	        int x = (encryptex.charAt(i) -  
	                    key.charAt(i) + 26) %26;
	        x += 'A'; 
	        original+=(char)(x); 
	    } 
	    return original; 
	} 
	
	public static void main(String[] args) throws FileNotFoundException 
	{
		File text = new File("/Users/ourarchive9820/Downloads/ETOWN FINAL SEMESTER/CS363/cipherKnownKey.txt");
        Scanner input = new Scanner(text);
        String message = input.nextLine();  
      
        String keyword = "TAGORE";
        
		String key = makekey(message, keyword);
		String decrypted =decryptex(message, key);
		
	
		try {
            FileWriter writer = new FileWriter("decryptedtext.txt", true);
            writer.write(decrypted);
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
 
	}
}
