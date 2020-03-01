using System.Threading.Tasks;
using back.Models.StarWarsApi;
using Refit;

namespace back.Clients.StarWarsApi
{
    public interface IChuckClient
    {
        [Get("/people")]
        Task<StarWarsPeoplesModel> GetAllCharacters(string theme);
    }
}