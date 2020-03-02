
using System;
using Newtonsoft.Json;

namespace back.Models
{
    public class CalendarModel
    {
        [JsonProperty("value")]
        public Value[] Value { get; set; }
    }

    public partial class Value
    {
        [JsonProperty("subject")]
        public string Subject { get; set; }

        [JsonProperty("start")]
        public Start Start { get; set; }
    }

    public class Start
    {
        [JsonProperty("dateTime")]
        public DateTimeOffset DateTime { get; set; }
    }
}
