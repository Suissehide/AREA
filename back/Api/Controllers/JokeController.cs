using System.Threading.Tasks;
using back.Clients;
using back.Models.JokeApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers
{
    [ApiController]
    [Route("api/joke")]
    public class JokeController : ControllerBase
    {
        #region MEMBERS

        private readonly ILogger<JokeController> _logger;
        private readonly IJokeClient _jokeClient;

        #endregion

        #region CONSTRUCTOR

        public JokeController(ILogger<JokeController> logger)
        {
            _logger = logger;
            _jokeClient = RestService.For<IJokeClient>("https://icanhazdadjoke.com");
        }

        #endregion

        #region ROUTE
        
        [HttpGet("{theme}")]
        public async Task<IActionResult> ClientGetJokeByThemeAsync(string theme)
        {
            try
            {
                JokeModel jokes = await _jokeClient.ApiGetJokeByTheme(theme);
                return Ok(jokes);
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