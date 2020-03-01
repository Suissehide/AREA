using System.Threading.Tasks;
using back.Models.StarWarsApi.StarWarsPeopleModel;
using back.Models.StarWarsApi.StarWarsPeoplesModel;
using Refit;

namespace back.Clients.StarWarsApi
{
    public interface IStarWarsApiClient
    {
        [Get("/people")]
        Task<StarWarsPeoplesModel> GetAllCharacters();

        [Get("/people/{id}")]
        Task<StarWarsPeopleModel> getCharacterById(string id);
    }
}