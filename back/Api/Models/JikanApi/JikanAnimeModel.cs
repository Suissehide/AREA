using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.JikanApi
{
    public class JikanAnimeModel
    {
        [JsonProperty("results")]
        public List<AnimeInfoModel> Result { get; set; }
    }
}