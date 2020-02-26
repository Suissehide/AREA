using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.HeroApi
{
    public class HeroApparenceModel
    {
        [JsonProperty("gender")]
        public string Gender { get; set; }

        [JsonProperty("race")]
        public string Race { get; set; }

        [JsonProperty("height")]
        public List<string> Height { get; set; }

        [JsonProperty("weight")]
        public List<string> Weight { get; set; }

        [JsonProperty("eye-color")]
        public string EyeColor { get; set; }

        [JsonProperty("hair-color")]
        public string HairColor { get; set; }
    }
}