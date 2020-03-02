using Newtonsoft.Json;

namespace back.Models
{
    public class TmdbApiMovieModel
    {
        [JsonProperty("id")]
        public string Id { get; set; }

        [JsonProperty("original_title")]
        public string Title { get; set; }

        [JsonProperty("overview")]
        public string Overview { get; set; }

        [JsonProperty("popularity")]
        public string Popularity { get; set; }

        [JsonProperty("vote_average")]
        public string VoteAverage { get; set; }

        [JsonProperty ("release_date")]
        public string Release { get; set; }

    }
}
