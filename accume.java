public class Accumul {
    
    public static String accum(String s) {
      String copy = s.toLowerCase();
      int i = 0;
      String out = "";
      for (char ch : copy.toCharArray()){
        String c = Character.toString(ch);
        String rep = new String(new char[i]).replace("\0", c);
        if (out == ""){
          out = c.toUpperCase();
        }
        else {
          out += "-" + c.toUpperCase() + rep;
        }
        i++;
      }
      return out;
    }
}
