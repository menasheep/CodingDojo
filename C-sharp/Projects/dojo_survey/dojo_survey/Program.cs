using System.IO; // contains all classes that deal w/ input/output
using Microsoft.AspNetCore.Hosting;

namespace dojo_survey{
    public class Program{
        public static void Main(string[] args){
            IWebHost host = new WebHostBuilder()
                .UseKestrel()
                .UseContentRoot(Directory.GetCurrentDirectory())
                .UseStartup<Startup>()
                .Build();

            host.Run();
        }
    }
}
