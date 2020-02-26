using Newtonsoft.Json;

namespace back.Models.JokeApi
{
    public class ResultJokeModel
    {
        [JsonProperty("joke")]
        public string Joke { get; set; }
    }
}
