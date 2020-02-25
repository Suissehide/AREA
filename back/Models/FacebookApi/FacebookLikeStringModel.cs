﻿using Newtonsoft.Json;

 namespace back.Models.FacebookApi
{
    public class FacebookLikeStringModel
    {
        [JsonProperty("name")]
        public string Name { get; set; }
    }
}
