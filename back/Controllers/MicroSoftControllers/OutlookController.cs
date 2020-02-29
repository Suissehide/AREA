using System.Threading.Tasks;
using back.Clients;
using back.Clients.MicrosoftClients;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers.MicroSoftControllers
{
    [ApiController]
    [Route("api/microsoft/outlook")]
    public class OutlookController : MicrosoftMainController
    {
        public OutlookController(ILogger<MicrosoftMainController> logger) : base(logger)
        {
        }

        #region ROUTES

        [HttpGet]
        public async Task<IActionResult> ClientGetOutlookAsync([Header("Authorization")] string authorization)
        {
            var outlookApiClient = RestService.For<IOutlookClient>(HostUrl);
            try
            {
                var mails = await outlookApiClient.ApiGetOutlook(authorization).ConfigureAwait(true);
                return Ok(mails);
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