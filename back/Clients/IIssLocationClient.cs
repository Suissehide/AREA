using System.Threading.Tasks;
using back.Models.IssLocationApi;
using Refit;

namespace back.Clients
{
    public interface IIssLocationClient
    {
        [Get("/iss-now.json")]
        Task<IssLocationModel> StationLocation();
        
        [Get("/astros.json")]
        Task<IssPersonModel> PersonInStation();
    }
}