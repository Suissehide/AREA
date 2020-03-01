using System.Threading.Tasks;
using back.Models;
using Refit;

namespace back.Clients.MicrosoftClients
{
    public interface ICalendarApi
    {
        [Get("/v1.0/me/events?$select=subject,start")]
        Task<CalendarModel> ApiGetCalendar([Header("Authorization")] string authorization);
    }
}
