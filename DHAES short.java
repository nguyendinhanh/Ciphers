import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.Base64;
 
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
 
public class DHAES {
 
    private static SecretKeySpec secretKey;
    private static byte[] key;
    
	//set up the key, please don't edit here
    public static void setKey(String myKey)
    {
        MessageDigest sha = null;
        try {
            key = myKey.getBytes("UTF-8");
            sha = MessageDigest.getInstance("SHA-1");
            key = sha.digest(key);
            key = Arrays.copyOf(key, 16);
            secretKey = new SecretKeySpec(key, "AES");
        }
        catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
    }
    
	//encryption, please don't edit here
    public static byte[] encrypt(byte[] strToEncrypt, String secret)
    {
        try
        {
            setKey(secret);
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
            
            cipher.init(Cipher.ENCRYPT_MODE, secretKey);
            return cipher.doFinal(strToEncrypt);
        }
        catch (Exception e)
        {
            System.out.println("Error while encrypting bytes: " + e.toString());
        }
        return null;
    }

    //decryption, please don't edit here
    public static byte[] decrypt(byte[] strToDecrypt, String secret)
    {
        try
        {
            setKey(secret);
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
            cipher.init(Cipher.DECRYPT_MODE, secretKey);
            return cipher.doFinal(strToDecrypt);
        }
        catch (Exception e)
        {
            System.out.println("Error while decrypting bytes: " + e.toString());
        }
        return null;
    }
	
	/**********************
     * Please edit in the main function.
     * 1. read the file in bytes
     * 2. generate the key
     * 3. decrypt the file using corresponding function above
     */
	
	public static void main(String[] args) throws FileNotFoundException, IOException
    {
		//Read the File in bytes
		FileInputStream fs = null;
    	File fileinput = new File("U:\\Private\\a.aes");
    	byte[] fileinbyte = null;
		try{
    		fs = new FileInputStream(fileinput);
    		fileinbyte = new byte[(int)fileinput.length()];
    		fs.read(fileinbyte);
    	}catch(Exception e){
    		e.printStackTrace();
    	}
        
		//Generate the key
		int a = 5;
		int b = 3;
		
		BigInteger p = new BigInteger("521419622856657689423872613771");
		BigInteger q = new BigInteger("153312796669816512924567214991");
		
		BigInteger k = (q.modPow(BigInteger.valueOf(b), p)).modPow(BigInteger.valueOf(a), p);
		
		//Using decrypt to solve
		byte[] msg = DHAES.decrypt(fileinbyte, k.toString());
        
		//Output
		FileOutputStream fos = new FileOutputStream("msgoutput.png");
        fos.write(msg);
        fos.close();
    }
 
}
