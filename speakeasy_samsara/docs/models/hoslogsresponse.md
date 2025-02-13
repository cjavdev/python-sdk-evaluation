# HosLogsResponse

HOS logs and pagination info.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `data`                                                         | List[[models.HosLogsForDriver](../models/hoslogsfordriver.md)] | :heavy_check_mark:                                             | List of HOS logs for the specified drivers.                    |
| `pagination`                                                   | [models.PaginationResponse](../models/paginationresponse.md)   | :heavy_check_mark:                                             | Pagination parameters.                                         |