using System.Collections.Generic;
using System.Threading.Tasks;
using back.Controllers;
using back.Models.HeroApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Xunit;
using Xunit.Abstractions;

namespace BackUnitTest
{
    public class HeroTests
    {
        private readonly ITestOutputHelper _testOutputHelper;

        public HeroTests(ITestOutputHelper testOutputHelper)
        {
            _testOutputHelper = testOutputHelper;
        }

        public Dictionary<string, string> InitParam()
        {
            Dictionary<string, string> param = new Dictionary<string, string>();
            param.Add("OneName", "Hulk");
            param.Add("WrongName", "Justine");
            param.Add("NoName", "");
            return param;
        }

        [Fact]
        public async Task OneName()
        {
            // Arrange
            var logger = new Logger<HeroController>(new LoggerFactory());
            var param = InitParam()["OneName"];
            var heroController = new HeroController(logger);
            
            // Act
            var result = await heroController.HeroByName(param);

            // Assert
            var okResult = result as OkObjectResult;
            var myHeroObject = okResult.Value as HeroNameModel;
            _testOutputHelper.WriteLine(myHeroObject.Results[0].Name);
            
            Assert.StrictEqual("Hulk", myHeroObject.Results[0].Name);
            Assert.IsType<HeroApparenceModel>(myHeroObject.Results[0].Appearance);
            Assert.IsType<HeroBiographyModel>(myHeroObject.Results[0].Biography);
            Assert.IsType<HeroPowerStatModel>(myHeroObject.Results[0].Powerstats);
        }
        
    }
}