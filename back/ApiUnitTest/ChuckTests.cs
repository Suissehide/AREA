using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using back.Controllers;
using back.Models.ChuckApi;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Xunit;
using Xunit.Abstractions;

namespace BackUnitTest
{
    public class ChuckTests
    {
        private readonly ITestOutputHelper _testOutputHelper;

        public ChuckTests(ITestOutputHelper testOutputHelper)
        {
            _testOutputHelper = testOutputHelper;
        }

        public Dictionary<string, string> InitParam()
        {
            Dictionary<string, string> param = new Dictionary<string, string>();
            param.Add("OneWord", "life");
            param.Add("FrenchWord", "bonjour");
            param.Add("NoWord", "");
            param.Add("MultipleWord", "i'm the best");
            return param;
        }
        
        [Fact]
        public async Task OneWord()
        {
            // Arrange
            var logger = new Logger<ChuckController>(new LoggerFactory());
            var param = InitParam()["OneWord"];
            var chuckController = new ChuckController(logger);

            // Act
            var result = await chuckController.ChuckByTheme(param);

            // Assert
            var okResult = result as OkObjectResult;
            var myChuckObject = okResult.Value as ChuckModel;
            Assert.IsType<int>(myChuckObject.Total);
            Assert.IsType<List<ChuckJokeModel>>(myChuckObject.Result);
            Assert.IsType<string>(myChuckObject.Result[0].Value);
        }
        
        [Fact]
        public async Task NoWord()
        {
            // Arrange
            var logger = new Logger<ChuckController>(new LoggerFactory());
            var param = InitParam()["NoWord"];
            var chuckController = new ChuckController(logger);

            // Act
            var result = await chuckController.ChuckByTheme(param);

            // Assert
            var badRequest = result as BadRequestResult;
            Assert.Equal(400, badRequest.StatusCode);
        }
        
        [Fact]
        public async Task MultipleWord()
        {
            // Arrange
            
            var logger = new Logger<ChuckController>(new LoggerFactory());
            var param = InitParam()["MultipleWord"];
            var chuckController = new ChuckController(logger);

            // Act
            var result = await chuckController.ChuckByTheme(param);

            // Assert
            var okRequest = result as OkObjectResult;
            Assert.Equal(200, okRequest.StatusCode);

            var myChuckObject = okRequest.Value as ChuckModel;
            Assert.IsType<int>(myChuckObject.Total);
            Assert.IsType<List<ChuckJokeModel>>(myChuckObject.Result);
        }
    }
}