using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System.Collections.Generic;
using FormSubmission.Models;

namespace FormSubmission.Controllers
{
    
    public class UserSubmission : Controller 
    {
        
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            ViewBag.errors = new List<string>();
            return View("index");
        }


        [HttpPost]
        [Route("process")]
        public IActionResult Process(string first, string last, int age, string email, string password)
        {

            User noob = new User
            {
                first = first,
                last = last,
                age = age,
                email = email,
                password = password
            };

            TryValidateModel(noob);
            System.Console.WriteLine(ModelState.IsValid);

            if(ModelState.IsValid)
            {
                System.Console.WriteLine("You have a valid model!");
            }

            else
            {
                System.Console.WriteLine("Sorry, you don't have a good model");
                ViewBag.errors = ModelState.Values;
                return View("index");
            }

            return View();
        }
    }
}