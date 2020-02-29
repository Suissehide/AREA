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
        private const string HostUrl = "https://api.unsplash.com";
        private readonly ILogger<PhotoController> _logger;

        public PhotoController(ILogger<PhotoController> logger)
        {
            _logger = logger;
        }

        [HttpGet("{themePhoto}")]
        public async Task<IActionResult> ClientGetPhotoByThemeAsync(string themePhoto)
        {
            var photoApiClient = RestService.For<IPhotoApiClient>(HostUrl);
            try
            {
                var photos = await photoApiClient.ApiGetPhotoByTheme(themePhoto);
                return Ok(photos);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError(exMessage.Message);
                return NotFound(exMessage);
            }
        }
    }
}
