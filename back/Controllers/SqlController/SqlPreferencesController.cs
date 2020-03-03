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
    [Route("database")]
    public partial class SqlController : ControllerBase
    {
        #region ROUTES
    
        [HttpGet("preferences/{email}")]
        public SqlPreferencesModel GetPreferences(string email)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);
            SqlPreferencesModel pref = new SqlPreferencesModel();
            pref.services = new Dictionary<string, Service>();
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

                sql = "select * from preferences where email = '"+email+"';";
                cmd = new MySqlCommand(sql, conn);
                rdr = cmd.ExecuteReader();
                if (rdr.Read())
                {
                    pref.Id = int.Parse(rdr[0].ToString());
                    pref.Email = rdr[1].ToString();
                    int indexService = 0;
                
                    List<List<int>> listIds = new List<List<int>>();
                    for (int indexPref = 2; indexPref <= 16; indexPref++) {
                        listIds.Add(stringToListInt(rdr[indexPref].ToString()));
                    }
                    rdr.Close();

                    foreach(List<int> ids in listIds) {
                        Service service = new Service();
                        service.Widgets = new Dictionary<string, bool>();
                        Dictionary<string, int> widgets = new Dictionary<string, int>();

                        service.State = Convert.ToBoolean(ids[0]);
                        ids.RemoveAt(0);

                        sql = "select id, name from widgets where service = '"+colomns[indexService]+"' ORDER BY name;";
                        cmd = new MySqlCommand(sql, conn);
                        rdr = cmd.ExecuteReader();
                        while (rdr.Read()) {
                            widgets.Add(rdr[1].ToString(), int.Parse(rdr[0].ToString()));
                        }
                        rdr.Close();

                        foreach (KeyValuePair<string, int> elem in widgets) {
                            if (ids.Contains(elem.Value)) {
                                service.Widgets.Add(elem.Key, true);
                            }
                            else {
                                service.Widgets.Add(elem.Key.ToString(), false);
                            }
                        }

                        pref.services.Add(colomns[indexService], service);
                        indexService = indexService + 1;
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error");
                Console.WriteLine(ex.ToString());
            }
            conn.Close();
            return pref;
        }

        private List<int> stringToListInt(string ids)
        {
            List<int> ret = new List<int>();
            string[] strArray = ids.Split(',');

            foreach (string str in strArray) {
                ret.Add(int.Parse(str));
            }
            return ret;
        }
        #endregion
    }
}