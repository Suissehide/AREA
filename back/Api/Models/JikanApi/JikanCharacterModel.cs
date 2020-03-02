using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.JikanApi
{
    public class JikanCharacterModel
    {
        [JsonProperty("request_hash")]
        public string RequestHash { get; set; }
        
        [JsonProperty("request_cached")]
        public bool RequestCached { get; set; }

        [JsonProperty("request_cache_expiry")]
        public int RequestCacheExpiry { get; set; }

        [JsonProperty("results")]
        public List<CharacterInfoModel> CharacterInfo { get; set; }
        
        [JsonProperty("last_page")]
        public int LastPage { get; set; }
    }
}