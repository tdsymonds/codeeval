import java.io.*;
public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            String[] list_array = line.split(",", -1);
            int n = Integer.parseInt(list_array[0]);
            int m = Integer.parseInt(list_array[1]);

            System.out.println(n-((n/m)*m));
        }
    }
}