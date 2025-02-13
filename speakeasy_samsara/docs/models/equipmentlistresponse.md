# EquipmentListResponse

List of all equipment objects, and pagination information.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `data`                                                       | List[[models.Equipment](../models/equipment.md)]             | :heavy_check_mark:                                           | List of equipment objects.                                   |
| `pagination`                                                 | [models.PaginationResponse](../models/paginationresponse.md) | :heavy_check_mark:                                           | Pagination parameters.                                       |