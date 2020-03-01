using System;
using Newtonsoft.Json;

namespace back.Models.HeroApi
{
    public class HeroPowerStatModel
    {
        [JsonProperty("intelligence")]
        public String Intelligence { get; set; }

        [JsonProperty("strength")]
        public String Strength { get; set; }

        [JsonProperty("speed")]
        public String Speed { get; set; }

        [JsonProperty("durability")]
        public String Durability { get; set; }

        [JsonProperty("power")]
        public String Power { get; set; }

        [JsonProperty("combat")]
        public String Combat { get; set; }
    }
}