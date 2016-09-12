import java.io.*;
public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            String longestWord = "";
            String[] sentance = line.split(" ", -1);

            for (String word : sentance){
                if (word.length() > longestWord.length()){
                    longestWord = word;
                }
            }

            System.out.println(longestWord);
        }
    }
}