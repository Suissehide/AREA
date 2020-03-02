using back.Clients;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;
using System.Threading.Tasks;
using back.Clients.MicrosoftClients;
using back.Controllers.MicroSoftControllers;

namespace back.Controllers.MicrosoftControllers
{
    [ApiController]
    [Route("api/microsoft/calendar")]
    public class CalendarController : MicrosoftMainController
    {
        public CalendarController(ILogger<MicrosoftMainController> logger) : base(logger)
        {
        }
        
        [HttpGet]
        public async Task<IActionResult> ClientGetCalendarAsync([Header("Authorization")] string authorization)
        {
            var calendarApiClient = RestService.For<ICalendarApi>(HostUrl);
            try
            {
                var calendar = await calendarApiClient.ApiGetCalendar(authorization).ConfigureAwait(true);
                return Ok(calendar);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError(exMessage.Message);
                return NotFound();
            }
        }
    }
}
