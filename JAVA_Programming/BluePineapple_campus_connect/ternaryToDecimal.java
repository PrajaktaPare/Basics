public class ternaryToDecimal {
    static int ternarytodec(int n)
    {
        int decimal =0;
        int base=1;
        while(n>0)
        {
            decimal+=(n%10)*base;
            n/=10;
            base*=3;
        }
        return decimal;
    }
    public static void main(String[] args )
    {
        int ternary=102;
        System.out.println(ternarytodec(ternary));
    }
}
