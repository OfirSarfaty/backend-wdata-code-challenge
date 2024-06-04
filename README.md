# Weather Data Service - Code Challenge

## Overview

This service analyzes historical weather data to provide insights based on user-specified conditions. It ingests CSV data into a database and exposes an API endpoint for easy access.

## How to Use the Service

### Base URL

The service is hosted at:

https://weather-service-for-tommorow-io.onrender.com

### Route

**GET** `/weather/insight`

### Query Parameters

- `condition`: The weather condition to check (`veryHot` or `rainyAndCold`).
- `lat`: Latitude of the location.
- `lon`: Longitude of the location.

### Conditions Defined

- `veryHot`: Returns `true` if the temperature is above 30°C.
- `rainyAndCold`: Returns `true` if the temperature is below 10°C and precipitation is more than 0.5 mm/hr.


### Example Request

Can run on browser:

`https://weather-service-for-tommorow-io.onrender.com/weather/insight?lon=51.5&lat=24.5&condition=veryHot`

Or as CURL Command:

```console
 curl "https://weather-service-for-tommorow-io.onrender.com/weather/insight?condition=veryHot&lat=42.332&lon=35.421"
```

The response will look like this:

```json
[
  {
    "conditionMet": true,
    "forecastTime": "2021-04-02T13:00:00"
  },
  {
    "conditionMet": true,
    "forecastTime": "2021-04-02T14:00:00"
  },
  {
    "conditionMet": false,
    "forecastTime": "2021-04-02T15:00:00"
  }
]
```

Note: If using a browser, press on the small box at the top-right of the page for 'Pretty-print'.

## Assumptions

- **Preciptatom rate units**: In file3, the Precipitation Rate is described in the units 'in/hr', while in the other files, it is described as mm/hr. I assomed that this is not a mistake, and convert the values from inch to millmetre. 
- **time format**: the time format in the CSV files is ISO 8601, without a time zone information. But the results in the instruction were with time zone information (with Z in the end of the timestamp). I assumaed that I need to represent the timestamp as it in the files, without time zone information. 
- **Data Consistency**: I assumed that the CSV files are reliable, without missing fields or corrupt data.


## Optimizations and Pitfalls

There are many ways to improve the project. Here are some of them that I would consider doing:

- **Database Performance**: Indexing key columns like latitude, longitude, and forecast_time to improve query response times.
- **Caching**: Implementing caching mechanisms for frequently requested data to reduce load on the database.for exsample, the data from a contrys that uses the service freactlly, or by datatime that can be freauanly asked. 
- **Data Integrity**: The current setup does not fully validate the CSV data for errors before ingestion, and it may lead to corrupted data in the database. In this project, I build only one test for the data, to check that all the data from the files inserted to the database, But it would be helpfull to add more tests.

## Requirements for Production

To make this project a production-ready service, the following changes and adding are necessary:

- **Security Measures**: Implement authentication mechanisms to control access to the API endpoints.
- **Error Handling**: Enhance error handling to gracefully manage and log errors, to provide to the user clear error messages.
- **(CI/CD)**: Set up CI/CD pipelines to automate testing and deployment, ensuring code changes do not break the API functionality.
- **Monitoring and Logging**: Implement logging and monitoring methods and tools to track the API’s performance and quickly identify issues when they arise.
- **Data Backup and Recovery**: Establish backup procedures and a disaster recovery plan to prevent data loss and ensure data availability.



