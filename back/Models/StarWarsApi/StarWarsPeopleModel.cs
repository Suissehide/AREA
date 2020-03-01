using System;
using System.Collections.Generic;

using System.Globalization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

namespace back.Models.StarWarsApi.StarWarsPeopleModel
{
    public partial class StarWarsPeopleModel
    {
        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("height")]
        [JsonConverter(typeof(ParseStringConverter))]
        public long Height { get; set; }

        [JsonProperty("mass")]
        [JsonConverter(typeof(ParseStringConverter))]
        public long Mass { get; set; }

        [JsonProperty("hair_color")]
        public string HairColor { get; set; }

        [JsonProperty("skin_color")]
        public string SkinColor { get; set; }

        [JsonProperty("eye_color")]
        public string EyeColor { get; set; }

        [JsonProperty("birth_year")]
        public string BirthYear { get; set; }

        [JsonProperty("gender")]
        public string Gender { get; set; }

        [JsonProperty("homeworld")]
        public Uri Homeworld { get; set; }

        [JsonProperty("films")]
        public List<Uri> Films { get; set; }

        [JsonProperty("species")]
        public List<Uri> Species { get; set; }

        [JsonProperty("vehicles")]
        public List<Uri> Vehicles { get; set; }

        [JsonProperty("starships")]
        public List<Uri> Starships { get; set; }

        [JsonProperty("created")]
        public DateTimeOffset Created { get; set; }

        [JsonProperty("edited")]
        public DateTimeOffset Edited { get; set; }

        [JsonProperty("url")]
        public Uri Url { get; set; }
    }

    public partial class StarWarsPeopleModel
    {
        public static StarWarsPeopleModel FromJson(string json) => JsonConvert.DeserializeObject<StarWarsPeopleModel>(json, back.Models.StarWarsApi.StarWarsPeopleModel.Converter.Settings);
    }

    public static class Serialize
    {
        public static string ToJson(this StarWarsPeopleModel self) => JsonConvert.SerializeObject(self, back.Models.StarWarsApi.StarWarsPeopleModel.Converter.Settings);
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

    internal class ParseStringConverter : JsonConverter
    {
        public override bool CanConvert(Type t) => t == typeof(long) || t == typeof(long?);

        public override object ReadJson(JsonReader reader, Type t, object existingValue, JsonSerializer serializer)
        {
            if (reader.TokenType == JsonToken.Null) return null;
            var value = serializer.Deserialize<string>(reader);
            long l;
            if (Int64.TryParse(value, out l))
            {
                return l;
            }
            throw new Exception("Cannot unmarshal type long");
        }

        public override void WriteJson(JsonWriter writer, object untypedValue, JsonSerializer serializer)
        {
            if (untypedValue == null)
            {
                serializer.Serialize(writer, null);
                return;
            }
            var value = (long)untypedValue;
            serializer.Serialize(writer, value.ToString());
            return;
        }

        public static readonly ParseStringConverter Singleton = new ParseStringConverter();
    }
}
