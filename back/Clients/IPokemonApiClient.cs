using back.Models;
using System.Threading.Tasks;
using Refit;

namespace back.Clients
{
    public interface IPokemonApiClient
    {
        [Get("/v2/pokemon/{name}")]
        Task<PokemonModel> ApiGetPokemonByName(string name);

        [Get("/v2/pokemon/{name}")]
        Task<PokemonApiMovesModel> ApiGetPokemonMoveset(string name);
    }
}
