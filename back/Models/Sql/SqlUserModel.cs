using System;
using System.Collections.Generic;

using System.Globalization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

namespace back.Models.Sql
{
    public partial class SqlUserModel
    {
        [JsonProperty("users")]
        public User[] Users { get; set; }
    }

    public partial class User
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("pwd")]
        public string Pwd { get; set; }

        [JsonProperty("email")]
        public string Email { get; set; }

        [JsonProperty("microsoftToken")]
        public string MicrosoftToken { get; set; }

        [JsonProperty("facebookToken")]
        public string FacebookToken { get; set; }

        [JsonProperty("googleToken")]
        public string GoogleToken { get; set; }
    }
}
