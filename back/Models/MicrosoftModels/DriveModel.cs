using Newtonsoft.Json;

namespace back.Models.DriveModel
{
    public class DriveModel
    {
        [JsonProperty("value")]
        public Value[] Value { get; set; }
    }

    public class Value
    {
        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("createdBy")]
        public EdBy CreatedBy { get; set; }

        [JsonProperty("lastModifiedBy")]
        public EdBy LastModifiedBy { get; set; }
    }

    public class EdBy
    {
        [JsonProperty("user")]
        public User User { get; set; }
    }

    public class User
    {
        [JsonProperty("email")]
        public string Email { get; set; }

        [JsonProperty("displayName")]
        public string DisplayName { get; set; }
    }
}
