using System.Threading.Tasks;
using back.Clients.GoogleApi;
using back.Models.GoogleApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers.GoogleControllers
{

    [ApiController]
    [Route("api/google/maps/place")]
    public class PlacesApiController : ControllerBase
    {
        #region MEMBERS

        private readonly IPlacesApiClient _placesApiClient;
        private readonly ILogger<DistanceMatrixApiController> _logger;

        #endregion

        #region CONSTRUCTOR

        public PlacesApiController(ILogger<DistanceMatrixApiController> logger)
        {
            _logger = logger;
            _placesApiClient = RestService.For<IPlacesApiClient>("https://maps.googleapis.com/");
        }

        #endregion

        #region ROUTES

        [HttpGet("search/query={place}&key={key}")]
        public async Task<ActionResult<PlacesApiModel>> ClientGetPlace(string place, string key)
        {
            try
            {
                PlacesApiModel placeModel = await _placesApiClient.GetPlaces(place, key);
                return Ok(placeModel);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError(exMessage.Message);
                return NotFound();
            }
        }

        [HttpGet("detail/id={placeId}&key={key}")]
        public async Task<ActionResult<PlaceDetailApiModel>> ClientGetPlaceDetail(string placeId, string key)
        {
            try
            {
                PlaceDetailApiModel placeDetailModel = await _placesApiClient.GetPlaceDetail(placeId, key);
                return Ok(placeDetailModel);
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