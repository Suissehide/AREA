using System;
using Newtonsoft.Json;

namespace back.Models.JikanApi
{
    public class AnimeInfoModel
    {
        [JsonProperty("url")]
        public String Url { get; set; }
    
        [JsonProperty("title")]
        public String Title { get; set; }
        
        [JsonProperty("synopsis")]
        public String Synopsis { get; set; }
        
        [JsonProperty("type")]
        public String Type { get; set; }
        
        [JsonProperty("episodes")]
        public String Episodes { get; set; }
    }
}