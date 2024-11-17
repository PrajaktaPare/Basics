/**Write a java program to display the system date and time in various formats shown below:  
Current date is : 31/07/2015  
Current date is : 07-31-2015  
Current date is : Friday July 31 2015  
Current date and time is : Fri July 31 16:25:56 IST 2015  
Current date and time is : 31/07/15 16:25:56 PM +0530  
Current time is : 16:25:56  
Current week of year is : 31  
Current week of month : 5  
Current day of the year is : 212  
Note: Use java.util.Date and java.text.SimpleDateFormat class */




import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class DateTimeDisplay {

    public static void main(String[] args) {
        // Create a Date object to get the current date and time
        Date currentDate = new Date();
        Calendar calendar = Calendar.getInstance();

        // Format the date in various ways using SimpleDateFormat
        SimpleDateFormat format1 = new SimpleDateFormat("dd/MM/yyyy");
        SimpleDateFormat format2 = new SimpleDateFormat("MM-dd-yyyy");
        SimpleDateFormat format3 = new SimpleDateFormat("EEEE MMMM dd yyyy");
        SimpleDateFormat format4 = new SimpleDateFormat("EEE MMM dd HH:mm:ss z yyyy");
        SimpleDateFormat format5 = new SimpleDateFormat("dd/MM/yy HH:mm:ss a Z");
        SimpleDateFormat format6 = new SimpleDateFormat("HH:mm:ss");

        // Print formatted date and time
        System.out.println("Current date is : " + format1.format(currentDate));
        System.out.println("Current date is : " + format2.format(currentDate));
        System.out.println("Current date is : " + format3.format(currentDate));
        System.out.println("Current date and time is : " + format4.format(currentDate));
        System.out.println("Current date and time is : " + format5.format(currentDate));
        System.out.println("Current time is : " + format6.format(currentDate));

        // Additional details using Calendar
        System.out.println("Current week of year is : " + calendar.get(Calendar.WEEK_OF_YEAR));
        System.out.println("Current week of month : " + calendar.get(Calendar.WEEK_OF_MONTH));
        System.out.println("Current day of the year is : " + calendar.get(Calendar.DAY_OF_YEAR));
    }
}