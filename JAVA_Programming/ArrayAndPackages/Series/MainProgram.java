/* Create a package named Series having three different classes to print series:  
a. Prime numbers b. Fibonacci series c. Squares of numbers  
Write a program to generate ‘n’ terms of the above series.  */

import series.PrimeNumber;
import series.fibonaccniSeries;
import series.sqauares;
omport java.util.Scanner;

public class Mainprogram
{
    public static void  main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter number : ");
        int n=sc.nextInt();
        PrimeNumber prime =new PrimeNumber();
        fibonacciSeries fibonacci =new fibonacciSeries();
        squares sq=new squares();
        prime.pn(n);
        fibonacci.printFibonacci(n);
        squares.printsquares(n);
    }
}