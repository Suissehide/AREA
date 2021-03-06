﻿using System.Threading.Tasks;
using back.Models.GoogleApi;
using Refit;

namespace back.Clients.GoogleApi
{
    interface IPlacesApiClient
    {
        [Get("/maps/api/place/textsearch/json?query={place}&key={key}")]
        Task<PlacesApiModel> GetPlaces(string place, string key);

        [Get("/maps/api/place/details/json?place_id={placeId}&fields=name,rating,formatted_phone_number,photos,types,opening_hours&key={key}")]
        Task<PlaceDetailApiModel> GetPlaceDetail(string placeId, string key);
    }

}