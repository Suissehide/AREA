using System;
using System.Threading.Tasks;
using back.Models.JikanApi;
using Refit;

namespace back.Clients
{
    public interface IJikanClient
    {
        [Get("/search/anime?q={name}&limit=8")]
        Task<JikanAnimeModel> SearchAnime(String name);
    }
}