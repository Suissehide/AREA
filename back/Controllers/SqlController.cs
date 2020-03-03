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
    [Route("database")]
    public class SqlController : ControllerBase
    {
        #region MEMBERS
        private readonly ILogger<SqlController> _logger;

        #endregion

        #region CONSTRUCTOR

        public SqlController(ILogger<SqlController> logger)
        {
            _logger = logger;
        }

        #endregion

        #region ROUTES
    
        [HttpGet("signup/{email}/{pwd}/{name}")]
        public bool CreateUser(string email, string pwd, string name)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);

            try
            {
                conn.Open();
                string sql = "select * from users where email = '"+email+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                int id = 0;

                if (rdr.Read())
                {
                    Console.WriteLine("Error: email "+email+" already exist.");
                    rdr.Close();
                    conn.Close();
                    return false;
                }
                rdr.Close();
            
                Console.WriteLine(name);
                Console.WriteLine(pwd);
                Console.WriteLine(email);

                sql = "INSERT INTO users (email, pwd, name) VALUES ('"+email+"', '"+pwd+"', '"+name+"');";
                cmd = new MySqlCommand(sql, conn);
                cmd.ExecuteNonQuery();

                sql = "select * from users where email = '"+email+"';";
                cmd = new MySqlCommand(sql, conn);
                rdr = cmd.ExecuteReader();
                if (rdr.Read()) {
                    id = int.Parse(rdr[0].ToString());
                }
                rdr.Close();

                sql = "INSERT INTO preferences (id, email, ChuckService, FacebookService, GoogleMapService, HeroService, JikanService, JokeService, "+
                "MicrosoftService, NewsService, PhotoService, PotterService, PokemonService, TheMovieDatabaseService, WheatherService) "+
                "VALUES ("+id.ToString()+", '"+email+"', '0', '0', '0', '0', '0', '0', '0', '1,17,18', '0', '0', '0', '0', '0');";
                Console.WriteLine(sql);
                cmd = new MySqlCommand(sql, conn);
                cmd.ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
            conn.Close();
            return true;
        }

        [HttpGet("login/{email}/{pwd}")]
        public bool LoginUser(string email, string pwd)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);

            try
            {
                conn.Open();
                string sql = "select pwd from users where email = '"+email+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                if (rdr.Read())
                {
                    if (rdr[0].ToString() == pwd) {
                        rdr.Close();
                        conn.Close();
                        return true;
                    }
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

        [HttpGet("users")]
        public SqlUserModel GetAllUsers()
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);
            SqlUserModel users = new SqlUserModel();
            List<User> listUser = new List<User>();

            try
            {
                conn.Open();

                string sql = "select * from users;";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();

                while (rdr.Read())
                {
                    User user = new User();
                    user.Id = int.Parse(rdr[0].ToString());
                    user.Email = rdr[1].ToString();
                    user.Pwd = rdr[2].ToString();
                    user.Name = rdr[3].ToString();
                    user.MicrosoftToken = rdr[4].ToString();
                    user.FacebookToken = rdr[5].ToString();
                    user.GoogleToken = rdr[6].ToString();
                    listUser.Add(user);
                }
                rdr.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error");
                Console.WriteLine(ex.ToString());
            }
            conn.Close();
            users.Users = listUser.ToArray();
            return users;
        }

        [HttpGet("users/{email}")]
        public SqlUserModel GetUser(string email)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);
            SqlUserModel users = new SqlUserModel();
            List<User> listUser = new List<User>();

            try
            {
                conn.Open();

                string sql = "select * from users where email = '"+email+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();

                while (rdr.Read())
                {
                    User user = new User();

                    user.Id = int.Parse(rdr[0].ToString());
                    user.Email = rdr[1].ToString();
                    user.Pwd = rdr[2].ToString();
                    user.Name = rdr[3].ToString();
                    user.MicrosoftToken = rdr[4].ToString();
                    user.FacebookToken = rdr[5].ToString();
                    user.GoogleToken = rdr[6].ToString();
                    listUser.Add(user);
                }
                rdr.Close();
                users.Users = listUser.ToArray();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error");
                Console.WriteLine(ex.ToString());
            }
            conn.Close();
            return users;
        }

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
                    for (int indexPref = 2; indexPref <= 14; indexPref++) {
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

                    sql = "select id from widgets where name = '"+widget+"';";
                    cmd = new MySqlCommand(sql, conn);
                    rdr = cmd.ExecuteReader();
                    if (rdr.Read()) {
                        id = int.Parse(rdr[0].ToString());
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

        [HttpGet("delete/{email}")]
        public bool DeleteUser(string email)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);

            try
            {
                conn.Open();
                string sql = "select * from users where email = '"+email+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                if (rdr.Read())
                {
                    rdr.Close();
                    sql = "DELETE from preferences where email = '"+email+"';";
                    cmd = new MySqlCommand(sql, conn);
                    cmd.ExecuteNonQuery();
                    sql = "DELETE from users where email = '"+email+"';";
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