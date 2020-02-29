using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace back.Controllers.MicroSoftControllers
{
    public class MicrosoftMainController : ControllerBase
    {
        #region MEMBERS

        protected readonly ILogger<MicrosoftMainController> _logger;
        protected const string HostUrl = "https://graph.microsoft.com";

        #endregion

        #region CONSTRUCTOR

        public MicrosoftMainController(ILogger<MicrosoftMainController> logger)
        {
            _logger = logger;
        }

        #endregion

    }
}
