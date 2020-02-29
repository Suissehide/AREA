ng System.Threading.Tasks;
using back.Clients.GoogleApi;
using back.Models.GoogleApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;
using System;

namespace back.Controllers.GoogleControllers
{

    [ApiController]
    [Route("api/google/maps/distance")]
    public class DistanceMatrixApiController : ControllerBase
    {
        #region MEMBERS

        private readonly IDistanceMatrixApiClient _distanceMatrixApiClient;
        private readonly ILogger<DistanceMatrixApiController> _logger;

        #endregion

        #region CONSTRUCTOR

        public DistanceMatrixApiController(ILogger<DistanceMatrixApiController> logger)
        {
            _logger = logger;
            _distanceMatrixApiClient = RestService.For<IDistanceMatrixApiClient>("https://maps.googleapis.com/");
        }

        #endregion

        #region ROUTES

        [HttpGet("origin={origin}&destination={destination}&key={key}")]
        public async Task<ActionResult<DistanceMatrixApiModel>> ClientGetDistanceMatrix(string origin, string destination, string key)
        {
            try
            {
                var distanceMatrix = await _distanceMatrixApiClient.GetDistanceMatrix(origin, destination, key);
                Console.WriteLine(key);
                return Ok(distanceMatrix);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError(exMessage.Message);
                return NotFound();
            }
        }

        #endregion
    }
