using System;
using back.Controllers;
using Microsoft.Extensions.Logging;
using Xunit;

namespace BackUnitTest
{
    public class UnitTest1
    {
        [Fact]
        public void Test1()
        {
            var logger = new Logger<ChuckController>(new LoggerFactory());
            
            var chuckController = new ChuckController(logger);
        }
    }
}