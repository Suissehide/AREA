using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.GoogleApi.Maps.PlaceDetail
{
    public class PlaceDetailApiModel
    {
        [JsonProperty("result")]
        public Result Result { get; set; }

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

        [JsonProperty("photos")]
        public List<Photo> Photos { get; set; }

        [JsonProperty("opening_hours")]
        public OpeningHours OpeningHours{ get; set; }

        [JsonProperty("types")]
        public List<string> Types { get; set; }

    }

    public class Photo
    {
        [JsonProperty("height")]
        public int Height { get; set; }

        [JsonProperty("width")]
        public int Width { get; set; }

        [JsonProperty("photo_reference")]
        public string PhotoReference { get; set; }
    }

    public class OpeningHours
    {
        [JsonProperty("open_now")]
        public bool OpenNow { get; set; }
    }

}
