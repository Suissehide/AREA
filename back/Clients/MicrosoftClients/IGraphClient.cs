using back.Models.GraphModel;
using Refit;
using System.Threading.Tasks;

namespace back.Clients
{
    public interface IGraphApi
    {
        [Get("/v1.0/me/")]
        Task<GraphModel> ApiGetGraph([Header("Authorization")] string authorization);
    }
}
