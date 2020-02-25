using System.Threading.Tasks;
using back.Clients.ItmdbApiClient;
using back.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers
{

    [ApiController]
    [Route("[controller]")]
    public class TmdbApiController : ControllerBase
    {
        #region MEMBERS

        private readonly ITmdbApiClient _tmdbApiClient;
        private readonly ILogger<TmdbApiController> _logger;

        #endregion

        #region CONSTRUCTOR

        public TmdbApiController(ILogger<TmdbApiController> logger)
        {
            _logger = logger;
            _tmdbApiClient = RestService.For<ITmdbApiClient>("https://api.themoviedb.org/3/");
        }

        #endregion

        #region ROUTES


        [HttpGet("movie/{title}")]
        public async Task<ActionResult<TmdbApiMovieModel>> GetMovie(string title)
        {
            try
            {
                var movies = await _tmdbApiClient.GetMovieInfos(title);
                return Ok(movies.Result);
            }
            catch (ApiException e)
            {
                _logger.LogError($"Movies : {e}");
                return StatusCode((int)e.StatusCode);
            }
        }

        #endregion
    }
}
