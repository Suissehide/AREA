using Newtonsoft.Json;
using System;

namespace DashboardAPI.Models.CalendarModels
{
    public class CalendarModel
    {
        [JsonProperty("value")]
        public Value[] Value { get; set; }
    }

    public class Value
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
