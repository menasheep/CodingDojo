using System;
using System.Collections.Generic;

namespace ConsoleApplication
{
    public class Human
    {
        public string name;
        public int strength = 3;
        public int intelligence = 3;
        public int dexterity = 3;
        public int health = 100;


        // basic constructor that only takes name arg
        public Human(string n){
            name = n;
        }

        // custom constructor
        public Human(string n, int str, int intl, int dex, int hp){
            name = n;
            strength = str;
            intelligence = intl;
            dexterity = dex;
            health = hp; 
        }

        //attacks another Human object
        public void Attack(object target){
            Human enemy = target as Human;
            if(enemy != null){
                enemy.health -= 5 * strength;
            }
        }
    }
}