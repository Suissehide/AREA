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

        [Get("/search/character?q={name}&limit=20")]
        Task<JikanCharacterModel> SearchCharacter(String name);
    }
}