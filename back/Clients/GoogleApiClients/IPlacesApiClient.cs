using System.Threading.Tasks;
using Refit;
using back.Models.GoogleApi;

namespace back.Clients.GoogleApi
{
    interface IPlaceApiClient
    {
        [Get("/maps/api/place/textsearch/json?query={place}&key={key}")]
        Task<PlacesApiModel> GetPlaces(string place, string key);
    }
}