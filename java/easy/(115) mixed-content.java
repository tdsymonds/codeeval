import java.io.*;
import java.util.*;
public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            
            String[] lineArray = line.split(",", -1);
            
            List<String> wordList = new ArrayList<>();
            List<String> digitList = new ArrayList<>();

            for (String elm : lineArray){
                if (Main.isNumeric(elm)){
                    digitList.add(elm);
                }
                else{
                    wordList.add(elm);
                }
            }

            String result = "";

            if (wordList.size() > 0){
                for (String word : wordList){
                    result += word + ",";
                }
                result = result.substring(0, result.length()-1);
            }

            if ((wordList.size()) > 0 && (digitList.size() > 0)){
                result += "|";
            }

            if (digitList.size() > 0){
                for (String digit : digitList){
                    result += digit + ",";
                }
                result = result.substring(0, result.length()-1);
            }

            System.out.println(result);

        }
    }

    public static boolean isNumeric(String inputData) {
        return inputData.matches("[-+]?\\d+(\\.\\d+)?");
    }
}