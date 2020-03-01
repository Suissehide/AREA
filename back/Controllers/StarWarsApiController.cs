using System;
using System.Threading.Tasks;
using back.Clients.StarWarsApi;
using back.Models.StarWarsApi.StarWarsPeopleModel;
using back.Models.StarWarsApi.StarWarsPeoplesModel;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers
{
    [ApiController]
    [Route("api/starwars")]
    public class StarWarsApiController : ControllerBase
    {
        #region MEMBER
     
        private readonly ILogger<StarWarsApiController> _logger;
        private readonly IStarWarsApiClient _starWarsCient;

        #endregion
        
        #region CONSTRUCTOR

        public StarWarsApiController(ILogger<StarWarsApiController> logger)
        {
            _logger = logger;
            _starWarsCient = RestService.For<IStarWarsApiClient>("https://swapi.co/api/");
        }

        #endregion

        #region ROUTE

        [HttpGet("random")]
        public async Task<IActionResult> HeroRandom()
        {
            try
            {
                Random rand = new Random();
                int id = rand.Next(87);
                Console.WriteLine(id);
                StarWarsPeopleModel peopleInfo = await _starWarsCient.getCharacterById(id);
                return Ok(peopleInfo);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError(exMessage.Message);
                return NotFound(exMessage);
            }
        }
       
        [HttpGet("all")]
        public async Task<IActionResult> GetAllCharacters()
        {
            try
            {
                StarWarsPeoplesModel peoples = await _starWarsCient.GetAllCharacters();
                return Ok(peoples);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError(exMessage.Message);
                return NotFound(exMessage);
            }
        }
        
        #endregion
    }
}