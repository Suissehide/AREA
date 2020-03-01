using System;
using Newtonsoft.Json;

namespace back.Models.IssLocationApi
{
    public class IssLocationModel
    {
        [JsonProperty("iss_position")] public LocationModel IssPosition { get; set; }
    }

    public class LocationModel
    {
        [JsonProperty("latitude")]
        public String Latitude { get; set; }
        
        [JsonProperty("longitude")]
        public String Longitude { get; set; }
    }
}