using back.Clients;
using back.Models.PokemonApi.Moveset;
using back.Models.PokemonApi.PokemonDetail;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;
using System.Threading.Tasks;

namespace back.Controllers
{
    [ApiController]
    [Route("api/pokemon")]
    public class PokemonController : ControllerBase
    {
        #region MEMBERS

        private readonly IPokemonApiClient _pokemonApiClient;
        private readonly ILogger<PokemonController> _logger;

        #endregion

        #region CONSTRUCTOR

        public PokemonController(ILogger<PokemonController> logger)
        {
            _logger = logger;
            _pokemonApiClient = RestService.For<IPokemonApiClient>("https://pokeapi.co/api/");
        }

        #endregion

        #region ROUTES

        [HttpGet("{name}/detail")]
        public async Task<ActionResult<PokemonModel>> ClientGetPokemonByNameAsync(string name)
        {
            try
            {
                var pokemonInfo = await _pokemonApiClient.ApiGetPokemonByName(name);
                return Ok(pokemonInfo);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError(exMessage.Message);
                return NotFound();
            }
        }

        [HttpGet("{name}/moves")]
        public async Task<ActionResult<PokemonApiMovesModel>> ClientGetPokemonMoveset(string name)
        {
            try
            {
                var pokemonMoveset = await _pokemonApiClient.ApiGetPokemonMoveset(name);
                return Ok(pokemonMoveset);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError(exMessage.Message);
                return NotFound();
            }
        }
        #endregion
    }
}
