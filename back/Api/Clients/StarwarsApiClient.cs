using System.Threading.Tasks;
using back.Models.StarWarsApi.StarWarsPeopleModel;
using back.Models.StarWarsApi.StarWarsPlanetModel;
using back.Models.StarWarsApi.StarWarsStarshipModel;
using Refit;

namespace back.Clients.StarWarsApi
{
    public interface IStarWarsApiClient
    {
        [Get("/people/{id}")]
        Task<StarWarsPeopleModel> GetCharacterById(int id);

        [Get("/planets/{id}")]
        Task<StarWarsPlanetModel> GetPlanetById(int id);

        [Get("/starships/{id}")]
        Task<StarWarsStarshipModel> GetStarshipById(int id);
    }
}