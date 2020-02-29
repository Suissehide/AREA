using back.Clients;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;
using System.Threading.Tasks;

namespace back.Controllers.MicrosoftControllers
{
    [ApiController]
    [Route("api/microsoft/contacts")]
    public class ContactsController : MicrosoftMainController
    {
        public ContactsController(ILogger<MicrosoftMainController> logger) : base(logger)
        {
        }


        [HttpGet]
        public async Task<IActionResult> ClientGetContactsAsync([Header("Authorization")] string authorization)
        {
            var contactApiClient = RestService.For<IContactsClient>(HostUrl);
            try
            {
                var contacts = await contactApiClient.ApiGetContacts(authorization).ConfigureAwait(true);
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
