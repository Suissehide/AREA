using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.TmdbApi
{
    public class TmbdApiMovieListModel
    {
        [JsonProperty ("results")] 
        public List<TmdbApiMovieModel> Result { get; set; }
    }
}
