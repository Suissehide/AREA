using back.Clients;
using back.Models.WeatherModel;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;
using System.Threading.Tasks;

namespace back.Controllers
{
    [ApiController]
    [Route("api/weather")]
    public class WeatherApiController : ControllerBase
    {
        #region MEMBERS

        private readonly  IWeatherApiClient _weatherApiClient;
        private readonly ILogger<PokemonController> _logger;

        #endregion

        #region CONSTRUCTOR

        public WeatherApiController(ILogger<PokemonController> logger)
        {
            _logger = logger;
            _weatherApiClient = RestService.For<IWeatherApiClient>("http://api.openweathermap.org/");
        }

        #endregion

        #region ROUTES

        [HttpGet("{city}")]
        public async Task<ActionResult<WeatherModel>>GetWeatherByCityName(string city)
        {
            try
            {
                var weatherInfos = await _weatherApiClient.ApiGetWeatherByCityName(city);
                return Ok(weatherInfos);
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
