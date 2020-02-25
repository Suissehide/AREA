using System.Threading.Tasks;
using back.Clients;
using back.Models.JikanApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers
{
    public class JikanController : ControllerBase
    {
        private readonly ILogger<JikanController> _logger;
        private readonly IJikanClient _jikanClient;

        public JikanController(ILogger<JikanController> logger)
        {
            _logger = logger;
            _jikanClient = RestService.For<IJikanClient>("https://api.jikan.moe/v3/");
        }
        [HttpGet("{name}")]
        [ProducesResponseType(typeof(JikanAnimeModel), 200)]
        [ProducesResponseType(typeof(NotFoundResult), 404)]
        [ProducesResponseType(typeof(void), 500)]
        public async Task<IActionResult> AnimeByName(string name)
        {
            try
            {
                JikanAnimeModel animeSearchResult = await _jikanClient.SearchAnime(name);
                return Ok(animeSearchResult);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError($"Jikan search anime : {exMessage.Message}");
                return NotFound();
            }
        }
    }
}