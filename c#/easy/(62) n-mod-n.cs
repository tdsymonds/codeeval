using System;
using System.IO;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {
            string line = reader.ReadLine();
            if (null == line)
                continue;
            
            string[] line_array = line.Split(',');
            int n = Int32.Parse(line_array[0]);
            int m = Int32.Parse(line_array[1]);
            Console.WriteLine(n-((n/m)*m));
        }
    }
}