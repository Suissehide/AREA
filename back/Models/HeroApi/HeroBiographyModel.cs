using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.HeroApi
{
    public class HeroBiographyModel
    {
        [JsonProperty("full-name")]
        public string FullName { get; set; }

        [JsonProperty("alter-egos")]
        public string AlterEgos { get; set; }

        [JsonProperty("aliases")]
        public List<string> Aliases { get; set; }

        [JsonProperty("place-of-birth")]
        public string PlaceOfBirth { get; set; }

        [JsonProperty("first-appearance")]
        public string FirstAppearance { get; set; }

        [JsonProperty("publisher")]
        public string Publisher { get; set; }

        [JsonProperty("alignment")]
        public string Alignment { get; set; }
    }
}