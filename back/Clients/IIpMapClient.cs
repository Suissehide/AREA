using System.Threading.Tasks;
using back.Models.IpMapApi;
using Refit;

namespace back.Clients
{
    public interface IIpMapClient
    {
        [Get("/json/")]
        Task<IpMapModel> GetGeo();
    }
}