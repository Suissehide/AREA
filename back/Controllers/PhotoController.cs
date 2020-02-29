using back.Clients;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;
using System.Threading.Tasks;


namespace back.Controllers
{
    [ApiController]
    [Route("api/photo")]
    public class PhotoController : ControllerBase
    {
        #region MEMBERS

        private IPhotoApiClient _photoApiClient;
        private readonly ILogger<PhotoController> _logger;

        #endregion

        #region CONSTRUCTOR
        public PhotoController(ILogger<PhotoController> logger)
        {
            _logger = logger;
            _photoApiClient = RestService.For<IPhotoApiClient>("https://api.unsplash.com");
        }

        #endregion

        #region ROUTES
        [HttpGet("{themePhoto}")]
        public async Task<IActionResult> ClientGetPhotoByThemeAsync(string themePhoto)
        {
            try
            {
                var photos = await _photoApiClient.ApiGetPhotoByTheme(themePhoto);
                return Ok(photos);
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
