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
    
        [HttpGet("editmicrosofttoken/{email}/{microsoftToken}")]
        public bool MicrosoftToken(string email, string microsoftToken)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);

            try
            {
                conn.Open();
                string sql = "select microsoftToken from users where email = '"+email+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                if (rdr.Read())
                {
                    rdr.Close();
                    sql = "update users set microsoftToken = '"+microsoftToken+"' where email = '"+email+"';";
                    cmd = new MySqlCommand(sql, conn);
                    cmd.ExecuteNonQuery();

                    conn.Close();
                    return true;
                }
                rdr.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
            conn.Close();
            return false;
        }

        [HttpGet("editfacebooktoken/{email}/{facebookToken}")]
        public bool FacebookToken(string email, string facebookToken)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);

            try
            {
                conn.Open();
                string sql = "select facebookToken from users where email = '"+email+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                if (rdr.Read())
                {
                    rdr.Close();
                    sql = "update users set facebookToken = '"+facebookToken+"' where email = '"+email+"';";
                    cmd = new MySqlCommand(sql, conn);
                    cmd.ExecuteNonQuery();

                    conn.Close();
                    return true;
                }
                rdr.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
            conn.Close();
            return false;
        }

        [HttpGet("editgoogletoken/{email}/{googleToken}")]
        public bool GoogleToken(string email, string googleToken)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);

            try
            {
                conn.Open();
                string sql = "select googleToken from users where email = '"+email+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                if (rdr.Read())
                {
                    rdr.Close();
                    sql = "update users set googleToken = '"+googleToken+"' where email = '"+email+"';";
                    cmd = new MySqlCommand(sql, conn);
                    cmd.ExecuteNonQuery();

                    conn.Close();
                    return true;
                }
                rdr.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
            conn.Close();
            return false;
        }
        #endregion
    }
}