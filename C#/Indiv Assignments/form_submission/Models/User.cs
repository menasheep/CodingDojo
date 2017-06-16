using System.ComponentModel.DataAnnotations;

namespace  FormSubmission.Models{
    public class User : BaseEntity{
        [Required]
        [MinLength(2)]
        public string first { get; set; }

        [Required]
        [EmailAddress]
        public string last { get; set; }

        [Required]
        public int age { get; set; }

        [Required]
        [EmailAddress]
        public string email { get; set; }

        [Required]
        [DataType(DataType.Password)]
        public string password { get; set; }
    }
}