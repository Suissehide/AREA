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
        private readonly ILogger<ChuckController> _logger;
        private readonly IChuckClient _chuckClient;

        public ChuckController(ILogger<ChuckController> logger)
        {
            _logger = logger;
            _chuckClient = RestService.For<IChuckClient>("https://api.chucknorris.io");
        }

        [HttpGet("{themeChuck}")]
        public async Task<IActionResult> ChuckByTheme(string themeChuck)
        {
            try
            {
                ChuckModel jokes = await _chuckClient.ChuckByTheme(themeChuck);
                return Ok(jokes);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError($"Chuck : {exMessage.Message}");
                return NotFound(exMessage);
            }
        }
    }
}