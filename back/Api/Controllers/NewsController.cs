using System;
using System.Threading.Tasks;
using back.Clients;
using back.Models.NewsApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers
{
    [ApiController]
    [Route("api/news")]
    public class NewsController : ControllerBase
    {
        #region MEMBERS
        
        private readonly INewsClient _newsClient;
        private readonly ILogger<NewsController> _logger;

        #endregion

        #region CONSTRUCTOR

        public NewsController(ILogger<NewsController> logger)
                {
                    _logger = logger;
                    _newsClient = RestService.For<INewsClient>("http://newsapi.org/v2/");
                }

        #endregion

        #region ROUTE

        [HttpGet("banana")]
        public async Task<ActionResult<NewsModel>> BananaNew()
        {
            try
            {
                NewsModel newsModel = await _newsClient.BananaNews();
                return Ok(newsModel);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError(exMessage.Message);
                return NotFound();
            }
        }
        
        [HttpGet("{theme}")]
        public async Task<ActionResult<NewsModel>> NewsByTheme(String theme)
        {
            try
            {
                NewsModel newsModel = await _newsClient.NewsByTheme(theme);
                return Ok(newsModel);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError(exMessage.Message);
                return NotFound();
            }
        }
        
        #endregion
    }
}