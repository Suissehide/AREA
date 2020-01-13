using Newtonsoft.Json;

namespace back.Models.PotterApi
{
    public class PotterCharactersModel
    {
        [JsonProperty("_id")]
        public string Id { get; set; }
        
        [JsonProperty("name")]
        public string Name { get; set; }
        
        [JsonProperty("role")]
        public string Role { get; set; }
        
        [JsonProperty("house")]
        public string House { get; set; }
        
        [JsonProperty("school")]
        public string School { get; set; }
        
        [JsonProperty("__v")]
        public string V { get; set; }
        
        [JsonProperty("ministryOfMagic")]
        public bool MinistryOfMagic { get; set; }
        
        [JsonProperty("orderOfThePhoenix")]
        public bool OrderOfThePhoenix { get; set; }
        
        [JsonProperty("dumbledoresArmy")]
        public bool DumbledoresArmy { get; set; }
        
        [JsonProperty("deathEater")]
        public bool DeathEater { get; set; }
        
        [JsonProperty("bloodStatus")]
        public string BloodStatus { get; set; }
        
        [JsonProperty("species")]
        public string Species { get; set; }
    }
}