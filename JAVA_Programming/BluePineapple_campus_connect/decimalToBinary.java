public class decimalToBinary
{
    static void dectobi(int n)
    {
        String bistr="";
        while(n>0)
        {
            int rem=n%2;
            bistr=rem+bistr;
            n=n/2;
        }
        System.out.println(bistr);
    }
    public static void main(String[] args)
    {
        int n=14;
        dectobi(n);
    }
}