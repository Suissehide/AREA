using System.Threading.Tasks;
using Refit;
using back.Models.GoogleApi.Maps.Places;
using back.Models.GoogleApi.Maps.PlaceDetail;

namespace back.Clients.GoogleApi
{
    interface IPlacesApiClient
    {
        [Get("/maps/api/place/textsearch/json?query={place}&key={key}")]
        Task<PlacesApiModel> GetPlaces(string place, string key);

        [Get("/maps/api/place/details/json?place_id={placeId}&fields=name,rating,formatted_phone_number&,photokey={key}")]
        Task<PlaceDetailApiModel> GetPlaceDetail(string placeId, string key);
    }

}