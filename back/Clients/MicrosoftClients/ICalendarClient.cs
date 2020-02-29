using Refit;
using System.Threading.Tasks;
using back.Models;

namespace back.Clients
{
    public interface ICalendarApi
    {
        [Get("/v1.0/me/events?$select=subject,start")]
        Task<CalendarModel> ApiGetCalendar([Header("Authorization")] string authorization);
    }
}
