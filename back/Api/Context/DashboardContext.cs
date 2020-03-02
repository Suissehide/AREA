﻿using Microsoft.EntityFrameworkCore;

namespace DashboardApi.Context
{
    public class DashboardContext : DbContext
    {
        public DashboardContext(DbContextOptions options) : base(options)
        {
        }
    }
}