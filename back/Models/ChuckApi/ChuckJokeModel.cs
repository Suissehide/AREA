using Newtonsoft.Json;

namespace back.Models.ChuckApi
{
    public class ChuckJokeModel
    {
        [JsonProperty("value")]
        public string Value { get; set; }
    }
}