import java.util.Scanner;
class CaesarCipher {

    public static StringBuffer encrypt(String text, int s) {
        StringBuffer result = new StringBuffer();
        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);
            if (Character.isUpperCase(ch)) {
                char c = (char) (((ch - 'A' + s) % 26) + 'A');
                result.append(c);
            } else if (Character.isLowerCase(ch)) {
                char c = (char) (((ch - 'a' + s) % 26) + 'a');
                result.append(c);
            } else {
                result.append(ch);
            }
        }
        return result;
    }

    public static StringBuffer decrypt(String text, int s) {
        return encrypt(text, 26 - (s % 26));
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the Text Message");
        String text =sc.nextLine();
        System.out.println("Enter the no of Shift");
        int shift = sc.nextInt();

        StringBuffer encrypted = encrypt(text, shift);
        StringBuffer decrypted = decrypt(encrypted.toString(), shift);

        System.out.println("Original Text : " + text);
        System.out.println("Shift         : " + shift);
        System.out.println("Encrypted     : " + encrypted);
        System.out.println("Decrypted     : " + decrypted);
    }
}
