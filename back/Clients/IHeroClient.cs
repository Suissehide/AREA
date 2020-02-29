using System;
using System.Threading.Tasks;
using back.Models.HeroApi;
using Refit;

namespace back.Clients
{
    public interface IHeroClient
    {
        [Get("/api/10220539208371504/{idHero}")]
        Task<HeroIdModel> HeroById(int idHero);

        [Get("/api/10220539208371504//search/{name}")]
        Task<HeroNameModel> HeroByName(String name);
    }
}