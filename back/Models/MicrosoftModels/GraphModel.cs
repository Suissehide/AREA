using Newtonsoft.Json;
using System;

namespace back.Models.GraphModel
{
    public class GraphModel
    {
        [JsonProperty("businessPhones")]
        public object[] BusinessPhones { get; set; }

        [JsonProperty("displayName")]
        public string DisplayName { get; set; }

        [JsonProperty("givenName")]
        public string GivenName { get; set; }

        [JsonProperty("jobTitle")]
        public object JobTitle { get; set; }

        [JsonProperty("mail")]
        public string Mail { get; set; }

        [JsonProperty("mobilePhone")]
        public object MobilePhone { get; set; }

        [JsonProperty("officeLocation")]
        public object OfficeLocation { get; set; }

        [JsonProperty("preferredLanguage")]
        public object PreferredLanguage { get; set; }

        [JsonProperty("surname")]
        public string Surname { get; set; }

        [JsonProperty("userPrincipalName")]
        public string UserPrincipalName { get; set; }

        [JsonProperty("id")]
        public Guid Id { get; set; }
    }
}
