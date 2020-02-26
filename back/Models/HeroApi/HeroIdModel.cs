using System.Collections.Generic;

namespace back.Models.HeroApi
{
    public class HeroIdModel
    {
        public string Name { get; set; }
        public Dictionary<string, int> Powerstats { get; set; }
        public Dictionary<string, string> Work { get; set; }
        public Dictionary<string, string> Image { get; set; }
    }
}