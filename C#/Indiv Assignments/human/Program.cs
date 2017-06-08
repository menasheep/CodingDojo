using System;
using System.Collections.Generic;

namespace ConsoleApplication
{
    class Program
    {
        public class Human{
        {    
            public static void Main(string[] args)
            {
                Human player1 = new Human("Malina",20,8,16,500);
                Human player2 = new Human("Random NPC");
                player1.Attack(player2);
                Console.WriteLine($"After being attacked by {player1.name}, {player2.name}'s health is now {player2.health}");
            }
    }
}
