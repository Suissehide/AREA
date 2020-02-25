using back.Clients;
using back.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;
using System.Threading.Tasks;

namespace back.Controllers
{
    [ApiController]
    [Route("pokemon")]
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

        [HttpGet("{name}")]
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

        #endregion
    }
}
