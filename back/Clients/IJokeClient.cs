using System.Threading.Tasks;
using back.Models.JokeApi;
using Refit;

namespace back.Clients
{
    public interface IJokeClient
    {
        [Headers("Accept: application/json")]
        [Get("/search?accept=application/json&term={themeJoke}")]
        Task<JokeModel> ApiGetJokeByTheme(string themeJoke);
    }
}