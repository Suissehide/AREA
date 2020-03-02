using System.Threading.Tasks;
using back.Clients;
using back.Models.ChuckApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers
{
    [ApiController]
    [Route("api/chuck")]
    public class ChuckController : ControllerBase
    {
        #region MEMBERS

        private readonly ILogger<ChuckController> _logger;
        private readonly IChuckClient _chuckClient;
        
        #endregion

        #region CONTROLLER

        public ChuckController(ILogger<ChuckController> logger)
        {
            _logger = logger;
            _chuckClient = RestService.For<IChuckClient>("https://api.chucknorris.io");
        }

        #endregion

        #region ROUTE

        [HttpGet("{theme}")]
        public async Task<IActionResult> ChuckByTheme(string theme)
        {
            if (theme.Length < 3)
            {
                return BadRequest();
            }
            try
            {
                ChuckModel jokes = await _chuckClient.ChuckByTheme(theme);
                return Ok(jokes);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError($"Chuck : {exMessage.Message}");
                return NotFound(exMessage);
            }
        }

        #endregion
    }
}