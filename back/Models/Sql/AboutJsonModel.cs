using System;
using System.Collections.Generic;

using System.Globalization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

    public partial class AboutJsonModel
    {
        [JsonProperty(" client ")]
        public Client Client { get; set; }

        [JsonProperty(" server ")]
        public Server Server { get; set; }
    }

    public partial class Client
    {
        [JsonProperty(" host ")]
        public string Host { get; set; }
    }

    public partial class Server
    {
        [JsonProperty(" current_time ")]
        public long CurrentTime { get; set; }

        [JsonProperty(" services ")]
        public Services[] Services { get; set; }
    }

    public partial class Services
    {
        [JsonProperty(" name ")]
        public string Name { get; set; }

        [JsonProperty(" actions ")]
        public Actions[] Actions { get; set; }
    }

    public partial class Actions
    {
        [JsonProperty(" name ")]
        public string Name { get; set; }

        [JsonProperty(" description ")]
        public string Description { get; set; }
    }
