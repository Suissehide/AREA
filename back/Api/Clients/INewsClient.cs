using System;
using System.Threading.Tasks;
using back.Models.NewsApi;
using Refit;

namespace back.Clients
{
    public interface INewsClient
    {
        [Get("/everything?q=banana&apiKey=2332649d373b41e7bc8d9c521b5ca79c")]
        Task<NewsModel> BananaNews();
        
        [Get("/everything?q={theme}&apiKey=2332649d373b41e7bc8d9c521b5ca79c")]
        Task<NewsModel> NewsByTheme(String theme);
    }
}