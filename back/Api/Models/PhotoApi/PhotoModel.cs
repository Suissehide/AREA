using System.Collections.Generic;

namespace back.Models
{
    public class PhotoModel
    {
        public int Total { get; set; }
        public int Total_pages { get; set; }
        public List<ResultPhotoModel> Results { get; set; }
    }

    public class ResultPhotoModel
    {
        public string Description { get; set; }
        public Dictionary<string, string> Urls { get; set; }
    }
}
