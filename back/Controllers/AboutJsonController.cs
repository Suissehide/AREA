using System;
using System.Collections.Generic;
using System.Data;
using MySql.Data;
using MySql.Data.MySqlClient;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using back.Models.Sql;

namespace back.Controllers
{
    [ApiController]
    [Route("about.json")]
    public class AboutJsonController : ControllerBase
    {
        #region MEMBERS
        private readonly ILogger<AboutJsonController> _logger;

        #endregion

        #region CONSTRUCTOR

        public AboutJsonController(ILogger<AboutJsonController> logger)
        {
            _logger = logger;
        }

        #endregion

        #region ROUTES
    
        [HttpGet]
        public AboutJsonModel CreateAboutJsonModel()
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);
            AboutJsonModel json = new AboutJsonModel();
            List<string> colomns = new List<string>();

            try
            {
                conn.Open();

                string sql = "SHOW COLUMNS FROM preferences;";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                while (rdr.Read()) {
                    colomns.Add(rdr[0].ToString());
                }
                colomns.RemoveAt(0);
                colomns.RemoveAt(0);
                rdr.Close();

                json.Client = new Client();
                json.Server = new Server();
                json.Client.Host = "10.101.53.35";
                json.Server.CurrentTime = 1531680780;
                json.Server.Services = new Services[15];

                for (int idx = 0; idx < 15; idx++ ) {
                    List<Actions> widgets = new List<Actions>();
                    json.Server.Services[idx] = new Services();
                    json.Server.Services[idx].Name = colomns[idx];

                    sql = "select name, description from widgets where service = '"+colomns[idx]+"' ORDER BY name;";
                    cmd = new MySqlCommand(sql, conn);
                    rdr = cmd.ExecuteReader();
                    while (rdr.Read()) {
                        Actions a = new Actions();
                        a.Name = rdr[0].ToString();
                        a.Description = rdr[1].ToString();
                        widgets.Add(a);
                    }
                    json.Server.Services[idx].Actions = widgets.ToArray();
                    rdr.Close();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
            conn.Close();
            return json;
        }
        #endregion
    }
}