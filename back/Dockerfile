# ---- Build image ----
FROM mcr.microsoft.com/dotnet/core/sdk:3.1 as build

WORKDIR /src

ENV DOTNET_CLI_TELEMETRY_OPTOUT=true
ENV ASPNETCORE_ENVIRONMENT=Production

# Restore
COPY *.csproj ./back/
RUN dotnet restore ./back/*.csproj

# Sources
COPY . ./back/

# Build
RUN dotnet publish ./back/*.csproj -c Release -o /app

# ---- Runtime image ----
FROM mcr.microsoft.com/dotnet/core/aspnet:3.1

WORKDIR /app

ENV DOTNET_CLI_TELEMETRY_OPTOUT=true
ENV ASPNETCORE_ENVIRONMENT=Production

# SOURCES
COPY --from=build /app .

EXPOSE 8080
CMD ["dotnet", "back.dll"]
