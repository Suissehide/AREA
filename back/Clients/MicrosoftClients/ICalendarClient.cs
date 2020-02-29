using Refit;
using System.Threading.Tasks;
using back.Models;

namespace back.Clients.MicrosoftClients
{
    public interface ICalendarApi
    {
        [Refit.Get("/v1.0/me/events?$select=subject,start")]
        System.Threading.Tasks.Task<CalendarModel> ApiGetCalendar([Refit.Header("Authorization")] string authorization);
    }
}
