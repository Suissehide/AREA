﻿using Newtonsoft.Json;

 namespace back.Models.PotterApi
{
    public class PotterSpellsModel
    {
        [JsonProperty("_id")]
        public string Id { get; set; }
        
        [JsonProperty("spell")]
        public string Spell { get; set; }
        
        [JsonProperty("type")]
        public string Type { get; set; }
        
        [JsonProperty("effect")]
        public string Effect { get; set; }
        
        [JsonProperty("__v")]
        public int V { get; set; }
    }
}