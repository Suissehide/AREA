using back.Models;
using Refit;
using System.Threading.Tasks;

namespace back.Clients
{
    public interface IPhotoApiClient
    {
        [Get("/search/photos?client_id=736dd8475434072465dea0c8646e6ca9db847fbc8dcd8edb444c1e0effd7a3b1&query={themePhoto}")]
        Task<PhotoModel> ApiGetPhotoByTheme(string themePhoto);
    }

}
