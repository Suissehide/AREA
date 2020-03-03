FROM node:9-slim
WORKDIR /app_server
COPY appsettings.json /app_server
RUN dotnet build
COPY . /app_server
CMD ["dotnet", "run"]