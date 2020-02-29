using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.GoogleApi.Maps.PlaceDetail
{
    public class PlaceDetailApiModel
    {
        [JsonProperty("results")]
        public List<Result> Results { get; set; }

        [JsonProperty("status")]
        public string Status { get; set; }
    }

    public class Result
    {
        [JsonProperty("formatted_phone_number")]
        public string FormattedPhoneNumber { get; set; }

        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("rating")]
        public double Rating { get; set; }
    }
}
