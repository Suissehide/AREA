using Newtonsoft.Json;

namespace back.Models.HeroApi
{
    public class HeroConnectionsModel
    {
        [JsonProperty("group-affiliation")]
        public string GroupAffiliation { get; set; }

        [JsonProperty("relatives")]
        public string Relatives { get; set; }
    }
}