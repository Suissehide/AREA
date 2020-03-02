using back.Models;
using Refit;
using System.Threading.Tasks;

namespace back.Clients
{
    interface IContactsClient
    {
        [Get("/v1.0/me/people")]
        Task<ContactsModel> ApiGetContacts([Header("Authorization")] string authorization);
    }
}
