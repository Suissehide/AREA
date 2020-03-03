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
    public partial class SqlController : ControllerBase
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

                sql = "INSERT INTO preferences (id, email, Chuck_Norris_Service, Facebook_Service, Google_Service, Superhero_Service, ISS_Service, Jikan_Service, Joke_Service, "+
                "Microsoft_Service, The_Movie_Database_Service, News_Service, Picture_Database_Service, Pokemon_Service, Harry_Potter_Service, Star_Wars_Service, Weather_Service) "+
                "VALUES ("+id.ToString()+", '"+email+"', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1,22,23', '0', '0', '0', '0', '0');";
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