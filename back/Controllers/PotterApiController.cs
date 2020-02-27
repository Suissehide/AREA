using System;
using System.Threading.Tasks;
using back.Clients;
using back.Models.PotterApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers
{
    [ApiController]
    [Route("api/potter")]
    public class PotterApiController : ControllerBase
    {
        #region MEMBERS
        
        private readonly IPotterApiClient _potterApiClient;
        private readonly ILogger<PotterApiController> _logger;
        
        #endregion

        #region CONSTRUCTOR

        public PotterApiController(ILogger<PotterApiController> logger)
        {
            _logger = logger;
            _potterApiClient = RestService.For<IPotterApiClient>("https://www.potterapi.com/v1/");
        }

        #endregion

        #region ROUTES

        [HttpGet("random-spells")]
        public async Task<ActionResult<PotterSpellsModel>> GetRandomSpell()
        {
            try
            {
                var spells = await _potterApiClient.GetSpells();
                Random rand = new Random();
                int nbrInList = rand.Next(spells.Count);
                return Ok(spells[nbrInList]);
            }
            catch (ApiException e)
            {
                _logger.LogError($"PotterSpells : {e}");
                return StatusCode((int) e.StatusCode);
            }
        }

        [HttpGet("random-character")]
        public async Task<ActionResult<PotterCharactersModel>> GetRandomCharacter()
        {
            try
            {
                var characters = await _potterApiClient.GetCharacters();
                Random rand = new Random();
                int nbrInList = rand.Next(characters.Count);
                return Ok(characters[nbrInList]);
            }
            catch (ApiException e)
            {
                _logger.LogError($"PotterCharacters : {e}");
                return StatusCode((int) e.StatusCode);
            }
        }

        #endregion
        
    }
}