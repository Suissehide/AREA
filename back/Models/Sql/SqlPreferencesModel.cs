using System;
using System.Collections.Generic;

using System.Globalization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

namespace back.Models.Sql
{
    public partial class SqlPreferencesModel
    {
        [JsonProperty("id")]
        public long Id { get; set; }

        [JsonProperty("email")]
        public string Email { get; set; }

        [JsonProperty("preferences")]
        public Dictionary<string, Service> services { get; set; }
    }

    
    public partial class Service
    {
        [JsonProperty("service")]
        public bool State { get; set; }

        [JsonProperty("widgets")]
        public Dictionary<string, bool> Widgets { get; set; }
    }
}
