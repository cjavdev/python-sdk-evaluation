# GrossVehicleWeight

The gross weight of the vehicle in either pounds (lb) or kilograms (kg). Only returned for customers with commercial speed limits (CSL) enabled.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `unit`                                                                         | [Optional[models.GrossVehicleWeightUnit]](../models/grossvehicleweightunit.md) | :heavy_minus_sign:                                                             | The unit of weight for the vehicle.                                            | lb                                                                             |
| `weight`                                                                       | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | The weight value of the vehicle.                                               | 1000                                                                           |