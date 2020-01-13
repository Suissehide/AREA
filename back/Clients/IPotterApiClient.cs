using System.Collections.Generic;
using System.Threading.Tasks;
using back.Models.PotterApi;
using Refit;

namespace back.Clients
{
    public interface IPotterApiClient
    {
        [Get("/spells?key=$2a$10$GkDlDqEAEIcVTf6b1/7qfemelY9vQS36L83RBKknqIkHzBANciz2q")]
        Task<List<PotterSpellsModel>> GetSpells();

        [Get("/characters?key=$2a$10$GkDlDqEAEIcVTf6b1/7qfemelY9vQS36L83RBKknqIkHzBANciz2q")]
        Task<List<PotterCharactersModel>> GetCharacters();
    }
}