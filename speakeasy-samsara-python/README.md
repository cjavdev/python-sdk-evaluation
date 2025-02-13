# samsara

Developer-friendly & type-safe Python SDK specifically catered to leverage *samsara* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=samsara&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/cjav-dev/demo). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Samsara API: <style type="text/css">
n {
    padding: 1em;
    width: 100%;
    display: block;
    margin: 28px 0;
}
n.info {
    background-color: rgba(0, 51, 160, 0.1);
}
n.warning {
    background-color: #fdf6e3;
}
i:before {
    margin-right: 6px;
}
nh {
    font-size: 1.5rem;
    font-weight: 700;
    line-height: 1.1;
    display: block;
}
nb {
    margin-top: 10px;
    padding-left: 22px;
    display: block;
}
</style>

# Overview

<n class="info">
<nh>
<i class="fa fa-info-circle"></i>
Something new!
</nh>
<nb>
Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br>
<br>
Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api-legacy).<br>
<br>
*Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api-legacy) as we continue to transition all endpoints over. Check back here for updates!*<br>
<br>
Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)!
</nb>
</n>

Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.

The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.

Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.

If you have any questions, please visit https://samsara.com/help.

## Endpoints

All our APIs can be accessed through HTTP requests to URLs like:

```
https://api.samsara.com/<endpoint>
```

For EU customers, this URL will be:

```
https://api.eu.samsara.com/<endpoint>
```

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
Note
</nh>
<nb>
Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>`
</nb>
</n>

## Authentication

To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.

Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.

Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:

```curl
Authorization: Bearer {access_token}
```

All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.

### OAuth2
If building an application for our marketplace, our API is accessible via. OAuth2 as well.

| Type  | Value |
| ------------- |:-------------:|
| Security scheme      | OAuth2                                   |
| OAuth2 Flow          | accessCode                               |
| Authorization URL    | https://api.samsara.com/oauth2/authorize |
| Token URL            | https://api.samsara.com/oauth2/token     |



## Common Patterns

You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [samsara](#samsara)
* [Overview](#overview)
  * [Endpoints](#endpoints)
  * [Authentication](#authentication)
  * [Common Patterns](#common-patterns)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication-1)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from samsara python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "samsara",
# ]
# ///

from samsara import Samsara

sdk = Samsara(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.addresses.list_addresses()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from samsara import Samsara

async def main():
    async with Samsara(
        access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
    ) as s_client:

        res = await s_client.addresses.list_addresses_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                  | Type | Scheme      | Environment Variable          |
| --------------------- | ---- | ----------- | ----------------------------- |
| `access_token_header` | http | HTTP Bearer | `SAMSARA_ACCESS_TOKEN_HEADER` |

To authenticate with the API the `access_token_header` parameter must be set when initializing the SDK client instance. For example:

```python
import os
from samsara import Samsara

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.addresses.list_addresses()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [addresses](docs/sdks/addresses/README.md)

* [list_addresses](docs/sdks/addresses/README.md#list_addresses) - List all addresses
* [create_address](docs/sdks/addresses/README.md#create_address) - Create an address
* [delete_address](docs/sdks/addresses/README.md#delete_address) - Delete an address
* [get_address](docs/sdks/addresses/README.md#get_address) - Retrieve an address
* [update_address](docs/sdks/addresses/README.md#update_address) - Update an address

### [alerts](docs/sdks/alerts/README.md)

* [delete_configurations](docs/sdks/alerts/README.md#delete_configurations) - Delete alert configurations.
* [get_configurations](docs/sdks/alerts/README.md#get_configurations) - Get Alert Configurations.
* [patch_configurations](docs/sdks/alerts/README.md#patch_configurations) - Update alert configurations.
* [post_configurations](docs/sdks/alerts/README.md#post_configurations) - Create alert configurations.
* [get_incidents](docs/sdks/alerts/README.md#get_incidents) - Get Alert Incidents.

### [assets](docs/sdks/assets/README.md)

* [v1get_all_assets](docs/sdks/assets/README.md#v1get_all_assets) - List all assets
* [v1get_all_asset_current_locations](docs/sdks/assets/README.md#v1get_all_asset_current_locations) - List current location for all assets
* [v1get_assets_reefers](docs/sdks/assets/README.md#v1get_assets_reefers) - List stats for all reefers
* [v1get_asset_location](docs/sdks/assets/README.md#v1get_asset_location) - List historical locations for a given asset
* [v1get_asset_reefer](docs/sdks/assets/README.md#v1get_asset_reefer) - List stats for a given reefer

### [attributes](docs/sdks/attributes/README.md)

* [get_attributes_by_entity_type](docs/sdks/attributes/README.md#get_attributes_by_entity_type) - List all attributes by entity type
* [create_attribute](docs/sdks/attributes/README.md#create_attribute) - Create an attribute
* [delete_attribute](docs/sdks/attributes/README.md#delete_attribute) - Deleting an attribute
* [get_attribute](docs/sdks/attributes/README.md#get_attribute) - Retrieve an attribute
* [update_attribute](docs/sdks/attributes/README.md#update_attribute) - Update an attribute

### [beta_ap_is](docs/sdks/betaapis/README.md)

* [delete_asset](docs/sdks/betaapis/README.md#delete_asset) - [beta] Delete an existing asset.
* [list_assets](docs/sdks/betaapis/README.md#list_assets) - [beta] List all assets.
* [update_asset](docs/sdks/betaapis/README.md#update_asset) - [beta] Update an existing asset.
* [create_asset](docs/sdks/betaapis/README.md#create_asset) - [beta] Create a new asset.
* [get_assets_inputs](docs/sdks/betaapis/README.md#get_assets_inputs) - [beta] List asset inputs data in an organization.
* [get_aemp_equipment_list](docs/sdks/betaapis/README.md#get_aemp_equipment_list) - [beta] Get a list of AEMP equipment
* [get_driver_efficiency](docs/sdks/betaapis/README.md#get_driver_efficiency) - [beta] List driver efficiency
* [patch_equipment](docs/sdks/betaapis/README.md#patch_equipment) - [beta] Update an equipment
* [get_hos_eld_events](docs/sdks/betaapis/README.md#get_hos_eld_events) - [beta] Get driver HOS ELD events
* [get_trailer_stats_snapshot](docs/sdks/betaapis/README.md#get_trailer_stats_snapshot) - [beta] Get trailer stats
* [get_trailer_stats_feed](docs/sdks/betaapis/README.md#get_trailer_stats_feed) - [beta] Get trailer stats feed
* [get_trailer_stats_history](docs/sdks/betaapis/README.md#get_trailer_stats_history) - [beta] Get trailer stats history
* [update_engine_immobilizer_state](docs/sdks/betaapis/README.md#update_engine_immobilizer_state) - [beta] Update engine immobilizer state of a vehicle.
* [delete_job](docs/sdks/betaapis/README.md#delete_job) - [beta] Deletes an existing job
* [get_jobs](docs/sdks/betaapis/README.md#get_jobs) - [beta] Fetches all jobs
* [patch_job](docs/sdks/betaapis/README.md#patch_job) - [beta] Patches a job
* [create_job](docs/sdks/betaapis/README.md#create_job) - [beta] Create a job
* [get_media_retrieval](docs/sdks/betaapis/README.md#get_media_retrieval) - [beta] Get details for a media retrieval request
* [post_media_retrieval](docs/sdks/betaapis/README.md#post_media_retrieval) - [beta] Create a media retrieval request
* [get_devices](docs/sdks/betaapis/README.md#get_devices) - [beta] List devices.
* [get_driver_trailer_assignments](docs/sdks/betaapis/README.md#get_driver_trailer_assignments) - [beta] Get currently active driver-trailer assignments for driver.
* [update_driver_trailer_assignment](docs/sdks/betaapis/README.md#update_driver_trailer_assignment) - [beta] Update an existing driver-trailer assignment.
* [create_driver_trailer_assignment](docs/sdks/betaapis/README.md#create_driver_trailer_assignment) - [beta] Create a new driver-trailer assignment
* [post_driver_remote_signout](docs/sdks/betaapis/README.md#post_driver_remote_signout) - [beta] Sign out a driver
* [get_engine_immobilizer_states](docs/sdks/betaapis/README.md#get_engine_immobilizer_states) - [beta] Get engine immobilizer states
* [get_form_submissions](docs/sdks/betaapis/README.md#get_form_submissions) - [beta] Get a list of specified form submissions.
* [patch_form_submission](docs/sdks/betaapis/README.md#patch_form_submission) - [beta] Update a single form submission.
* [post_form_submission](docs/sdks/betaapis/README.md#post_form_submission) - [beta] Create a form submission.
* [get_form_submissions_pdf_exports](docs/sdks/betaapis/README.md#get_form_submissions_pdf_exports) - [beta] Return a PDF export for a form submission.
* [post_form_submissions_pdf_exports](docs/sdks/betaapis/README.md#post_form_submissions_pdf_exports) - [beta] Create a PDF export for a form submission.
* [get_form_submissions_stream](docs/sdks/betaapis/README.md#get_form_submissions_stream) - [beta] Get a stream of filtered form submissions.
* [update_shipping_docs](docs/sdks/betaapis/README.md#update_shipping_docs) - [beta] Update the shippingDocs field of an existing assignment.
* [get_issues](docs/sdks/betaapis/README.md#get_issues) - [beta] Get a list of specified issues.
* [patch_issue](docs/sdks/betaapis/README.md#patch_issue) - [beta] Update a single issue.
* [get_issues_stream](docs/sdks/betaapis/README.md#get_issues_stream) - [beta] Get a stream of filtered issues.
* [get_speeding_intervals](docs/sdks/betaapis/README.md#get_speeding_intervals) - [beta] Get Speeding Intervals
* [post_training_assignments](docs/sdks/betaapis/README.md#post_training_assignments) - [beta] Create training assignments.
* [get_training_assignments_stream](docs/sdks/betaapis/README.md#get_training_assignments_stream) - [beta] Get a stream of filtered training assignments.
* [get_trips](docs/sdks/betaapis/README.md#get_trips) - [beta] Get trips

### [carrier_proposed_assignments](docs/sdks/carrierproposedassignments/README.md)

* [list_carrier_proposed_assignments](docs/sdks/carrierproposedassignments/README.md#list_carrier_proposed_assignments) - Retrieve assignments
* [create_carrier_proposed_assignment](docs/sdks/carrierproposedassignments/README.md#create_carrier_proposed_assignment) - Create an assignment
* [delete_carrier_proposed_assignment](docs/sdks/carrierproposedassignments/README.md#delete_carrier_proposed_assignment) - Delete an assignment

### [coaching](docs/sdks/coaching/README.md)

* [get_driver_coach_assignment](docs/sdks/coaching/README.md#get_driver_coach_assignment) - Get driver coach assignments.
* [put_driver_coach_assignment](docs/sdks/coaching/README.md#put_driver_coach_assignment) - Put driver coach assignments.
* [get_coaching_sessions](docs/sdks/coaching/README.md#get_coaching_sessions) - Get coaching sessions.

### [contacts](docs/sdks/contacts/README.md)

* [list_contacts](docs/sdks/contacts/README.md#list_contacts) - List all contacts
* [create_contact](docs/sdks/contacts/README.md#create_contact) - Create a contact
* [delete_contact](docs/sdks/contacts/README.md#delete_contact) - Delete a contact
* [get_contact](docs/sdks/contacts/README.md#get_contact) - Retrieve a contact
* [update_contact](docs/sdks/contacts/README.md#update_contact) - Update a contact

### [documents](docs/sdks/documents/README.md)

* [get_document_types](docs/sdks/documents/README.md#get_document_types) - Fetch document types
* [get_documents](docs/sdks/documents/README.md#get_documents) - Fetch all documents
* [post_document](docs/sdks/documents/README.md#post_document) - Create document
* [generate_document_pdf](docs/sdks/documents/README.md#generate_document_pdf) - Create a document PDF
* [get_document_pdf](docs/sdks/documents/README.md#get_document_pdf) - Query a document PDF
* [delete_document](docs/sdks/documents/README.md#delete_document) - Delete document
* [get_document](docs/sdks/documents/README.md#get_document) - Fetch document

### [driver_qr_codes](docs/sdks/driverqrcodes/README.md)

* [delete_driver_qr_code](docs/sdks/driverqrcodes/README.md#delete_driver_qr_code) - Revoke driver's QR code
* [get_drivers_qr_codes](docs/sdks/driverqrcodes/README.md#get_drivers_qr_codes) - Get driver QR codes
* [create_driver_qr_code](docs/sdks/driverqrcodes/README.md#create_driver_qr_code) - Create new QR code for driver

### [driver_vehicle_assignments](docs/sdks/drivervehicleassignments/README.md)

* [delete_driver_vehicle_assignments](docs/sdks/drivervehicleassignments/README.md#delete_driver_vehicle_assignments) - Delete API generated driver-vehicle assignments
* [get_driver_vehicle_assignments](docs/sdks/drivervehicleassignments/README.md#get_driver_vehicle_assignments) - Get all driver-vehicle assignments
* [update_driver_vehicle_assignment](docs/sdks/drivervehicleassignments/README.md#update_driver_vehicle_assignment) - Update API generated driver-vehicle assignments
* [create_driver_vehicle_assignment](docs/sdks/drivervehicleassignments/README.md#create_driver_vehicle_assignment) - Create a new driver-vehicle assignment

### [drivers](docs/sdks/drivers/README.md)

* [list_drivers](docs/sdks/drivers/README.md#list_drivers) - List all drivers
* [create_driver](docs/sdks/drivers/README.md#create_driver) - Create a driver
* [get_driver](docs/sdks/drivers/README.md#get_driver) - Retrieve a driver
* [update_driver](docs/sdks/drivers/README.md#update_driver) - Update a driver

### [equipment](docs/sdks/equipmentsdk/README.md)

* [list_equipment](docs/sdks/equipmentsdk/README.md#list_equipment) - List all equipment
* [get_equipment_locations](docs/sdks/equipmentsdk/README.md#get_equipment_locations) - Get most recent locations for all equipment
* [get_equipment_locations_feed](docs/sdks/equipmentsdk/README.md#get_equipment_locations_feed) - Follow feed of equipment locations
* [get_equipment_locations_history](docs/sdks/equipmentsdk/README.md#get_equipment_locations_history) - Get historical equipment locations
* [get_equipment_stats](docs/sdks/equipmentsdk/README.md#get_equipment_stats) - Get most recent stats for all equipment
* [get_equipment_stats_feed](docs/sdks/equipmentsdk/README.md#get_equipment_stats_feed) - Follow a feed of equipment stats
* [get_equipment_stats_history](docs/sdks/equipmentsdk/README.md#get_equipment_stats_history) - Get historical equipment stats
* [get_equipment](docs/sdks/equipmentsdk/README.md#get_equipment) - Retrieve a unit of equipment

### [fuel_and_energy](docs/sdks/fuelandenergy/README.md)

* [get_fuel_energy_driver_reports](docs/sdks/fuelandenergy/README.md#get_fuel_energy_driver_reports) - Get fuel and energy efficiency driver reports.
* [get_fuel_energy_vehicle_reports](docs/sdks/fuelandenergy/README.md#get_fuel_energy_vehicle_reports) - Get fuel and energy efficiency vehicle reports.
* [post_fuel_purchase](docs/sdks/fuelandenergy/README.md#post_fuel_purchase) - Create a fuel purchase transaction.

### [gateways](docs/sdks/gateways/README.md)

* [get_gateways](docs/sdks/gateways/README.md#get_gateways) - List all gateways
* [post_gateway](docs/sdks/gateways/README.md#post_gateway) - Activate a new gateway
* [delete_gateway](docs/sdks/gateways/README.md#delete_gateway) - Deactivate a gateway

### [hours_of_service](docs/sdks/hoursofservice/README.md)

* [get_hos_clocks](docs/sdks/hoursofservice/README.md#get_hos_clocks) - Get HOS clocks
* [get_hos_daily_logs](docs/sdks/hoursofservice/README.md#get_hos_daily_logs) - Get all driver HOS daily logs
* [get_hos_logs](docs/sdks/hoursofservice/README.md#get_hos_logs) - Get HOS logs
* [get_hos_violations](docs/sdks/hoursofservice/README.md#get_hos_violations) - Get all driver HOS violations
* [set_current_duty_status](docs/sdks/hoursofservice/README.md#set_current_duty_status) - Set a duty status for a specific driver
* [v1get_fleet_hos_authentication_logs](docs/sdks/hoursofservice/README.md#v1get_fleet_hos_authentication_logs) - Get HOS signin and signout

### [idling](docs/sdks/idling/README.md)

* [get_vehicle_idling_reports](docs/sdks/idling/README.md#get_vehicle_idling_reports) - Get vehicle idling reports.

### [ifta](docs/sdks/ifta/README.md)

* [get_ifta_jurisdiction_reports](docs/sdks/ifta/README.md#get_ifta_jurisdiction_reports) - Get IFTA jurisdiction reports.
* [get_ifta_vehicle_reports](docs/sdks/ifta/README.md#get_ifta_vehicle_reports) - Get IFTA vehicle reports.
* [create_ifta_detail_job](docs/sdks/ifta/README.md#create_ifta_detail_job) - Create a job to generate csv files of IFTA mileage segments.
* [get_ifta_detail_job](docs/sdks/ifta/README.md#get_ifta_detail_job) - Get information about an existing IFTA detail job.

### [industrial](docs/sdks/industrial/README.md)

* [get_industrial_assets](docs/sdks/industrial/README.md#get_industrial_assets) - List all assets
* [create_industrial_asset](docs/sdks/industrial/README.md#create_industrial_asset) - Create an asset
* [delete_industrial_asset](docs/sdks/industrial/README.md#delete_industrial_asset) - Delete an existing asset
* [patch_industrial_asset](docs/sdks/industrial/README.md#patch_industrial_asset) - Update an asset
* [patch_asset_data_outputs](docs/sdks/industrial/README.md#patch_asset_data_outputs) - Writes to data outputs on an asset
* [get_data_inputs](docs/sdks/industrial/README.md#get_data_inputs) - List all data inputs
* [get_data_input_data_snapshot](docs/sdks/industrial/README.md#get_data_input_data_snapshot) - List most recent data points for data inputs
* [get_data_input_data_feed](docs/sdks/industrial/README.md#get_data_input_data_feed) - Follow a real-time feed of data points for data inputs
* [get_data_input_data_history](docs/sdks/industrial/README.md#get_data_input_data_history) - List historical data points for data inputs
* [v1get_cameras](docs/sdks/industrial/README.md#v1get_cameras) - Fetch industrial cameras
* [v1get_vision_programs_by_camera](docs/sdks/industrial/README.md#v1get_vision_programs_by_camera) - Fetch industrial camera programs
* [v1get_vision_latest_run_camera](docs/sdks/industrial/README.md#v1get_vision_latest_run_camera) - Fetch the latest run for a camera or program
* [v1get_vision_runs](docs/sdks/industrial/README.md#v1get_vision_runs) - Fetch runs
* [get_vision_runs_by_camera](docs/sdks/industrial/README.md#get_vision_runs_by_camera) - Fetch runs by camera
* [v1get_vision_runs_by_camera_and_program](docs/sdks/industrial/README.md#v1get_vision_runs_by_camera_and_program) - Fetch runs by camera and program
* [v1get_machines_history](docs/sdks/industrial/README.md#v1get_machines_history) - Get machine history
* [v1get_machines](docs/sdks/industrial/README.md#v1get_machines) - Get machines

### [legacy_ap_is](docs/sdks/legacyapis/README.md)

* [get_drivers_vehicle_assignments](docs/sdks/legacyapis/README.md#get_drivers_vehicle_assignments) - [legacy] Get all vehicles assigned to a set of drivers
* [get_vehicles_driver_assignments](docs/sdks/legacyapis/README.md#get_vehicles_driver_assignments) - [legacy] Get all drivers assigned to a set of vehicles

### [live_sharing_links](docs/sdks/livesharinglinks/README.md)

* [delete_live_sharing_link](docs/sdks/livesharinglinks/README.md#delete_live_sharing_link) - Delete non-expired Live Sharing Link
* [get_live_sharing_links](docs/sdks/livesharinglinks/README.md#get_live_sharing_links) - Get Live Sharing Links
* [update_live_sharing_link](docs/sdks/livesharinglinks/README.md#update_live_sharing_link) - Update non-expired Live Sharing Link
* [create_live_sharing_link](docs/sdks/livesharinglinks/README.md#create_live_sharing_link) - Create Live Sharing Link

### [location_and_speed](docs/sdks/locationandspeed/README.md)

* [get_location_and_speed](docs/sdks/locationandspeed/README.md#get_location_and_speed) - List asset location and speed data in an organization.

### [maintenance](docs/sdks/maintenance/README.md)

* [get_defect_types](docs/sdks/maintenance/README.md#get_defect_types) - Get DVIR defect types.
* [stream_defects](docs/sdks/maintenance/README.md#stream_defects) - Stream DVIR defects.
* [get_dvirs](docs/sdks/maintenance/README.md#get_dvirs) - Stream DVIRs
* [get_dvir_defects](docs/sdks/maintenance/README.md#get_dvir_defects) - Get all defects
* [update_dvir_defect](docs/sdks/maintenance/README.md#update_dvir_defect) - Update a defect
* [create_dvir](docs/sdks/maintenance/README.md#create_dvir) - Create a mechanic DVIR
* [get_dvir_history](docs/sdks/maintenance/README.md#get_dvir_history) - Get all DVIRs
* [update_dvir](docs/sdks/maintenance/README.md#update_dvir) - Resolve a DVIR
* [v1get_fleet_maintenance_list](docs/sdks/maintenance/README.md#v1get_fleet_maintenance_list) - Get vehicles with engine faults or check lights

### [messages](docs/sdks/messages/README.md)

* [v1get_messages](docs/sdks/messages/README.md#v1get_messages) - Get all messages.
* [v1create_messages](docs/sdks/messages/README.md#v1create_messages) - Send a message to a list of driver ids.

### [organization_info](docs/sdks/organizationinfosdk/README.md)

* [get_organization_info](docs/sdks/organizationinfosdk/README.md#get_organization_info) - Get information about your organization

### [preview_ap_is](docs/sdks/previewapis/README.md)

* [list_uploaded_media](docs/sdks/previewapis/README.md#list_uploaded_media) - [preview] List uploaded media by time range.
* [get_custom_report_configs](docs/sdks/previewapis/README.md#get_custom_report_configs) - [preview] Get custom report configs
* [get_custom_report_runs](docs/sdks/previewapis/README.md#get_custom_report_runs) - [preview] Get custom report runs
* [post_custom_report_run](docs/sdks/previewapis/README.md#post_custom_report_run) - [preview] Create a custom report run
* [get_custom_report_run_data](docs/sdks/previewapis/README.md#get_custom_report_run_data) - [preview] Get custom report run data
* [get_driver_efficiency_by_drivers](docs/sdks/previewapis/README.md#get_driver_efficiency_by_drivers) - [preview] Get Driver efficiency data grouped by drivers.
* [get_driver_efficiency_by_vehicles](docs/sdks/previewapis/README.md#get_driver_efficiency_by_vehicles) - [preview] Get Driver efficiency data grouped by vehicles.
* [get_form_templates](docs/sdks/previewapis/README.md#get_form_templates) - [preview] Get a list of form templates.
* [delete_training_assignments](docs/sdks/previewapis/README.md#delete_training_assignments) - [preview] Delete training assignments.
* [patch_training_assignments](docs/sdks/previewapis/README.md#patch_training_assignments) - [preview] Update training assignments.
* [get_training_courses](docs/sdks/previewapis/README.md#get_training_courses) - [preview] Get a list of filtered training courses.

### [routes](docs/sdks/routes/README.md)

* [fetch_routes](docs/sdks/routes/README.md#fetch_routes) - Fetch all routes
* [create_route](docs/sdks/routes/README.md#create_route) - Create a route
* [get_routes_feed](docs/sdks/routes/README.md#get_routes_feed) - Get route updates
* [delete_route](docs/sdks/routes/README.md#delete_route) - Delete a route.
* [fetch_route](docs/sdks/routes/README.md#fetch_route) - Fetch a route
* [patch_route](docs/sdks/routes/README.md#patch_route) - Update a route
* [v1delete_dispatch_route_by_id](docs/sdks/routes/README.md#v1delete_dispatch_route_by_id) - Delete a route

### [safety](docs/sdks/safety/README.md)

* [get_safety_events](docs/sdks/safety/README.md#get_safety_events) - List all safety events.
* [get_safety_activity_event_feed](docs/sdks/safety/README.md#get_safety_activity_event_feed) - Fetches safety activity event feed
* [v1get_driver_safety_score](docs/sdks/safety/README.md#v1get_driver_safety_score) - Fetch driver safety score
* [v1get_vehicle_harsh_event](docs/sdks/safety/README.md#v1get_vehicle_harsh_event) - Fetch harsh events
* [v1get_vehicle_safety_score](docs/sdks/safety/README.md#v1get_vehicle_safety_score) - Fetch vehicle safety scores


### [sensors](docs/sdks/sensors/README.md)

* [v1get_sensors_cargo](docs/sdks/sensors/README.md#v1get_sensors_cargo) - Get cargo status
* [v1get_sensors_door](docs/sdks/sensors/README.md#v1get_sensors_door) - Get door status
* [v1get_sensors_history](docs/sdks/sensors/README.md#v1get_sensors_history) - Get sensor history
* [v1get_sensors_humidity](docs/sdks/sensors/README.md#v1get_sensors_humidity) - Get humidity
* [v1get_sensors](docs/sdks/sensors/README.md#v1get_sensors) - Get all sensors
* [v1get_sensors_temperature](docs/sdks/sensors/README.md#v1get_sensors_temperature) - Get temperature

### [settings](docs/sdks/settings/README.md)

* [get_compliance_settings](docs/sdks/settings/README.md#get_compliance_settings) - Get compliance settings
* [patch_compliance_settings](docs/sdks/settings/README.md#patch_compliance_settings) - Update compliance settings
* [get_driver_app_settings](docs/sdks/settings/README.md#get_driver_app_settings) - Get driver app settings
* [patch_driver_app_settings](docs/sdks/settings/README.md#patch_driver_app_settings) - Update driver app settings
* [get_safety_settings](docs/sdks/settings/README.md#get_safety_settings) - Get safety settings

### [tachograph_eu_only](docs/sdks/tachographeuonly/README.md)

* [get_driver_tachograph_activity](docs/sdks/tachographeuonly/README.md#get_driver_tachograph_activity) - Get driver tachograph activity
* [get_driver_tachograph_files](docs/sdks/tachographeuonly/README.md#get_driver_tachograph_files) - Get tachograph driver files
* [get_vehicle_tachograph_files](docs/sdks/tachographeuonly/README.md#get_vehicle_tachograph_files) - Get tachograph vehicle files

### [tags](docs/sdks/tags/README.md)

* [list_tags](docs/sdks/tags/README.md#list_tags) - List all tags
* [create_tag](docs/sdks/tags/README.md#create_tag) - Create a tag
* [delete_tag](docs/sdks/tags/README.md#delete_tag) - Delete a tag
* [get_tag](docs/sdks/tags/README.md#get_tag) - Retrieve a tag
* [patch_tag](docs/sdks/tags/README.md#patch_tag) - Update a tag
* [replace_tag](docs/sdks/tags/README.md#replace_tag) - Update a tag

### [trailer_assignments](docs/sdks/trailerassignments/README.md)

* [v1get_all_trailer_assignments](docs/sdks/trailerassignments/README.md#v1get_all_trailer_assignments) - List trailer assignments for all trailers
* [v1get_fleet_trailer_assignments](docs/sdks/trailerassignments/README.md#v1get_fleet_trailer_assignments) - List trailer assignments for a given trailer

### [trailers](docs/sdks/trailers/README.md)

* [list_trailers](docs/sdks/trailers/README.md#list_trailers) - List all trailers
* [create_trailer](docs/sdks/trailers/README.md#create_trailer) - Creates a new trailer asset
* [delete_trailer](docs/sdks/trailers/README.md#delete_trailer) - Delete a trailer
* [get_trailer](docs/sdks/trailers/README.md#get_trailer) - Retrieve a trailer
* [update_trailer](docs/sdks/trailers/README.md#update_trailer) - Update a trailer

### [trips](docs/sdks/trips/README.md)

* [v1get_fleet_trips](docs/sdks/trips/README.md#v1get_fleet_trips) - Get vehicle trips

### [users](docs/sdks/users/README.md)

* [list_user_roles](docs/sdks/users/README.md#list_user_roles) - List all user roles
* [list_users](docs/sdks/users/README.md#list_users) - List all users
* [create_user](docs/sdks/users/README.md#create_user) - Create a user
* [delete_user](docs/sdks/users/README.md#delete_user) - Delete a user
* [get_user](docs/sdks/users/README.md#get_user) - Retrieve a user
* [update_user](docs/sdks/users/README.md#update_user) - Update a user

### [vehicle_locations](docs/sdks/vehiclelocations/README.md)

* [get_vehicle_locations](docs/sdks/vehiclelocations/README.md#get_vehicle_locations) - Locations snapshot
* [get_vehicle_locations_feed](docs/sdks/vehiclelocations/README.md#get_vehicle_locations_feed) - Locations feed
* [get_vehicle_locations_history](docs/sdks/vehiclelocations/README.md#get_vehicle_locations_history) - Historical locations

### [vehicle_stats](docs/sdks/vehiclestats/README.md)

* [get_vehicle_stats](docs/sdks/vehiclestats/README.md#get_vehicle_stats) - Stats snapshot
* [get_vehicle_stats_feed](docs/sdks/vehiclestats/README.md#get_vehicle_stats_feed) - Stats feed
* [get_vehicle_stats_history](docs/sdks/vehiclestats/README.md#get_vehicle_stats_history) - Historical stats

### [vehicles](docs/sdks/vehicles/README.md)

* [list_vehicles](docs/sdks/vehicles/README.md#list_vehicles) - List all vehicles.
* [get_vehicle](docs/sdks/vehicles/README.md#get_vehicle) - Retrieve a vehicle
* [update_vehicle](docs/sdks/vehicles/README.md#update_vehicle) - Update a vehicle

### [webhooks](docs/sdks/webhooks/README.md)

* [list_webhooks](docs/sdks/webhooks/README.md#list_webhooks) - List all webhooks belonging to a specific org.
* [post_webhooks](docs/sdks/webhooks/README.md#post_webhooks) - Create a webhook
* [delete_webhook](docs/sdks/webhooks/README.md#delete_webhook) - Delete a webhook with the given ID
* [get_webhook](docs/sdks/webhooks/README.md#get_webhook) - Retrieve a webhook with given ID
* [patch_webhook](docs/sdks/webhooks/README.md#patch_webhook) - Update a specific webhook's information.

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import os
from samsara import Samsara
from samsara.utils import BackoffStrategy, RetryConfig

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.addresses.list_addresses(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import os
from samsara import Samsara
from samsara.utils import BackoffStrategy, RetryConfig

with Samsara(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.addresses.list_addresses()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `delete_configurations_async` method may raise the following exceptions:

| Error Type                                                           | Status Code | Content Type     |
| -------------------------------------------------------------------- | ----------- | ---------------- |
| models.AlertsDeleteConfigurationsUnauthorizedErrorResponseBody       | 401         | application/json |
| models.AlertsDeleteConfigurationsNotFoundErrorResponseBody           | 404         | application/json |
| models.AlertsDeleteConfigurationsMethodNotAllowedErrorResponseBody   | 405         | application/json |
| models.AlertsDeleteConfigurationsTooManyRequestsErrorResponseBody    | 429         | application/json |
| models.AlertsDeleteConfigurationsInternalServerErrorResponseBody     | 500         | application/json |
| models.AlertsDeleteConfigurationsNotImplementedErrorResponseBody     | 501         | application/json |
| models.AlertsDeleteConfigurationsBadGatewayErrorResponseBody         | 502         | application/json |
| models.AlertsDeleteConfigurationsServiceUnavailableErrorResponseBody | 503         | application/json |
| models.AlertsDeleteConfigurationsGatewayTimeoutErrorResponseBody     | 504         | application/json |
| models.APIError                                                      | 4XX, 5XX    | \*/\*            |

### Example

```python
import os
from samsara import Samsara, models

with Samsara(
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:
    res = None
    try:

        res = s_client.alerts.delete_configurations(id="<id>")

        assert res is not None

        # Handle response
        print(res)

    except models.AlertsDeleteConfigurationsUnauthorizedErrorResponseBody as e:
        # handle e.data: models.AlertsDeleteConfigurationsUnauthorizedErrorResponseBodyData
        raise(e)
    except models.AlertsDeleteConfigurationsNotFoundErrorResponseBody as e:
        # handle e.data: models.AlertsDeleteConfigurationsNotFoundErrorResponseBodyData
        raise(e)
    except models.AlertsDeleteConfigurationsMethodNotAllowedErrorResponseBody as e:
        # handle e.data: models.AlertsDeleteConfigurationsMethodNotAllowedErrorResponseBodyData
        raise(e)
    except models.AlertsDeleteConfigurationsTooManyRequestsErrorResponseBody as e:
        # handle e.data: models.AlertsDeleteConfigurationsTooManyRequestsErrorResponseBodyData
        raise(e)
    except models.AlertsDeleteConfigurationsInternalServerErrorResponseBody as e:
        # handle e.data: models.AlertsDeleteConfigurationsInternalServerErrorResponseBodyData
        raise(e)
    except models.AlertsDeleteConfigurationsNotImplementedErrorResponseBody as e:
        # handle e.data: models.AlertsDeleteConfigurationsNotImplementedErrorResponseBodyData
        raise(e)
    except models.AlertsDeleteConfigurationsBadGatewayErrorResponseBody as e:
        # handle e.data: models.AlertsDeleteConfigurationsBadGatewayErrorResponseBodyData
        raise(e)
    except models.AlertsDeleteConfigurationsServiceUnavailableErrorResponseBody as e:
        # handle e.data: models.AlertsDeleteConfigurationsServiceUnavailableErrorResponseBodyData
        raise(e)
    except models.AlertsDeleteConfigurationsGatewayTimeoutErrorResponseBody as e:
        # handle e.data: models.AlertsDeleteConfigurationsGatewayTimeoutErrorResponseBodyData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                        |
| --- | ----------------------------- |
| 0   | `https://api.samsara.com/`    |
| 1   | `https://api.eu.samsara.com/` |

#### Example

```python
import os
from samsara import Samsara

with Samsara(
    server_idx=1,
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.addresses.list_addresses()

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import os
from samsara import Samsara

with Samsara(
    server_url="https://api.samsara.com/",
    access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
) as s_client:

    res = s_client.addresses.list_addresses()

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from samsara import Samsara
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Samsara(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from samsara import Samsara
from samsara.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Samsara(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Samsara` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
import os
from samsara import Samsara
def main():
    with Samsara(
        access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
    ) as s_client:
        # Rest of application here...


# Or when using async:
async def amain():
    async with Samsara(
        access_token_header=os.getenv("SAMSARA_ACCESS_TOKEN_HEADER", ""),
    ) as s_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from samsara import Samsara
import logging

logging.basicConfig(level=logging.DEBUG)
s = Samsara(debug_logger=logging.getLogger("samsara"))
```

You can also enable a default debug logger by setting an environment variable `SAMSARA_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation.
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release.

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=samsara&utm_campaign=python)
