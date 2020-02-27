using back.Models.CalendarModel;
using Refit;
using System.Threading.Tasks;

namespace back.Clients
{
    public interface ICalendarApi
    {
        [Get("/v1.0/me/events?$select=subject,start")]
        Task<CalendarModel> ApiGetCalendar([Header("Authorization")] string authorization);
    }
}
