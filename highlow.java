import java.util.Arrays;

public class Kata {
  public static String HighAndLow(String numbers) {
    String arr[] = numbers.split(" ");
    int high = Integer.parseInt(arr[0]);
    int low = Integer.parseInt(arr[0]);
    for (String n : arr){
        int i = Integer.parseInt(n);
        if (i > high) {
            high = i;
        }
        if (i < low) {
            low = i;
        }
    }
    return Integer.toString(high) + " " + Integer.toString(low);
  }
}
