using Newtonsoft.Json;

namespace back.Models.JikanApi
{
    public class OriginCharacterModel
    {
        [JsonProperty("mal_id")]
        public int MalId { get; set; }

        [JsonProperty("type")]
        public string Type { get; set; }
        
        [JsonProperty("name")]
        public string Name { get; set; }
        
        [JsonProperty("url")]
        public string Url { get; set; }
    }
}