#nullable enable
using System;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.JikanApi
{
    public class CharacterInfoModel
    {
        [JsonProperty("mal_id")]
        public int MalId { get; set; }
        
        [JsonProperty("url")]
        public string Url { get; set; }
        
        [JsonProperty("image_url")]
        public string ImageUrl { get; set; }
        
        [JsonProperty("name")]
        public string Name { get; set; }
        
        [JsonProperty("alternative_names")]
        public string[]? AlternativeNames { get; set; }
        
        [JsonProperty("anime")]
        public List<OriginCharacterModel?> Anime { get; set; }

        [JsonProperty("manga")]
        public List<OriginCharacterModel?> Manga { get; set; }
    }
}