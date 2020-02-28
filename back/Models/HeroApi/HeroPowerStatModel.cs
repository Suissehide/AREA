using Newtonsoft.Json;

namespace back.Models.HeroApi
{
    public class HeroPowerStatModel
    {
        [JsonProperty("intelligence")]
        [JsonConverter(typeof(ParseStringConverter))]
        public long Intelligence { get; set; }

        [JsonProperty("strength")]
        [JsonConverter(typeof(ParseStringConverter))]
        public long Strength { get; set; }

        [JsonProperty("speed")]
        [JsonConverter(typeof(ParseStringConverter))]
        public long Speed { get; set; }

        [JsonProperty("durability")]
        [JsonConverter(typeof(ParseStringConverter))]
        public long Durability { get; set; }

        [JsonProperty("power")]
        [JsonConverter(typeof(ParseStringConverter))]
        public long Power { get; set; }

        [JsonProperty("combat")]
        [JsonConverter(typeof(ParseStringConverter))]
        public long Combat { get; set; }
    }
}