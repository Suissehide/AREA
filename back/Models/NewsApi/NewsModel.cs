using System;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace back.Models.NewsApi
{
    public class NewsModel
    {
        [JsonProperty("totalResults")]
        public int TotalResults { get; set; }
        [JsonProperty("articles")]
        public List<Article> Articles { get; set; }
    }
    public class Source
    {
        [JsonProperty("name")]
        public string Name { get; set; }
    }

    public class Article
    {
        [JsonProperty("source")]
        public Source Source { get; set; }

        [JsonProperty("author")]
        public string Author { get; set; }
        
        [JsonProperty("title")]
        public string Title { get; set; }
        
        [JsonProperty("description")]
        public string Description { get; set; }
        
        [JsonProperty("url")]
        public string Url { get; set; }
        
        [JsonProperty("publishedAt")]
        public DateTime PublishedAt { get; set; }
        
        [JsonProperty("content")]
        public string Content { get; set; }
    }
}