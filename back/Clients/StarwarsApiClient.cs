using System.Threading.Tasks;
using back.Models.StarWarsApi.StarWarsPeopleModel;
using back.Models.StarWarsApi.StarWarsPeoplesModel;
using Refit;

namespace back.Clients.StarWarsApi
{
    public interface IStarWarsApiClient
    {
        [Get("/people/{id}")]
        Task<StarWarsPeopleModel> GetCharacterById(int id);

        [Get("/planets/{id}")]
        Task<StarWarsPlanetModel> GetPlanetById(int id);
    }
}