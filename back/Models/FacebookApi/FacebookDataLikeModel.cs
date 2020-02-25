﻿using System.Collections.Generic;
 using DashboardAPI.Models.FbModels;
 using Newtonsoft.Json;

 namespace back.Models.FacebookApi
{
    public class FacebookDataLike
    {
        [JsonProperty("data")]
        public List<FacebookLikeStringModel> Data { get; set; }
    }
}
