using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.JikanApi
{
    public class JikanTopMangaModel
    {
        [JsonProperty("top")]
        public List<TopManga> Top { get; set; }
    }
    
    public class TopManga
    {
        [JsonProperty("rank")]
        public int Rank { get; set; }
        
        [JsonProperty("title")]
        public string Title { get; set; }
        
        [JsonProperty("type")]
        public string Type { get; set; }
        
        [JsonProperty("start_date")]
        public string StartDate { get; set; }
        
        [JsonProperty("end_date")]
        public string EndDate { get; set; }
        
        [JsonProperty("score")]
        public double Score { get; set; }
        
        [JsonProperty("image_url")]
        public string ImageUrl { get; set; }
    }
}