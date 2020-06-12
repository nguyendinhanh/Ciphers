package lab3;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
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
		BigInteger p = new BigInteger("521419622856657689423872613771");
    	BigInteger a = new BigInteger("5");
    	BigInteger q = new BigInteger("153312796669816512924567214991");
    	BigInteger b = new BigInteger("3");
    	BigInteger A= converta(q,a,p);
    	BigInteger B= convertb(q,b,p);
    	BigInteger KB= GetKB(a,B,p);
    	BigInteger KA= GetKA(b,A,p);
    	//System.out.println(KB);
    	BigInteger K= KB;
    	String kString = K.toString();
		
    	
		FileInputStream fs = null;
    	File filea = new File("U:\\Public\\a.aes");
    	byte[] data = null;
		try{
    		fs = new FileInputStream(filea);
    		data = new byte[(int)filea.length()];
    		fs.read(data);
    	}catch(Exception e){
    		e.printStackTrace();
    	}
    	
    	byte[] decryptedData = decrypt(data, kString);
    	
    	FileOutputStream fos = new FileOutputStream("dataDecryptedAES.png");
        fos.write(decryptedData);
        fos.close();
	}

	private static BigInteger GetKA(BigInteger b, BigInteger A, BigInteger p) {
		System.out.println(A.modPow(b, p));
		return A.modPow(b, p);
	}

	private static BigInteger GetKB(BigInteger a, BigInteger B, BigInteger p) {
		System.out.println(B.modPow(a, p));
		return B.modPow(a, p);
	}

	private static BigInteger convertb(BigInteger q, BigInteger b, BigInteger p) {		
		return q.modPow(b,p);
	}

	private static BigInteger converta(BigInteger q, BigInteger a, BigInteger p) {
		return q.modPow(a,p);
	}

}

