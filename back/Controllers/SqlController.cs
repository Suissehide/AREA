using System;
using System.Collections.Generic;
using System.Data;
using MySql.Data;
using MySql.Data.MySqlClient;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using back.Models;

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
    
        [HttpGet("signup/{name}/{pwd}/{email}")]
        public int CreateUser(string name, string pwd, string email)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);
            int id = -1;

            try
            {
                conn.Open();
                string sql = "select * from users where email = '"+email+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                if (rdr.Read())
                {
                    Console.WriteLine("Error: email "+email+" already exist.");
                    rdr.Close();
                    conn.Close();
                    return id;
                }
                rdr.Close();
            
                Console.WriteLine(name);
                Console.WriteLine(pwd);
                Console.WriteLine(email);

                sql = "INSERT INTO users (name, pwd, email) VALUES ('"+name+"', '"+pwd+"', '"+email+"');";
                cmd = new MySqlCommand(sql, conn);
                cmd.ExecuteNonQuery();
                sql = "select id from users where name='"+name+"' AND pwd='"+pwd+"' AND email='"+email+"';";
                cmd = new MySqlCommand(sql, conn);
                rdr = cmd.ExecuteReader();
                while (rdr.Read())
                {
                    id = int.Parse(rdr[0].ToString());
                }
                rdr.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }

            conn.Close();
            return id;
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
        public SqlModel GetAllUsers()
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);
            SqlModel users = new SqlModel();
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
                    user.Name = rdr[1].ToString();
                    user.Pwd = rdr[2].ToString();
                    user.Email = rdr[3].ToString();
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

        [HttpGet("users/{id}")]
        public SqlModel GetUser(string id)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);
            SqlModel users = new SqlModel();
            List<User> listUser = new List<User>();

            try
            {
                conn.Open();

                string sql = "select * from users where email = '"+id+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();

                while (rdr.Read())
                {
                    User user = new User();

                    string tmp = rdr[0].ToString();
                    user.Id = int.Parse(rdr[0].ToString());
                    user.Name = rdr[1].ToString();
                    user.Pwd = rdr[2].ToString();
                    user.Email = rdr[3].ToString();
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

        [HttpGet("editname/{email}/{name}")]
        public bool EditName(string email, string name)
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
                    sql = "update users set name = '"+name+"' where email = '"+email+"';";
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

        [HttpGet("editemail/{email}/{newemail}")]
        public bool EditEmail(string email, string newemail)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);

            try
            {
                conn.Open();
                string sql = "select * from users where email = '"+newemail+"';";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                if (rdr.Read())
                {
                    rdr.Close();
                    conn.Close();
                    return false;
                }
                else {
                    rdr.Close();
                    sql = "update users set email = '"+newemail+"' where email = '"+email+"';";
                    cmd = new MySqlCommand(sql, conn);
                    cmd.ExecuteNonQuery();

                }
                rdr.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
            conn.Close();
            return true;
        }

        [HttpGet("editpwd/{email}/{pwd}")]
        public bool EditPwd(string email, string pwd)
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
                    rdr.Close();
                    sql = "update users set pwd = '"+pwd+"' where email = '"+email+"';";
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

        [HttpGet("editmicrosoftToken/{email}/{microsoftToken}")]
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

        [HttpGet("editfacebookToken/{email}/{facebookToken}")]
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

        [HttpGet("editgoogleToken/{email}/{googleToken}")]
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