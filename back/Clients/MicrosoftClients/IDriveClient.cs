using back.Models.DriveModel;
using Refit;
using System.Threading.Tasks;

namespace back.Clients
{
    public interface IDriveApi
    {
        [Get("/v1.0/me/drive/root/children")]
        Task<DriveModel> ApiGetDrive([Header("Authorization")] string authorization);
    }
}
