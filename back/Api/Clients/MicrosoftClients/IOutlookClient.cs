using System.Threading.Tasks;
using back.Models.MicrosoftModels;
using Refit;

namespace back.Clients.MicrosoftClients
{
    public interface IOutlookClient
    {
        [Get("/v1.0/me/messages/")]
        Task<OutlookModel> ApiGetOutlook([Header("Authorization")] string authorization);
    }
}