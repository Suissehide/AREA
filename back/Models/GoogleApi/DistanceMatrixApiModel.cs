using System;
using System.Collections.Generic;

using System.Globalization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

namespace back.Models.GoogleApi
{
    public partial class DistanceMatrixApiModel
    {
        [JsonProperty("destination_addresses")]
        public List<string> DestinationAddresses { get; set; }

        [JsonProperty("origin_addresses")]
        public List<string> OriginAddresses { get; set; }

        [JsonProperty("rows")]
        public List<Row> Rows { get; set; }

        [JsonProperty("status")]
        public string Status { get; set; }
    }

    public partial class Row
    {
        [JsonProperty("elements")]
        public List<Element> Elements { get; set; }
    }

    public partial class Element
    {
        [JsonProperty("distance")]
        public Distance Distance { get; set; }

        [JsonProperty("duration")]
        public Distance Duration { get; set; }

        [JsonProperty("status")]
        public string Status { get; set; }
    }

    public partial class Distance
    {
        [JsonProperty("text")]
        public string Text { get; set; }

        [JsonProperty("value")]
        public long Value { get; set; }
    }

    public partial class DistanceMatrixApiModel
    {
        public static DistanceMatrixApiModel FromJson(string json) => JsonConvert.DeserializeObject<DistanceMatrixApiModel>(json, back.Models.GoogleApi.Converter.Settings);
    }

    public static class Serialize
    {
        public static string ToJson(this DistanceMatrixApiModel self) => JsonConvert.SerializeObject(self, back.Models.GoogleApi.Converter.Settings);
    }

    internal static class Converter
    {
        public static readonly JsonSerializerSettings Settings = new JsonSerializerSettings
        {
            MetadataPropertyHandling = MetadataPropertyHandling.Ignore,
            DateParseHandling = DateParseHandling.None,
            Converters =
            {
                new IsoDateTimeConverter { DateTimeStyles = DateTimeStyles.AssumeUniversal }
            },
        };
    }
}
