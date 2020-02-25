using System;
using System.Threading.Tasks;
using back.Clients;
using back.Models.PotterApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Refit;

namespace back.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class FacebookController : ControllerBase
    {
        #region MEMBERS
        
        private readonly IFacebookClient _facebookClient;
        private readonly ILogger<FacebookController> _logger;
        
        #endregion

        #region CONSTRUCTOR

        public FacebookController(ILogger<FacebookController> logger)
        {
            _logger = logger;
            _facebookClient = RestService.For<IFacebookClient>("https://graph.facebook.com");
        }

        #endregion

        #region ROUTES

        [HttpGet("{token}")]
        public async Task<IActionResult> ClientFbLikeByToken(string token)
        {
            try
            {
                var fbLikes = await _facebookClient.ApiFbByToken(token);
                return Ok(fbLikes);
            }
            catch (ApiException exMessage)
            {
                _logger.LogError($"Facebook like : {exMessage.Message}");
                return NotFound();
            }
        }
        
        #endregion
        
    }
}