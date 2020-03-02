using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.JokeApi
{
    public class JokeModel
    {
        [JsonProperty("results")]
        public List<ResultJokeModel> Results { get; set; }
        
        [JsonProperty("total_jokes")]
        public int Total_jokes { get; set; }
    }
}
