using System;

namespace fundiesI
{
    class Program
    {
        static void Main(string[] args)
        {
            for(int i=1; i<256; i++){    //print vals 1-255
                Console.WriteLine(i);
            }

            
            for(int i=1; i<101; i++){    //print vals div by 3 or 5
                if(i % 3 == 0 || i % 5 == 0){
                    if(i % 15 != 0){
                        Console.WriteLine(i);
                    }
                }
            }


            for(int i=1; i<101; i++){    //FizzBuzz
                if(i % 3 == 0){
                    Console.WriteLine("Fizz");
                }
                else if( i % 5 == 0){
                    Console.WriteLine("Buzz");
                }
                else if(i % 15 == 0){
                    Console.WriteLine("FizzBuzz");
                }
            }
        }
    }
}

