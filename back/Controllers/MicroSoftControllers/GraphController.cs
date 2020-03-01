using back.Clients;
using back.Controllers.MicroSoftControllers;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;
using System.Threading.Tasks;
using back.Controllers.MicroSoftControllers;

namespace back.Controllers.MicrosoftControllers
{
    [ApiController]
    [Route("api/microsoft/graph")]
    public class GraphController : MicrosoftMainController
    {
        public GraphController(ILogger<MicrosoftMainController> logger) : base(logger)
        {
        }


        [HttpGet]
        public async Task<IActionResult> ClientGetContactsAsync([Header("Authorization")] string authorization)
        {
            var contactApiClient = RestService.For<IGraphApi>(HostUrl);
            try
            {
                var contacts = await contactApiClient.ApiGetGraph(authorization).ConfigureAwait(true);
                return Ok(contacts);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError(exMessage.Message);
                return NotFound();
            }
        }
    }
}
