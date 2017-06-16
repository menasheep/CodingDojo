using System;
using System.Collections.Generic;

namespace collections
{
    class Program
    {
        static void Main(string[] args)
        {   // Code south of here //

            // Three Basic Arrays
            // 1 Create an array to hold integer values 0 through 9 
            // 2 Create an array of the names "Tim", "Martin", "Nikki", & "Sara" 
            // 3 Create an array of length 10 that alternates between true and false values, starting with true
            
            int[] numArr = {11,22,33,44};
            
            foreach(int num in numArr){
                Console.Write(num);
            }

            string[] namesArr = {"Tim", "Martin", "Nikki", "Sara"};
            
            foreach(string name in namesArr){
                Console.WriteLine(name);
            }

            // Multiplication table
            int[,] mult = new int[10,10];
            for(int x=0; x<10; x++){
                for(int y=0; y<10; y++){
                    mult[x,y]=(x+1)*(y+1);
                }
            }

            // Multiplication table display
            for(int x=0; x<10; x++){
                string display="[";
                
                for(int y=0; y<10; y++){
                    display += mult[x,y] + ",";

                    if(mult[x,y]<10){
                        display += " ";
                    }
                }
                display += "]";
                Console.WriteLine(display);
            }

            // List of Ice Cream Flavors
            List <string> flavors = new List <string>();
            flavors.Add("Chocolate");
            flavors.Add("Vanilla");
            flavors.Add("Rocky Road");
            flavors.Add("Cookie Dough");
            flavors.Add("Neopolitan");
            flavors.Add("Rainbow Sherbet");

            // Outputs the length of list
            Console.WriteLine(flavors.Count);

            //Prints the 3rd val and removes it
            Console.WriteLine("The 3rd flavor in the list is " + flavors[2]);
            flavors.RemoveAt(2);

            //Outputs the updated length of the flavors list
            Console.WriteLine(flavors.Count);


            // User Dictionary Construction
            Dictionary <string, string> userInfo = new Dictionary <string, string>();
            Random rand = new Random();
            foreach(string name in namesArr){
                userInfo[name] = flavors[rand.Next(flavors.Count)];
            }

            //Looping through dictionary
            Console.WriteLine("Users and their favorite ice cream flavors:");
            foreach(KeyValuePair<string, string> info in userInfo){
                Console.WriteLine(info.Key + " - " + info.Value);
            }

        }   // Code north of here //
    }
}
