using System;
using System.Threading.Tasks;
using back.Clients;
using back.Models.IssLocationApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers
{
    [ApiController]
    [Route("api/location")]
    public class IssLocationController : ControllerBase
    {
        #region MEMBERS

        private readonly ILogger<IssLocationController> _logger;
        private readonly IIssLocationClient _iss;

        #endregion

        #region CONSTRUCTOR

        public IssLocationController(ILogger<IssLocationController> logger)
        {
            _logger = logger;
            _iss = RestService.For<IIssLocationClient>("http://api.open-notify.org/");
        }

        #endregion

        #region ROUTE

        [HttpGet("station_location")]
        public async Task<IActionResult> StationLocation()
        {
            try
            {
                IssLocationModel location = await _iss.StationLocation();
                return Ok(location);
            }
            catch (Exception exMessage)
            {
                _logger.LogError($"ISS location of station : {exMessage.Message}");
                return NotFound(exMessage);
            }
        }

        [HttpGet("person")]
        public async Task<IActionResult> PersonInStation()
        {
            try
            {
                IssPersonModel personInStation = await _iss.PersonInStation();
                return Ok(personInStation);
            }
            catch (Exception exMessage)
            {
                _logger.LogError($"ISS nbr of person in space : {exMessage.Message}");
                return NotFound(exMessage);
            }
        }
        
        #endregion
    }
}