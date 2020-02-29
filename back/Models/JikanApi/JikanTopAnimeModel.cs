using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.JikanApi
{
    public class JikanTopAnimeModel
    {
        [JsonProperty("top")]
        public List<Top> Top { get; set; }

    }

    public class Top
    {
        [JsonProperty("rank")]
        public int Rank { get; set; }
        
        [JsonProperty("title")]
        public string Title { get; set; }
        
        [JsonProperty("image_url")]
        public string ImageUrl { get; set; }
        
        [JsonProperty("type")]
        public string Type { get; set; }
        
        [JsonProperty("episodes")]
        public int Episodes { get; set; }
        
        [JsonProperty("start_date")]
        public string StartDate { get; set; }
        
        [JsonProperty("end_date")]
        public string EndDate { get; set; }
        
        [JsonProperty("score")]
        public double Score { get; set; }
    }
}