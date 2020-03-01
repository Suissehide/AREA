using System.Threading.Tasks;
using back.Models.StarWarsApi;
using Refit;

namespace back.Clients.StarWarsApi
{
    public interface IChuckClient
    {
        [Get("/jokes/search?query={theme}")]
        Task<StarWarsPeoplesModel> ChuckByTheme(string theme);
    }
}