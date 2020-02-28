using back.Clients;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;
using System.Threading.Tasks;

namespace back.Controllers.MicrosoftControllers
{
    [ApiController]
    [Route("api/microsoft/drive")]
    public class DriveController : MicrosoftMainController
    {
        public DriveController(ILogger<MicrosoftMainController> logger) : base(logger)
        {
        }

        [HttpGet]
        public async Task<IActionResult> ClientGetDriveAsync([Header("Authorization")] string authorization)
        {
            var driveApiClient = RestService.For<IDriveApi>(HostUrl);
            try
            {
                var items = await driveApiClient.ApiGetDrive(authorization).ConfigureAwait(true);
                return Ok(items);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError(exMessage.Message);
                return NotFound();
            }
        }
    }
}
