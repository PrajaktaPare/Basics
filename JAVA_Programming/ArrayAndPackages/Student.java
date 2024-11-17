/**Define a Student class (roll number, name, percentage). Define a default and parameterized  
constructor. Keep a count of objects created. Create objects using parameterized constructor and  
display the object count after each object is created. (Use static member and method). Also  
display the contents of each object.   */

import java.util.*;

 public class Student {
    int rollnumber;
    String name;
    float per;
    static int count=0;
    public Student()
    {
        rollnumber=0;
        name=null;
        per=0;

    }

    public Student(int rollnumber,String name,float per)
    {
        this.rollnumber=rollnumber;
        this.name=name;
        this.per=per;
        count++;
    }
    public static void count()
    {
        System.out.println("Total number of Students :"+count);
    }
    public void display()
    {
        System.out.println("Roll number : "+rollnumber);
        System.out.println("Name : "+name);
        System.out.println("Percentage : "+per);
        System.out.println("\n");
    }


}

public  class StudentMain
{
    public static void main(String [] args) 
    {
        Student s1=new Student(1,"Rani",78.89f );
       Student s2=new Student(2,"Raja",78.89f);
        Student.count();
        s1.display();
        s2.display();
    }
}