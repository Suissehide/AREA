using System.Threading.Tasks;
using back.Clients.GoogleApi;
using back.Models.GoogleApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;
using System;

namespace back.Controllers.GoogleControllers
{

    [ApiController]
    [Route("api/google/maps/place")]
    public class PlacesApiController : ControllerBase
    {
        #region MEMBERS

        private readonly IPlaceApiClient _placesApiClient;
        private readonly ILogger<DistanceMatrixApiController> _logger;

        #endregion

        #region CONSTRUCTOR

        public PlacesApiController(ILogger<DistanceMatrixApiController> logger)
        {
            _logger = logger;
            _placesApiClient = RestService.For<IPlaceApiClient>("https://maps.googleapis.com/");
        }

        #endregion

        #region ROUTES

        [HttpGet("query={place}&key={key}")]
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

        #endregion
    }
}