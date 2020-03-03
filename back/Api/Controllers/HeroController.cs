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
    [Route("api/hero")]
    public class HeroController : ControllerBase
    {
        #region MEMBER
     
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

        [HttpGet("random")]
        public async Task<IActionResult> HeroRandom()
        {
            try
            {
                Random rand = new Random();
                int nbrInList = rand.Next(731);
                HeroIdModel heroInfo = await _heroClient.HeroById(nbrInList);
                return Ok(heroInfo);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError($"Hero get a random hero : {exMessage.Message}");
                return NotFound(exMessage);
            }
        }
       
        [HttpGet("name/{name}")]
        public async Task<IActionResult> HeroByName(String name)
        {
            try
            {
                HeroNameModel heroInfo = await _heroClient.HeroByName(name);
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