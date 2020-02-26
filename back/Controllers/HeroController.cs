using System;
using System.Threading.Tasks;
using back.Clients;
using back.Models.HeroApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class HeroController : ControllerBase
    {
        #region MEMBERS

        private readonly ILogger<HeroController> _logger;
        private readonly IHeroClient _heroClient;

        #endregion

        #region CONSTRUCTOR

        public HeroController(ILogger<HeroController> logger)
        {
            _logger = logger;
            _heroClient = RestService.For<IHeroClient>("https://superheroapi.com");
        }

        #endregion

        #region ROUTE

        [HttpGet("id/{idHero}")]
        public async Task<IActionResult> HeroById(int idHero)
        {
            try
            {
                if (idHero > 731 || idHero < 1)
                {
                    return NotFound();
                }
                HeroIdModel heroInfo = await _heroClient.HeroById(idHero);
                return Ok(heroInfo);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError($"Hero search by id : {exMessage.Message}");
                return NotFound(exMessage);
            }
        }
        
        [HttpGet("name/{nameHero}")]
        public async Task<IActionResult> HeroById(String nameHero)
        {
            try
            {
                HeroNameModel heroInfo = await _heroClient.HeroByName(nameHero);
                if (heroInfo.Response == "error")
                {
                    return NotFound();
                }
                return Ok(heroInfo);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError($"Hero search by name : {exMessage.Message}");
                return NotFound(exMessage);
            }
        }
        
        #endregion
        
    }
}