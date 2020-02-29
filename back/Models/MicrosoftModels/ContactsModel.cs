using Newtonsoft.Json;

namespace back.Models
{
    public class ContactsModel
    {
        [JsonProperty("value")]
        public Value[] Value { get; set; }
    }
    public partial class Value
    {
        [JsonProperty("displayName")]
        public string DisplayName { get; set; }

        [JsonProperty("scoredEmailAddresses")]
        public ScoredEmailAddress[] ScoredEmailAddresses { get; set; }
    }

    public class ScoredEmailAddress
    {
        [JsonProperty("address")]
        public string Address { get; set; }
    }
}
