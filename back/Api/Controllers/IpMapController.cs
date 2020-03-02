using System.Threading.Tasks;
using back.Clients;
using back.Models.IpMapApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers
{
    [ApiController]
    [Route("api/ip")]
    public class IpMapController : ControllerBase
    {
        #region MEMBERS

        private readonly ILogger<IpMapController> _logger;
        private readonly IIpMapClient _ipMapClient;

        #endregion

        #region CONSTRUCTOR

        public IpMapController(ILogger<IpMapController> logger)
        {
            _logger = logger;
            _ipMapClient = RestService.For<IIpMapClient>("http://ip-api.com");
        }

        #endregion

        #region ROUTE

        [HttpGet]
        public async Task<IActionResult> IpMapAsync()
        {
            try
            {
                IpMapModel ipInfo = await _ipMapClient.GetGeo();
                return Ok(ipInfo);
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