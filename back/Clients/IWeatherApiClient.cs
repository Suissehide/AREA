using back.Models.WeatherModel;
using System.Threading.Tasks;
using Refit;

namespace back.Clients
{
    public interface IWeatherApiClient
    {
        [Get("/data/2.5/weather?q={city}&appid=958c4227b2f11af546f128edb530f94b")]
        Task<WeatherModel> ApiGetWeatherByCityName(string city);
    }
}
