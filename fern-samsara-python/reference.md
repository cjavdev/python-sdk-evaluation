# Reference
## Addresses
<details><summary><code>client.addresses.<a href="src/samsara/addresses/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all addresses in an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.addresses.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**created_after_time:** `typing.Optional[str]` — A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.addresses.<a href="src/samsara/addresses/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new address in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import CreateAddressRequestGeofence, Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.addresses.create(
    formatted_address="350 Rhode Island St, San Francisco, CA",
    geofence=CreateAddressRequestGeofence(),
    name="Samsara HQ",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**formatted_address:** `str` — The full street address for this address/geofence, as it might be recognized by Google Maps.
    
</dd>
</dl>

<dl>
<dd>

**geofence:** `CreateAddressRequestGeofence` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the address.
    
</dd>
</dl>

<dl>
<dd>

**address_types:** `typing.Optional[typing.Sequence[CreateAddressRequestAddressTypesItem]]` — Reporting location type associated with the address (used for ELD reporting purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`, `industrialSite`, `alertsOnly`.
    
</dd>
</dl>

<dl>
<dd>

**contact_ids:** `typing.Optional[typing.Sequence[str]]` — An array of Contact IDs associated with this Address.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    
</dd>
</dl>

<dl>
<dd>

**latitude:** `typing.Optional[float]` — Latitude of the address. Will be geocoded from `formattedAddress` if not provided.
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `typing.Optional[float]` — Longitude of the address. Will be geocoded from `formattedAddress` if not provided.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about the address.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.addresses.<a href="src/samsara/addresses/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific address. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.addresses.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.addresses.<a href="src/samsara/addresses/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific address. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.addresses.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.addresses.<a href="src/samsara/addresses/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific address. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.addresses.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`
    
</dd>
</dl>

<dl>
<dd>

**address_types:** `typing.Optional[typing.Sequence[UpdateAddressRequestAddressTypesItem]]` — Reporting location type associated with the address (used for ELD reporting purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`, `industrialSite`, `alertsOnly`.
    
</dd>
</dl>

<dl>
<dd>

**contact_ids:** `typing.Optional[typing.Sequence[str]]` — An array of Contact IDs associated with this Address.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    
</dd>
</dl>

<dl>
<dd>

**formatted_address:** `typing.Optional[str]` — The full street address for this address/geofence, as it might be recognized by Google Maps.
    
</dd>
</dl>

<dl>
<dd>

**geofence:** `typing.Optional[UpdateAddressRequestGeofence]` 
    
</dd>
</dl>

<dl>
<dd>

**latitude:** `typing.Optional[float]` — Latitude of the address. Will be geocoded from `formattedAddress` if not provided.
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `typing.Optional[float]` — Longitude of the address. Will be geocoded from `formattedAddress` if not provided.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the address.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about the address.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Alerts
<details><summary><code>client.alerts.<a href="src/samsara/alerts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an alert configuration.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import (
    ActionObjectRequestBody,
    Samsara,
    ScopeObjectRequestBody,
    WorkflowTriggerObjectRequestBody,
)

client = Samsara(
    token="YOUR_TOKEN",
)
client.alerts.create(
    actions=[
        ActionObjectRequestBody(
            action_type_id=1,
        )
    ],
    is_enabled=True,
    name="My Harsh Event Alert",
    scope=ScopeObjectRequestBody(
        all_=True,
    ),
    triggers=[
        WorkflowTriggerObjectRequestBody(
            trigger_type_id=1000,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**actions:** `typing.Sequence[ActionObjectRequestBody]` — An array of actions.
    
</dd>
</dl>

<dl>
<dd>

**is_enabled:** `bool` — Whether the alert is enabled or not.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The custom name of the configuration.
    
</dd>
</dl>

<dl>
<dd>

**scope:** `ScopeObjectRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**triggers:** `typing.Sequence[WorkflowTriggerObjectRequestBody]` — An array of triggers.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**operational_settings:** `typing.Optional[OperationalSettingsObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alerts.<a href="src/samsara/alerts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an alert configuration.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.alerts.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unqiue Samsara id of the alert configuration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alerts.<a href="src/samsara/alerts/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an alert configuration.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.alerts.update(
    id="e1c5dffc-c7b7-47b0-a778-6a65de638abf",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unqiue Samsara id of the alert configuration.
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[ActionObjectRequestBody]]` — An array of actions.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**is_enabled:** `typing.Optional[bool]` — Whether the alert is enabled or not.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The custom name of the configuration.
    
</dd>
</dl>

<dl>
<dd>

**operational_settings:** `typing.Optional[OperationalSettingsObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[ScopeObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**triggers:** `typing.Optional[typing.Sequence[WorkflowTriggerObjectRequestBody]]` — An array of triggers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LocationAndSpeed
<details><summary><code>client.location_and_speed.<a href="src/samsara/location_and_speed/client.py">stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return asset locations and speed data that has been collected for your organization based on the time parameters passed in. Results are paginated. If you include an endTime, the endpoint will return data up until that point. If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call. The endpoint will only return data up until the endTime that has been processed by the server at the time of the original request. You will need to request the same [startTime, endTime) range again to receive data for assets processed after the original request time. This endpoint sorts the time-series data by device.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Vehicles** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.location_and_speed.stream()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to never if not provided; if not provided then pagination will not cease, and a valid pagination cursor will always be returned. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of asset IDs.
    
</dd>
</dl>

<dl>
<dd>

**include_speed:** `typing.Optional[bool]` — Optional boolean indicating whether or not to return the 'speed' object
    
</dd>
</dl>

<dl>
<dd>

**include_reverse_geo:** `typing.Optional[bool]` — Optional boolean indicating whether or not to return the 'address' object
    
</dd>
</dl>

<dl>
<dd>

**include_geofence_lookup:** `typing.Optional[bool]` — Optional boolean indicating whether or not to return the 'geofence' object
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Attributes
<details><summary><code>client.attributes.<a href="src/samsara/attributes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all attributes in an organization associated with either drivers or assets. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.attributes.list(
    entity_type="driver",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_type:** `AttributesListRequestEntityType` — Denotes the type of entity, driver or asset.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attributes.<a href="src/samsara/attributes/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new attribute in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.attributes.create(
    attribute_type="string",
    attribute_value_quantity="single",
    entity_type="driver",
    name="License Certifications",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute_type:** `CreateAttributeRequestAttributeType` — Denotes the data type of the attribute's values. Valid values: `string`, `number`.
    
</dd>
</dl>

<dl>
<dd>

**attribute_value_quantity:** `CreateAttributeRequestAttributeValueQuantity` — Defines whether or not this attribute can be used on the same entity many times (with different values). Valid values: `single`, `multi`.
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `CreateAttributeRequestEntityType` — Denotes the type of entity, driver or asset.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name
    
</dd>
</dl>

<dl>
<dd>

**entities:** `typing.Optional[typing.Sequence[CreateAttributeRequestEntities]]` — Entities that will be applied to this attribute
    
</dd>
</dl>

<dl>
<dd>

**number_values:** `typing.Optional[typing.Sequence[float]]` — Number values that can be associated with this attribute
    
</dd>
</dl>

<dl>
<dd>

**string_values:** `typing.Optional[typing.Sequence[str]]` — String values that can be associated with this attribute
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attributes.<a href="src/samsara/attributes/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch an attribute by id, including all of its applications. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.attributes.get(
    id="id",
    entity_type="driver",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Samsara-provided UUID of the attribute.
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `AttributesGetRequestEntityType` — Denotes the type of entity, driver or asset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attributes.<a href="src/samsara/attributes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an attribute by id, including all of its applications. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.attributes.delete(
    id="id",
    entity_type="driver",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Samsara-provided UUID of the attribute.
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `AttributesDeleteRequestEntityType` — Denotes the type of entity, driver or asset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attributes.<a href="src/samsara/attributes/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an attribute in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.attributes.update(
    id="id",
    entity_type="driver",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Samsara-provided UUID of the attribute.
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `UpdateAttributeRequestEntityType` — Denotes the type of entity, driver or asset.
    
</dd>
</dl>

<dl>
<dd>

**attribute_type:** `typing.Optional[UpdateAttributeRequestAttributeType]` — Denotes the data type of the attribute's values. Valid values: `string`, `number`.
    
</dd>
</dl>

<dl>
<dd>

**attribute_value_quantity:** `typing.Optional[UpdateAttributeRequestAttributeValueQuantity]` — Defines whether or not this attribute can be used on the same entity many times (with different values). Denotes the type of entity, driver or asset. Valid values: `driver`, `asset`.
    
</dd>
</dl>

<dl>
<dd>

**entities:** `typing.Optional[typing.Sequence[CreateAttributeRequestEntities]]` — Entities that will be applied to this attribute
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name
    
</dd>
</dl>

<dl>
<dd>

**number_values:** `typing.Optional[typing.Sequence[float]]` — Number values that can be associated with this attribute
    
</dd>
</dl>

<dl>
<dd>

**string_values:** `typing.Optional[typing.Sequence[str]]` — String values that can be associated with this attribute
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Beta
<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">get_media_retrieval</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint returns media information corresponding to a retrieval ID. Retrieval IDs are associated to prior [media retrieval requests](https://developers.samsara.com/reference/postmediaretrieval). Urls provided by this endpoint expire in 8 hours.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Media Retrieval** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.get_media_retrieval(
    retrieval_id="retrievalId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**retrieval_id:** `str` — Retrieval ID associated with this media capture request. Examples: 2308cec4-82e0-46f1-8b3c-a3592e5cc21e
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">post_media_retrieval</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint creates an asynchronous request to upload certain media from a device. Currently, images and videos can be requested for timestamps when there's high resolution footage stored on the device, even if low resolution footage exists on the device during that timestamp. Other types of media (e.g. hyperlapse) are planned to be supported in the future. Currently, only unblurred media is supported; orgs with blurring enabled will not be able to retrieve media. If a device is offline, the requested media will be uploaded once it comes back online. Quota limits for media requests will be enforced in GA, but not in closed beta.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Media Retrieval** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.post_media_retrieval(
    end_time="2019-06-13T19:08:55Z",
    inputs=["dashcamRoadFacing", "dashcamRoadFacing", "dashcamRoadFacing"],
    media_type="IMAGE",
    start_time="2019-06-13T19:08:25Z",
    vehicle_id="1234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. If endTime is the same as startTime, an image will be captured at startTime. Must be equal to or after startTime and no more than 60 seconds after startTime. Repeated requests with identical parameters, except for a different endTime, are not currently supported; please increment the startTime instead. (Examples: 2019-06-13T19:08:55Z, 2019-06-13T19:08:55.455Z, OR 2015-09-15T14:00:42-04:00).
    
</dd>
</dl>

<dl>
<dd>

**inputs:** `typing.Sequence[MediaRetrievalPostMediaRetrievalRequestBodyInputsItem]` — A list of desired camera inputs for which to capture media. Only media with valid inputs (e.g. device has that input stream and device was recording at the time) will be uploaded. An empty list is invalid.
    
</dd>
</dl>

<dl>
<dd>

**media_type:** `MediaRetrievalPostMediaRetrievalRequestBodyMediaType` — The desired media type. If a video is requested, endTime must be after startTime. If an image is requested, endTime must be the same as startTime. Must be one of: IMAGE, VIDEO_HIGH_RES, VIDEO_LOW_RES. Examples: IMAGE, VIDEO_HIGH_RES, VIDEO_LOW_RES  Valid values: `IMAGE`, `VIDEO_HIGH_RES`, `VIDEO_LOW_RES`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `str` — Vehicle ID for which to initiate media capture. Examples: 1234
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">get_driver_trailer_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get currently active driver-trailer assignments for driver.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.get_driver_trailer_assignments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">create_driver_trailer_assignment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new driver-trailer assignment

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.create_driver_trailer_assignment(
    driver_id="494123",
    trailer_id="12345",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `str` — ID of the driver. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    
</dd>
</dl>

<dl>
<dd>

**trailer_id:** `str` — ID of the trailer. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the trailer.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` — The start time in RFC 3339 format. The time needs to be current or within the past 7 days. Defaults to now if not provided
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">update_driver_trailer_assignment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing driver-trailer assignment.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.update_driver_trailer_assignment(
    id="id",
    end_time="2019-06-13T19:08:25Z",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Samsara ID for the assignment.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — The end time in RFC 3339 format. The end time should not be in the future
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">create_driver_remote_signout</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sign out a driver from the Samsara Driver App

To access this endpoint, your organization must have the Samsara Platform Premier license.

Note: Sign out requests made while a logged-in driver does not have internet connection will not log the driver out. A success response will still be provided and the driver will be logged out once they have internet connection.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Driver Remote Signout** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.create_driver_remote_signout(
    driver_id="12434",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `str` — ID of the driver.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">get_engine_immobilizer_states</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the engine immobilizer states of the queried vehicles. If a vehicle has never had an engine immobilizer connected, there won't be any state returned for that vehicle.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Vehicle Immobilization** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.get_engine_immobilizer_states(
    vehicle_ids="vehicleIds",
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vehicle_ids:** `str` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">get_form_submissions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all form submissions data for the specified IDs. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Forms APIs enabled for your organization.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Form Submissions** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.get_form_submissions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 100 form submission IDs to filter on. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the form submission.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of strings indicating whether to return additional information. Valid values: `externalIds`, `fieldLabels`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">post_form_submission</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a form submission. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Forms APIs enabled for your organization.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Form Submissions** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import FormTemplateReferenceObjectRequestBody, Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.post_form_submission(
    form_template=FormTemplateReferenceObjectRequestBody(
        id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        revision_id="1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**form_template:** `FormTemplateReferenceObjectRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**assigned_to:** `typing.Optional[FormSubmissionRequestAssignedToRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**due_at_time:** `typing.Optional[dt.datetime]` — Due date of the form submission. UTC timestamp in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[
    typing.Sequence[FormSubmissionRequestFieldInputObjectRequestBody]
]` — List of field inputs in a form submission.
    
</dd>
</dl>

<dl>
<dd>

**is_required:** `typing.Optional[bool]` — Indicates whether the worker is required to complete this form or not at a specific route stop. Defaults to `true` if the form is assigned to a user or driver. When true, the worker cannot depart the route stop until this form submission is `submitted`.
    
</dd>
</dl>

<dl>
<dd>

**route_stop_id:** `typing.Optional[str]` — ID of the route stop the form submission is assigned to. Must be a unique Samsara ID.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title of the form submission.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">patch_form_submission</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an instance of a form submission. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Forms APIs enabled for your organization.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Form Submissions** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.patch_form_submission(
    id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the form submission.
    
</dd>
</dl>

<dl>
<dd>

**assigned_to:** `typing.Optional[FormSubmissionRequestAssignedToRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**due_at_time:** `typing.Optional[dt.datetime]` — Due date of the form submission. UTC timestamp in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**is_required:** `typing.Optional[bool]` — Indicates whether the worker is required to complete this form or not at a specific route stop. Defaults to `true` if the form is assigned to a user or driver. When true, the worker cannot depart the route stop until this form submission is `submitted`.
    
</dd>
</dl>

<dl>
<dd>

**route_stop_id:** `typing.Optional[str]` — ID of the route stop the form submission is assigned to. Must be a unique Samsara ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[FormSubmissionsPatchFormSubmissionRequestBodyStatus]` — Status of the form submission.  Valid values: `toDo`, `dismissed`
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title of the form submission.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">get_form_submissions_pdf_exports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a PDF export for a form submission. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Forms APIs enabled for your organization.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Form Submissions** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.get_form_submissions_pdf_exports(
    pdf_id="pdfId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pdf_id:** `str` — ID of the form submission PDF export.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">post_form_submissions_pdf_exports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a PDF export for a form submission. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Forms APIs enabled for your organization.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Form Submissions** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.post_form_submissions_pdf_exports(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the form submission to create a PDF export from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">get_form_submissions_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all form submissions data that has been created or modified for your organization based on the time parameters passed in. Results are paginated and are sorted by last modified date. If you include an endTime, the endpoint will return data up until that point (exclusive). If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Forms APIs enabled for your organization.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Form Submissions** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.get_form_submissions_stream(
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**form_template_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 50 template IDs to filter data to.
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 50 user IDs to filter data to.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 50 user IDs to filter data to.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of strings indicating whether to return additional information. Valid values: `externalIds`, `fieldLabels`
    
</dd>
</dl>

<dl>
<dd>

**assigned_to_route_stop_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 50 route stop IDs to filter data to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">update_shipping_docs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the shippingDocs field of an existing assignment.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write ELD Hours of Service (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.update_shipping_docs(
    hos_date="hosDate",
    driver_id="driverID",
    shipping_docs="ShippingID1, ShippingID2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**hos_date:** `str` — A start date in yyyy-mm-dd format. Required.
    
</dd>
</dl>

<dl>
<dd>

**driver_id:** `str` — ID of the driver for whom the duty status is being set.
    
</dd>
</dl>

<dl>
<dd>

**shipping_docs:** `str` — ShippingDocs associated with the driver for the day.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">get_issues</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all issues data for the specified IDs. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Forms APIs enabled for your organization.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Issues** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.get_issues()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 100 issue IDs to filter on. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the issue.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma separated list of additional fields to include on requested objects. Valid values: `externalIds`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">patch_issue</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an instance of an issue. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Forms APIs enabled for your organization.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Issues** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.patch_issue(
    id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the issue. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the issue.
    
</dd>
</dl>

<dl>
<dd>

**assigned_to:** `typing.Optional[PatchIssueRequestBodyAssignedToRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[dt.datetime]` — Due date of the issue. UTC timestamp in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[IssuesPatchIssueRequestBodyStatus]` — Status of the issue.  Valid values: `open`, `inProgress`, `resolved`, `dismissed`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">get_issues_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all issues data that has been created or modified for your organization based on the time parameters passed in. Results are paginated and are sorted by last modified date. If you include an endTime, the endpoint will return data up until that point (exclusive). If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Forms APIs enabled for your organization.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Issues** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.get_issues_stream(
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing status values to filter issues on. Valid values: `open`, `inProgress`, `resolved`, `dismissed`
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 50 asset IDs to filter issues on. Issues with untracked assets can also be included by passing the value: 'untracked'.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma separated list of additional fields to include on requested objects. Valid values: `externalIds`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">get_speeding_intervals</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return all speeding intervals associated with trips that have been collected for your organization based on the time parameters passed in. Only completed trips are included. Results are paginated.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Speeding Intervals** under the Speeding Intervals category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.get_speeding_intervals(
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — RFC 3339 timestamp that indicates when to begin receiving data. Value is compared against `updatedAtTime` or `tripStartTime` depending on the queryBy parameter.
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of asset IDs. Include up to 50 asset IDs.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — RFC 3339 timestamp which is compared against `updatedAtTime` or `tripStartTime` depending on the queryBy parameter. If not provided then the endpoint behaves as an unending feed of changes.
    
</dd>
</dl>

<dl>
<dd>

**query_by:** `typing.Optional[BetaGetSpeedingIntervalsRequestQueryBy]` — Decide which timestamp the `startTime` and `endTime` are compared to.  Valid values: `updatedAtTime`, `tripStartTime`
    
</dd>
</dl>

<dl>
<dd>

**include_asset:** `typing.Optional[bool]` — Indicates whether or not to return expanded “asset” data
    
</dd>
</dl>

<dl>
<dd>

**include_driver_id:** `typing.Optional[bool]` — Indicates whether or not to return trip's driver id
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**severity_levels:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma-separated severity levels to filter speeding intervals by. Valid values:  “light”, ”moderate”, ”heavy”, “severe”.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">post_training_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create training assignments. Existing assignments will remain unchanged. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Training APIs enabled for your organization.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Training Assignments** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.post_training_assignments(
    course_id="courseId",
    due_at_time="dueAtTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**course_id:** `str` — String for the course ID.
    
</dd>
</dl>

<dl>
<dd>

**due_at_time:** `str` — Due date of the training assignment in RFC 3339 format. Millisecond precision and timezones are supported.
    
</dd>
</dl>

<dl>
<dd>

**learner_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated learner IDs. If learner ID is present, training assignments for the specified learner(s) will be returned. Max value for this value is 100 objects. Example: `learnerIds=driver-281474,driver-46282156`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">get_training_assignments_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all training assignments data that has been created or modified for your organization based on the time parameters passed in. Results are paginated and are sorted by last modified date. If you include an endTime, the endpoint will return data up until that point (exclusive). If you don't include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Training APIs enabled for your organization.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Training Assignments** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.get_training_assignments_stream(
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**learner_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated learner IDs. If learner ID is present, training assignments for the specified learner(s) will be returned. Max value for this value is 100 objects. Example: `learnerIds=driver-281474,driver-46282156`
    
</dd>
</dl>

<dl>
<dd>

**course_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated course IDs. If course ID is present, training assignments for the specified course ID(s) will be returned. Max value for this value is 100 objects. Defaults to returning all courses. Example: `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated values. If status is present, training assignments for the specified status(s) will be returned. Valid values: "notStarted", "inProgress", "completed". Defaults to returning all courses.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.<a href="src/samsara/beta/client.py">get_trips</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return trips that have been collected for your organization based on the time parameters passed in. Results are paginated. Reach out to your Samsara Representative to have this API enabled for your organization.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Trips** under the Trips category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.get_trips(
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — RFC 3339 timestamp that indicates when to begin receiving data. Value is compared against `updatedAtTime` or `tripStartTime` depending on the queryBy parameter.
    
</dd>
</dl>

<dl>
<dd>

**include_asset:** `typing.Optional[bool]` — Indicates whether or not to return expanded “asset” data
    
</dd>
</dl>

<dl>
<dd>

**completion_status:** `typing.Optional[BetaGetTripsRequestCompletionStatus]` — Filters trips based on a specific completion status  Valid values: `inProgress`, `completed`, `all`
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — RFC 3339 timestamp which is compared against `updatedAtTime` or `tripStartTime` depending on the queryBy parameter. If not provided then the endpoint behaves as an unending feed of changes.
    
</dd>
</dl>

<dl>
<dd>

**query_by:** `typing.Optional[BetaGetTripsRequestQueryBy]` — Decide which timestamp the `startTime` and `endTime` are compared to.  Valid values: `updatedAtTime`, `tripStartTime`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of asset IDs. Include up to 50 asset IDs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Coaching
<details><summary><code>client.coaching.<a href="src/samsara/coaching/client.py">get_driver_assignment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return coach assignments for your organization based on the parameters passed in. Results are paginated.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Coaching** under the Coaching category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.coaching.get_driver_assignment()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated IDs of the drivers. This can be either a unique Samsara driver ID or an external ID for the driver.
    
</dd>
</dl>

<dl>
<dd>

**coach_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated IDs of the coaches.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.coaching.<a href="src/samsara/coaching/client.py">put_driver_assignment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will update an existing or create a new coach-to-driver assignment for your organization based on the parameters passed in. This endpoint should only be used for existing Coach to Driver assignments. In order to remove a driver-coach-assignment for a given driver, set coachId to null

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Coaching** under the Coaching category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.coaching.put_driver_assignment(
    driver_id="driverId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `str` — Required string ID of the driver. This is a unique Samsara ID of a driver.
    
</dd>
</dl>

<dl>
<dd>

**coach_id:** `typing.Optional[str]` — Optional string ID of the coach. This is a unique Samsara user ID. If not provided, existing coach assignment will be removed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.coaching.<a href="src/samsara/coaching/client.py">get_sessions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return coaching sessions for your organization based on the time parameters passed in. Results are paginated by sessions. If you include an endTime, the endpoint will return data up until that point. If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Coaching** under the Coaching category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.coaching.get_sessions(
    start_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `dt.datetime` — Required RFC 3339 timestamp that indicates when to begin receiving data. Value is compared against `updatedAtTime`
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated driver IDs. If driver ID is present, sessions for the specified driver(s) will be returned.
    
</dd>
</dl>

<dl>
<dd>

**coach_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated user IDs. If coach ID is present, sessions for the specified coach(s) will be returned for either assignedCoach or completedCoach. If both driverId(s) and coachId(s) are present, sessions with specified driver(s) and coach(es) will be returned.
    
</dd>
</dl>

<dl>
<dd>

**session_statuses:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated statuses. Valid values:  “upcoming”, “completed”, “deleted”.
    
</dd>
</dl>

<dl>
<dd>

**include_coachable_events:** `typing.Optional[bool]` — Optional boolean to control whether behaviors will include coachableEvents in the response. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[dt.datetime]` — Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an unending feed of changes. If endTime is set the same as startTime, the most recent data point before that time will be returned per asset. Value is compared against `updatedAtTime`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Contacts
<details><summary><code>client.contacts.<a href="src/samsara/contacts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all contacts in an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Alert Contacts** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.contacts.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/samsara/contacts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a contact to the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Alert Contacts** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.contacts.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email address of the contact.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — First name of the contact.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — Last name of the contact.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — Phone number of the contact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/samsara/contacts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific contact's information. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Alert Contacts** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.contacts.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the contact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/samsara/contacts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the given contact. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Alert Contacts** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.contacts.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the contact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/samsara/contacts/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific contact's information. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Alert Contacts** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.contacts.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the contact.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email address of the contact.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — First name of the contact.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — Last name of the contact.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — Phone number of the contact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Maintenance
<details><summary><code>client.maintenance.<a href="src/samsara/maintenance/client.py">get_defect_types</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get DVIR defect types.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Defect Types** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.maintenance.get_defect_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of defect type IDs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/samsara/maintenance/client.py">stream_defects</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream DVIR defects.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Defects** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.maintenance.stream_defects(
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — Required RFC 3339 timestamp to begin the feed or history by `updatedAtTime` at `startTime`.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 200 objects.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an unending feed of changes.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**is_resolved:** `typing.Optional[bool]` — Boolean value for whether filter defects by resolved status.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/samsara/maintenance/client.py">get_dvirs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a history/feed of changed DVIRs by updatedAtTime between startTime and endTime parameters. In case of missing `endTime` parameter it will return a never ending stream of data.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.maintenance.get_dvirs(
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — Required RFC 3339 timestamp to begin the feed or history by `updatedAtTime` at `startTime`.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 200 objects.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an unending feed of changes.
    
</dd>
</dl>

<dl>
<dd>

**safety_status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional list of safety statuses. Valid values: [safe, unsafe, resolved]
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/samsara/maintenance/client.py">get_dvir_defects</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of DVIR defects in an organization, filtered by creation time. The maximum time period you can query for is 30 days. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Defects** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.maintenance.get_dvir_defects(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). *The maximum time period you can query for is 30 days.*
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). *The maximum time period you can query for is 30 days.*
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**is_resolved:** `typing.Optional[bool]` — A filter on the data based on resolution status. Example: `isResolved=true`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/samsara/maintenance/client.py">update_dvir_defect</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a given defect. Can be used to resolve a defect by marking its `isResolved` field to `true`. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Defects** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.maintenance.update_dvir_defect(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the defect.
    
</dd>
</dl>

<dl>
<dd>

**is_resolved:** `typing.Optional[bool]` — Resolves the defect. Must be `true`.
    
</dd>
</dl>

<dl>
<dd>

**mechanic_notes:** `typing.Optional[str]` — The mechanics notes on the defect.
    
</dd>
</dl>

<dl>
<dd>

**resolved_at_time:** `typing.Optional[str]` — Time when defect was resolved. Defaults to now if not provided. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    
</dd>
</dl>

<dl>
<dd>

**resolved_by:** `typing.Optional[ResolvedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/samsara/maintenance/client.py">create_dvir</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new mechanic DVIR in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.maintenance.create_dvir(
    author_id="11",
    safety_status="safe",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**author_id:** `str` — Samsara user ID of the mechanic creating the DVIR.
    
</dd>
</dl>

<dl>
<dd>

**safety_status:** `CreateDvirRequestSafetyStatus` — Whether or not this vehicle or trailer is safe to drive.
    
</dd>
</dl>

<dl>
<dd>

**license_plate:** `typing.Optional[str]` — The license plate of this vehicle.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — Optional string if your jurisdiction requires a location of the DVIR.
    
</dd>
</dl>

<dl>
<dd>

**mechanic_notes:** `typing.Optional[str]` — The mechanics notes on the DVIR.
    
</dd>
</dl>

<dl>
<dd>

**odometer_meters:** `typing.Optional[int]` — The odometer reading in meters.
    
</dd>
</dl>

<dl>
<dd>

**resolved_defect_ids:** `typing.Optional[typing.Sequence[str]]` — Array of ids for defects being resolved with this DVIR.
    
</dd>
</dl>

<dl>
<dd>

**trailer_id:** `typing.Optional[str]` — Id of trailer being inspected. Either vehicleId or trailerId must be provided.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `typing.Optional[str]` — Id of vehicle being inspected. Either vehicleId or trailerId must be provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/samsara/maintenance/client.py">get_dvir_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all DVIRs in an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.maintenance.get_dvir_history(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/samsara/maintenance/client.py">update_dvir</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resolves a given DVIR by marking its `isResolved` field to `true`. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.maintenance.update_dvir(
    id="id",
    author_id="11",
    is_resolved=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the DVIR.
    
</dd>
</dl>

<dl>
<dd>

**author_id:** `str` — The user who is resolving the dvir.
    
</dd>
</dl>

<dl>
<dd>

**is_resolved:** `bool` — Resolves the DVIR. Must be `true`.
    
</dd>
</dl>

<dl>
<dd>

**mechanic_notes:** `typing.Optional[str]` — The mechanics notes on the DVIR.
    
</dd>
</dl>

<dl>
<dd>

**signed_at_time:** `typing.Optional[str]` — Time when user signed this DVIR. Defaults to now. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/samsara/maintenance/client.py">v_1_get_fleet_maintenance_list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get list of the vehicles with any engine faults or check light data. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.maintenance.v_1_get_fleet_maintenance_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DriverQrCodes
<details><summary><code>client.driver_qr_codes.<a href="src/samsara/driver_qr_codes/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for requested driver(s) QR code, used for driver trip assignment.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.driver_qr_codes.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — String of comma separated driver IDs. List of driver - QR codes for specified driver(s) will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.driver_qr_codes.<a href="src/samsara/driver_qr_codes/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assign a new QR code for the requested driver. Return error if an active QR code already exists.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.driver_qr_codes.create(
    driver_id=494123,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `int` — Unique ID of the driver.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.driver_qr_codes.<a href="src/samsara/driver_qr_codes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke requested driver's currently active QR code.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.driver_qr_codes.delete(
    driver_id=494123,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `int` — Unique ID of the driver.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Carrier Proposed Assignments
<details><summary><code>client.carrier_proposed_assignments.<a href="src/samsara/carrier_proposed_assignments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Show the assignments created by the POST fleet/carrier-proposed-assignments. This endpoint will only show the assignments that are active for drivers and currently visible to them in the driver app. Once a proposed assignment has been accepted, the endpoint will not return any data. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Carrier-Proposed Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.carrier_proposed_assignments.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**active_time:** `typing.Optional[str]` — If specified, shows assignments that will be active at this time. Defaults to now, which would show current active assignments. In RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.carrier_proposed_assignments.<a href="src/samsara/carrier_proposed_assignments/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new assignment that a driver can later use. Each driver can only have one future assignment. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Carrier-Proposed Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.carrier_proposed_assignments.create(
    driver_id="42",
    vehicle_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `str` — ID for the driver for the driver that this assignment is for. This can be either a unique Samsara ID or an external ID for the driver.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `str` — ID for the vehicle to propose. This can be either a unique Samsara ID or an external ID for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**active_time:** `typing.Optional[str]` — Time after which this assignment will be active and visible to the driver on the mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    
</dd>
</dl>

<dl>
<dd>

**shipping_docs:** `typing.Optional[str]` — Shipping Documents that this assignment will propose to the driver.
    
</dd>
</dl>

<dl>
<dd>

**trailer_ids:** `typing.Optional[typing.Sequence[str]]` — IDs of trailers to propose. This can be either a unique Samsara IDs or an external IDs for the trailers. (forbidden if trailerNames is set)
    
</dd>
</dl>

<dl>
<dd>

**trailer_names:** `typing.Optional[typing.Sequence[str]]` — Names of trailers to propose. (forbidden if trailerIds is set)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.carrier_proposed_assignments.<a href="src/samsara/carrier_proposed_assignments/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete an assignment. You can only delete assignments that are not yet active. To override a currently active assignment, create a new empty one, instead. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Carrier-Proposed Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.carrier_proposed_assignments.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the assignment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Documents
<details><summary><code>client.documents.<a href="src/samsara/documents/client.py">list_types</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of the organization document types. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getDriverDocumentTypesByOrgId).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.documents.list_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/samsara/documents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all documents for the given time range. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getDriverDocumentsByOrgId).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.documents.list(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**document_type_id:** `typing.Optional[str]` — ID of the document template type.
    
</dd>
</dl>

<dl>
<dd>

**query_by:** `typing.Optional[str]` — Query by document creation time (`created`) or updated time (`updated`). Defaults to `created`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/samsara/documents/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a single document. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/createDriverDocument).

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.documents.create(
    document_type_id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
    driver_id="45646",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_type_id:** `str` — ID for the document type.
    
</dd>
</dl>

<dl>
<dd>

**driver_id:** `str` — ID of the driver. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[FieldObjectPostRequestBody]]` — The fields associated with this document.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the document.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes on the document.
    
</dd>
</dl>

<dl>
<dd>

**route_stop_id:** `typing.Optional[str]` — ID of the route stop. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the route stop.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[DocumentsPostDocumentRequestBodyState]` — The condition of the document created for the driver. Can be either `required` or `submitted`, if no value is specified, `state` defaults to `required`. `required` documents are pre-populated documents for the Driver to fill out in the Driver App.  Valid values: `submitted`, `required`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `typing.Optional[str]` — ID of the vehicle. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/samsara/documents/client.py">create_pdf</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request creation of a document PDF. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.documents.create_pdf(
    document_id="6c8c0c01-206a-41a4-9d21-15b9978d04cb",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `str` — ID of the document.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/samsara/documents/client.py">get_pdf</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns generation job status and download URL for a PDF. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.documents.get_pdf(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the pdf.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/samsara/documents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single document. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getDriverDocumentByIdAndDriverId).

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.documents.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the document
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/samsara/documents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single document. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/deleteDriverDocumentByIdAndDriverId).

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.documents.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the document to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DriverVehicleAssignments
<details><summary><code>client.driver_vehicle_assignments.<a href="src/samsara/driver_vehicle_assignments/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all driver-vehicle assignments for the requested drivers or vehicles in the requested time range. To fetch driver-vehicle assignments out of the vehicle trips' time ranges, assignmentType needs to be specified. Note: this endpoint replaces past endpoints to fetch assignments by driver or by vehicle. Visit [this migration guide](https://developers.samsara.com/docs/migrating-from-driver-vehicle-assignment-or-vehicle-driver-assignment-endpoints) for more information.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.driver_vehicle_assignments.get(
    filter_by="drivers",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter_by:** `DriverVehicleAssignmentsGetRequestFilterBy` — Option to filter by drivers or vehicles.  Valid values: `drivers`, `vehicles`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: "key:value". For example, "maintenanceId:250020".
    
</dd>
</dl>

<dl>
<dd>

**driver_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of driver tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**assignment_type:** `typing.Optional[DriverVehicleAssignmentsGetRequestAssignmentType]` — Specifies which assignment type to filter by.  Valid values: `HOS`, `idCard`, `static`, `faceId`, `tachograph`, `safetyManual`, `RFID`, `trailer`, `external`, `qrCode`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.driver_vehicle_assignments.<a href="src/samsara/driver_vehicle_assignments/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assign vehicle drive-time to a driver via API. For a step-by-step instruction on how to leverage this endpoint, see [this guide](https://developers.samsara.com/docs/creating-driver-vehicle-assignments)

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.driver_vehicle_assignments.create(
    driver_id="494123",
    vehicle_id="281474978683353",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `str` — ID of the driver. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `str` — ID of the vehicle. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**assigned_at_time:** `typing.Optional[str]` — The time at which the assignment was made in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — The end time in RFC 3339 format. Defaults to max-time (meaning it's an ongoing assignment) if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**is_passenger:** `typing.Optional[bool]` — Is this driver a passenger? Defaults to false if not provided
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[PostDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` — The start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.driver_vehicle_assignments.<a href="src/samsara/driver_vehicle_assignments/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete driver assignments that were created using the `POST fleet/driver-vehicle-assignments` endpoint for the requested vehicle in the requested time range.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.driver_vehicle_assignments.delete(
    vehicle_id="281474978683353",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vehicle_id:** `str` — ID of the vehicle. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**assigned_at_time:** `typing.Optional[str]` —  Assigned at time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**is_passenger:** `typing.Optional[bool]` — Indicates if assigned driver is passenger
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.driver_vehicle_assignments.<a href="src/samsara/driver_vehicle_assignments/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update driver assignments that were created using the `POST fleet/driver-vehicle-assignments`. Vehicle Id, Driver Id, and Start Time must match an existing assignment.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.driver_vehicle_assignments.update(
    driver_id="494123",
    start_time="2019-06-13T19:08:25Z",
    vehicle_id="281474978683353",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `str` — ID of the driver. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — The start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `str` — ID of the vehicle. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**assigned_at_time:** `typing.Optional[str]` — The time at which the assignment was made in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — The end time in RFC 3339 format. To make this an ongoing assignment (ie. an assignment with no end time), provide an endTime value of 'null'. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**is_passenger:** `typing.Optional[bool]` — Is this driver a passenger?
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[PatchDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Drivers
<details><summary><code>client.drivers.<a href="src/samsara/drivers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all drivers in organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.drivers.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_activation_status:** `typing.Optional[DriversListRequestDriverActivationStatus]` — If value is `deactivated`, only drivers that are deactivated will appear in the response. This parameter will default to `active` if not provided (fetching only active drivers).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**attribute_value_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of attribute value IDs. Only entities associated with ALL of the referenced values will be returned (i.e. the intersection of the sets of entities with each value). Example: `attributeValueIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**updated_after_time:** `typing.Optional[str]` — A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**created_after_time:** `typing.Optional[str]` — A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drivers.<a href="src/samsara/drivers/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a driver to the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.drivers.create(
    name="Susan Jones",
    password="aSecurePassword1234",
    username="SusanJones",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Driver's name.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — Password that the driver can use to login to the Samsara driver app.
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — Driver's login username into the driver app. The username may not contain spaces or the '@' symbol. The username must be unique.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Sequence[CreateDriverRequestAttributes]]` 
    
</dd>
</dl>

<dl>
<dd>

**carrier_settings:** `typing.Optional[DriverCarrierSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**current_id_card_code:** `typing.Optional[str]` — The ID Card Code on the back of the physical card assigned to the driver.  Contact Samsara if you would like to enable this feature.
    
</dd>
</dl>

<dl>
<dd>

**eld_adverse_weather_exemption_enabled:** `typing.Optional[bool]` — Flag indicating this driver may use Adverse Weather exemptions in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**eld_big_day_exemption_enabled:** `typing.Optional[bool]` — Flag indicating this driver may use Big Day exemption in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**eld_day_start_hour:** `typing.Optional[int]` — `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate noon-to-noon driving hours.
    
</dd>
</dl>

<dl>
<dd>

**eld_exempt:** `typing.Optional[bool]` — Flag indicating this driver is exempt from the Electronic Logging Mandate.
    
</dd>
</dl>

<dl>
<dd>

**eld_exempt_reason:** `typing.Optional[str]` — Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt).
    
</dd>
</dl>

<dl>
<dd>

**eld_pc_enabled:** `typing.Optional[bool]` — Flag indicating this driver may select the Personal Conveyance duty status in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**eld_ym_enabled:** `typing.Optional[bool]` — Flag indicating this driver may select the Yard Move duty status in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    
</dd>
</dl>

<dl>
<dd>

**has_driving_features_hidden:** `typing.Optional[DriverHasDrivingFeaturesHidden]` 
    
</dd>
</dl>

<dl>
<dd>

**hos_setting:** `typing.Optional[DriverHosSetting]` 
    
</dd>
</dl>

<dl>
<dd>

**license_number:** `typing.Optional[str]` — Driver's state issued license number. The combination of this number and `licenseState` must be unique.
    
</dd>
</dl>

<dl>
<dd>

**license_state:** `typing.Optional[str]` — Abbreviation of US state, Canadian province, or US territory that issued driver's license.
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[CreateDriverRequestLocale]` — Locale override (uncommon). These are specified by ISO 3166-2 country codes for supported locales. Valid values: `us`, `at`, `be`, `ca`, `gb`, `fr`, `de`, `ie`, `it`, `lu`, `mx`, `nl`, `es`, `ch`, `pr`.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about the driver.
    
</dd>
</dl>

<dl>
<dd>

**peer_group_tag_id:** `typing.Optional[str]` — The peer group tag id this driver belong to, used for gamification.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — Phone number of the driver.
    
</dd>
</dl>

<dl>
<dd>

**static_assigned_vehicle_id:** `typing.Optional[str]` — ID of vehicle that the driver is permanently assigned to. (uncommon).
    
</dd>
</dl>

<dl>
<dd>

**tachograph_card_number:** `typing.Optional[str]` — Driver's assigned tachograph card number (Europe specific)
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — IDs of tags the driver is associated with. If your access to the API is scoped by one or more tags, this field is required to pass in.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. Driver timezones use [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).
    
</dd>
</dl>

<dl>
<dd>

**us_driver_ruleset_override:** `typing.Optional[UsDriverRulesetOverride]` 
    
</dd>
</dl>

<dl>
<dd>

**vehicle_group_tag_id:** `typing.Optional[str]` — Tag ID which determines which vehicles a driver will see when selecting vehicles.
    
</dd>
</dl>

<dl>
<dd>

**waiting_time_duty_status_enabled:** `typing.Optional[bool]` — Flag indicating this driver may select waiting time duty status in ELD logs
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drivers.<a href="src/samsara/drivers/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a driver. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.drivers.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drivers.<a href="src/samsara/drivers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific driver's information. This can also be used to activate or de-activate a given driver by setting the driverActivationStatus field. If the driverActivationStatus field is 'deactivated' then the user can also specify the deactivatedAtTime. The deactivatedAtTime cannot be more than 6 months in the past and must not come before the dirver's latest active HOS log. It will be considered an error if deactivatedAtTime is provided with a driverActivationStatus of active. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.drivers.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Sequence[CreateDriverRequestAttributes]]` 
    
</dd>
</dl>

<dl>
<dd>

**carrier_settings:** `typing.Optional[DriverCarrierSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**current_id_card_code:** `typing.Optional[str]` — The ID Card Code on the back of the physical card assigned to the driver.  Contact Samsara if you would like to enable this feature.
    
</dd>
</dl>

<dl>
<dd>

**deactivated_at_time:** `typing.Optional[str]` — The date and time this driver is considered to be deactivated in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**driver_activation_status:** `typing.Optional[UpdateDriverRequestDriverActivationStatus]` — A value indicating whether the driver is active or deactivated. Valid values: `active`, `deactivated`.
    
</dd>
</dl>

<dl>
<dd>

**eld_adverse_weather_exemption_enabled:** `typing.Optional[bool]` — Flag indicating this driver may use Adverse Weather exemptions in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**eld_big_day_exemption_enabled:** `typing.Optional[bool]` — Flag indicating this driver may use Big Day exemption in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**eld_day_start_hour:** `typing.Optional[int]` — `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate noon-to-noon driving hours.
    
</dd>
</dl>

<dl>
<dd>

**eld_exempt:** `typing.Optional[bool]` — Flag indicating this driver is exempt from the Electronic Logging Mandate.
    
</dd>
</dl>

<dl>
<dd>

**eld_exempt_reason:** `typing.Optional[str]` — Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt).
    
</dd>
</dl>

<dl>
<dd>

**eld_pc_enabled:** `typing.Optional[bool]` — Flag indicating this driver may select the Personal Conveyance duty status in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**eld_ym_enabled:** `typing.Optional[bool]` — Flag indicating this driver may select the Yard Move duty status in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    
</dd>
</dl>

<dl>
<dd>

**has_driving_features_hidden:** `typing.Optional[DriverHasDrivingFeaturesHidden]` 
    
</dd>
</dl>

<dl>
<dd>

**hos_setting:** `typing.Optional[UpdateDriverRequestHosSetting]` 
    
</dd>
</dl>

<dl>
<dd>

**license_number:** `typing.Optional[str]` — Driver's state issued license number. The combination of this number and `licenseState` must be unique.
    
</dd>
</dl>

<dl>
<dd>

**license_state:** `typing.Optional[str]` — Abbreviation of US state, Canadian province, or US territory that issued driver's license.
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[UpdateDriverRequestLocale]` — Locale override (uncommon). These are specified by ISO 3166-2 country codes for supported locales. Valid values: `us`, `at`, `be`, `ca`, `gb`, `fr`, `de`, `ie`, `it`, `lu`, `mx`, `nl`, `es`, `ch`, `pr`.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Driver's name.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about the driver.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Password that the driver can use to login to the Samsara driver app.
    
</dd>
</dl>

<dl>
<dd>

**peer_group_tag_id:** `typing.Optional[str]` — The peer group tag id this driver belong to, leave blank to be in group with everyone, used for gamification.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — Phone number of the driver.
    
</dd>
</dl>

<dl>
<dd>

**static_assigned_vehicle_id:** `typing.Optional[str]` — ID of vehicle that the driver is permanently assigned to. (uncommon).
    
</dd>
</dl>

<dl>
<dd>

**tachograph_card_number:** `typing.Optional[str]` — Driver's assigned tachograph card number (Europe specific)
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — IDs of tags the driver is associated with. If your access to the API is scoped by one or more tags, this field is required to pass in.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. Driver timezones use [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).
    
</dd>
</dl>

<dl>
<dd>

**us_driver_ruleset_override:** `typing.Optional[UsDriverRulesetOverride]` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Driver's login username into the driver app. The username may not contain spaces or the '@' symbol. The username must be unique.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_group_tag_id:** `typing.Optional[str]` — Tag ID which determines which vehicles a driver will see when selecting vehicles.
    
</dd>
</dl>

<dl>
<dd>

**waiting_time_duty_status_enabled:** `typing.Optional[bool]` — Flag indicating this driver may select waiting time duty status in ELD logs
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TachographEuOnly
<details><summary><code>client.tachograph_eu_only.<a href="src/samsara/tachograph_eu_only/client.py">get_driver_tachograph_activity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all known tachograph activity for all specified drivers in the time range. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tachograph (EU)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.tachograph_eu_only.get_driver_tachograph_activity(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. It can't be more than 30 days past startTime. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tachograph_eu_only.<a href="src/samsara/tachograph_eu_only/client.py">get_driver_tachograph_files</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all known tachograph files for all specified drivers in the time range. 

 <b>Rate limit:</b> 50 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tachograph (EU)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.tachograph_eu_only.get_driver_tachograph_files(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tachograph_eu_only.<a href="src/samsara/tachograph_eu_only/client.py">get_tachograph_files</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all known tachograph files for all specified vehicles in the time range. 

 <b>Rate limit:</b> 150 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tachograph (EU)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.tachograph_eu_only.get_tachograph_files(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Legacy
<details><summary><code>client.legacy.<a href="src/samsara/legacy/client.py">get_drivers_vehicle_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Note: This is a legacy endpoint, consider using [this endpoint](https://developers.samsara.com/reference/getdrivervehicleassignments) instead. The endpoint will continue to function as documented.** Get all vehicle assignments for the requested drivers in the requested time range. The only type of assignment supported right now are assignments created through the driver app.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.legacy.get_drivers_vehicle_assignments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). The maximum allowed startTime-endTime range is 7 days.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). The maximum allowed startTime-endTime range is 7 days.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of driver tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of driver parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**driver_activation_status:** `typing.Optional[LegacyGetDriversVehicleAssignmentsRequestDriverActivationStatus]` — If value is `deactivated`, only drivers that are deactivated will appear in the response. This parameter will default to `active` if not provided (fetching only active drivers).  Valid values: `active`, `deactivated`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.legacy.<a href="src/samsara/legacy/client.py">get_vehicles_driver_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Note: This is a legacy endpoint, consider using [this endpoint](https://developers.samsara.com/reference/getdrivervehicleassignments) instead. The endpoint will continue to function as documented.** Get all driver assignments for the requested vehicles in the requested time range. The only type of assignment supported right now are assignments created through the driver app.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.legacy.get_vehicles_driver_assignments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). The maximum allowed startTime-endTime range is 7 days.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). The maximum allowed startTime-endTime range is 7 days.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Equipment
<details><summary><code>client.equipment.<a href="src/samsara/equipment/client.py">list_equipment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all equipment in an organization. Equipment objects represent powered assets connected to a [Samsara AG26](https://www.samsara.com/products/models/ag26) via an APWR, CAT, or J1939 cable. They are automatically created with a unique Samsara Equipment ID whenever an AG26 is activated in your organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.equipment.list_equipment()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.equipment.<a href="src/samsara/equipment/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the unit of equipment with the given Samsara ID. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.equipment.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Samsara ID of the Equipment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Hours of Service
<details><summary><code>client.hours_of_service.<a href="src/samsara/hours_of_service/client.py">get_clocks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current HOS status for all drivers. Note that this includes inactive as well as active drivers. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getFleetHosLogsSummary). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.hours_of_service.get_clocks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hours_of_service.<a href="src/samsara/hours_of_service/client.py">get_daily_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get summarized daily Hours of Service charts for the specified drivers.

The time range for a log is defined by the `driver`'s `eldDayStartHour`. This value is configurable per driver.

The `startDate` and `endDate` parameters indicate the date range you'd like to retrieve daily logs for. A daily log will be returned if its `startTime` is on any of the days within in this date range (inclusive of `startDate` and `endDate`).

**Note:** If data is still being uploaded from the Samsara Driver App, it may not be completely reflected in the response from this endpoint. The best practice is to wait a couple of days before querying this endpoint to make sure that all data from the Samsara Driver App has been uploaded.

If you are using the legacy version of this endpoint and looking for its documentation, you can find it [here](https://www.samsara.com/api-legacy#operation/getFleetDriversHosDailyLogs).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.hours_of_service.get_daily_logs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` —  A start date in YYYY-MM-DD. This is a date only without an associated time. Example: `2019-06-13`. This is a required field
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` —  An end date in YYYY-MM-DD. This is a date only without an associated time. Must be greater than or equal to the start date. Example: `2019-07-21`. This is a required field
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**driver_activation_status:** `typing.Optional[HoursOfServiceGetDailyLogsRequestDriverActivationStatus]` — If value is `deactivated`, only drivers that are deactivated will appear in the response. This parameter will default to `active` if not provided (fetching only active drivers).  Valid values: `active`, `deactivated`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Literal["vehicle"]]` 

Expands the specified value(s) in the response object. Expansion populates additional fields in an object, if supported. Unsupported fields are ignored. To expand multiple fields, input a comma-separated list.

Valid value: `vehicle`  Valid values: `vehicle`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hours_of_service.<a href="src/samsara/hours_of_service/client.py">get_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns HOS logs between a given `startTime` and `endTime`. The logs can be further filtered using tags or by providing a list of driver IDs (including external IDs). The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getFleetHosLogs).

**Note:** If data is still being uploaded from the Samsara Driver App, it may not be completely reflected in the response from this endpoint. The best practice is to wait a couple of days before querying this endpoint to make sure that all data from the Samsara Driver App has been uploaded. 

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.hours_of_service.get_logs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` — A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hours_of_service.<a href="src/samsara/hours_of_service/client.py">get_violations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get active Hours of Service violations for the specified drivers.

The day object time range for a violation is defined by the `driver`'s `eldDayStartHour`. This value is configurable per driver.

The `startTime` and `endTime` parameters indicate the datetime range you'd like to retrieve violations for. A violation will be returned if its `violationStartTime` falls within this datetime range (inclusive of `startTime` and `endTime`) 

**Note:** The following are all the violation types with a short explanation about what each of them means: `californiaMealbreakMissed` (Missed California Meal Break), `cycleHoursOn` (Cycle Limit), `cycleOffHoursAfterOnDutyHours` (Cycle 2 Limit), `dailyDrivingHours` (Daily Driving Limit), `dailyOffDutyDeferralAddToDay2Consecutive` (Daily Off-Duty Deferral: Add To Day2 Consecutive), `dailyOffDutyDeferralNotPartMandatory` (Daily Off-Duty Deferral: Not Part Of Mandatory), `dailyOffDutyDeferralTwoDayDrivingLimit` (Daily Off-Duty Deferral: 2 Day Driving Limit), `dailyOffDutyDeferralTwoDayOffDuty` (Daily Off-Duty Deferral: 2 Day Off Duty), `dailyOffDutyNonResetHours` (Daily Off-Duty Time: Non-Reset), `dailyOffDutyTotalHours` (Daily Off-Duty Time), `dailyOnDutyHours` (Daily On-Duty Limit), `mandatory24HoursOffDuty` (24 Hours of Off Duty required), `restbreakMissed` (Missed Rest Break), `shiftDrivingHours` (Shift Driving Limit), `shiftHours` (Shift Duty Limit), `shiftOnDutyHours` (Shift On-Duty Limit), `unsubmittedLogs` (Missing Driver Certification)

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.hours_of_service.get_violations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on violations data based on the violation type enum. Supported types: `NONE, californiaMealbreakMissed, cycleHoursOn, cycleOffHoursAfterOnDutyHours, dailyDrivingHours, dailyOffDutyDeferralAddToDay2Consecutive, dailyOffDutyDeferralNotPartMandatory, dailyOffDutyDeferralTwoDayDrivingLimit, dailyOffDutyDeferralTwoDayOffDuty, dailyOffDutyNonResetHours, dailyOffDutyTotalHours, dailyOnDutyHours, mandatory24HoursOffDuty, restbreakMissed, shiftDrivingHours, shiftHours, shiftOnDutyHours, unsubmittedLogs`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hours_of_service.<a href="src/samsara/hours_of_service/client.py">set_current_duty_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Set an individual driver’s current duty status to 'On Duty' or 'Off Duty'.

 To ensure compliance with the ELD Mandate, only  authenticated drivers can make direct duty status changes on their own logbook. Any system external to the Samsara Driver App using this endpoint to trigger duty status changes must ensure that such changes are only triggered directly by the driver in question and that the driver has been properly authenticated. This endpoint should not be used to algorithmically trigger duty status changes nor should it be used by personnel besides the driver to trigger duty status changes on the driver’s behalf. Carriers and their drivers are ultimately responsible for maintaining accurate logs and should confirm that their use of the endpoint is compliant with the ELD Mandate. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write ELD Hours of Service (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.hours_of_service.set_current_duty_status(
    driver_id=1000000,
    duty_status="ON_DUTY",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `int` — ID of the driver for whom the duty status is being set.
    
</dd>
</dl>

<dl>
<dd>

**duty_status:** `str` — Duty status to set the driver to. The only supported values are 'ON_DUTY' and 'OFF_DUTY'.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — Location to associate the duty status change with.
    
</dd>
</dl>

<dl>
<dd>

**remark:** `typing.Optional[str]` — Remark to associate the duty status change with.
    
</dd>
</dl>

<dl>
<dd>

**status_change_at_ms:** `typing.Optional[int]` — Timestamp that the duty status will begin at specified in milliseconds UNIX time. Defaults to the current time if left blank. This can only be set to up to 8 hours in the past.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `typing.Optional[int]` — Vehicle ID to associate the duty status change with.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hours_of_service.<a href="src/samsara/hours_of_service/client.py">v_1_get_fleet_hos_authentication_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get the HOS (hours of service) signin and signout logs for the specified driver. The response includes 4 fields that are now deprecated.

**Note:** If data is still being uploaded from the Samsara Driver App, it may not be completely reflected in the response from this endpoint. The best practice is to wait a couple of days before querying this endpoint to make sure that all data from the Samsara Driver App has been uploaded. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read ELD Hours of Service (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.hours_of_service.v_1_get_fleet_hos_authentication_logs(
    driver_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `int` — Driver ID to query.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Beginning of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — End of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FuelAndEnergy
<details><summary><code>client.fuel_and_energy.<a href="src/samsara/fuel_and_energy/client.py">get_driver_reports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get fuel and energy efficiency driver reports for the requested time range.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.fuel_and_energy.get_driver_reports(
    start_date="startDate",
    end_date="endDate",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `str` — A start date in RFC 3339 format. This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time zone is passed in, then the UTC time zone will be used. This parameter is inclusive, so data on the date specified will be considered. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `str` — An end date in RFC 3339 format. This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time zone is passed in, then the UTC time zone will be used. This parameter is inclusive, so data on the date specified will be considered. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fuel_and_energy.<a href="src/samsara/fuel_and_energy/client.py">get_vehicle_reports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get fuel and energy efficiency vehicle reports for the requested time range.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.fuel_and_energy.get_vehicle_reports(
    start_date="startDate",
    end_date="endDate",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `str` — A start date in RFC 3339 format. This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time zone is passed in, then the UTC time zone will be used. This parameter is inclusive, so data on the date specified will be considered. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `str` — An end date in RFC 3339 format. This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time zone is passed in, then the UTC time zone will be used. This parameter is inclusive, so data on the date specified will be considered. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**energy_type:** `typing.Optional[FuelAndEnergyGetVehicleReportsRequestEnergyType]` — The type of energy used by the vehicle.  Valid values: `fuel`, `hybrid`, `electric`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fuel_and_energy.<a href="src/samsara/fuel_and_energy/client.py">post_fuel_purchase</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a fuel purchase transaction.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Fuel Purchase** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import PostFuelPurchaseRequestBodyPriceRequestBody, Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.fuel_and_energy.post_fuel_purchase(
    fuel_quantity_liters="676.8",
    transaction_location="350 Rhode Island St, San Francisco, CA 94103",
    transaction_price=PostFuelPurchaseRequestBodyPriceRequestBody(
        amount="640.2",
        currency="usd",
    ),
    transaction_reference="5454534",
    transaction_time="2022-07-13T14:20:50.52-07:00",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fuel_quantity_liters:** `str` — The amount of fuel purchased in liters.
    
</dd>
</dl>

<dl>
<dd>

**transaction_location:** `str` — The full street address for the location of the fuel transaction, as it might be recognized by Google Maps. Ideal entries should be in accordance with the format used by the national postal service of the country concerned (example: 1 De Haro St, San Francisco, CA 94107, United States). Alternatively, exact latitude/longitude can be provided (example: 40.748441, -73.985664).
    
</dd>
</dl>

<dl>
<dd>

**transaction_price:** `PostFuelPurchaseRequestBodyPriceRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_reference:** `str` — The fuel transaction reference. This is the transaction identifier. For instance, this can be the Serial Number on the invoice.
    
</dd>
</dl>

<dl>
<dd>

**transaction_time:** `str` — The time of the fuel transaction in RFC 3339 format. Timezone must be specified. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.
    
</dd>
</dl>

<dl>
<dd>

**ifta_fuel_type:** `typing.Optional[FuelPurchasePostFuelPurchaseRequestBodyIftaFuelType]` — The type of fuel purchased supported by IFTA.  Valid values: `Unspecified`, `A55`, `Biodiesel`, `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`, `Other`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `typing.Optional[str]` — Samsara ID of the vehicle that purchased the fuel.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Ifta
<details><summary><code>client.ifta.<a href="src/samsara/ifta/client.py">get_jurisdiction_reports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all jurisdiction IFTA reports for the requested time duration. Data is returned in your organization's defined timezone.

**Note:** The most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read IFTA (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.ifta.get_jurisdiction_reports(
    year=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**year:** `int` —  The year of the requested IFTA report summary. Must be provided with a month or quarter param. Example: `year=2021`
    
</dd>
</dl>

<dl>
<dd>

**month:** `typing.Optional[IftaGetJurisdictionReportsRequestMonth]` —  The month of the requested IFTA report summary. Can not be provided with the quarter param. Example: `month=January`  Valid values: `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`
    
</dd>
</dl>

<dl>
<dd>

**quarter:** `typing.Optional[IftaGetJurisdictionReportsRequestQuarter]` —  The quarter of the requested IFTA report summary. Can not be provided with the month param. Q1: January, February, March. Q2: April, May, June. Q3: July, August, September. Q4: October, November, December. Example: `quarter=Q1`  Valid values: `Q1`, `Q2`, `Q3`, `Q4`
    
</dd>
</dl>

<dl>
<dd>

**jurisdictions:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of jurisdictions. Example: `jurisdictions=GA`
    
</dd>
</dl>

<dl>
<dd>

**fuel_type:** `typing.Optional[IftaGetJurisdictionReportsRequestFuelType]` —  A filter on the data based on this comma-separated list of IFTA fuel types. Example: `fuelType=Diesel`  Valid values: `Unspecified`, `A55`, `Biodiesel`, `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`, `Other`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ifta.<a href="src/samsara/ifta/client.py">get_vehicle_reports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all vehicle IFTA reports for the requested time duration. Data is returned in your organization's defined timezone.

**Note:** The most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read IFTA (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.ifta.get_vehicle_reports(
    year=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**year:** `int` —  The year of the requested IFTA report summary. Must be provided with a month or quarter param. Example: `year=2021`
    
</dd>
</dl>

<dl>
<dd>

**month:** `typing.Optional[IftaGetVehicleReportsRequestMonth]` —  The month of the requested IFTA report summary. Can not be provided with the quarter param. Example: `month=January`  Valid values: `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`
    
</dd>
</dl>

<dl>
<dd>

**quarter:** `typing.Optional[IftaGetVehicleReportsRequestQuarter]` —  The quarter of the requested IFTA report summary. Can not be provided with the month param. Q1: January, February, March. Q2: April, May, June. Q3: July, August, September. Q4: October, November, December. Example: `quarter=Q1`  Valid values: `Q1`, `Q2`, `Q3`, `Q4`
    
</dd>
</dl>

<dl>
<dd>

**jurisdictions:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of jurisdictions. Example: `jurisdictions=GA`
    
</dd>
</dl>

<dl>
<dd>

**fuel_type:** `typing.Optional[IftaGetVehicleReportsRequestFuelType]` —  A filter on the data based on this comma-separated list of IFTA fuel types. Example: `fuelType=Diesel`  Valid values: `Unspecified`, `A55`, `Biodiesel`, `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`, `Other`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ifta.<a href="src/samsara/ifta/client.py">create_detail_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a job to generate csv files of IFTA mileage segments.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write IFTA (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.ifta.create_detail_job(
    end_hour="2019-06-13T19:00:00Z",
    start_hour="2019-06-13T19:00:00Z",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_hour:** `str` —  An end time in RFC 3339 format. Hour precision and timezones are supported. Any minutes or seconds will be truncated down to the nearest hour. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. The maximum request duration is 1 month. Limit the number of vehicles to 1000 when requesting more than 24 hours of data. (Examples: 2019-06-13T19:00:00Z, 2019-06-13T19:00:00.000Z, OR 2015-09-15T14:00:00-04:00).
    
</dd>
</dl>

<dl>
<dd>

**start_hour:** `str` —  A start time in RFC 3339 format. Hour precision and timezones are supported. Any minutes or seconds will be truncated down to the nearest hour. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. The maximum request duration is 1 month. Limit the number of vehicles to 1000 when requesting more than 24 hours of data. (Examples: 2019-06-13T19:00:00Z, 2019-06-13T19:00:00.000Z, OR 2015-09-15T14:00:00-04:00).
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` — A filter on the data based on this comma-separated list of vehicle IDs and external IDs. The number of vehicles requested per job shouldn't exceed 5000. Example: `vehicleIds: '1234,5678,samsara.vin:1HGBH41JXMN109186'`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle parent tag IDs. The number of vehicles requested per job shouldn't exceed 5000. Example: `vehicleParentTagIds: '1234,5678'`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle tag IDs. The number of vehicles requested per job shouldn't exceed 5000. Example: `vehicleTagIds: '1234,5678'`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ifta.<a href="src/samsara/ifta/client.py">get_detail_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about an existing IFTA detail job.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read IFTA (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.ifta.get_detail_job(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the requested job.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Idling
<details><summary><code>client.idling.<a href="src/samsara/idling/client.py">get_vehicle_reports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all vehicle idling reports for the requested time duration.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.idling.get_vehicle_reports(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**is_pto_active:** `typing.Optional[bool]` — A filter on the data based on power take-off being active or inactive.
    
</dd>
</dl>

<dl>
<dd>

**min_idling_duration_minutes:** `typing.Optional[int]` — A filter on the data based on a minimum idling duration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Routes
<details><summary><code>client.routes.<a href="src/samsara/routes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns multiple routes. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/fetchAllDispatchRoutes).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.routes.list(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.routes.<a href="src/samsara/routes/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a route. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/createDispatchRoute).

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import CreateRoutesStopRequestObjectRequestBody, Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.routes.create(
    name="Bid 123",
    stops=[CreateRoutesStopRequestObjectRequestBody()],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name for the route
    
</dd>
</dl>

<dl>
<dd>

**stops:** `typing.Sequence[CreateRoutesStopRequestObjectRequestBody]` — List of stops along the route. For each stop, exactly one of `addressId` and `singleUseLocation` are required. Depending on the `settings` on your route, either a `scheduledArrivalTime` or `scheduledDepartureTime` must be specified for the first job.
    
</dd>
</dl>

<dl>
<dd>

**driver_id:** `typing.Optional[str]` — ID of the driver. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about the route.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RouteSettingsRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `typing.Optional[str]` — ID of the vehicle. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.routes.<a href="src/samsara/routes/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single route. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getDispatchRouteById).

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.routes.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the route. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.routes.<a href="src/samsara/routes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a dispatch route and its associated stops.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.routes.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the route. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.routes.<a href="src/samsara/routes/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a route.  **Note** this implementation of patch uses [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
 This means that any fields included in the patch request will _overwrite_ fields which exist on the target resource.
 For arrays, this means any array included in the request will _replace_ the array that exists at the specified path, it will not _add_ to the existing array.

The legacy version of this endpoint (which uses PUT instead of PATCH) can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/updateDispatchRouteById).

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.routes.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the route. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
    
</dd>
</dl>

<dl>
<dd>

**driver_id:** `typing.Optional[str]` — ID of the driver. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name for the route
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about the route.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RouteSettingsRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**stops:** `typing.Optional[typing.Sequence[UpdateRoutesStopRequestObjectRequestBody]]` — List of stops along the route. If a valid `id` of a stop is provided, that stop will be updated. If no `id` is provided for a passed in stop, that stop will be created. If `id` value are passed in for some stops and not for others, those with `id` value specified will be retained and updated in the original route, those without `id` value specified in the body will be created, and those without `id` value specified that already existed on the route will be deleted. For each new stop, exactly one of `addressId` and `singleUseLocation` are required. Depending on the `settings` on your route, either a `scheduledArrivalTime` or `scheduledDepartureTime` must be specified for the first job, if a new first job is being added.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `typing.Optional[str]` — ID of the vehicle. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Safety
<details><summary><code>client.safety.<a href="src/samsara/safety/client.py">list_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch safety events for the organization in a given time period. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.safety.list_events(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.safety.<a href="src/samsara/safety/client.py">get_activity_event_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get continuous safety events. The safety activity event feed offers a change-log for safety events. Use this endpoint to subscribe to safety event changes. See documentation below for all supported change-log types.

| ActivityType      | Description |
| ----------- | ----------- |
| CreateSafetyEventActivityType | a new safety event is processed by Samsara      |
| BehaviorLabelActivityType     | a label is added or removed from a safety event |
| CoachingStateActivityType     | a safety event coaching state is updated        |

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.safety.get_activity_event_feed()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.safety.<a href="src/samsara/safety/client.py">get_driver_safety_score</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch the safety score for the driver.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.safety.get_driver_safety_score(
    driver_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `int` — ID of the driver. Must contain only digits 0-9.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.safety.<a href="src/samsara/safety/client.py">get_harsh_event</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch harsh event details for a vehicle. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.safety.get_harsh_event(
    vehicle_id=1000000,
    timestamp=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vehicle_id:** `int` — ID of the vehicle. Must contain only digits 0-9.
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `int` — Timestamp in milliseconds representing the timestamp of a harsh event.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.safety.<a href="src/samsara/safety/client.py">get_vehicle_safety_score</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch the safety score for the vehicle. 

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.safety.get_vehicle_safety_score(
    vehicle_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vehicle_id:** `int` — ID of the vehicle. Must contain only digits 0-9.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Settings
<details><summary><code>client.settings.<a href="src/samsara/settings/client.py">get_compliance</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get organization's compliance settings, including carrier name, office address, and DOT number

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.settings.get_compliance()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.settings.<a href="src/samsara/settings/client.py">patch_compliance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update organization's compliance settings, including carrier name, office address, and DOT number

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.settings.patch_compliance()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**allow_unregulated_vehicles_enabled:** `typing.Optional[bool]` — [deprecated] Allow Unregulated Vehicles. This setting is deprecated as all organizations can now mark vehicles as unregulated.
    
</dd>
</dl>

<dl>
<dd>

**canada_hos_enabled:** `typing.Optional[bool]` — Enable Canada HOS
    
</dd>
</dl>

<dl>
<dd>

**carrier_name:** `typing.Optional[str]` — Carrier Name / Principal Place of Business Name
    
</dd>
</dl>

<dl>
<dd>

**dot_number:** `typing.Optional[int]` — Carrier US DOT Number
    
</dd>
</dl>

<dl>
<dd>

**driver_auto_duty_enabled:** `typing.Optional[bool]` — Enable Driver Auto-Duty
    
</dd>
</dl>

<dl>
<dd>

**edit_certified_logs_enabled:** `typing.Optional[bool]` — Drivers Can Edit Certified Log
    
</dd>
</dl>

<dl>
<dd>

**force_manual_location_for_duty_status_changes_enabled:** `typing.Optional[bool]` — Force Manual Location For Duty Status Changes
    
</dd>
</dl>

<dl>
<dd>

**force_review_unassigned_hos_enabled:** `typing.Optional[bool]` — Force Review of Unassigned HOS
    
</dd>
</dl>

<dl>
<dd>

**main_office_formatted_address:** `typing.Optional[str]` — Main Office Address / Principal Place of Businesss Address
    
</dd>
</dl>

<dl>
<dd>

**persistent_duty_status_enabled:** `typing.Optional[bool]` — Persistent Duty Status
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.settings.<a href="src/samsara/settings/client.py">get_driver_app</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get driver app settings.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Driver App Settings** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.settings.get_driver_app()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.settings.<a href="src/samsara/settings/client.py">patch_driver_app</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update driver app settings.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Driver App Settings** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.settings.patch_driver_app()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_fleet_id:** `typing.Optional[str]` — Global login user name for the fleet driver app
    
</dd>
</dl>

<dl>
<dd>

**gamification:** `typing.Optional[bool]` — Driver gamification feature. Enabling this will turn on the feature for all drivers using the mobile app. Drivers can be configured into peer groups within the Drivers Page. Unconfigured drivers will be grouped on an organization level.
    
</dd>
</dl>

<dl>
<dd>

**gamification_config:** `typing.Optional[DriverAppSettingsGamificationConfigTinyObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**org_vehicle_search:** `typing.Optional[bool]` — Allow drivers to search for vehicles outside of their selection tag when connected to the internet.
    
</dd>
</dl>

<dl>
<dd>

**trailer_selection:** `typing.Optional[bool]` — Allow drivers to see and select trailers in the Samsara Driver app. 
    
</dd>
</dl>

<dl>
<dd>

**trailer_selection_config:** `typing.Optional[DriverAppSettingsTrailerSelectionConfigTinyObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.settings.<a href="src/samsara/settings/client.py">get_safety</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get safety settings

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.settings.get_safety()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Trailers
<details><summary><code>client.trailers.<a href="src/samsara/trailers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all trailers.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.trailers.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trailers.<a href="src/samsara/trailers/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new trailer asset.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.trailers.create(
    name="Trailer-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The human-readable name of the Trailer. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Sequence[GoaAttributeTinyRequestBody]]` — A list of attributes to assign to the trailer.
    
</dd>
</dl>

<dl>
<dd>

**enabled_for_mobile:** `typing.Optional[bool]` — Indicates if the trailer is visible on the Samsara mobile apps.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**license_plate:** `typing.Optional[str]` — The license plate of the Trailer. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — These are generic notes about the Trailer. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this trailer. If your access to the API is scoped by one or more tags, this field is required to pass in.
    
</dd>
</dl>

<dl>
<dd>

**trailer_serial_number:** `typing.Optional[str]` — The serial number of the trailer.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trailers.<a href="src/samsara/trailers/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a trailer with given ID.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.trailers.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the trailer. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: "key:value". For example, "maintenanceId:250020".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trailers.<a href="src/samsara/trailers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a trailer with the given ID.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.trailers.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the trailer to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trailers.<a href="src/samsara/trailers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a trailer.  **Note** this implementation of patch uses [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
 This means that any fields included in the patch request will _overwrite_ fields which exist on the target resource.
 For arrays, this means any array included in the request will _replace_ the array that exists at the specified path, it will not _add_ to the existing array

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.trailers.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the trailer. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the trailer.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Sequence[GoaAttributeTinyRequestBody]]` — A list of attributes to assign to the trailer.
    
</dd>
</dl>

<dl>
<dd>

**enabled_for_mobile:** `typing.Optional[bool]` — Indicates if the trailer is visible on the Samsara mobile apps.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**license_plate:** `typing.Optional[str]` — The license plate of the Trailer. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The human-readable name of the Trailer. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — These are generic notes about the Trailer. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**odometer_meters:** `typing.Optional[int]` — When you provide a manual odometer override, Samsara will begin updating a trailer's odometer using GPS distance traveled since this override was set. Only applies to trailers installed with Samsara gateways.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this trailer. If your access to the API is scoped by one or more tags, this field is required to pass in.
    
</dd>
</dl>

<dl>
<dd>

**trailer_serial_number:** `typing.Optional[str]` — The serial number of the trailer.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Vehicles
<details><summary><code>client.vehicles.<a href="src/samsara/vehicles/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all vehicles.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Vehicles** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.vehicles.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**attribute_value_ids:** `typing.Optional[str]` — A filter on the data based on this comma-separated list of attribute value IDs. Only entities associated with ALL of the referenced values will be returned (i.e. the intersection of the sets of entities with each value). Example: `attributeValueIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**updated_after_time:** `typing.Optional[str]` —  A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**created_after_time:** `typing.Optional[str]` —  A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/samsara/vehicles/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific vehicle. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicles** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.vehicles.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource, or automatically populated by fields on the vehicle. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.vin:1HGBH41JXMN109186`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicles.<a href="src/samsara/vehicles/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the given Vehicle object.

**Note:** Vehicle objects are automatically created when Samsara Vehicle Gateways are installed. You cannot create a Vehicle object via API.

You are able to *update* many of the fields of a Vehicle.

**Note**: There are no required fields in the request body, and you only need to provide the fields you wish to update. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Vehicles** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.vehicles.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource, or automatically populated by fields on the vehicle. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.vin:1HGBH41JXMN109186`.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Sequence[AttributeTiny]]` 
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_1:** `typing.Optional[UpdateVehicleRequestAuxInputType1]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_10:** `typing.Optional[UpdateVehicleRequestAuxInputType10]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_11:** `typing.Optional[UpdateVehicleRequestAuxInputType11]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_12:** `typing.Optional[UpdateVehicleRequestAuxInputType12]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_13:** `typing.Optional[UpdateVehicleRequestAuxInputType13]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_2:** `typing.Optional[UpdateVehicleRequestAuxInputType2]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_3:** `typing.Optional[UpdateVehicleRequestAuxInputType3]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_4:** `typing.Optional[UpdateVehicleRequestAuxInputType4]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_5:** `typing.Optional[UpdateVehicleRequestAuxInputType5]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_6:** `typing.Optional[UpdateVehicleRequestAuxInputType6]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_7:** `typing.Optional[UpdateVehicleRequestAuxInputType7]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_8:** `typing.Optional[UpdateVehicleRequestAuxInputType8]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_9:** `typing.Optional[UpdateVehicleRequestAuxInputType9]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**engine_hours:** `typing.Optional[int]` — A manual override for the vehicle's engine hours. You may only override a vehicle's engine hours if it cannot be read from on-board diagnostics. When you provide a manual engine hours override, Samsara will begin updating a vehicle's engine hours based on when the Samsara Vehicle Gateway is recieving power or not. Setting the value to 0 will unset the manual engine hours.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The <a href="/docs/external-ids" target="_blank">external IDs</a> for the given object.
    
</dd>
</dl>

<dl>
<dd>

**gateway_serial:** `typing.Optional[UserIdentifierSerial]` 
    
</dd>
</dl>

<dl>
<dd>

**gross_vehicle_weight:** `typing.Optional[GrossVehicleWeight]` 
    
</dd>
</dl>

<dl>
<dd>

**harsh_acceleration_setting_type:** `typing.Optional[UpdateVehicleRequestHarshAccelerationSettingType]` — The harsh acceleration setting type. This setting influences the acceleration sensitivity from which a <a href="https://kb.samsara.com/hc/en-us/articles/360043051792-Safety-Event-Overview" target="_blank">harsh event</a> is triggered. **By default**, this setting is inferred by the Samsara Vehicle Gateway from the engine computer, but it may be set or updated through the Samsara Dashboard or the API at any time. If set to `off`, then no acceleration based harsh events are triggered for the vehicle. Valid values: `passengerCar`, `lightTruck`, `heavyDuty`, `off`, `automatic`.
    
</dd>
</dl>

<dl>
<dd>

**license_plate:** `typing.Optional[str]` — The license plate of the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — These are generic notes about the Vehicle. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**odometer_meters:** `typing.Optional[int]` — A manual override for the vehicle's odometer. You may only override a vehicle's odometer if it cannot be read from on-board diagnostics. When you provide a manual odometer override, Samsara will begin updating a vehicle's odometer using GPS distance traveled since this override was set. See <a href="https://kb.samsara.com/hc/en-us/articles/115005273667" target="_blank">here</a> for more details.
    
</dd>
</dl>

<dl>
<dd>

**static_assigned_driver_id:** `typing.Optional[str]` — ID for the static assigned driver of the vehicle. Setting the value to 0 will unassign the current driver.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this vehicle. If your access to the API is scoped by one or more tags, this field is required to pass in.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_regulation_mode:** `typing.Optional[VehicleRegulationMode]` 
    
</dd>
</dl>

<dl>
<dd>

**vehicle_type:** `typing.Optional[VehicleType]` 
    
</dd>
</dl>

<dl>
<dd>

**vin:** `typing.Optional[str]` — The VIN of the Vehicle. Most of the time, this will be automatically read from the engine computer by the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Vehicle Locations
<details><summary><code>client.vehicle_locations.<a href="src/samsara/vehicle_locations/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestats) instead.***

Returns the last known location of all vehicles at the given `time`. If no `time` is specified, the current time is used. This can be optionally filtered by tags or specific vehicle IDs.

Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.vehicle_locations.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[str]` — A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Example: `2020-01-27T07:06:25Z`).
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicle_locations.<a href="src/samsara/vehicle_locations/client.py">get_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestatsfeed) instead.***

Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.

Your first call to this endpoint will provide you with the most recent location for each vehicle and a `pagination` object that contains an `endCursor`.

You can provide the `endCursor` to the `after` parameter of this endpoint to get location updates since that `endCursor`. 

If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates.

Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicle category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.vehicle_locations.get_feed()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicle_locations.<a href="src/samsara/vehicle_locations/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestatshistory) instead.***

Returns all known vehicle locations during the given time range. This can be optionally filtered by tags or specific vehicle IDs.

Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicle category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.vehicle_locations.get_history(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Vehicle Stats
<details><summary><code>client.vehicle_stats.<a href="src/samsara/vehicle_stats/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the last known stats of all vehicles at the given `time`. If no `time` is specified, the current time is used.

Related guide: <a href="/docs/telematics" target="_blank">Telematics</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.vehicle_stats.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[str]` — A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Example: `2020-01-27T07:06:25Z`).
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[
    typing.Union[
        VehicleStatsListRequestTypesItem,
        typing.Sequence[VehicleStatsListRequestTypesItem],
    ]
]` 

The stat types you want this endpoint to return information on. See also the <a href="/docs/telematics#query-parameters" target="_blank">Telematics</a> guide for more details.

You may list ***up to 3*** types using comma-separated format. For example: `types=gps,engineStates,obdOdometerMeters`.

*Note:* `auxInput3`-`auxInput10` count as a single type against the limit of 3. For example, you could list `types=engineStates,obdOdometerMeters,auxInput3,auxInput4` because `auxInput3` and `auxInput4` count as a single stat type. `auxInput1` and `auxInput2` still count as their own individual types.

- `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius.
- `auxInput1`-`auxInput13`: Stat events from the <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary inputs</a> for the vehicle.
- `barometricPressurePa`: The barometric pressure reading in pascals.
- `batteryMilliVolts`: The vehicle battery voltage reading.
- `defLevelMilliPercent`: The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc).
- `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU.
- `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius.
- `engineImmobilizer`: The state of the engine immobilizer - Valid values: `ignition_disabled`, `ignition_enabled`. This stat type will only return states of our first Engine Immobilizer Hardware (ACC-EI). Please use <a href="https://developers.samsara.com/reference/getengineimmobilizerstates" target="_blank">Get engine immobilizer states</a> to get states for both Engine Immobilizer Hardware versions (incl. HW-EI21).
- `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc).
- `engineOilPressureKPa`: The engine oil pressure reading in kilopascals.
- `engineRpm`: The revolutions per minute of the engine.
- `engineStates`: The state of the engine (`Off`, `On`, `Idle`).
- `faultCodes`: The diagnostic fault codes for the vehicle.
- `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc).
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
- `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
- `gpsOdometerMeters`: Odometer reading provided by GPS calculations when OBD odometer cannot be pulled automatically. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the [PATCH /fleet/vehicles/{id}](ref:updatevehicle) endpoint or through the <a href="https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading" target="_blank">cloud dasbhoard</a>. Odometer readings that are manually set will update as GPS trip data is gathered. Try combining with `obdOdometerMeters`.
- `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius.
- `nfcCardScans`: ID card scans.
- `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics.
- `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. Try combining with `gpsOdometerMeters`. 
- `syntheticEngineSeconds`: Data for the synthetic engine seconds for the vehicle.
- `evStateOfChargeMilliPercent`: Milli percent State of Charge for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evChargingStatus`: Charging status for electric and hybrid vehicles. Not all EV and HEVs may report this field. Statuses:  unknown - 0, not charging - 1, charging - 2.
- `evChargingEnergyMicroWh`: Charging energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evChargingVoltageMilliVolt`: Charging voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evChargingCurrentMilliAmp`: Charging current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evConsumedEnergyMicroWh`: Consumed energy (including regenerated) for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evRegeneratedEnergyMicroWh`: Regenerated energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evBatteryVoltageMilliVolt`: Battery voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evBatteryCurrentMilliAmp`: Battery current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evBatteryStateOfHealthMilliPercent`: Milli percent battery state of health for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evAverageBatteryTemperatureMilliCelsius`: Battery temperature for electric and hybrid vehicles in milli celsius. Not all EV and HEVs may report this field.
- `evDistanceDrivenMeters`: Electric distance driven for electric and hybrid vehicles in meters. Not all EV and HEVs may report this field.
- `spreaderLiquidRate`: Liquid spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderGranularRate`: Granular spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderPrewetRate`: Prewet spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderAirTemp`: Air (ambient) temperature in milli celsius reading from material spreader.
- `spreaderRoadTemp`: Road temperature reading in milli celsius from material spreader.
- `spreaderOnState`: Whether vehicle spreader is enabled.
- `spreaderActive`: Whether vehicle is actively spreading any material.
- `spreaderBlastState`: Whether vehicle is actively spreading material in ‘blast mode’.
- `spreaderGranularName`: Name of most recent type of granular material spread, read from the material spreader.
- `spreaderPrewetName`: Name of most recent type of prewet material spread, read from the material spreader.
- `spreaderLiquidName`: Name of most recent type of liquid material spread, read from the material spreader.
- `spreaderPlowStatus`: Snow plow status (`Up` or `Down`), as read from the material spreader. Note: this is separate from plow status defined via auxInput.
- `seatbeltDriver`: Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`. (Beta only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicle_stats.<a href="src/samsara/vehicle_stats/client.py">get_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a feed of vehicle stats. 

Your first call to this endpoint will provide you with the most recent stats for each vehicle and an `endCursor`.

You can the provide the `endCursor` value to the `after` query parameter to get all updates since the last call you made.

If `hasNextPage` is `false`, no new data is immediately available. You should wait a minimum of 5 seconds making a subsequent request.

Related guide: <a href="/docs/telematics" target="_blank">Telematics</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.vehicle_stats.get_feed()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[
    typing.Union[
        VehicleStatsGetFeedRequestTypesItem,
        typing.Sequence[VehicleStatsGetFeedRequestTypesItem],
    ]
]` 

The stat types you want this endpoint to return information on. See also the <a href="/docs/telematics#query-parameters" target="_blank">Telematics</a> guide for more details.

You may list ***up to 3*** types using comma-separated format. For example: `types=gps,engineStates,obdOdometerMeters`.

*Note:* `auxInput3`-`auxInput10` count as a single type against the limit of 3. For example, you could list `types=engineStates,obdOdometerMeters,auxInput3,auxInput4` because `auxInput3` and `auxInput4` count as a single stat type. `auxInput1` and `auxInput2` still count as their own individual types.

- `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius.
- `auxInput1`-`auxInput13`: Stat events from the <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary inputs</a> for the vehicle.
- `barometricPressurePa`: The barometric pressure reading in pascals.
- `batteryMilliVolts`: The vehicle battery voltage reading.
- `defLevelMilliPercent`: The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc).
- `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU.
- `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius.
- `engineImmobilizer`: The state of the engine immobilizer - Valid values: `ignition_disabled`, `ignition_enabled`. This stat type will only return states of our first Engine Immobilizer Hardware (ACC-EI). Please use <a href="https://developers.samsara.com/reference/getengineimmobilizerstates" target="_blank">Get engine immobilizer states</a> to get states for both Engine Immobilizer Hardware versions (incl. HW-EI21).
- `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc).
- `engineOilPressureKPa`: The engine oil pressure reading in kilopascals.
- `engineRpm`: The revolutions per minute of the engine.
- `engineStates`: The state of the engine (`Off`, `On`, `Idle`).
- `faultCodes`: The diagnostic fault codes for the vehicle.
- `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc).
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
- `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
- `gpsOdometerMeters`: Odometer reading provided by GPS calculations when OBD odometer cannot be pulled automatically. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the [PATCH /fleet/vehicles/{id}](ref:updatevehicle) endpoint or through the <a href="https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading" target="_blank">cloud dasbhoard</a>. Odometer readings that are manually set will update as GPS trip data is gathered. Try combining with `obdOdometerMeters`.
- `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius.
- `nfcCardScans`: ID card scans.
- `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics.
- `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. Try combining with `gpsOdometerMeters`. 
- `syntheticEngineSeconds`: Data for the synthetic engine seconds for the vehicle.
- `evStateOfChargeMilliPercent`: Milli percent State of Charge for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evChargingStatus`: Charging status for electric and hybrid vehicles. Not all EV and HEVs may report this field. Statuses:  unknown - 0, not charging - 1, charging - 2.
- `evChargingEnergyMicroWh`: Charging energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evChargingVoltageMilliVolt`: Charging voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evChargingCurrentMilliAmp`: Charging current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evConsumedEnergyMicroWh`: Consumed energy (including regenerated) for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evRegeneratedEnergyMicroWh`: Regenerated energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evBatteryVoltageMilliVolt`: Battery voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evBatteryCurrentMilliAmp`: Battery current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evBatteryStateOfHealthMilliPercent`: Milli percent battery state of health for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evAverageBatteryTemperatureMilliCelsius`: Battery temperature for electric and hybrid vehicles in milli celsius. Not all EV and HEVs may report this field.
- `evDistanceDrivenMeters`: Electric distance driven for electric and hybrid vehicles in meters. Not all EV and HEVs may report this field.
- `spreaderLiquidRate`: Liquid spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderGranularRate`: Granular spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderPrewetRate`: Prewet spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderAirTemp`: Air (ambient) temperature in milli celsius reading from material spreader.
- `spreaderRoadTemp`: Road temperature reading in milli celsius from material spreader.
- `spreaderOnState`: Whether vehicle spreader is enabled.
- `spreaderActive`: Whether vehicle is actively spreading any material.
- `spreaderBlastState`: Whether vehicle is actively spreading material in ‘blast mode’.
- `spreaderGranularName`: Name of most recent type of granular material spread, read from the material spreader.
- `spreaderPrewetName`: Name of most recent type of prewet material spread, read from the material spreader.
- `spreaderLiquidName`: Name of most recent type of liquid material spread, read from the material spreader.
- `spreaderPlowStatus`: Snow plow status (`Up` or `Down`), as read from the material spreader. Note: this is separate from plow status defined via auxInput.
- `seatbeltDriver`: Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`. (Beta only)
    
</dd>
</dl>

<dl>
<dd>

**decorations:** `typing.Optional[
    typing.Union[
        VehicleStatsGetFeedRequestDecorationsItem,
        typing.Sequence[VehicleStatsGetFeedRequestDecorationsItem],
    ]
]` 

Decorations to add to the primary stats listed in the `types` parameter. For example, if you wish to know the vehicle's location whenever the engine changes state, you may set `types=engineStates&decorations=gps`.

You may list ***up to 2*** decorations using comma-separated format. If multiple stats are listed in the `types` parameter, the decorations will be added to each one. For example: `types=engineStates,obdOdometerMeters,faultCodes&decorations=gps,fuelPercents` will list GPS and fuel decorations for each engine state change, each odometer reading, and each fault code. See the <a href="/docs/telematics#query-parameters" target="_blank">Telematics</a> guide for more details.

Note that decorations may significantly increase the response payload size.

- `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius.
- `auxInput1`-`auxInput13`: Stat events from the <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary inputs</a> for the vehicle.
- `batteryMilliVolts`: The vehicle battery voltage reading.
- `barometricPressurePa`: The barometric pressure reading in pascals.
- `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU.
- `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius.
- `engineImmobilizer`: The state of the engine immobilizer - Valid values: `ignition_disabled`, `ignition_enabled`. This stat type will only return states of our first Engine Immobilizer Hardware (ACC-EI). Please use <a href="https://developers.samsara.com/reference/getengineimmobilizerstates" target="_blank">Get engine immobilizer states</a> to get states for both Engine Immobilizer Hardware versions (incl. HW-EI21).
- `engineOilPressureKPa`: The engine oil pressure reading in kilopascals.
- `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc).
- `engineRpm`: The revolutions per minute of the engine.
- `engineStates`: The state of the engine (`Off`, `On`, `Idle`).
- `faultCodes`: The diagnostic fault codes for the vehicle.
- `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc).
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
- `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
- `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius.
- `nfcCardScans`: ID card scans.
- `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics.
- `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted.
- `syntheticEngineSeconds`: Data for the synthetic engine seconds for the vehicle.
- `evStateOfChargeMilliPercent`: Milli percent State of Charge for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evChargingStatus`: Charging status for electric and hybrid vehicles. Not all EV and HEVs may report this field. Statuses:  unknown - 0, not charging - 1, charging - 2.
- `evChargingEnergyMicroWh`: Charging energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evChargingVoltageMilliVolt`: Charging voltage for electric and hybrid vehicles in milli  volts. Not all EV and HEVs may report this field.
- `evChargingCurrentMilliAmp`: Charging current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evConsumedEnergyMicroWh`: Consumed energy (including regenerated) for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evRegeneratedEnergyMicroWh`: Regenerated energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evBatteryVoltageMilliVolt`: Battery voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evBatteryCurrentMilliAmp`: Battery current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evBatteryStateOfHealthMilliPercent`: Milli percent battery state of health for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evAverageBatteryTemperatureMilliCelsius`: Battery temperature for electric and hybrid vehicles in milli celsius. Not all EV and HEVs may report this field.
- `evDistanceDrivenMeters`: Electric distance driven for electric and hybrid vehicles in meters. Not all EV and HEVs may report this field.
- `spreaderLiquidRate`: Liquid spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderGranularRate`: Granular spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderPrewetRate`: Prewet spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderAirTemp`: Air (ambient) temperature in milli celsius reading from material spreader.
- `spreaderRoadTemp`: Road temperature reading in milli celsius from material spreader.
- `spreaderOnState`: Whether vehicle spreader is enabled.
- `spreaderActive`: Whether vehicle is actively spreading any material.
- `spreaderBlastState`: Whether vehicle is actively spreading material in ‘blast mode’.
- `spreaderGranularName`: Name of most recent type of granular material spread, read from the material spreader.
- `spreaderPrewetName`: Name of most recent type of prewet material spread, read from the material spreader.
- `spreaderLiquidName`: Name of most recent type of liquid material spread, read from the material spreader.
- `spreaderPlowStatus`: Snow plow status (`Up` or `Down`), as read from the material spreader. Note: this is separate from plow status defined via auxInput.
- `seatbeltDriver`: Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`. (Beta only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vehicle_stats.<a href="src/samsara/vehicle_stats/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns vehicle stats during the given time range for all vehicles. This can be optionally filtered by tags or specific vehicle IDs.

Related guide: <a href="/docs/telematics" target="_blank">Telematics</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.vehicle_stats.get_history(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[
    typing.Union[
        VehicleStatsGetHistoryRequestTypesItem,
        typing.Sequence[VehicleStatsGetHistoryRequestTypesItem],
    ]
]` 

The stat types you want this endpoint to return information on. See also the <a href="/docs/telematics#query-parameters" target="_blank">Telematics</a> guide for more details.

You may list ***up to 3*** types using comma-separated format. For example: `types=gps,engineStates,obdOdometerMeters`.

*Note:* `auxInput3`-`auxInput10` count as a single type against the limit of 3. For example, you could list `types=engineStates,obdOdometerMeters,auxInput3,auxInput4` because `auxInput3` and `auxInput4` count as a single stat type. `auxInput1` and `auxInput2` still count as their own individual types.

- `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius.
- `auxInput1`-`auxInput13`: Stat events from the <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary inputs</a> for the vehicle.
- `barometricPressurePa`: The barometric pressure reading in pascals.
- `batteryMilliVolts`: The vehicle battery voltage reading.
- `defLevelMilliPercent`: The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc).
- `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU.
- `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius.
- `engineImmobilizer`: The state of the engine immobilizer - Valid values: `ignition_disabled`, `ignition_enabled`. This stat type will only return states of our first Engine Immobilizer Hardware (ACC-EI). Please use <a href="https://developers.samsara.com/reference/getengineimmobilizerstates" target="_blank">Get engine immobilizer states</a> to get states for both Engine Immobilizer Hardware versions (incl. HW-EI21).
- `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc).
- `engineOilPressureKPa`: The engine oil pressure reading in kilopascals.
- `engineRpm`: The revolutions per minute of the engine.
- `engineStates`: The state of the engine (`Off`, `On`, `Idle`).
- `faultCodes`: The diagnostic fault codes for the vehicle.
- `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc).
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
- `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
- `gpsOdometerMeters`: Odometer reading provided by GPS calculations when OBD odometer cannot be pulled automatically. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the [PATCH /fleet/vehicles/{id}](ref:updatevehicle) endpoint or through the <a href="https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading" target="_blank">cloud dasbhoard</a>. Odometer readings that are manually set will update as GPS trip data is gathered. Try combining with `obdOdometerMeters`.
- `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius.
- `nfcCardScans`: ID card scans.
- `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics.
- `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. Try combining with `gpsOdometerMeters`. 
- `syntheticEngineSeconds`: Data for the synthetic engine seconds for the vehicle.
- `evStateOfChargeMilliPercent`: Milli percent State of Charge for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evChargingStatus`: Charging status for electric and hybrid vehicles. Not all EV and HEVs may report this field. Statuses:  unknown - 0, not charging - 1, charging - 2.
- `evChargingEnergyMicroWh`: Charging energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evChargingVoltageMilliVolt`: Charging voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evChargingCurrentMilliAmp`: Charging current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evConsumedEnergyMicroWh`: Consumed energy (including regenerated) for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evRegeneratedEnergyMicroWh`: Regenerated energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evBatteryVoltageMilliVolt`: Battery voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evBatteryCurrentMilliAmp`: Battery current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evBatteryStateOfHealthMilliPercent`: Milli percent battery state of health for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evAverageBatteryTemperatureMilliCelsius`: Battery temperature for electric and hybrid vehicles in milli celsius. Not all EV and HEVs may report this field.
- `evDistanceDrivenMeters`: Electric distance driven for electric and hybrid vehicles in meters. Not all EV and HEVs may report this field.
- `spreaderLiquidRate`: Liquid spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderGranularRate`: Granular spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderPrewetRate`: Prewet spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderAirTemp`: Air (ambient) temperature in milli celsius reading from material spreader.
- `spreaderRoadTemp`: Road temperature reading in milli celsius from material spreader.
- `spreaderOnState`: Whether vehicle spreader is enabled.
- `spreaderActive`: Whether vehicle is actively spreading any material.
- `spreaderBlastState`: Whether vehicle is actively spreading material in ‘blast mode’.
- `spreaderGranularName`: Name of most recent type of granular material spread, read from the material spreader.
- `spreaderPrewetName`: Name of most recent type of prewet material spread, read from the material spreader.
- `spreaderLiquidName`: Name of most recent type of liquid material spread, read from the material spreader.
- `spreaderPlowStatus`: Snow plow status (`Up` or `Down`), as read from the material spreader. Note: this is separate from plow status defined via auxInput.
- `seatbeltDriver`: Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`. (Beta only)
    
</dd>
</dl>

<dl>
<dd>

**decorations:** `typing.Optional[
    typing.Union[
        VehicleStatsGetHistoryRequestDecorationsItem,
        typing.Sequence[VehicleStatsGetHistoryRequestDecorationsItem],
    ]
]` 

Decorations to add to the primary stats listed in the `types` parameter. For example, if you wish to know the vehicle's location whenever the engine changes state, you may set `types=engineStates&decorations=gps`.

You may list ***up to 2*** decorations using comma-separated format. If multiple stats are listed in the `types` parameter, the decorations will be added to each one. For example: `types=engineStates,obdOdometerMeters,faultCodes&decorations=gps,fuelPercents` will list GPS and fuel decorations for each engine state change, each odometer reading, and each fault code. See the <a href="/docs/telematics#query-parameters" target="_blank">Telematics</a> guide for more details.

Note that decorations may significantly increase the response payload size.

- `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius.
- `auxInput1`-`auxInput13`: Stat events from the <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary inputs</a> for the vehicle.
- `batteryMilliVolts`: The vehicle battery voltage reading.
- `barometricPressurePa`: The barometric pressure reading in pascals.
- `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU.
- `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius.
- `engineImmobilizer`: The state of the engine immobilizer - Valid values: `ignition_disabled`, `ignition_enabled`. This stat type will only return states of our first Engine Immobilizer Hardware (ACC-EI). Please use <a href="https://developers.samsara.com/reference/getengineimmobilizerstates" target="_blank">Get engine immobilizer states</a> to get states for both Engine Immobilizer Hardware versions (incl. HW-EI21).
- `engineOilPressureKPa`: The engine oil pressure reading in kilopascals.
- `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc).
- `engineRpm`: The revolutions per minute of the engine.
- `engineStates`: The state of the engine (`Off`, `On`, `Idle`).
- `faultCodes`: The diagnostic fault codes for the vehicle.
- `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc).
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
- `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
- `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius.
- `nfcCardScans`: ID card scans.
- `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics.
- `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted.
- `syntheticEngineSeconds`: Data for the synthetic engine seconds for the vehicle.
- `evStateOfChargeMilliPercent`: Milli percent State of Charge for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evChargingStatus`: Charging status for electric and hybrid vehicles. Not all EV and HEVs may report this field. Statuses:  unknown - 0, not charging - 1, charging - 2.
- `evChargingEnergyMicroWh`: Charging energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evChargingVoltageMilliVolt`: Charging voltage for electric and hybrid vehicles in milli  volts. Not all EV and HEVs may report this field.
- `evChargingCurrentMilliAmp`: Charging current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evConsumedEnergyMicroWh`: Consumed energy (including regenerated) for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evRegeneratedEnergyMicroWh`: Regenerated energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evBatteryVoltageMilliVolt`: Battery voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evBatteryCurrentMilliAmp`: Battery current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evBatteryStateOfHealthMilliPercent`: Milli percent battery state of health for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evAverageBatteryTemperatureMilliCelsius`: Battery temperature for electric and hybrid vehicles in milli celsius. Not all EV and HEVs may report this field.
- `evDistanceDrivenMeters`: Electric distance driven for electric and hybrid vehicles in meters. Not all EV and HEVs may report this field.
- `spreaderLiquidRate`: Liquid spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderGranularRate`: Granular spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderPrewetRate`: Prewet spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderAirTemp`: Air (ambient) temperature in milli celsius reading from material spreader.
- `spreaderRoadTemp`: Road temperature reading in milli celsius from material spreader.
- `spreaderOnState`: Whether vehicle spreader is enabled.
- `spreaderActive`: Whether vehicle is actively spreading any material.
- `spreaderBlastState`: Whether vehicle is actively spreading material in ‘blast mode’.
- `spreaderGranularName`: Name of most recent type of granular material spread, read from the material spreader.
- `spreaderPrewetName`: Name of most recent type of prewet material spread, read from the material spreader.
- `spreaderLiquidName`: Name of most recent type of liquid material spread, read from the material spreader.
- `spreaderPlowStatus`: Snow plow status (`Up` or `Down`), as read from the material spreader. Note: this is separate from plow status defined via auxInput.
- `seatbeltDriver`: Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`. (Beta only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Gateways
<details><summary><code>client.gateways.<a href="src/samsara/gateways/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all gateways

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Gateways** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.gateways.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**models:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by a comma separated list of gateway models.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gateways.<a href="src/samsara/gateways/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Activate a new gateway. To activate a device and associate it with your organization, enter its serial number. Each device's serial number can also be found on its label or packaging, or from your order confirmation email. A Not Found error could mean that the serial was not found or it has already been activated

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Gateways** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.gateways.create(
    serial="GFRV-43N-VGX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**serial:** `str` — Gateway serial number
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gateways.<a href="src/samsara/gateways/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deactivate a gateway

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Gateways** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.gateways.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Gateway serial number
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Industrial
<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">get_assets</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all assets in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.get_assets()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">create_asset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an asset with optional configuration parameters. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.create_asset(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `AssetName` 
    
</dd>
</dl>

<dl>
<dd>

**custom_metadata:** `typing.Optional[CustomMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[AssetLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**location_data_input_id:** `typing.Optional[str]` — Required if locationType is "dataInput". Specifies the id of a location data input which will determine the asset's location. **The data input will be moved to the new asset.**
    
</dd>
</dl>

<dl>
<dd>

**location_type:** `typing.Optional[LocationType]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[ParentId]` 
    
</dd>
</dl>

<dl>
<dd>

**running_status_data_input_id:** `typing.Optional[str]` — The asset's isRunning status will be true when the associated data input's value is 1. Data input cannot be of location format. **The data input will be moved to the new asset.**
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[TagIds]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">delete_asset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete asset. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.delete_asset(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the asset to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">patch_asset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing asset. Only the provided fields will be updated. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.patch_asset(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the asset to be updated
    
</dd>
</dl>

<dl>
<dd>

**custom_metadata:** `typing.Optional[CustomMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[AssetLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**location_data_input_id:** `typing.Optional[str]` — Required if locationType is "dataInput". Specifies the id of a location data input which will determine the asset's location. The data input must be in the asset.
    
</dd>
</dl>

<dl>
<dd>

**location_type:** `typing.Optional[LocationType]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[AssetName]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — The id of the parent asset that the asset belongs to. Pass in an empty string to remove the child from the parent.
    
</dd>
</dl>

<dl>
<dd>

**running_status_data_input_id:** `typing.Optional[str]` — The asset's isRunning status will be true when the associated data input's value is 1. Data input cannot be of location format. The data input must be in the asset.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[TagIds]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">patch_asset_data_outputs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Writes values to multiple data outputs on an asset simultaneously. Only the provided data outputs will be updated.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.patch_asset_data_outputs(
    id="id",
    values={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Asset ID
    
</dd>
</dl>

<dl>
<dd>

**values:** `typing.Dict[str, typing.Optional[typing.Any]]` — A map of data output IDs to values. All data outputs must belong to the same asset. Only the specified IDs will be written to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">get_data_inputs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all data inputs, optionally filtered by tags or asset ids. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.get_data_inputs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">get_data_input_data_snapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns last known data points for all data inputs. This can be filtered by optional tags, specific data input IDs or asset IDs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.get_data_input_data_snapshot()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**data_input_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">get_data_input_data_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a continuous feed of all data input data points.

Your first call to this endpoint will provide you with the most recent data points for each data input and a `pagination` object that contains an `endCursor`.

You can provide the `endCursor` to the `after` parameter of this endpoint to get data point updates since that `endCursor`.

If `hasNextPage` is `false`, no updates are readily available yet. We suggest waiting a minimum of 5 seconds before requesting updates. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.get_data_input_data_feed()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**data_input_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">get_data_input_data_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all known data points during the given time range for all data inputs. This can be filtered by optional tags, specific data input IDs or asset IDs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.get_data_input_data_history(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**data_input_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch all cameras. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">list_programs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch configured programs on the camera. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.list_programs(
    camera_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `int` — The camera_id should be valid for the given accessToken.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">get_latest_run</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the latest run for a camera or program by default. If startedAtMs is supplied, fetch the specific run that corresponds to that start time. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.get_latest_run(
    camera_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `int` — The camera_id should be valid for the given accessToken.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[int]` — The configured program's ID on the camera.
    
</dd>
</dl>

<dl>
<dd>

**started_at_ms:** `typing.Optional[int]` — EndMs is an optional param. It will default to the current time.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit is an integer value from 1 to 1,000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">list_runs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch runs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.list_runs(
    duration_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**duration_ms:** `int` — DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `typing.Optional[int]` — EndMs is an optional param. It will default to the current time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">get_vision_runs_by_camera</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch runs by camera. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.get_vision_runs_by_camera(
    camera_id=1000000,
    duration_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `int` — The camera_id should be valid for the given accessToken.
    
</dd>
</dl>

<dl>
<dd>

**duration_ms:** `int` — DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `typing.Optional[int]` — EndMs is an optional param. It will default to the current time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.industrial.<a href="src/samsara/industrial/client.py">get_vision_runs_by_camera_and_program</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch runs by camera and program. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.industrial.get_vision_runs_by_camera_and_program(
    camera_id=1000000,
    program_id=1000000,
    started_at_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `int` — The camera_id should be valid for the given accessToken.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `int` — The configured program's ID on the camera.
    
</dd>
</dl>

<dl>
<dd>

**started_at_ms:** `int` — Started_at_ms is a required param. Indicates the start time of the run to be fetched.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LiveSharingLinks
<details><summary><code>client.live_sharing_links.<a href="src/samsara/live_sharing_links/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all non-expired Live Sharing Links.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Live Sharing Links** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.live_sharing_links.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of Live Share Link IDs
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[LiveSharingLinksListRequestType]` — A filter on the data based on the Live Sharing Link type.  Valid values: `all`, `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 100 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_sharing_links.<a href="src/samsara/live_sharing_links/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Live Sharing Link.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Live Sharing Links** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.live_sharing_links.create(
    name="Example Live Sharing Link name",
    type="assetsLocation",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the Live Sharing Link.
    
</dd>
</dl>

<dl>
<dd>

**type:** `LiveSharingLinksCreateLiveSharingLinkRequestBodyType` — Type of the Live Sharing Link. This field specifies which one of '<type>LinkConfig' objects will be used to configure the sharing link.  Valid values: `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`
    
</dd>
</dl>

<dl>
<dd>

**assets_location_link_config:** `typing.Optional[AssetsLocationLinkConfigObject]` 
    
</dd>
</dl>

<dl>
<dd>

**assets_near_location_link_config:** `typing.Optional[AssetsNearLocationLinkConfigObject]` 
    
</dd>
</dl>

<dl>
<dd>

**assets_on_route_link_config:** `typing.Optional[AssetsOnRouteLinkConfigObject]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).
    
</dd>
</dl>

<dl>
<dd>

**expires_at_time:** `typing.Optional[str]` — Date that this link expires in RFC 3339 format. Can't be set in the past. If not provided then link will never expire.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_sharing_links.<a href="src/samsara/live_sharing_links/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Live Sharing Link.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Live Sharing Links** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.live_sharing_links.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the Live Sharing Link.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_sharing_links.<a href="src/samsara/live_sharing_links/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Live Sharing Link.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Live Sharing Links** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.live_sharing_links.update(
    id="id",
    name="Example Live Sharing Link name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the Live Sharing Link.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the Live Sharing Link.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).
    
</dd>
</dl>

<dl>
<dd>

**expires_at_time:** `typing.Optional[str]` — Date that this link expires in RFC 3339 format. Can't be set in the past. If not provided then link will never expire.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization Info
<details><summary><code>client.organization_info.<a href="src/samsara/organization_info/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about your organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Org Information** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.organization_info.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Preview
<details><summary><code>client.preview.<a href="src/samsara/preview/client.py">list_uploaded_media</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint returns a list of all uploaded media (video and still images) matching query parameters. Additional media can be retrieved with the [Create a media retrieval request](https://developers.samsara.com/reference/postmediaretrieval) endpoint, and they will be included in the list after they are uploaded. Urls provided by this endpoint expire in 8 hours.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Preview** under the  category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.preview.list_uploaded_media(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**inputs:** `typing.Optional[
    typing.Union[
        PreviewListUploadedMediaRequestInputsItem,
        typing.Sequence[PreviewListUploadedMediaRequestInputsItem],
    ]
]` — A list of desired camera inputs for which to return captured media. If empty, media for all available inputs will be returned.
    
</dd>
</dl>

<dl>
<dd>

**media_types:** `typing.Optional[
    typing.Union[
        typing.Literal["image"], typing.Sequence[typing.Literal["image"]]
    ]
]` — A list of desired media types for which to return captured media. If empty, media for all available media types will be returned.
    
</dd>
</dl>

<dl>
<dd>

**trigger_reasons:** `typing.Optional[
    typing.Union[
        PreviewListUploadedMediaRequestTriggerReasonsItem,
        typing.Sequence[PreviewListUploadedMediaRequestTriggerReasonsItem],
    ]
]` — A list of desired trigger reasons for which to return captured media. If empty, media for all available trigger reasons will be returned.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**available_after_time:** `typing.Optional[str]` — A timestamp in RFC 3339 format that can act as a cursor to track which media has previously been retrieved; only media whose availableAtTime comes after this parameter will be returned. Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preview.<a href="src/samsara/preview/client.py">get_custom_report_configs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get paginated custom report configs created in the organization.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Custom Reports** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.preview.get_custom_report_configs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many reports will be in the response. Default and max for this value is 100 objects.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preview.<a href="src/samsara/preview/client.py">get_custom_report_runs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all custom report runs with the provided IDs or customReportIds.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Custom Reports** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.preview.get_custom_report_runs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_report_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Required array of custom report IDs for the custom report runs wanted. Only one of customReportIds or ids is allowed.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Required array of custom report run IDs to fetch. Only one of ids or customReportIds is allowed.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preview.<a href="src/samsara/preview/client.py">post_custom_report_run</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a custom report run which then gets queued up to generate custom report data for the report run.

 <b>Rate limit:</b> 240 requests/day (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Custom Reports** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.preview.post_custom_report_run(
    custom_report_id="4f71fd67-54f0-41de-991c-ee1e031134d1",
    end_time=datetime.datetime.fromisoformat(
        "2019-06-13 21:08:25+00:00",
    ),
    start_time=datetime.datetime.fromisoformat(
        "2019-06-13 19:08:25+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_report_id:** `str` — Required unique ID for the custom report linked to this run.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `dt.datetime` — The end time of the custom report run in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `dt.datetime` — The start time of the custom report run in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**attribute_value_ids:** `typing.Optional[typing.Sequence[str]]` — The optional array of attribute value ids to filter the custom report run by.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[int]]` — The optional array of tag ids to filter the custom report run by.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preview.<a href="src/samsara/preview/client.py">get_custom_report_run_data</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return the custom report data for a given custom report run ID. For more information regarding custom report columns, please see our [KB article section on Custom Report Fields](https://kb.samsara.com/hc/en-us/articles/360052711232-Manage-Custom-Reports).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Custom Reports** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.preview.get_custom_report_run_data()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — The ID of the specified run for the requested custom report.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preview.<a href="src/samsara/preview/client.py">get_driver_efficiency_by_drivers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return driver efficiency data that has been collected for your organization and grouped by drivers based on the time parameters passed in. Results are paginated.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Driver Efficiency** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.preview.get_driver_efficiency_by_drivers(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Must be in multiple of hours and at least 1 day before endTime. Timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-11T19:00:00Z, 2015-09-12T14:00:00-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Must be in multiple of hours and no later than 3 hours before the current time. Timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:00:00Z, 2015-09-15T14:00:00-04:00).
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**data_formats:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of data formats you want to fetch. Valid values: `score`, `raw` and `percentage`. The default data format is `score`. Example: `dataFormats=raw,score`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preview.<a href="src/samsara/preview/client.py">get_driver_efficiency_by_vehicles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return driver efficiency data that has been collected for your organization and grouped by vehicle drivers used based on the time parameters passed in. Results are paginated.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Driver Efficiency** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.preview.get_driver_efficiency_by_vehicles(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Must be in multiple of hours and at least 1 day before endTime. Timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-11T19:00:00Z, 2015-09-12T14:00:00-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Must be in multiple of hours and no later than 3 hours before the current time. Timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:00:00Z, 2015-09-15T14:00:00-04:00).
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**data_formats:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of data formats you want to fetch. Valid values: `score`, `raw` and `percentage`. The default data format is `score`. Example: `dataFormats=raw,score`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preview.<a href="src/samsara/preview/client.py">get_form_templates</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of the organization's form templates.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Preview** under the  category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.preview.get_form_templates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 100 template IDs to filter on.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preview.<a href="src/samsara/preview/client.py">delete_training_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint supports batch deletion operations. The response does not indicate which specific deletions, if any, have failed. On a successful deletion or partial failure, a ‘204 No Content’ status is returned.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Training Assignments** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.preview.delete_training_assignments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — String of comma separated assignments IDs. Max value for this value is 100 objects .Example: `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preview.<a href="src/samsara/preview/client.py">patch_training_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Preview:** This endpoint is in preview and is likely to change before being broadly available. Reach out to your Samsara Representative to have Training APIs enabled for your organization.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Training Assignments** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.preview.patch_training_assignments(
    due_at_time="dueAtTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**due_at_time:** `str` — Due date of the training assignment in RFC 3339 format. Millisecond precision and timezones are supported.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — String of comma separated assignments IDs. Max value for this value is 100 objects .Example: `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.preview.<a href="src/samsara/preview/client.py">get_training_courses</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all training courses data. Results are paginated. 
 Courses in the ‘draft’ status are excluded from the data returned by this endpoint.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Preview** under the  category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.preview.get_training_courses()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**course_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated course IDs. If course ID is present, training assignments for the specified course ID(s) will be returned. Max value for this value is 100 objects. Defaults to returning all courses. Example: `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    
</dd>
</dl>

<dl>
<dd>

**category_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated course category IDs. If courseCategoryId is present, training courses for the specified course category(s) will be returned. Max value for this value is 100 objects. Defaults to returning all courses.  Example: `categoryIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated values. If status is present, training courses with the specified status(s) will be returned. Valid values: “published”, “deleted”, “archived”. Defaults to returning all courses.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tags
<details><summary><code>client.tags.<a href="src/samsara/tags/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all of the tags for an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tags** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.tags.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/samsara/tags/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new tag for the organization. This may include up to 20,000 tagged entities. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Tags** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.tags.create(
    name="California",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of this tag.
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The addresses that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**assets:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The trailers, unpowered, and powered assets that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**drivers:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The drivers that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    
</dd>
</dl>

<dl>
<dd>

**machines:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The machines that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_id:** `typing.Optional[str]` — If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted.
    
</dd>
</dl>

<dl>
<dd>

**sensors:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The sensors that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**vehicles:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The vehicles that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/samsara/tags/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a tag by id. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tags** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.tags.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/samsara/tags/client.py">replace</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a tag with a new name and new members. This API call would replace all old members of a tag with new members specified in the request body. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Tags** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.tags.replace(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`.
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The addresses that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**assets:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The trailers, unpowered, and powered assets that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**drivers:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The drivers that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**machines:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The machines that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of this tag.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_id:** `typing.Optional[str]` — If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted.
    
</dd>
</dl>

<dl>
<dd>

**sensors:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The sensors that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**vehicles:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The vehicles that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/samsara/tags/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a tag. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Tags** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.tags.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/samsara/tags/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing tag. **Note** this implementation of patch uses [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard. 

 This means that any fields included in the patch request will _overwrite_ fields which exist on the target resource. 

 For arrays, this means any array included in the request will _replace_ the array that exists at the specified path, it will not _add_ to the existing array. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Tags** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.tags.patch(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`.
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The addresses that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**assets:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The trailers, unpowered, and powered assets that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**drivers:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The drivers that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    
</dd>
</dl>

<dl>
<dd>

**machines:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The machines that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of this tag.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_id:** `typing.Optional[str]` — If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted.
    
</dd>
</dl>

<dl>
<dd>

**sensors:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The sensors that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**vehicles:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The vehicles that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/samsara/users/client.py">lis_roles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all user roles in an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.users.lis_roles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/samsara/users/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all users in an organization. Users that have expired access will not be returned. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.users.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/samsara/users/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a user to the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import CreateUserRequestRoles, Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.users.create(
    auth_type="default",
    email="user@company.com",
    name="Bob Smith",
    roles=[
        CreateUserRequestRoles(
            role_id="8a9371af-82d1-4158-bf91-4ecc8d3a114c",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_type:** `CreateUserRequestAuthType` — The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. Valid values: `default`, `saml`.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — The email address of this user.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The first and last name of the user.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Sequence[CreateUserRequestRoles]` — The list of roles that applies to this user. A user may have "organizational" roles, which apply to the user at the organizational level, and "tag-specific" roles, which apply to the user for a given tag.
    
</dd>
</dl>

<dl>
<dd>

**expire_at:** `typing.Optional[str]` — For users with temporary access, this is the expiration datetime in RFC3339 format
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/samsara/users/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific user's information. Users that have expired access will not be returned. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.users.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/samsara/users/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the given user. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.users.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/samsara/users/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific user's information. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.users.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the user.
    
</dd>
</dl>

<dl>
<dd>

**auth_type:** `typing.Optional[UpdateUserRequestAuthType]` — The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. Valid values: `default`, `saml`.
    
</dd>
</dl>

<dl>
<dd>

**expire_at:** `typing.Optional[str]` — For users with temporary access, this is the expiration datetime in RFC3339 format
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The first and last name of the user.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.Sequence[CreateUserRequestRoles]]` — The list of roles that applies to this user. A user may have "organizational" roles, which apply to the user at the organizational level, and "tag-specific" roles, which apply to the user for a given tag.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Assets
<details><summary><code>client.assets.<a href="src/samsara/assets/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch all of the assets. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.assets.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/samsara/assets/client.py">list_current_locations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch current locations of all assets. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
response = client.assets.list_current_locations()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/samsara/assets/client.py">get_reefers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetches all reefers and reefer-specific stats. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
response = client.assets.get_reefers(
    start_ms=1000000,
    end_ms=1000000,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_ms:** `int` — Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/samsara/assets/client.py">get_location</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

List historical locations for a given asset. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.assets.get_location(
    asset_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `int` — ID of the asset. Must contain only digits 0-9.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets.<a href="src/samsara/assets/client.py">get_reefer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch the reefer-specific stats of an asset. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.assets.get_reefer(
    asset_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `int` — ID of the asset. Must contain only digits 0-9.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Dispatch
<details><summary><code>client.dispatch.<a href="src/samsara/dispatch/client.py">delete_route</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Delete a dispatch route and its associated jobs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.dispatch.delete_route(
    route_id_or_external_id="route_id_or_external_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**route_id_or_external_id:** `str` — ID of the route. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
    
</dd>
</dl>

<dl>
<dd>

**apply_to_future_routes:** `typing.Optional[bool]` — This is only for a recurring route.  If set to true, delete all following runs of the route.  If set to false, only delete the current route.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Messages
<details><summary><code>client.messages.<a href="src/samsara/messages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get all messages. 

 <b>Rate limit:</b> 75 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Messages** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.messages.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_ms:** `typing.Optional[int]` — Time in unix milliseconds that represents the end of time range of messages to return. Used in combination with durationMs. Defaults to now.
    
</dd>
</dl>

<dl>
<dd>

**duration_ms:** `typing.Optional[int]` — Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/samsara/messages/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Send a message to a list of driver ids. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Messages** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.messages.create(
    driver_ids=[111, 222, 333],
    text="This is a message.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Sequence[int]` — IDs of the drivers for whom the messages are sent to.
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — The text sent in the message. Max 2500 characters allowed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Trailer Assignments
<details><summary><code>client.trailer_assignments.<a href="src/samsara/trailer_assignments/client.py">list_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch trailer assignment data for all trailers in your organization. 

 <b>Rate limit:</b> 100 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
response = client.trailer_assignments.list_all()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_ms:** `typing.Optional[int]` — Timestamp in Unix epoch miliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `typing.Optional[int]` — Timestamp in Unix epoch miliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trailer_assignments.<a href="src/samsara/trailer_assignments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch trailer assignment data for a single trailer. 

 <b>Rate limit:</b> 100 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.trailer_assignments.list(
    trailer_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trailer_id:** `int` — ID of trailer. Must contain only digits 0-9.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `typing.Optional[int]` — Timestamp in Unix epoch milliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `typing.Optional[int]` — Timestamp in Unix epoch milliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Trips
<details><summary><code>client.trips.<a href="src/samsara/trips/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get historical trips data for specified vehicle. This method returns a set of historical trips data for the specified vehicle in the specified time range. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Trips** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.trips.list(
    vehicle_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vehicle_id:** `int` — Vehicle ID to query.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Beginning of the time range, specified in milliseconds UNIX time. Limited to a 90 day window with respect to startMs and endMs
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — End of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Machines
<details><summary><code>client.machines.<a href="src/samsara/machines/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get historical data for machine objects. This method returns a set of historical data for all machines. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.machines.get_history(
    end_ms=1462881998034,
    start_ms=1462878398034,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_ms:** `int` — End of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Beginning of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.machines.<a href="src/samsara/machines/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get machine objects. This method returns a list of the machine objects in the Samsara Cloud and information about them. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.machines.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sensors
<details><summary><code>client.sensors.<a href="src/samsara/sensors/client.py">get_cargo</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get cargo monitor status (empty / full) for requested sensors. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Sensors** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.sensors.get_cargo(
    sensors=[122],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sensors:** `typing.Sequence[int]` — List of sensor IDs to query.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sensors.<a href="src/samsara/sensors/client.py">get_door</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get door monitor status (closed / open) for requested sensors. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Sensors** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.sensors.get_door(
    sensors=[122],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sensors:** `typing.Sequence[int]` — List of sensor IDs to query.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sensors.<a href="src/samsara/sensors/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get historical data for specified sensors. This method returns a set of historical data for the specified sensors in the specified time range and at the specified time resolution. 

 <b>Rate limit:</b> 100 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Sensors** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara, V1SensorsHistorySeries

client = Samsara(
    token="YOUR_TOKEN",
)
client.sensors.get_history(
    end_ms=1462881998034,
    series=[
        V1SensorsHistorySeries(
            field="ambientTemperature",
            widget_id=1,
        )
    ],
    start_ms=1462878398034,
    step_ms=3600000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_ms:** `int` — End of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**series:** `typing.Sequence[V1SensorsHistorySeries]` 
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Beginning of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**step_ms:** `int` — Time resolution for which data should be returned, in milliseconds. Specifying 3600000 will return data at hour intervals.
    
</dd>
</dl>

<dl>
<dd>

**fill_missing:** `typing.Optional[InlineObject6FillMissing]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sensors.<a href="src/samsara/sensors/client.py">get_humidity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get humidity for requested sensors. This method returns the current relative humidity for the requested sensors. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Sensors** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.sensors.get_humidity(
    sensors=[122],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sensors:** `typing.Sequence[int]` — List of sensor IDs to query.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sensors.<a href="src/samsara/sensors/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get sensor objects. This method returns a list of the sensor objects in the Samsara Cloud and information about them. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Sensors** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.sensors.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sensors.<a href="src/samsara/sensors/client.py">get_temperature</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get temperature for requested sensors. This method returns the current ambient temperature (and probe temperature if applicable) for the requested sensors. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Sensors** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.sensors.get_temperature(
    sensors=[122],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sensors:** `typing.Sequence[int]` — List of sensor IDs to query.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/samsara/webhooks/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all webhooks belonging to a specific org.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.webhooks.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of webhook IDs. Example: `ids=49412323223,49412329928`
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/samsara/webhooks/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a webhook

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.webhooks.create(
    name="Webhook-123",
    url="https://www.Webhook-123.com/webhook/listener",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The  name of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The url of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**custom_headers:** `typing.Optional[typing.Sequence[CustomHeadersObjectRequestBody]]` — The list of custom headers that users can include with their request
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.Sequence[WebhooksPostWebhooksRequestBodyEventTypesItem]]` — [beta] The list of event types associated with a particular event type
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[WebhooksPostWebhooksRequestBodyVersion]` — The version of the webhook.  Valid values: `2018-01-01`, `2021-06-09`, `2022-09-13`, `2024-02-27`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/samsara/webhooks/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a webhook with given ID.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.webhooks.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the webhook. This is the Samsara-specified ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/samsara/webhooks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a webhook with the given ID.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.webhooks.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the webhook to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/samsara/webhooks/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific webhook's information.  **Note** this implementation of patch uses [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
 This means that any fields included in the patch request will _overwrite_ fields which exist on the target resource.
 For arrays, this means any array included in the request will _replace_ the array that exists at the specified path, it will not _add_ to the existing array

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.webhooks.patch(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the webhook to update.
    
</dd>
</dl>

<dl>
<dd>

**custom_headers:** `typing.Optional[typing.Sequence[CustomHeadersObjectRequestBody]]` — The list of custom headers that users can include with their request
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The  name of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The url of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[WebhooksPatchWebhookRequestBodyVersion]` — The version of the webhook.  Valid values: `2018-01-01`, `2021-06-09`, `2022-09-13`, `2024-02-27`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Auth
<details><summary><code>client.auth.<a href="src/samsara/auth/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Obtain an OAuth2 access token using client credentials
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.auth.get_token(
    client_id="client_id",
    client_secret="client_secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — The client ID of the application
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — The client secret of the application
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Alerts Configurations
<details><summary><code>client.alerts.configurations.<a href="src/samsara/alerts/configurations/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get specified Alert Configurations.

The following trigger types are API enabled and will show up in the results:
Vehicle Speed
Ambient Temperature
Fuel Level (Percentage)
Vehicle DEF Level (Percentage)
Vehicle Battery
Gateway Unplugged
Dashcam Disconnected
Camera Connector Disconnected
Asset starts moving
Inside Geofence
Outside Geofence
Unassigned Driving
Driver HOS Violation
Vehicle Engine Idle
Asset Engine On
Asset Engine Off
Harsh Event
Scheduled Maintenance
Scheduled Maintenance by Odometer
Scheduled Maintenance by Engine Hours
Out of Route
GPS Signal Loss
Cell Signal Loss
Fault Code
Tire Faults
Gateway Disconnected
Panic Button
Tampering Detected
If vehicle is severely speeding (as defined by your organization)
DVIR Submitted for Asset
Driver Document Submitted
Driver App Sign In
Driver App Sign Out
Geofence Entry
Geofence Exit
Route Stop ETA Alert
Driver Recorded
Scheduled Date And Time

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.alerts.configurations.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by the IDs. Returns all if no ids are provided.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ConfigurationsGetRequestStatus]` — The status of the alert configuration.  Valid values: `all`, `enabled`, `disabled`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Alerts Incidents
<details><summary><code>client.alerts.incidents.<a href="src/samsara/alerts/incidents/client.py">stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Alert Incidents for specific Alert Configurations over a specified period of time.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.alerts.incidents.stream(
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — Required RFC 3339 timestamp that indicates when to begin receiving data. This will be based on updatedAtTime.
    
</dd>
</dl>

<dl>
<dd>

**configuration_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Required array of alert configuration ids to return incident data for.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — Optional RFC 3339 timestamp to stop receiving data. Defaults to now if not provided. This will be based on updatedAtTime.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Beta Assets
<details><summary><code>client.beta.assets.<a href="src/samsara/beta/assets/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all assets. Up to 300 assets will be returned per page.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Assets** under the Assets category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.assets.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[AssetsListRequestType]` — The operational context in which the asset interacts with the Samsara system. Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer, flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg: container, dumpster...), or Uncategorized.  Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**updated_after_time:** `typing.Optional[str]` —  A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**include_tags:** `typing.Optional[bool]` — Optional boolean indicating whether to return tags on supported entities
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of asset IDs and External IDs.
    
</dd>
</dl>

<dl>
<dd>

**attribute_value_ids:** `typing.Optional[str]` — A filter on the data based on this comma-separated list of attribute value IDs. Only entities associated with ALL of the referenced values will be returned (i.e. the intersection of the sets of entities with each value). Example: `attributeValueIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.assets.<a href="src/samsara/beta/assets/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new asset.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assets** under the Assets category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.assets.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**license_plate:** `typing.Optional[str]` — The license plate of the asset.
    
</dd>
</dl>

<dl>
<dd>

**make:** `typing.Optional[str]` — The manufacturer of the asset. (If a VIN is entered and the system detects it is registered to a different manufacturer than provided an error will be returned).
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — The manufacturer model of the asset. (If a VIN is entered and the system detects it is registered to a different model than provided an error will be returned).
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The human-readable name of the asset. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — These are generic notes about the asset. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**regulation_mode:** `typing.Optional[AssetsCreateAssetRequestBodyRegulationMode]` — Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use unregulated asset. Primarily used with vehicles.  Valid values: `mixed`, `regulated`, `unregulated`
    
</dd>
</dl>

<dl>
<dd>

**serial_number:** `typing.Optional[str]` — The serial number of the asset.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[AssetsCreateAssetRequestBodyType]` — The operational context in which the asset interacts with the Samsara system. Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer, flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg: container, dumpster...), or Uncategorized.  Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    
</dd>
</dl>

<dl>
<dd>

**vin:** `typing.Optional[str]` — The vehicle identification number of the asset.
    
</dd>
</dl>

<dl>
<dd>

**year:** `typing.Optional[int]` — The year of manufacture of the asset.  (If a VIN is entered and the system detects it is registered to a different year than provided an error will be returned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.assets.<a href="src/samsara/beta/assets/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an existing asset.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assets** under the Assets category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.assets.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A filter selecting a single asset by id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.assets.<a href="src/samsara/beta/assets/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing asset.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assets** under the Assets category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.assets.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A filter selecting a single asset by id.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**license_plate:** `typing.Optional[str]` — The license plate of the asset.
    
</dd>
</dl>

<dl>
<dd>

**make:** `typing.Optional[str]` — The manufacturer of the asset. (If a VIN is entered and the system detects it is registered to a different manufacturer than provided an error will be returned).
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — The manufacturer model of the asset. (If a VIN is entered and the system detects it is registered to a different model than provided an error will be returned).
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The human-readable name of the asset. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — These are generic notes about the asset. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**regulation_mode:** `typing.Optional[AssetsUpdateAssetRequestBodyRegulationMode]` — Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use unregulated asset. Primarily used with vehicles.  Valid values: `mixed`, `regulated`, `unregulated`
    
</dd>
</dl>

<dl>
<dd>

**serial_number:** `typing.Optional[str]` — The serial number of the asset.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[AssetsUpdateAssetRequestBodyType]` — The operational context in which the asset interacts with the Samsara system. Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer, flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg: container, dumpster...), or Uncategorized.  Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    
</dd>
</dl>

<dl>
<dd>

**vin:** `typing.Optional[str]` — The vehicle identification number of the asset.
    
</dd>
</dl>

<dl>
<dd>

**year:** `typing.Optional[int]` — The year of manufacture of the asset.  (If a VIN is entered and the system detects it is registered to a different year than provided an error will be returned).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Beta Inputs
<details><summary><code>client.beta.inputs.<a href="src/samsara/beta/inputs/client.py">stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return data collected from the inputs of your organization's assets based on the time parameters passed in. Results are paginated. If you include an endTime, the endpoint will return data up until that point. If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call. The endpoint will only return data up until the endTime that has been processed by the server at the time of the original request. You will need to request the same [startTime, endTime) range again to receive data for assets processed after the original request time. This endpoint sorts data by time ascending.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Assets** under the Assets category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.inputs.stream(
    type="auxInput1",
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `InputsStreamRequestType` — Input stat type to query for.  Valid values: `auxInput1`, `auxInput2`, `auxInput3`, `auxInput4`, `auxInput5`, `auxInput6`, `auxInput7`, `auxInput8`, `auxInput9`, `auxInput10`, `auxInput11`, `auxInput12`, `auxInput13`, `analogInput1Voltage`, `analogInput2Voltage`, `analogInput1Current`, `analogInput2Current`, `batteryVoltage`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of asset IDs. Limited to 100 ID's for each request.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to never if not provided; if not provided then pagination will not cease, and a valid pagination cursor will always be returned. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**include_tags:** `typing.Optional[bool]` — Optional boolean indicating whether to return tags on supported entities
    
</dd>
</dl>

<dl>
<dd>

**include_attributes:** `typing.Optional[bool]` — Optional boolean indicating whether to return attributes on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Beta Aemp
<details><summary><code>client.beta.aemp.<a href="src/samsara/beta/aemp/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of equipment following the AEMP ISO 15143-3 standard.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read AEMP** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.aemp.get(
    page_number="pageNumber",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_number:** `str` — The number corresponding to a specific page of paginated results, defaulting to the first page if not provided. The default page size is 100 records.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Beta Fleet
<details><summary><code>client.beta.fleet.<a href="src/samsara/beta/fleet/client.py">get_driver_efficiency</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all driver and associated vehicle efficiency data. 

 <b>Rate limit:</b> 50 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.fleet.get_driver_efficiency()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_activation_status:** `typing.Optional[FleetGetDriverEfficiencyRequestDriverActivationStatus]` — If value is `deactivated`, only drivers that are deactivated will appear in the response. This parameter will default to `active` if not provided (fetching only active drivers).
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of driver IDs. Cannot be used with tag filtering or driver status. Example: `driverIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**driver_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filters summary to drivers based on this comma-separated list of tag IDs. Data from all the drivers' respective vehicles will be included in the summary, regardless of which tag the vehicle is associated with. Should not be provided in addition to `driverIds`. Example: driverTagIds=1234,5678
    
</dd>
</dl>

<dl>
<dd>

**driver_parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filters like `driverTagIds` but includes descendants of all the given parent tags. Should not be provided in addition to `driverIds`. Example: `driverParentTagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[dt.datetime]` 

A start time in RFC 3339 format. The results will be truncated to the hour mark for the provided time. For example, if `startTime` is 2020-03-17T12:06:19Z then the results will include data starting from 2020-03-17T12:00:00Z. The provided start time cannot be in the future. Start time can be at most 31 days before the end time. If the start time is within the last hour, the results will be empty. Default: 24 hours prior to endTime.

Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[dt.datetime]` 

An end time in RFC 3339 format. The results will be truncated to the hour mark for the provided time. For example, if `endTime` is 2020-03-17T12:06:19Z then the results will include data up until 2020-03-17T12:00:00Z. The provided end time cannot be in the future. End time can be at most 31 days after the start time. Default: The current time truncated to the hour mark.

Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.fleet.<a href="src/samsara/beta/fleet/client.py">update_equipment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an equipment.  **Note** this implementation of patch uses [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
 This means that any fields included in the patch request will _overwrite_ fields which exist on the target resource.
 For arrays, this means any array included in the request will _replace_ the array that exists at the specified path, it will not _add_ to the existing array

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.fleet.update_equipment(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique Samsara ID of the Equipment. This is automatically generated when the Equipment object is created. It cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Sequence[GoaAttributeTiny]]` — List of attributes associated with the entity
    
</dd>
</dl>

<dl>
<dd>

**engine_hours:** `typing.Optional[int]` — When you provide a manual engine hours override, Samsara will begin updating a equipment's engine hours used since this override was set.
    
</dd>
</dl>

<dl>
<dd>

**equipment_serial_number:** `typing.Optional[str]` — The serial number of the equipment.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**equipment_patch_equipment_request_body_id:** `typing.Optional[str]` — The unique Samsara ID of the Equipment. This is automatically generated when the Equipment object is created. It cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The human-readable name of the Equipment. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — These are generic notes about the Equipment. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**odometer_meters:** `typing.Optional[int]` — When you provide a manual odometer override, Samsara will begin updating a equipment's odometer using GPS distance traveled since this override was set.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this equipment. If your access to the API is scoped by one or more tags, this field is required to pass in. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.fleet.<a href="src/samsara/beta/fleet/client.py">get_hos_eld_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all HOS ELD events in a time range, grouped by driver. Attributes will be populated depending on which ELD Event Type is being returned.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.fleet.get_hos_eld_events(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**driver_activation_status:** `typing.Optional[FleetGetHosEldEventsRequestDriverActivationStatus]` — If value is `deactivated`, only drivers that are deactivated will appear in the response. This parameter will default to `active` if not provided (fetching only active drivers).  Valid values: `active`, `deactivated`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 25 objects.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.fleet.<a href="src/samsara/beta/fleet/client.py">get_trailer_stats_snapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the last known stats of all trailers at the given `time`. If no `time` is specified, the current time is used.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Trailer Statistics** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.fleet.get_trailer_stats_snapshot(
    types="types",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**types:** `str` 

The stat types you want this endpoint to return information on.

You may list **up to 3** types using comma-separated format. For example: `types=gps,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters`.

* `gps`: GPS data including lat/long, heading, speed, and a reverse geocode address.
* `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint or through the [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings wthat are manually set will update as GPS trip data is gathered.
* `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of the reefer in millidegree Celsius.
* `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run according to onboard diagnostics. Only supported on reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air temperature zone 1 in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferFuelPercent`: The fuel level of the reefer unit in percentage points (e.g. `99`, `50`, etc). Only supported on reefer solutions.
* `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only supported on multizone Carrier reefer solutions.
* `reeferStateZone1`: The state of the reefer in zone 1. For single zone reefers, this applies tot he single zone. Only supported on multizone reefer solutions.
* `reeferStateZone2`: The state of the reefer in zone 2. Only supported on multizone reefer solutions.
* `reeferStateZone3`: The state of the reefer in zone 3. Only supported on multizone reefer solutions.
* `reeferRunMode`: The operational mode of the reefer (`Start/Stop`, `Continuous`)
* `reeferAlarms`: Any alarms that are present on the reefer. Only supported on reefer solutions.
* `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single zone reefers, this applies to the single zone.
* `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only supported on multizone reefer solutions.
* `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only supported on multizone reefer solutions.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**trailer_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of trailer IDs and externalIds. Example: `trailerIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[str]` —  A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 Format. Millisecond precision and timezones are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.fleet.<a href="src/samsara/beta/fleet/client.py">get_trailer_stats_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a feed of trailer stats.

The first call to this endpoint will provide the most recent stats for each trailer and an `endCursor`.

Providing the `endCursor` value to the `after` query parameter will fetch all updates since the previous API call.

If `hasNextPage` is false, no new data is immediately available. Please wait a minimum of 5 seconds before making a subsequent request.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Trailer Statistics** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.fleet.get_trailer_stats_feed(
    types="types",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**types:** `str` 

The stat types you want this endpoint to return information on.

You may list **up to 3** types using comma-separated format. For example: `types=gps,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters`.

* `gps`: GPS data including lat/long, heading, speed, and a reverse geocode address.
* `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint or through the [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings wthat are manually set will update as GPS trip data is gathered.
* `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of the reefer in millidegree Celsius.
* `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run according to onboard diagnostics. Only supported on reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air temperature zone 1 in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferFuelPercent`: The fuel level of the reefer unit in percentage points (e.g. `99`, `50`, etc). Only supported on reefer solutions.
* `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only supported on multizone Carrier reefer solutions.
* `reeferStateZone1`: The state of the reefer in zone 1. For single zone reefers, this applies tot he single zone. Only supported on multizone reefer solutions.
* `reeferStateZone2`: The state of the reefer in zone 2. Only supported on multizone reefer solutions.
* `reeferStateZone3`: The state of the reefer in zone 3. Only supported on multizone reefer solutions.
* `reeferRunMode`: The operational mode of the reefer (`Start/Stop`, `Continuous`)
* `reeferAlarms`: Any alarms that are present on the reefer. Only supported on reefer solutions.
* `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single zone reefers, this applies to the single zone.
* `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only supported on multizone reefer solutions.
* `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only supported on multizone reefer solutions.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**trailer_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of trailer IDs and externalIds. Example: `trailerIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**decorations:** `typing.Optional[str]` 

Decorations add to the primary stats listed in the `types` parameter. For example, if you wish to know the trailer's location whenever the odometer updates, you may set `types=gpsOdometerMeters&decorations=gps`.

You may list **up to 2** types using comma-separated format. If multiple stats are listed in the types parameter, the decorations will be added to each type. For example: `types=reeferStateZone1,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters&decorations=gps` will list GPS decorations for each reeferStateZone1 reading, each reeferAmbientAirTemperatureMilliC reding, and gpsOdometerMeters reading.

Note that decorations may significantly increase the response payload size.

* `gps`: GPS data including lat/long, heading, speed, and a reverse geocode address.
* `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint or through the [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings wthat are manually set will update as GPS trip data is gathered.
* `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of the reefer in millidegree Celsius.
* `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run according to onboard diagnostics. Only supported on reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air temperature zone 1 in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferFuelPercent`: The fuel level of the reefer unit in percentage points (e.g. `99`, `50`, etc). Only supported on reefer solutions.
* `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only supported on multizone Carrier reefer solutions.
* `reeferStateZone1`: The state of the reefer in zone 1. For single zone reefers, this applies tot he single zone. Only supported on multizone reefer solutions.
* `reeferStateZone2`: The state of the reefer in zone 2. Only supported on multizone reefer solutions.
* `reeferStateZone3`: The state of the reefer in zone 3. Only supported on multizone reefer solutions.
* `reeferRunMode`: The operational mode of the reefer (`Start/Stop`, `Continuous`)
* `reeferAlarms`: Any alarms that are present on the reefer. Only supported on reefer solutions.
* `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single zone reefers, this applies to the single zone.
* `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only supported on multizone reefer solutions.
* `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only supported on multizone reefer solutions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.fleet.<a href="src/samsara/beta/fleet/client.py">get_trailer_stats_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns trailer stats during the given time range for all trailers. This can be optionally filtered by tags or specific trailer IDs.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Trailer Statistics** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.fleet.get_trailer_stats_history(
    start_time="startTime",
    end_time="endTime",
    types="types",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**types:** `str` 

The stat types you want this endpoint to return information on.

You may list **up to 3** types using comma-separated format. For example: `types=gps,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters`.

* `gps`: GPS data including lat/long, heading, speed, and a reverse geocode address.
* `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint or through the [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings wthat are manually set will update as GPS trip data is gathered.
* `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of the reefer in millidegree Celsius.
* `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run according to onboard diagnostics. Only supported on reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air temperature zone 1 in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferFuelPercent`: The fuel level of the reefer unit in percentage points (e.g. `99`, `50`, etc). Only supported on reefer solutions.
* `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only supported on multizone Carrier reefer solutions.
* `reeferStateZone1`: The state of the reefer in zone 1. For single zone reefers, this applies tot he single zone. Only supported on multizone reefer solutions.
* `reeferStateZone2`: The state of the reefer in zone 2. Only supported on multizone reefer solutions.
* `reeferStateZone3`: The state of the reefer in zone 3. Only supported on multizone reefer solutions.
* `reeferRunMode`: The operational mode of the reefer (`Start/Stop`, `Continuous`)
* `reeferAlarms`: Any alarms that are present on the reefer. Only supported on reefer solutions.
* `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single zone reefers, this applies to the single zone.
* `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only supported on multizone reefer solutions.
* `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only supported on multizone reefer solutions.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**trailer_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of trailer IDs and externalIds. Example: `trailerIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**decorations:** `typing.Optional[str]` 

Decorations add to the primary stats listed in the `types` parameter. For example, if you wish to know the trailer's location whenever the odometer updates, you may set `types=gpsOdometerMeters&decorations=gps`.

You may list **up to 2** types using comma-separated format. If multiple stats are listed in the types parameter, the decorations will be added to each type. For example: `types=reeferStateZone1,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters&decorations=gps` will list GPS decorations for each reeferStateZone1 reading, each reeferAmbientAirTemperatureMilliC reding, and gpsOdometerMeters reading.

Note that decorations may significantly increase the response payload size.

* `gps`: GPS data including lat/long, heading, speed, and a reverse geocode address.
* `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint or through the [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings wthat are manually set will update as GPS trip data is gathered.
* `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of the reefer in millidegree Celsius.
* `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run according to onboard diagnostics. Only supported on reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air temperature zone 1 in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferFuelPercent`: The fuel level of the reefer unit in percentage points (e.g. `99`, `50`, etc). Only supported on reefer solutions.
* `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only supported on multizone Carrier reefer solutions.
* `reeferStateZone1`: The state of the reefer in zone 1. For single zone reefers, this applies tot he single zone. Only supported on multizone reefer solutions.
* `reeferStateZone2`: The state of the reefer in zone 2. Only supported on multizone reefer solutions.
* `reeferStateZone3`: The state of the reefer in zone 3. Only supported on multizone reefer solutions.
* `reeferRunMode`: The operational mode of the reefer (`Start/Stop`, `Continuous`)
* `reeferAlarms`: Any alarms that are present on the reefer. Only supported on reefer solutions.
* `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single zone reefers, this applies to the single zone.
* `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only supported on multizone reefer solutions.
* `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only supported on multizone reefer solutions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.fleet.<a href="src/samsara/beta/fleet/client.py">update_engine_immobilizer_state</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the engine immobilizer state of a vehicle. This requires an engine immobilizer to be installed on the vehicle gateway.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Vehicle Immobilization** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import (
    Samsara,
    UpdateEngineImmobilizerRelayStateRequestBodyRequestBody,
)

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.fleet.update_engine_immobilizer_state(
    id=1000000,
    relay_states=[
        UpdateEngineImmobilizerRelayStateRequestBodyRequestBody(
            id="relay1",
            is_open=False,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Vehicle ID
    
</dd>
</dl>

<dl>
<dd>

**relay_states:** `typing.Sequence[UpdateEngineImmobilizerRelayStateRequestBodyRequestBody]` — A list of relay states. If a relay is omitted, its state won't be updated. If the list is empty, a 400 bad request status code will be returned. If there are multiple states for the same relay, a 400 bad request status code will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Beta Jobs
<details><summary><code>client.beta.jobs.<a href="src/samsara/beta/jobs/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches jobs based on id/uuid or provided filters.

To use this endpoint, select **Read Jobs** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.jobs.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — A jobId or uuid in STRING format. JobId must be prefixed with `jobId:`(Examples: `"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596"`, `"jobId:98765"`).
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` —  A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` —  An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**industrial_asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — IndustrialAssetId in STRING format. (Example: `"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596"`).
    
</dd>
</dl>

<dl>
<dd>

**fleet_device_ids:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — FleetDeviceId in INTEGER format. (Example: `123456`).
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[JobsGetRequestStatus]` — A job status in STRING format. Job statuses can be one of three (ignores case): `"active", "scheduled", "completed"`  Valid values: `active`, `scheduled`, `completed`
    
</dd>
</dl>

<dl>
<dd>

**customer_name:** `typing.Optional[str]` — Customer name to filter by
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.jobs.<a href="src/samsara/beta/jobs/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new job and returns it.

To use this endpoint, select **Write Jobs** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import PostJobObjectRequestBody, Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.jobs.create(
    job=PostJobObjectRequestBody(
        end_date="2019-06-13T19:08:25Z",
        id="8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
        name="My Job Name",
        start_date="2019-06-13T19:08:25Z",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job:** `PostJobObjectRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.jobs.<a href="src/samsara/beta/jobs/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing job.

To use this endpoint, select **Write Jobs** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.jobs.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A jobId or uuid in STRING format. JobId must be prefixed with `jobId:`(Examples: `"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596"`, `"jobId:98765"`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beta.jobs.<a href="src/samsara/beta/jobs/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches an existing job and returns it.

To use this endpoint, select **Write Jobs** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import PatchJobObjectRequestBody, Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.beta.jobs.update(
    id="id",
    job=PatchJobObjectRequestBody(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A jobId or uuid in STRING format. JobId must be prefixed with `jobId:`(Examples: `"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596"`, `"jobId:98765"`).
    
</dd>
</dl>

<dl>
<dd>

**job:** `PatchJobObjectRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**keep_history:** `typing.Optional[bool]` — Defaults to true if user does not want to overwrite entire history for an active job (irrelevant for scheduled/completed jobs)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Equipment Locations
<details><summary><code>client.equipment.locations.<a href="src/samsara/equipment/locations/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns last known locations for all equipment. This can be optionally filtered by tags or specific equipment IDs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.equipment.locations.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**equipment_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.equipment.locations.<a href="src/samsara/equipment/locations/client.py">get_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a continuous feed of all equipment locations from Samsara AG26s.

Your first call to this endpoint will provide you with the most recent location for each unit of equipment and a `pagination` object that contains an `endCursor`.

You can provide the `endCursor` to subsequent calls via the `after` parameter. The response will contain any equipment location updates since that `endCursor`.

If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.equipment.locations.get_feed()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**equipment_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.equipment.locations.<a href="src/samsara/equipment/locations/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns historical equipment locations during the given time range. This can be optionally filtered by tags or specific equipment IDs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.equipment.locations.get_history(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**equipment_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Equipment Stats
<details><summary><code>client.equipment.stats.<a href="src/samsara/equipment/stats/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the last known stats for all equipment. This can be optionally filtered by tags or specific equipment IDs. 

 <b>Rate limit:</b> 150 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.equipment.stats.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**equipment_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[
    typing.Union[
        StatsGetRequestTypesItem, typing.Sequence[StatsGetRequestTypesItem]
    ]
]` 

The types of equipment stats you want to query. Currently, you may submit up to 3 types.

- `engineRpm`: The revolutions per minute of the engine.
- `fuelPercents`: The percent of fuel in the unit of equipment.
- `obdEngineSeconds`: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics.
- `gatewayEngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the asset gateway has been receiving power with an offset provided manually through the Samsara cloud dashboard. This is supported with the following hardware configurations: 
  - AG24/AG26/AG46P + APWR cable ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d) required) 
  - AG52 + BPWR/BEQP cable ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d) required). 
- `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG26 device is receiving power via J1939/CAT cable and an offset provided manually through the Samsara cloud dashboard.
- `obdEngineStates`: The state of the engine read from on-board diagnostics. Can be `Off`, `On`, or `Idle`.
- `gatewayEngineStates`: An approximation of engine state based on readings the AG26 receives from the aux/digio cable. Can be `Off` or `On`.
- `gpsOdometerMeters`: An approximation of odometer reading based on GPS calculations since the AG26 was activated, and a manual odometer offset provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.equipment.stats.<a href="src/samsara/equipment/stats/client.py">get_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a continuous feed of all equipment stats from Samsara AG26s.

Your first call to this endpoint will provide you with the most recent stats for each unit of equipment and a `pagination` object that contains an `endCursor`.

You can provide the `endCursor` to subsequent calls via the `after` parameter. The response will contain any equipment stats updates since that `endCursor`.

If `hasNextPage` is `false`, no updates are readily available yet. Each stat type has a different refresh rate, but in general we'd suggest waiting a minimum of 5 seconds before requesting updates. 

 <b>Rate limit:</b> 150 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.equipment.stats.get_feed()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**equipment_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[
    typing.Union[
        StatsGetFeedRequestTypesItem,
        typing.Sequence[StatsGetFeedRequestTypesItem],
    ]
]` 

The types of equipment stats you want to query. Currently, you may submit up to 3 types.

- `engineRpm`: The revolutions per minute of the engine.
- `fuelPercents`: The percent of fuel in the unit of equipment.
- `obdEngineSeconds`: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics.
- `gatewayEngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the asset gateway has been receiving power with an offset provided manually through the Samsara cloud dashboard. This is supported with the following hardware configurations: 
  - AG24/AG26/AG46P + APWR cable ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d) required) 
  - AG52 + BPWR/BEQP cable ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d) required). 
- `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG26 device is receiving power via J1939/CAT cable and an offset provided manually through the Samsara cloud dashboard.
- `obdEngineStates`: The state of the engine read from on-board diagnostics. Can be `Off`, `On`, or `Idle`.
- `gatewayEngineStates`: An approximation of engine state based on readings the AG26 receives from the aux/digio cable. Can be `Off` or `On`.
- `gpsOdometerMeters`: An approximation of odometer reading based on GPS calculations since the AG26 was activated, and a manual odometer offset provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.equipment.stats.<a href="src/samsara/equipment/stats/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns historical equipment status during the given time range. This can be optionally filtered by tags or specific equipment IDs. 

 <b>Rate limit:</b> 150 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.equipment.stats.get_history(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**equipment_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[
    typing.Union[
        StatsGetHistoryRequestTypesItem,
        typing.Sequence[StatsGetHistoryRequestTypesItem],
    ]
]` 

The types of equipment stats you want to query. Currently, you may submit up to 3 types.

- `engineRpm`: The revolutions per minute of the engine.
- `fuelPercents`: The percent of fuel in the unit of equipment.
- `obdEngineSeconds`: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics.
- `gatewayEngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the asset gateway has been receiving power with an offset provided manually through the Samsara cloud dashboard. This is supported with the following hardware configurations: 
  - AG24/AG26/AG46P + APWR cable ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d) required) 
  - AG52 + BPWR/BEQP cable ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d) required). 
- `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG26 device is receiving power via J1939/CAT cable and an offset provided manually through the Samsara cloud dashboard.
- `obdEngineStates`: The state of the engine read from on-board diagnostics. Can be `Off`, `On`, or `Idle`.
- `gatewayEngineStates`: An approximation of engine state based on readings the AG26 receives from the aux/digio cable. Can be `Off` or `On`.
- `gpsOdometerMeters`: An approximation of odometer reading based on GPS calculations since the AG26 was activated, and a manual odometer offset provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Routes AuditLogs
<details><summary><code>client.routes.audit_logs.<a href="src/samsara/routes/audit_logs/client.py">get_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Subscribes to a feed of immutable, append-only updates for routes. The initial request to this feed endpoint returns a cursor, which can be used on the next request to fetch updated routes that have had state changes since that request.

The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/fetchAllRouteJobUpdates).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.routes.audit_logs.get_feed()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Literal["route"]]` 

Expands the specified value(s) in the response object. Expansion populates additional fields in an object, if supported. Unsupported fields are ignored. To expand multiple fields, input a comma-separated list.

Valid value: `route`  Valid values: `route`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

