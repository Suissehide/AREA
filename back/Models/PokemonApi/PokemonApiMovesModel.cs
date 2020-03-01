using System;
using System.Collections.Generic;

using System.Globalization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;


namespace back.Models
{

    public class PokemonApiMovesModel
    {
        [JsonProperty("moves")]
        public List<MoveElement> Moves { get; set; }
    }

    public partial class MoveElement
    {
        [JsonProperty("move")]
        public MoveLearnMethodClass Move { get; set; }

        [JsonProperty("version_group_details")]
        public List<VersionGroupDetail> VersionGroupDetails { get; set; }
    }

    public partial class MoveLearnMethodClass
    {
        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("url")]
        public Uri Url { get; set; }
    }

    public partial class VersionGroupDetail
    {
        [JsonProperty("level_learned_at")]
        public long LevelLearnedAt { get; set; }

        [JsonProperty("move_learn_method")]
        public MoveLearnMethodClass MoveLearnMethod { get; set; }

        [JsonProperty("version_group")]
        public MoveLearnMethodClass VersionGroup { get; set; }
    }

}

