using System.Threading.Tasks;
using Refit;
using back.Models.GoogleApi;

namespace back.Clients.GoogleApi
{
    interface IDistanceMatrixApiClient
    {
        [Get("/maps/api/distancematrix/json?units=metric&origins={origin}&destinations={destination}&key={key}")]
        Task<DistanceMatrixApiModel> GetDistanceMatrix(string origin, string destination, string key);

        [Get("/maps/api/distancematrix/json?units=metric&origins={origin}&destinations={destination}&mode={mode}&key={key}")]
        Task<DistanceMatrixApiModel> GetDistanceMatrixWithMode(string origin, string destination, string key);
    }
}
