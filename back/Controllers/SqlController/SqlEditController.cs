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
    
        [HttpGet("editservice/{email}/{service}/{state}")]
        public bool EditService(string email, string service, string state)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);
            string str = "";

            try
            {
                conn.Open();
                string sql = "select * from users where email = '"+email+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                if (rdr.Read())
                {
                    rdr.Close();
                    sql = "select "+service+" from preferences where email = '"+email+"';";
                    cmd = new MySqlCommand(sql, conn);
                    rdr = cmd.ExecuteReader();
                    if (rdr.Read()) {
                        str = rdr[0].ToString();
                    }
                    rdr.Close();
                    str = str.Substring(1);
                    if (state == "true") {
                        str = '1' + str;
                    }
                    else {
                        str = '0' + str;
                    }
                    sql = "update preferences set "+service+" = '"+str+"' where email = '"+email+"';";
                    cmd = new MySqlCommand(sql, conn);
                    cmd.ExecuteNonQuery();
                }
                else {
                    conn.Close();
                    return false;            
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
            conn.Close();
            return true;            
        }

        [HttpGet("editwidget/{email}/{service}/{widget}/{state}")]
        public bool EditWidget(string email, string service, string widget, string state)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);
            string str = "";
            int id = -1;

            try
            {
                conn.Open();
                string sql = "select * from users where email = '"+email+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                if (rdr.Read())
                {
                    rdr.Close();
                    sql = "select "+service+" from preferences where email = '"+email+"';";
                    cmd = new MySqlCommand(sql, conn);
                    rdr = cmd.ExecuteReader();
                    if (rdr.Read()) {
                        str = rdr[0].ToString();
                    }
                    rdr.Close();

                    sql = "select id from widgets where service = '"+service+"' AND name = '"+widget+"';";
                    cmd = new MySqlCommand(sql, conn);
                    rdr = cmd.ExecuteReader();
                    if (rdr.Read()) {
                        id = int.Parse(rdr[0].ToString());
                    }
                    else {
                        Console.WriteLine("Error: The widget "+widget+" doesn't exist.");   
                    }
                    rdr.Close();

                    if (state == "true") {
                        List<int> ids = stringToListInt(str);
                        if (!ids.Contains(id)) {
                            ids.Add(id); 
                            str = "";
                            foreach(int i in ids) {
                                str = str + i.ToString() + ',';
                            }
                            str = str.Remove(str.Length - 1);
                        }
                    }
                    else {
                        List<int> ids = stringToListInt(str);
                        if (ids.Contains(id)) {
                            ids.Remove(id); 
                            str = "";
                            foreach(int i in ids) {
                                str = str + i.ToString() + ',';
                            }
                            str = str.Remove(str.Length - 1);
                        }
                    }
                    sql = "update preferences set "+service+" = '"+str+"' where email = '"+email+"';";
                    Console.WriteLine(sql);
                    cmd = new MySqlCommand(sql, conn);
                    cmd.ExecuteNonQuery();
                }
                else {
                    conn.Close();
                    return false;            
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
            conn.Close();
            return true;            
        }

        [HttpGet("editaccount/{newname}/{newpwd}/{newemail}/{email}")]
        public bool EditAccount(string newname, string newpwd, string newemail, string email)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);

            try
            {
                conn.Open();
                string sql = "select * from users where email = '"+newemail+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                if (rdr.Read() && email != newemail)
                {
                    Console.WriteLine("Error: the new email "+newemail+" already exist. And the mail is "+email);
                    rdr.Close();
                    conn.Close();
                    return false;
                }
                rdr.Close();
                sql = "update preferences set email = '"+newemail+"';";
                cmd = new MySqlCommand(sql, conn);
                cmd.ExecuteNonQuery();
                sql = "update users set email = '"+newemail+"', name = '"+newname+"', pwd = '"+newpwd+"' where email = '"+email+"';";
                cmd = new MySqlCommand(sql, conn);
                cmd.ExecuteNonQuery();
                conn.Close();
                return true;
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