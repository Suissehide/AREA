using Newtonsoft.Json;

namespace Entrainement.Models
{
    public class TmdbApiMovieModel
    {
        [JsonProperty("id")]
        public string Id { get; set; }

        [JsonProperty("original_title")]
        public string Title { get; set; }

        [JsonProperty("overview")]
        public string Overview { get; set; }

    }
}
