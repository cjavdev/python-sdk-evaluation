# V1TripResponse

Contains the trips for the vehicle in the requested timeframe. A trip is represented as an object that contains startMs, startLocation, startAddress, startCoordinates, endMs, endLocation, endAddress and endCoordinates. Ongoing trips will be returned with 9223372036854775807 as their endMs.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `trips`                                                              | List[[models.V1TripResponseTrips](../models/v1tripresponsetrips.md)] | :heavy_minus_sign:                                                   | N/A                                                                  |