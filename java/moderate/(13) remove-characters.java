import java.io.*;
public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            
            String[] splitLine = line.split(", ");
            String sentance = splitLine[0];
            String charsToRemove = splitLine[1];

            for (char ch: charsToRemove.toCharArray()){
                sentance = sentance.replaceAll(String.valueOf(ch), "");
            }

            System.out.println(sentance);
        }
    }
}
