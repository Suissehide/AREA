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

        [HttpGet("signup/{name}/{pwd}/{email}")]
        public int CreateUser(string name, string pwd, string email)
        {
            string connStr = "server=localhost;user=root;database=area;port=3306;password=root";
            MySqlConnection conn = new MySqlConnection(connStr);
            int id = -1;

            try
            {
                conn.Open();
                Console.WriteLine(name);
                Console.WriteLine(pwd);
                Console.WriteLine(email);
                string sql = "INSERT INTO users (name, pwd, email) VALUES ('"+name+"', '"+pwd+"', '"+email+"');";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                cmd.ExecuteNonQuery();
                sql = "select id from users where name='"+name+"' AND pwd='"+pwd+"' AND email='"+email+"';";
                cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
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
    }
}