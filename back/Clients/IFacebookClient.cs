using System.Threading.Tasks;
using DashboardAPI.Models.FbModels;
using Refit;

namespace back.Clients
{
    public interface IFacebookClient
    {
        [Get("/v5.0/me?fields=likes&access_token={token}")]
        Task<FacebookLikeModel> ApiFbByToken(string token);
    }
}