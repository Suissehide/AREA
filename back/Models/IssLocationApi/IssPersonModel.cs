using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.IssLocationApi
{
    public class IssPersonModel
    {
        [JsonProperty("people")]
        public List<Person> People { get; set; }

        [JsonProperty("number")]
        public long Number { get; set; }
    }

    public partial class Person
    {
        [JsonProperty("craft")]
        public string Craft { get; set; }

        [JsonProperty("name")]
        public string Name { get; set; }
    }
}