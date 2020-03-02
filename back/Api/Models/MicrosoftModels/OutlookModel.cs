using Newtonsoft.Json;

namespace back.Models.MicrosoftModels
{
    public class OutlookModel
    {
        [JsonProperty("value")]
        public Value[] Value { get; set; }
    }

    public class Value
    {
        [JsonProperty("subject")]
        public string Subject { get; set; }

        [JsonProperty("sender")]
        public Sender Sender { get; set; }
    }

    public class Sender
    {
        [JsonProperty("emailAddress")]
        public EmailAddress EmailAddress { get; set; }
    }

    public class EmailAddress
    {
        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("address")]
        public string Address { get; set; }
    }
}