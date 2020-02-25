using System.Threading.Tasks;
using back.Models.TmdbApi;
using Refit;

namespace back.Clients
{
    interface ITmdbApiClient
    {
        [Get("/search/movie?api_key=bec82ed690e629d60b98dc6f4b85bfaf&language=en&query={title}")]
        Task<TmbdApiMovieListModel> GetMovieInfos(string title);
    }
}
