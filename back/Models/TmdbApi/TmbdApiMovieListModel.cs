using System.Collections.Generic;
using Newtonsoft.Json;

namespace Entrainement.Models
{
    public class TmbdApiMovieListModel
    {
        [JsonProperty ("results")] 
        public List<TmdbApiMovieModel> Result { get; set; }
    }
}
