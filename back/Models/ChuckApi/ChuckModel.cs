using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.ChuckApi
{
    public class ChuckModel
    {
        [JsonProperty("result")]
        public List<ChuckJokeModel> Result { set; get; }
        
        [JsonProperty("total")]
        public int Total { get; set; }
    }
}