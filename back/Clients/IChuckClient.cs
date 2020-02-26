using System.Threading.Tasks;
using back.Models.ChuckApi;
using Refit;

namespace back.Clients
{
    public interface IChuckClient
    {
        [Get("/jokes/search?query={themeChuck}")]
        Task<ChuckModel> ChuckByTheme(string themeChuck);
    }
}