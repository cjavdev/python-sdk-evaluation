# Addresses

Types:

```python
from samsara.types import Address, AddressListResponse, AddressDeleteResponse
```

Methods:

- <code title="post /addresses">client.addresses.<a href="./src/samsara/resources/addresses.py">create</a>(\*\*<a href="src/samsara/types/address_create_params.py">params</a>) -> <a href="./src/samsara/types/address.py">Address</a></code>
- <code title="get /addresses/{id}">client.addresses.<a href="./src/samsara/resources/addresses.py">retrieve</a>(id) -> <a href="./src/samsara/types/address.py">Address</a></code>
- <code title="get /addresses">client.addresses.<a href="./src/samsara/resources/addresses.py">list</a>(\*\*<a href="src/samsara/types/address_list_params.py">params</a>) -> <a href="./src/samsara/types/address_list_response.py">AddressListResponse</a></code>
- <code title="delete /addresses/{id}">client.addresses.<a href="./src/samsara/resources/addresses.py">delete</a>(id) -> str</code>
- <code title="patch /addresses/{id}">client.addresses.<a href="./src/samsara/resources/addresses.py">modify</a>(id, \*\*<a href="src/samsara/types/address_modify_params.py">params</a>) -> <a href="./src/samsara/types/address.py">Address</a></code>

# Alerts

## Configurations

Types:

```python
from samsara.types.alerts import (
    ConfigurationCreateResponse,
    ConfigurationUpdateResponse,
    ConfigurationListResponse,
)
```

Methods:

- <code title="post /alerts/configurations">client.alerts.configurations.<a href="./src/samsara/resources/alerts/configurations.py">create</a>(\*\*<a href="src/samsara/types/alerts/configuration_create_params.py">params</a>) -> <a href="./src/samsara/types/alerts/configuration_create_response.py">ConfigurationCreateResponse</a></code>
- <code title="patch /alerts/configurations">client.alerts.configurations.<a href="./src/samsara/resources/alerts/configurations.py">update</a>(\*\*<a href="src/samsara/types/alerts/configuration_update_params.py">params</a>) -> <a href="./src/samsara/types/alerts/configuration_update_response.py">ConfigurationUpdateResponse</a></code>
- <code title="get /alerts/configurations">client.alerts.configurations.<a href="./src/samsara/resources/alerts/configurations.py">list</a>(\*\*<a href="src/samsara/types/alerts/configuration_list_params.py">params</a>) -> <a href="./src/samsara/types/alerts/configuration_list_response.py">ConfigurationListResponse</a></code>
- <code title="delete /alerts/configurations">client.alerts.configurations.<a href="./src/samsara/resources/alerts/configurations.py">delete</a>(\*\*<a href="src/samsara/types/alerts/configuration_delete_params.py">params</a>) -> None</code>

## Incidents

Types:

```python
from samsara.types.alerts import IncidentStreamResponse
```

Methods:

- <code title="get /alerts/incidents/stream">client.alerts.incidents.<a href="./src/samsara/resources/alerts/incidents.py">stream</a>(\*\*<a href="src/samsara/types/alerts/incident_stream_params.py">params</a>) -> <a href="./src/samsara/types/alerts/incident_stream_response.py">IncidentStreamResponse</a></code>

# Assets

Types:

```python
from samsara.types import AssetCreateResponse, AssetUpdateResponse, AssetListResponse
```

Methods:

- <code title="post /assets">client.assets.<a href="./src/samsara/resources/assets/assets.py">create</a>(\*\*<a href="src/samsara/types/asset_create_params.py">params</a>) -> <a href="./src/samsara/types/asset_create_response.py">AssetCreateResponse</a></code>
- <code title="patch /assets">client.assets.<a href="./src/samsara/resources/assets/assets.py">update</a>(\*\*<a href="src/samsara/types/asset_update_params.py">params</a>) -> <a href="./src/samsara/types/asset_update_response.py">AssetUpdateResponse</a></code>
- <code title="get /assets">client.assets.<a href="./src/samsara/resources/assets/assets.py">list</a>(\*\*<a href="src/samsara/types/asset_list_params.py">params</a>) -> <a href="./src/samsara/types/asset_list_response.py">AssetListResponse</a></code>
- <code title="delete /assets">client.assets.<a href="./src/samsara/resources/assets/assets.py">delete</a>(\*\*<a href="src/samsara/types/asset_delete_params.py">params</a>) -> None</code>

## Inputs

Types:

```python
from samsara.types.assets import InputStreamResponse
```

Methods:

- <code title="get /assets/inputs/stream">client.assets.inputs.<a href="./src/samsara/resources/assets/inputs.py">stream</a>(\*\*<a href="src/samsara/types/assets/input_stream_params.py">params</a>) -> <a href="./src/samsara/types/assets/input_stream_response.py">InputStreamResponse</a></code>

## LocationAndSpeed

Types:

```python
from samsara.types.assets import LocationAndSpeedStreamResponse
```

Methods:

- <code title="get /assets/location-and-speed/stream">client.assets.location_and_speed.<a href="./src/samsara/resources/assets/location_and_speed.py">stream</a>(\*\*<a href="src/samsara/types/assets/location_and_speed_stream_params.py">params</a>) -> <a href="./src/samsara/types/assets/location_and_speed_stream_response.py">LocationAndSpeedStreamResponse</a></code>

# Attributes

Types:

```python
from samsara.types import Attribute, AttributeListResponse, AttributeDeleteResponse
```

Methods:

- <code title="post /attributes">client.attributes.<a href="./src/samsara/resources/attributes.py">create</a>(\*\*<a href="src/samsara/types/attribute_create_params.py">params</a>) -> <a href="./src/samsara/types/attribute.py">Attribute</a></code>
- <code title="get /attributes/{id}">client.attributes.<a href="./src/samsara/resources/attributes.py">retrieve</a>(id, \*\*<a href="src/samsara/types/attribute_retrieve_params.py">params</a>) -> <a href="./src/samsara/types/attribute.py">Attribute</a></code>
- <code title="patch /attributes/{id}">client.attributes.<a href="./src/samsara/resources/attributes.py">update</a>(id, \*\*<a href="src/samsara/types/attribute_update_params.py">params</a>) -> <a href="./src/samsara/types/attribute.py">Attribute</a></code>
- <code title="get /attributes">client.attributes.<a href="./src/samsara/resources/attributes.py">list</a>(\*\*<a href="src/samsara/types/attribute_list_params.py">params</a>) -> <a href="./src/samsara/types/attribute_list_response.py">AttributeListResponse</a></code>
- <code title="delete /attributes/{id}">client.attributes.<a href="./src/samsara/resources/attributes.py">delete</a>(id, \*\*<a href="src/samsara/types/attribute_delete_params.py">params</a>) -> str</code>

# Beta

## Aemp

### Fleet

Types:

```python
from samsara.types.beta.aemp import FleetListResponse
```

Methods:

- <code title="get /beta/aemp/Fleet/{pageNumber}">client.beta.aemp.fleet.<a href="./src/samsara/resources/beta/aemp/fleet.py">list</a>(page_number) -> <a href="./src/samsara/types/beta/aemp/fleet_list_response.py">FleetListResponse</a></code>

## Fleet

### Drivers

Types:

```python
from samsara.types.beta.fleet import DriverEfficiencyResponse
```

Methods:

- <code title="get /beta/fleet/drivers/efficiency">client.beta.fleet.drivers.<a href="./src/samsara/resources/beta/fleet/drivers.py">efficiency</a>(\*\*<a href="src/samsara/types/beta/fleet/driver_efficiency_params.py">params</a>) -> <a href="./src/samsara/types/beta/fleet/driver_efficiency_response.py">DriverEfficiencyResponse</a></code>

### Equipment

Types:

```python
from samsara.types.beta.fleet import EquipmentUpdateResponse
```

Methods:

- <code title="patch /beta/fleet/equipment/{id}">client.beta.fleet.equipment.<a href="./src/samsara/resources/beta/fleet/equipment.py">update</a>(\*, path_id, \*\*<a href="src/samsara/types/beta/fleet/equipment_update_params.py">params</a>) -> <a href="./src/samsara/types/beta/fleet/equipment_update_response.py">EquipmentUpdateResponse</a></code>

### Hos

#### Drivers

##### EldEvents

Types:

```python
from samsara.types.beta.fleet.hos.drivers import EldEventListResponse
```

Methods:

- <code title="get /beta/fleet/hos/drivers/eld-events">client.beta.fleet.hos.drivers.eld_events.<a href="./src/samsara/resources/beta/fleet/hos/drivers/eld_events.py">list</a>(\*\*<a href="src/samsara/types/beta/fleet/hos/drivers/eld_event_list_params.py">params</a>) -> <a href="./src/samsara/types/beta/fleet/hos/drivers/eld_event_list_response.py">EldEventListResponse</a></code>

### Trailers

#### Stats

Types:

```python
from samsara.types.beta.fleet.trailers import (
    StatListResponse,
    StatFeedResponse,
    StatHistoryResponse,
)
```

Methods:

- <code title="get /beta/fleet/trailers/stats">client.beta.fleet.trailers.stats.<a href="./src/samsara/resources/beta/fleet/trailers/stats.py">list</a>(\*\*<a href="src/samsara/types/beta/fleet/trailers/stat_list_params.py">params</a>) -> <a href="./src/samsara/types/beta/fleet/trailers/stat_list_response.py">StatListResponse</a></code>
- <code title="get /beta/fleet/trailers/stats/feed">client.beta.fleet.trailers.stats.<a href="./src/samsara/resources/beta/fleet/trailers/stats.py">feed</a>(\*\*<a href="src/samsara/types/beta/fleet/trailers/stat_feed_params.py">params</a>) -> <a href="./src/samsara/types/beta/fleet/trailers/stat_feed_response.py">StatFeedResponse</a></code>
- <code title="get /beta/fleet/trailers/stats/history">client.beta.fleet.trailers.stats.<a href="./src/samsara/resources/beta/fleet/trailers/stats.py">history</a>(\*\*<a href="src/samsara/types/beta/fleet/trailers/stat_history_params.py">params</a>) -> <a href="./src/samsara/types/beta/fleet/trailers/stat_history_response.py">StatHistoryResponse</a></code>

### Vehicles

#### Immobilizer

Methods:

- <code title="patch /beta/fleet/vehicles/{id}/immobilizer">client.beta.fleet.vehicles.immobilizer.<a href="./src/samsara/resources/beta/fleet/vehicles/immobilizer.py">update</a>(id, \*\*<a href="src/samsara/types/beta/fleet/vehicles/immobilizer_update_params.py">params</a>) -> None</code>

## Industrial

### Jobs

Types:

```python
from samsara.types.beta.industrial import (
    Job,
    JobCreateResponse,
    JobUpdateResponse,
    JobDeleteResponse,
)
```

Methods:

- <code title="post /beta/industrial/jobs">client.beta.industrial.jobs.<a href="./src/samsara/resources/beta/industrial/jobs.py">create</a>(\*\*<a href="src/samsara/types/beta/industrial/job_create_params.py">params</a>) -> <a href="./src/samsara/types/beta/industrial/job_create_response.py">JobCreateResponse</a></code>
- <code title="patch /beta/industrial/jobs">client.beta.industrial.jobs.<a href="./src/samsara/resources/beta/industrial/jobs.py">update</a>(\*\*<a href="src/samsara/types/beta/industrial/job_update_params.py">params</a>) -> <a href="./src/samsara/types/beta/industrial/job_update_response.py">JobUpdateResponse</a></code>
- <code title="get /beta/industrial/jobs">client.beta.industrial.jobs.<a href="./src/samsara/resources/beta/industrial/jobs.py">list</a>(\*\*<a href="src/samsara/types/beta/industrial/job_list_params.py">params</a>) -> <a href="./src/samsara/types/beta/industrial/job.py">Job</a></code>
- <code title="delete /beta/industrial/jobs">client.beta.industrial.jobs.<a href="./src/samsara/resources/beta/industrial/jobs.py">delete</a>(\*\*<a href="src/samsara/types/beta/industrial/job_delete_params.py">params</a>) -> <a href="./src/samsara/types/beta/industrial/job_delete_response.py">JobDeleteResponse</a></code>

# Cameras

## Media

### Retrieval

Types:

```python
from samsara.types.cameras.media import RetrievalCreateResponse, RetrievalRetrieveResponse
```

Methods:

- <code title="post /cameras/media/retrieval">client.cameras.media.retrieval.<a href="./src/samsara/resources/cameras/media/retrieval.py">create</a>(\*\*<a href="src/samsara/types/cameras/media/retrieval_create_params.py">params</a>) -> <a href="./src/samsara/types/cameras/media/retrieval_create_response.py">RetrievalCreateResponse</a></code>
- <code title="get /cameras/media/retrieval">client.cameras.media.retrieval.<a href="./src/samsara/resources/cameras/media/retrieval.py">retrieve</a>(\*\*<a href="src/samsara/types/cameras/media/retrieval_retrieve_params.py">params</a>) -> <a href="./src/samsara/types/cameras/media/retrieval_retrieve_response.py">RetrievalRetrieveResponse</a></code>

# Coaching

## DriverCoachAssignments

Types:

```python
from samsara.types.coaching import (
    DriverCoachAssignmentUpdateResponse,
    DriverCoachAssignmentListResponse,
)
```

Methods:

- <code title="put /coaching/driver-coach-assignments">client.coaching.driver_coach_assignments.<a href="./src/samsara/resources/coaching/driver_coach_assignments.py">update</a>(\*\*<a href="src/samsara/types/coaching/driver_coach_assignment_update_params.py">params</a>) -> <a href="./src/samsara/types/coaching/driver_coach_assignment_update_response.py">DriverCoachAssignmentUpdateResponse</a></code>
- <code title="get /coaching/driver-coach-assignments">client.coaching.driver_coach_assignments.<a href="./src/samsara/resources/coaching/driver_coach_assignments.py">list</a>(\*\*<a href="src/samsara/types/coaching/driver_coach_assignment_list_params.py">params</a>) -> <a href="./src/samsara/types/coaching/driver_coach_assignment_list_response.py">DriverCoachAssignmentListResponse</a></code>

## Sessions

Types:

```python
from samsara.types.coaching import SessionStreamResponse
```

Methods:

- <code title="get /coaching/sessions/stream">client.coaching.sessions.<a href="./src/samsara/resources/coaching/sessions.py">stream</a>(\*\*<a href="src/samsara/types/coaching/session_stream_params.py">params</a>) -> <a href="./src/samsara/types/coaching/session_stream_response.py">SessionStreamResponse</a></code>

# Contacts

Types:

```python
from samsara.types import Contact, ContactListResponse, ContactDeleteResponse
```

Methods:

- <code title="post /contacts">client.contacts.<a href="./src/samsara/resources/contacts.py">create</a>(\*\*<a href="src/samsara/types/contact_create_params.py">params</a>) -> <a href="./src/samsara/types/contact.py">Contact</a></code>
- <code title="get /contacts/{id}">client.contacts.<a href="./src/samsara/resources/contacts.py">retrieve</a>(id) -> <a href="./src/samsara/types/contact.py">Contact</a></code>
- <code title="patch /contacts/{id}">client.contacts.<a href="./src/samsara/resources/contacts.py">update</a>(id, \*\*<a href="src/samsara/types/contact_update_params.py">params</a>) -> <a href="./src/samsara/types/contact.py">Contact</a></code>
- <code title="get /contacts">client.contacts.<a href="./src/samsara/resources/contacts.py">list</a>(\*\*<a href="src/samsara/types/contact_list_params.py">params</a>) -> <a href="./src/samsara/types/contact_list_response.py">ContactListResponse</a></code>
- <code title="delete /contacts/{id}">client.contacts.<a href="./src/samsara/resources/contacts.py">delete</a>(id) -> str</code>

# DefectTypes

Types:

```python
from samsara.types import DefectTypeListResponse
```

Methods:

- <code title="get /defect-types">client.defect_types.<a href="./src/samsara/resources/defect_types.py">list</a>(\*\*<a href="src/samsara/types/defect_type_list_params.py">params</a>) -> <a href="./src/samsara/types/defect_type_list_response.py">DefectTypeListResponse</a></code>

# Defects

Types:

```python
from samsara.types import DefectStreamResponse
```

Methods:

- <code title="get /defects/stream">client.defects.<a href="./src/samsara/resources/defects.py">stream</a>(\*\*<a href="src/samsara/types/defect_stream_params.py">params</a>) -> <a href="./src/samsara/types/defect_stream_response.py">DefectStreamResponse</a></code>

# DriverTrailerAssignments

Types:

```python
from samsara.types import (
    DriverTrailerAssignmentCreateResponse,
    DriverTrailerAssignmentUpdateResponse,
    DriverTrailerAssignmentListResponse,
)
```

Methods:

- <code title="post /driver-trailer-assignments">client.driver_trailer_assignments.<a href="./src/samsara/resources/driver_trailer_assignments.py">create</a>(\*\*<a href="src/samsara/types/driver_trailer_assignment_create_params.py">params</a>) -> <a href="./src/samsara/types/driver_trailer_assignment_create_response.py">DriverTrailerAssignmentCreateResponse</a></code>
- <code title="patch /driver-trailer-assignments">client.driver_trailer_assignments.<a href="./src/samsara/resources/driver_trailer_assignments.py">update</a>(\*\*<a href="src/samsara/types/driver_trailer_assignment_update_params.py">params</a>) -> <a href="./src/samsara/types/driver_trailer_assignment_update_response.py">DriverTrailerAssignmentUpdateResponse</a></code>
- <code title="get /driver-trailer-assignments">client.driver_trailer_assignments.<a href="./src/samsara/resources/driver_trailer_assignments.py">list</a>(\*\*<a href="src/samsara/types/driver_trailer_assignment_list_params.py">params</a>) -> <a href="./src/samsara/types/driver_trailer_assignment_list_response.py">DriverTrailerAssignmentListResponse</a></code>

# Drivers

## QrCodes

Types:

```python
from samsara.types.drivers import QrCodeCreateResponse, QrCodeListResponse
```

Methods:

- <code title="post /drivers/qr-codes">client.drivers.qr_codes.<a href="./src/samsara/resources/drivers/qr_codes.py">create</a>(\*\*<a href="src/samsara/types/drivers/qr_code_create_params.py">params</a>) -> <a href="./src/samsara/types/drivers/qr_code_create_response.py">QrCodeCreateResponse</a></code>
- <code title="get /drivers/qr-codes">client.drivers.qr_codes.<a href="./src/samsara/resources/drivers/qr_codes.py">list</a>(\*\*<a href="src/samsara/types/drivers/qr_code_list_params.py">params</a>) -> <a href="./src/samsara/types/drivers/qr_code_list_response.py">QrCodeListResponse</a></code>
- <code title="delete /drivers/qr-codes">client.drivers.qr_codes.<a href="./src/samsara/resources/drivers/qr_codes.py">revoke</a>(\*\*<a href="src/samsara/types/drivers/qr_code_revoke_params.py">params</a>) -> None</code>

# Dvirs

Types:

```python
from samsara.types import DvirStreamResponse
```

Methods:

- <code title="get /dvirs/stream">client.dvirs.<a href="./src/samsara/resources/dvirs.py">stream</a>(\*\*<a href="src/samsara/types/dvir_stream_params.py">params</a>) -> <a href="./src/samsara/types/dvir_stream_response.py">DvirStreamResponse</a></code>

# Fleet

## CarrierProposedAssignments

Types:

```python
from samsara.types.fleet import (
    CarrierProposedAssignmentCreateResponse,
    CarrierProposedAssignmentListResponse,
    CarrierProposedAssignmentDeleteResponse,
)
```

Methods:

- <code title="post /fleet/carrier-proposed-assignments">client.fleet.carrier_proposed_assignments.<a href="./src/samsara/resources/fleet/carrier_proposed_assignments.py">create</a>(\*\*<a href="src/samsara/types/fleet/carrier_proposed_assignment_create_params.py">params</a>) -> <a href="./src/samsara/types/fleet/carrier_proposed_assignment_create_response.py">CarrierProposedAssignmentCreateResponse</a></code>
- <code title="get /fleet/carrier-proposed-assignments">client.fleet.carrier_proposed_assignments.<a href="./src/samsara/resources/fleet/carrier_proposed_assignments.py">list</a>(\*\*<a href="src/samsara/types/fleet/carrier_proposed_assignment_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/carrier_proposed_assignment_list_response.py">CarrierProposedAssignmentListResponse</a></code>
- <code title="delete /fleet/carrier-proposed-assignments/{id}">client.fleet.carrier_proposed_assignments.<a href="./src/samsara/resources/fleet/carrier_proposed_assignments.py">delete</a>(id) -> str</code>

## Defects

Types:

```python
from samsara.types.fleet import DefectUpdateResponse
```

Methods:

- <code title="patch /fleet/defects/{id}">client.fleet.defects.<a href="./src/samsara/resources/fleet/defects/defects.py">update</a>(id, \*\*<a href="src/samsara/types/fleet/defect_update_params.py">params</a>) -> <a href="./src/samsara/types/fleet/defect_update_response.py">DefectUpdateResponse</a></code>

### History

Types:

```python
from samsara.types.fleet.defects import HistoryListResponse
```

Methods:

- <code title="get /fleet/defects/history">client.fleet.defects.history.<a href="./src/samsara/resources/fleet/defects/history.py">list</a>(\*\*<a href="src/samsara/types/fleet/defects/history_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/defects/history_list_response.py">HistoryListResponse</a></code>

## DocumentTypes

Types:

```python
from samsara.types.fleet import DocumentTypeListResponse
```

Methods:

- <code title="get /fleet/document-types">client.fleet.document_types.<a href="./src/samsara/resources/fleet/document_types.py">list</a>(\*\*<a href="src/samsara/types/fleet/document_type_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/document_type_list_response.py">DocumentTypeListResponse</a></code>

## Documents

Types:

```python
from samsara.types.fleet import (
    DocumentCreateResponse,
    DocumentRetrieveResponse,
    DocumentListResponse,
)
```

Methods:

- <code title="post /fleet/documents">client.fleet.documents.<a href="./src/samsara/resources/fleet/documents/documents.py">create</a>(\*\*<a href="src/samsara/types/fleet/document_create_params.py">params</a>) -> <a href="./src/samsara/types/fleet/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="get /fleet/documents/{id}">client.fleet.documents.<a href="./src/samsara/resources/fleet/documents/documents.py">retrieve</a>(id) -> <a href="./src/samsara/types/fleet/document_retrieve_response.py">DocumentRetrieveResponse</a></code>
- <code title="get /fleet/documents">client.fleet.documents.<a href="./src/samsara/resources/fleet/documents/documents.py">list</a>(\*\*<a href="src/samsara/types/fleet/document_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /fleet/documents/{id}">client.fleet.documents.<a href="./src/samsara/resources/fleet/documents/documents.py">delete</a>(id) -> None</code>

### Pdfs

Types:

```python
from samsara.types.fleet.documents import PdfCreateResponse, PdfRetrieveResponse
```

Methods:

- <code title="post /fleet/documents/pdfs">client.fleet.documents.pdfs.<a href="./src/samsara/resources/fleet/documents/pdfs.py">create</a>(\*\*<a href="src/samsara/types/fleet/documents/pdf_create_params.py">params</a>) -> <a href="./src/samsara/types/fleet/documents/pdf_create_response.py">PdfCreateResponse</a></code>
- <code title="get /fleet/documents/pdfs/{id}">client.fleet.documents.pdfs.<a href="./src/samsara/resources/fleet/documents/pdfs.py">retrieve</a>(id) -> <a href="./src/samsara/types/fleet/documents/pdf_retrieve_response.py">PdfRetrieveResponse</a></code>

## DriverVehicleAssignments

Types:

```python
from samsara.types.fleet import (
    DriverVehicleAssignmentCreateResponse,
    DriverVehicleAssignmentUpdateResponse,
    DriverVehicleAssignmentListResponse,
)
```

Methods:

- <code title="post /fleet/driver-vehicle-assignments">client.fleet.driver_vehicle_assignments.<a href="./src/samsara/resources/fleet/driver_vehicle_assignments.py">create</a>(\*\*<a href="src/samsara/types/fleet/driver_vehicle_assignment_create_params.py">params</a>) -> <a href="./src/samsara/types/fleet/driver_vehicle_assignment_create_response.py">DriverVehicleAssignmentCreateResponse</a></code>
- <code title="patch /fleet/driver-vehicle-assignments">client.fleet.driver_vehicle_assignments.<a href="./src/samsara/resources/fleet/driver_vehicle_assignments.py">update</a>(\*\*<a href="src/samsara/types/fleet/driver_vehicle_assignment_update_params.py">params</a>) -> <a href="./src/samsara/types/fleet/driver_vehicle_assignment_update_response.py">DriverVehicleAssignmentUpdateResponse</a></code>
- <code title="get /fleet/driver-vehicle-assignments">client.fleet.driver_vehicle_assignments.<a href="./src/samsara/resources/fleet/driver_vehicle_assignments.py">list</a>(\*\*<a href="src/samsara/types/fleet/driver_vehicle_assignment_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/driver_vehicle_assignment_list_response.py">DriverVehicleAssignmentListResponse</a></code>
- <code title="delete /fleet/driver-vehicle-assignments">client.fleet.driver_vehicle_assignments.<a href="./src/samsara/resources/fleet/driver_vehicle_assignments.py">delete</a>(\*\*<a href="src/samsara/types/fleet/driver_vehicle_assignment_delete_params.py">params</a>) -> None</code>

## Drivers

Types:

```python
from samsara.types.fleet import Driver, DriverListResponse
```

Methods:

- <code title="post /fleet/drivers">client.fleet.drivers.<a href="./src/samsara/resources/fleet/drivers/drivers.py">create</a>(\*\*<a href="src/samsara/types/fleet/driver_create_params.py">params</a>) -> <a href="./src/samsara/types/fleet/driver.py">Driver</a></code>
- <code title="get /fleet/drivers/{id}">client.fleet.drivers.<a href="./src/samsara/resources/fleet/drivers/drivers.py">retrieve</a>(id) -> <a href="./src/samsara/types/fleet/driver.py">Driver</a></code>
- <code title="patch /fleet/drivers/{id}">client.fleet.drivers.<a href="./src/samsara/resources/fleet/drivers/drivers.py">update</a>(id, \*\*<a href="src/samsara/types/fleet/driver_update_params.py">params</a>) -> <a href="./src/samsara/types/fleet/driver.py">Driver</a></code>
- <code title="get /fleet/drivers">client.fleet.drivers.<a href="./src/samsara/resources/fleet/drivers/drivers.py">list</a>(\*\*<a href="src/samsara/types/fleet/driver_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/driver_list_response.py">DriverListResponse</a></code>

### TachographActivity

#### History

Types:

```python
from samsara.types.fleet.drivers.tachograph_activity import HistoryListResponse
```

Methods:

- <code title="get /fleet/drivers/tachograph-activity/history">client.fleet.drivers.tachograph_activity.history.<a href="./src/samsara/resources/fleet/drivers/tachograph_activity/history.py">list</a>(\*\*<a href="src/samsara/types/fleet/drivers/tachograph_activity/history_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/drivers/tachograph_activity/history_list_response.py">HistoryListResponse</a></code>

### TachographFiles

#### History

Types:

```python
from samsara.types.fleet.drivers.tachograph_files import HistoryListResponse
```

Methods:

- <code title="get /fleet/drivers/tachograph-files/history">client.fleet.drivers.tachograph_files.history.<a href="./src/samsara/resources/fleet/drivers/tachograph_files/history.py">list</a>(\*\*<a href="src/samsara/types/fleet/drivers/tachograph_files/history_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/drivers/tachograph_files/history_list_response.py">HistoryListResponse</a></code>

### Safety

Types:

```python
from samsara.types.fleet.drivers import V1DriverSafetyScoreResponse
```

Methods:

- <code title="get /v1/fleet/drivers/{driverId}/safety/score">client.fleet.drivers.safety.<a href="./src/samsara/resources/fleet/drivers/safety.py">score</a>(driver_id, \*\*<a href="src/samsara/types/fleet/drivers/safety_score_params.py">params</a>) -> <a href="./src/samsara/types/fleet/drivers/v1_driver_safety_score_response.py">V1DriverSafetyScoreResponse</a></code>

### Hos

Methods:

- <code title="post /v1/fleet/drivers/{driver_id}/hos/duty_status">client.fleet.drivers.hos.<a href="./src/samsara/resources/fleet/drivers/hos.py">duty_status</a>(driver_id, \*\*<a href="src/samsara/types/fleet/drivers/ho_duty_status_params.py">params</a>) -> None</code>

## Dvirs

Types:

```python
from samsara.types.fleet import DvirCreateResponse, DvirResolveResponse
```

Methods:

- <code title="post /fleet/dvirs">client.fleet.dvirs.<a href="./src/samsara/resources/fleet/dvirs/dvirs.py">create</a>(\*\*<a href="src/samsara/types/fleet/dvir_create_params.py">params</a>) -> <a href="./src/samsara/types/fleet/dvir_create_response.py">DvirCreateResponse</a></code>
- <code title="patch /fleet/dvirs/{id}">client.fleet.dvirs.<a href="./src/samsara/resources/fleet/dvirs/dvirs.py">resolve</a>(id, \*\*<a href="src/samsara/types/fleet/dvir_resolve_params.py">params</a>) -> <a href="./src/samsara/types/fleet/dvir_resolve_response.py">DvirResolveResponse</a></code>

### History

Types:

```python
from samsara.types.fleet.dvirs import HistoryListResponse
```

Methods:

- <code title="get /fleet/dvirs/history">client.fleet.dvirs.history.<a href="./src/samsara/resources/fleet/dvirs/history.py">list</a>(\*\*<a href="src/samsara/types/fleet/dvirs/history_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/dvirs/history_list_response.py">HistoryListResponse</a></code>

## Equipment

Types:

```python
from samsara.types.fleet import Equipment, EquipmentListResponse
```

Methods:

- <code title="get /fleet/equipment">client.fleet.equipment.<a href="./src/samsara/resources/fleet/equipment/equipment.py">list</a>(\*\*<a href="src/samsara/types/fleet/equipment_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/equipment_list_response.py">EquipmentListResponse</a></code>

### Locations

Types:

```python
from samsara.types.fleet.equipment import LocationListResponse
```

Methods:

- <code title="get /fleet/equipment/locations">client.fleet.equipment.locations.<a href="./src/samsara/resources/fleet/equipment/locations.py">list</a>(\*\*<a href="src/samsara/types/fleet/equipment/location_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/equipment/location_list_response.py">LocationListResponse</a></code>

## Reports

### DriversFuelEnergy

Types:

```python
from samsara.types.fleet.reports import DriversFuelEnergyListResponse
```

Methods:

- <code title="get /fleet/reports/drivers/fuel-energy">client.fleet.reports.drivers_fuel_energy.<a href="./src/samsara/resources/fleet/reports/drivers_fuel_energy.py">list</a>(\*\*<a href="src/samsara/types/fleet/reports/drivers_fuel_energy_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/reports/drivers_fuel_energy_list_response.py">DriversFuelEnergyListResponse</a></code>

### IftaJurisdiction

Types:

```python
from samsara.types.fleet.reports import IftaJurisdictionListResponse
```

Methods:

- <code title="get /fleet/reports/ifta/jurisdiction">client.fleet.reports.ifta_jurisdiction.<a href="./src/samsara/resources/fleet/reports/ifta_jurisdiction.py">list</a>(\*\*<a href="src/samsara/types/fleet/reports/ifta_jurisdiction_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/reports/ifta_jurisdiction_list_response.py">IftaJurisdictionListResponse</a></code>

### IftaVehicle

Types:

```python
from samsara.types.fleet.reports import IftaVehicleListResponse
```

Methods:

- <code title="get /fleet/reports/ifta/vehicle">client.fleet.reports.ifta_vehicle.<a href="./src/samsara/resources/fleet/reports/ifta_vehicle.py">list</a>(\*\*<a href="src/samsara/types/fleet/reports/ifta_vehicle_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/reports/ifta_vehicle_list_response.py">IftaVehicleListResponse</a></code>

### VehicleIdling

Types:

```python
from samsara.types.fleet.reports import VehicleIdlingListResponse
```

Methods:

- <code title="get /fleet/reports/vehicle/idling">client.fleet.reports.vehicle_idling.<a href="./src/samsara/resources/fleet/reports/vehicle_idling.py">list</a>(\*\*<a href="src/samsara/types/fleet/reports/vehicle_idling_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/reports/vehicle_idling_list_response.py">VehicleIdlingListResponse</a></code>

### VehiclesFuelEnergy

Types:

```python
from samsara.types.fleet.reports import VehiclesFuelEnergyListResponse
```

Methods:

- <code title="get /fleet/reports/vehicles/fuel-energy">client.fleet.reports.vehicles_fuel_energy.<a href="./src/samsara/resources/fleet/reports/vehicles_fuel_energy.py">list</a>(\*\*<a href="src/samsara/types/fleet/reports/vehicles_fuel_energy_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/reports/vehicles_fuel_energy_list_response.py">VehiclesFuelEnergyListResponse</a></code>

## Routes

Types:

```python
from samsara.types.fleet import (
    RoutesPatchRouteResponseBody,
    RouteCreateResponse,
    RouteRetrieveResponse,
    RouteListResponse,
)
```

Methods:

- <code title="post /fleet/routes">client.fleet.routes.<a href="./src/samsara/resources/fleet/routes/routes.py">create</a>(\*\*<a href="src/samsara/types/fleet/route_create_params.py">params</a>) -> <a href="./src/samsara/types/fleet/route_create_response.py">RouteCreateResponse</a></code>
- <code title="get /fleet/routes/{id}">client.fleet.routes.<a href="./src/samsara/resources/fleet/routes/routes.py">retrieve</a>(id) -> <a href="./src/samsara/types/fleet/route_retrieve_response.py">RouteRetrieveResponse</a></code>
- <code title="patch /fleet/routes/{id}">client.fleet.routes.<a href="./src/samsara/resources/fleet/routes/routes.py">update</a>(id, \*\*<a href="src/samsara/types/fleet/route_update_params.py">params</a>) -> <a href="./src/samsara/types/fleet/routes_patch_route_response_body.py">RoutesPatchRouteResponseBody</a></code>
- <code title="get /fleet/routes">client.fleet.routes.<a href="./src/samsara/resources/fleet/routes/routes.py">list</a>(\*\*<a href="src/samsara/types/fleet/route_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/route_list_response.py">RouteListResponse</a></code>
- <code title="delete /fleet/routes/{id}">client.fleet.routes.<a href="./src/samsara/resources/fleet/routes/routes.py">delete</a>(id) -> None</code>

### AuditLogs

Types:

```python
from samsara.types.fleet.routes import AuditLogFeedResponse
```

Methods:

- <code title="get /fleet/routes/audit-logs/feed">client.fleet.routes.audit_logs.<a href="./src/samsara/resources/fleet/routes/audit_logs.py">feed</a>(\*\*<a href="src/samsara/types/fleet/routes/audit_log_feed_params.py">params</a>) -> <a href="./src/samsara/types/fleet/routes/audit_log_feed_response.py">AuditLogFeedResponse</a></code>

## SafetyEvents

Types:

```python
from samsara.types.fleet import SafetyEventsListResponse
```

Methods:

- <code title="get /fleet/safety-events">client.fleet.safety_events.<a href="./src/samsara/resources/fleet/safety_events/safety_events.py">list</a>(\*\*<a href="src/samsara/types/fleet/safety_event_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/safety_events_list_response.py">SafetyEventsListResponse</a></code>

### AuditLogs

Types:

```python
from samsara.types.fleet.safety_events import SafetyEventsGetSafetyActivityEventFeedResponseBody
```

Methods:

- <code title="get /fleet/safety-events/audit-logs/feed">client.fleet.safety_events.audit_logs.<a href="./src/samsara/resources/fleet/safety_events/audit_logs.py">feed</a>(\*\*<a href="src/samsara/types/fleet/safety_events/audit_log_feed_params.py">params</a>) -> <a href="./src/samsara/types/fleet/safety_events/safety_events_get_safety_activity_event_feed_response_body.py">SafetyEventsGetSafetyActivityEventFeedResponseBody</a></code>

## Settings

### Compliance

Types:

```python
from samsara.types.fleet.settings import (
    SettingsGetComplianceSettingsResponseBody,
    SettingsPatchComplianceSettingsResponseBody,
)
```

Methods:

- <code title="get /fleet/settings/compliance">client.fleet.settings.compliance.<a href="./src/samsara/resources/fleet/settings/compliance.py">retrieve</a>() -> <a href="./src/samsara/types/fleet/settings/settings_get_compliance_settings_response_body.py">SettingsGetComplianceSettingsResponseBody</a></code>
- <code title="patch /fleet/settings/compliance">client.fleet.settings.compliance.<a href="./src/samsara/resources/fleet/settings/compliance.py">update</a>(\*\*<a href="src/samsara/types/fleet/settings/compliance_update_params.py">params</a>) -> <a href="./src/samsara/types/fleet/settings/settings_patch_compliance_settings_response_body.py">SettingsPatchComplianceSettingsResponseBody</a></code>

### DriverApp

Types:

```python
from samsara.types.fleet.settings import (
    SettingsGetDriverAppSettingsResponseBody,
    SettingsPatchDriverAppSettingsResponseBody,
)
```

Methods:

- <code title="get /fleet/settings/driver-app">client.fleet.settings.driver_app.<a href="./src/samsara/resources/fleet/settings/driver_app.py">retrieve</a>() -> <a href="./src/samsara/types/fleet/settings/settings_get_driver_app_settings_response_body.py">SettingsGetDriverAppSettingsResponseBody</a></code>
- <code title="patch /fleet/settings/driver-app">client.fleet.settings.driver_app.<a href="./src/samsara/resources/fleet/settings/driver_app.py">update</a>(\*\*<a href="src/samsara/types/fleet/settings/driver_app_update_params.py">params</a>) -> <a href="./src/samsara/types/fleet/settings/settings_patch_driver_app_settings_response_body.py">SettingsPatchDriverAppSettingsResponseBody</a></code>

### Safety

Types:

```python
from samsara.types.fleet.settings import SafetySettingsGetSafetySettingsResponseBody
```

Methods:

- <code title="get /fleet/settings/safety">client.fleet.settings.safety.<a href="./src/samsara/resources/fleet/settings/safety.py">retrieve</a>() -> <a href="./src/samsara/types/fleet/settings/safety_settings_get_safety_settings_response_body.py">SafetySettingsGetSafetySettingsResponseBody</a></code>

## Trailers

Types:

```python
from samsara.types.fleet import (
    TrailersCreateTrailerResponseBody,
    TrailersGetTrailerResponseBody,
    TrailersListTrailersResponseBody,
    TrailersUpdateTrailerResponseBody,
)
```

Methods:

- <code title="post /fleet/trailers">client.fleet.trailers.<a href="./src/samsara/resources/fleet/trailers/trailers.py">create</a>(\*\*<a href="src/samsara/types/fleet/trailer_create_params.py">params</a>) -> <a href="./src/samsara/types/fleet/trailers_create_trailer_response_body.py">TrailersCreateTrailerResponseBody</a></code>
- <code title="get /fleet/trailers">client.fleet.trailers.<a href="./src/samsara/resources/fleet/trailers/trailers.py">list</a>(\*\*<a href="src/samsara/types/fleet/trailer_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/trailers_list_trailers_response_body.py">TrailersListTrailersResponseBody</a></code>

### Assignments

Types:

```python
from samsara.types.fleet.trailers import InlineResponse200_7, V1TrailerAssignmentsResponse
```

## Vehicles

Types:

```python
from samsara.types.fleet import VehicleResponse, VehiclesListVehiclesResponseBody
```

Methods:

- <code title="get /fleet/vehicles/{id}">client.fleet.vehicles.<a href="./src/samsara/resources/fleet/vehicles/vehicles.py">retrieve</a>(id) -> <a href="./src/samsara/types/fleet/vehicle_response.py">VehicleResponse</a></code>
- <code title="patch /fleet/vehicles/{id}">client.fleet.vehicles.<a href="./src/samsara/resources/fleet/vehicles/vehicles.py">update</a>(id, \*\*<a href="src/samsara/types/fleet/vehicle_update_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicle_response.py">VehicleResponse</a></code>

### Stats

Types:

```python
from samsara.types.fleet.vehicles import VehicleStatsListResponse, VehicleStatsResponse
```

Methods:

- <code title="get /fleet/vehicles/stats/feed">client.fleet.vehicles.stats.<a href="./src/samsara/resources/fleet/vehicles/stats.py">feed</a>(\*\*<a href="src/samsara/types/fleet/vehicles/stat_feed_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicles/vehicle_stats_list_response.py">VehicleStatsListResponse</a></code>
- <code title="get /fleet/vehicles/stats/history">client.fleet.vehicles.stats.<a href="./src/samsara/resources/fleet/vehicles/stats.py">history</a>(\*\*<a href="src/samsara/types/fleet/vehicles/stat_history_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicles/vehicle_stats_list_response.py">VehicleStatsListResponse</a></code>

### TachographFiles

Types:

```python
from samsara.types.fleet.vehicles import TachographVehicleFilesResponse
```

Methods:

- <code title="get /fleet/vehicles/tachograph-files/history">client.fleet.vehicles.tachograph_files.<a href="./src/samsara/resources/fleet/vehicles/tachograph_files.py">history</a>(\*\*<a href="src/samsara/types/fleet/vehicles/tachograph_file_history_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicles/tachograph_vehicle_files_response.py">TachographVehicleFilesResponse</a></code>

### DriverAssignments

Types:

```python
from samsara.types.fleet.vehicles import (
    VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody,
)
```

### ImmobilizerStream

Types:

```python
from samsara.types.fleet.vehicles import EngineImmobilizerGetEngineImmobilizerStatesResponseBody
```

### Locations

Types:

```python
from samsara.types.fleet.vehicles import VehicleLocationsListResponse, VehicleLocationsResponse
```

### Safety

Types:

```python
from samsara.types.fleet.vehicles import V1VehicleHarshEventResponse, V1VehicleSafetyScoreResponse
```

## Assets

Types:

```python
from samsara.types.fleet import InlineResponse200_1, V1AssetLocationResponse, V1AssetReeferResponse
```

Methods:

- <code title="get /v1/fleet/assets">client.fleet.assets.<a href="./src/samsara/resources/fleet/assets/assets.py">list</a>() -> <a href="./src/samsara/types/fleet/inline_response_200_1.py">InlineResponse200_1</a></code>
- <code title="get /v1/fleet/assets/{asset_id}/reefer">client.fleet.assets.<a href="./src/samsara/resources/fleet/assets/assets.py">reefer</a>(asset_id, \*\*<a href="src/samsara/types/fleet/asset_reefer_params.py">params</a>) -> <a href="./src/samsara/types/fleet/v1_asset_reefer_response.py">V1AssetReeferResponse</a></code>

### Locations

Types:

```python
from samsara.types.fleet.assets import LocationListResponse
```

Methods:

- <code title="get /v1/fleet/assets/{asset_id}/locations">client.fleet.assets.locations.<a href="./src/samsara/resources/fleet/assets/locations.py">retrieve</a>(asset_id, \*\*<a href="src/samsara/types/fleet/assets/location_retrieve_params.py">params</a>) -> <a href="./src/samsara/types/fleet/v1_asset_location_response.py">V1AssetLocationResponse</a></code>
- <code title="get /v1/fleet/assets/locations">client.fleet.assets.locations.<a href="./src/samsara/resources/fleet/assets/locations.py">list</a>(\*\*<a href="src/samsara/types/fleet/assets/location_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/assets/location_list_response.py">LocationListResponse</a></code>

### Reefers

Types:

```python
from samsara.types.fleet.assets import ReeferListResponse
```

Methods:

- <code title="get /v1/fleet/assets/reefers">client.fleet.assets.reefers.<a href="./src/samsara/resources/fleet/assets/reefers.py">list</a>(\*\*<a href="src/samsara/types/fleet/assets/reefer_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/assets/reefer_list_response.py">ReeferListResponse</a></code>

## Dispatch

### Routes

Methods:

- <code title="delete /v1/fleet/dispatch/routes/{route_id_or_external_id}">client.fleet.dispatch.routes.<a href="./src/samsara/resources/fleet/dispatch/routes.py">delete</a>(route_id_or_external_id, \*\*<a href="src/samsara/types/fleet/dispatch/route_delete_params.py">params</a>) -> None</code>

## Maintenance

Types:

```python
from samsara.types.fleet import InlineResponse200_4
```

## Messages

Types:

```python
from samsara.types.fleet import InlineResponse200_5, InlineResponse200_6
```

## Trips

Types:

```python
from samsara.types.fleet import V1TripResponse
```

# Equipment

Methods:

- <code title="get /fleet/equipment/{id}">client.equipment.<a href="./src/samsara/resources/equipment/equipment.py">retrieve</a>(id) -> <a href="./src/samsara/types/fleet/equipment/equipment.py">Equipment</a></code>

## Locations

Types:

```python
from samsara.types.equipment import LocationFeedResponse, LocationHistoryResponse
```

Methods:

- <code title="get /fleet/equipment/locations/feed">client.equipment.locations.<a href="./src/samsara/resources/equipment/locations.py">feed</a>(\*\*<a href="src/samsara/types/equipment/location_feed_params.py">params</a>) -> <a href="./src/samsara/types/equipment/location_feed_response.py">LocationFeedResponse</a></code>
- <code title="get /fleet/equipment/locations/history">client.equipment.locations.<a href="./src/samsara/resources/equipment/locations.py">history</a>(\*\*<a href="src/samsara/types/equipment/location_history_params.py">params</a>) -> <a href="./src/samsara/types/equipment/location_history_response.py">LocationHistoryResponse</a></code>

## Stats

Types:

```python
from samsara.types.equipment import StatRetrieveResponse, StatFeedResponse, StatHistoryResponse
```

Methods:

- <code title="get /fleet/equipment/stats">client.equipment.stats.<a href="./src/samsara/resources/equipment/stats.py">retrieve</a>(\*\*<a href="src/samsara/types/equipment/stat_retrieve_params.py">params</a>) -> <a href="./src/samsara/types/equipment/stat_retrieve_response.py">StatRetrieveResponse</a></code>
- <code title="get /fleet/equipment/stats/feed">client.equipment.stats.<a href="./src/samsara/resources/equipment/stats.py">feed</a>(\*\*<a href="src/samsara/types/equipment/stat_feed_params.py">params</a>) -> <a href="./src/samsara/types/equipment/stat_feed_response.py">StatFeedResponse</a></code>
- <code title="get /fleet/equipment/stats/history">client.equipment.stats.<a href="./src/samsara/resources/equipment/stats.py">history</a>(\*\*<a href="src/samsara/types/equipment/stat_history_params.py">params</a>) -> <a href="./src/samsara/types/equipment/stat_history_response.py">StatHistoryResponse</a></code>

# Hos

## Clocks

Types:

```python
from samsara.types.hos import ClockListResponse
```

Methods:

- <code title="get /fleet/hos/clocks">client.hos.clocks.<a href="./src/samsara/resources/hos/clocks.py">list</a>(\*\*<a href="src/samsara/types/hos/clock_list_params.py">params</a>) -> <a href="./src/samsara/types/hos/clock_list_response.py">ClockListResponse</a></code>

## DailyLogs

Types:

```python
from samsara.types.hos import HosDailyLogsUpdateShippingDocsResponseBody, DailyLogListResponse
```

Methods:

- <code title="get /fleet/hos/daily-logs">client.hos.daily_logs.<a href="./src/samsara/resources/hos/daily_logs.py">list</a>(\*\*<a href="src/samsara/types/hos/daily_log_list_params.py">params</a>) -> <a href="./src/samsara/types/hos/daily_log_list_response.py">DailyLogListResponse</a></code>
- <code title="patch /hos/daily-logs/log-meta-data">client.hos.daily_logs.<a href="./src/samsara/resources/hos/daily_logs.py">update_log_metadata</a>(\*\*<a href="src/samsara/types/hos/daily_log_update_log_metadata_params.py">params</a>) -> <a href="./src/samsara/types/hos/hos_daily_logs_update_shipping_docs_response_body.py">HosDailyLogsUpdateShippingDocsResponseBody</a></code>

## Logs

Types:

```python
from samsara.types.hos import LogListResponse
```

Methods:

- <code title="get /fleet/hos/logs">client.hos.logs.<a href="./src/samsara/resources/hos/logs.py">list</a>(\*\*<a href="src/samsara/types/hos/log_list_params.py">params</a>) -> <a href="./src/samsara/types/hos/log_list_response.py">LogListResponse</a></code>

## Violations

Types:

```python
from samsara.types.hos import ViolationListResponse
```

Methods:

- <code title="get /fleet/hos/violations">client.hos.violations.<a href="./src/samsara/resources/hos/violations.py">list</a>(\*\*<a href="src/samsara/types/hos/violation_list_params.py">params</a>) -> <a href="./src/samsara/types/hos/violation_list_response.py">ViolationListResponse</a></code>

# Trailers

Methods:

- <code title="get /fleet/trailers/{id}">client.trailers.<a href="./src/samsara/resources/trailers/trailers.py">retrieve</a>(id) -> <a href="./src/samsara/types/fleet/trailers_get_trailer_response_body.py">TrailersGetTrailerResponseBody</a></code>
- <code title="patch /fleet/trailers/{id}">client.trailers.<a href="./src/samsara/resources/trailers/trailers.py">update</a>(id, \*\*<a href="src/samsara/types/trailer_update_params.py">params</a>) -> <a href="./src/samsara/types/fleet/trailers_update_trailer_response_body.py">TrailersUpdateTrailerResponseBody</a></code>
- <code title="delete /fleet/trailers/{id}">client.trailers.<a href="./src/samsara/resources/trailers/trailers.py">delete</a>(id) -> None</code>

## Assignments

Methods:

- <code title="get /v1/fleet/trailers/{trailerId}/assignments">client.trailers.assignments.<a href="./src/samsara/resources/trailers/assignments.py">retrieve</a>(trailer_id, \*\*<a href="src/samsara/types/trailers/assignment_retrieve_params.py">params</a>) -> <a href="./src/samsara/types/fleet/trailers/v1_trailer_assignments_response.py">V1TrailerAssignmentsResponse</a></code>
- <code title="get /v1/fleet/trailers/assignments">client.trailers.assignments.<a href="./src/samsara/resources/trailers/assignments.py">list</a>(\*\*<a href="src/samsara/types/trailers/assignment_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/trailers/inline_response_200_7.py">InlineResponse200_7</a></code>

# Vehicles

Methods:

- <code title="get /fleet/vehicles">client.vehicles.<a href="./src/samsara/resources/vehicles/vehicles.py">list</a>(\*\*<a href="src/samsara/types/vehicle_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicles_list_vehicles_response_body.py">VehiclesListVehiclesResponseBody</a></code>

## DriverAssignments

Methods:

- <code title="get /fleet/vehicles/driver-assignments">client.vehicles.driver_assignments.<a href="./src/samsara/resources/vehicles/driver_assignments.py">list</a>(\*\*<a href="src/samsara/types/vehicles/driver_assignment_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicles/vehicles_driver_assignments_get_vehicles_driver_assignments_response_body.py">VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody</a></code>

## ImmobilizerStream

Methods:

- <code title="get /fleet/vehicles/immobilizer/stream">client.vehicles.immobilizer_stream.<a href="./src/samsara/resources/vehicles/immobilizer_stream.py">list</a>(\*\*<a href="src/samsara/types/vehicles/immobilizer_stream_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicles/engine_immobilizer_get_engine_immobilizer_states_response_body.py">EngineImmobilizerGetEngineImmobilizerStatesResponseBody</a></code>

## Locations

Methods:

- <code title="get /fleet/vehicles/locations">client.vehicles.locations.<a href="./src/samsara/resources/vehicles/locations.py">list</a>(\*\*<a href="src/samsara/types/vehicles/location_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicles/vehicle_locations_response.py">VehicleLocationsResponse</a></code>
- <code title="get /fleet/vehicles/locations/feed">client.vehicles.locations.<a href="./src/samsara/resources/vehicles/locations.py">feed</a>(\*\*<a href="src/samsara/types/vehicles/location_feed_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicles/vehicle_locations_list_response.py">VehicleLocationsListResponse</a></code>
- <code title="get /fleet/vehicles/locations/history">client.vehicles.locations.<a href="./src/samsara/resources/vehicles/locations.py">history</a>(\*\*<a href="src/samsara/types/vehicles/location_history_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicles/vehicle_locations_list_response.py">VehicleLocationsListResponse</a></code>

## Stats

Methods:

- <code title="get /fleet/vehicles/stats">client.vehicles.stats.<a href="./src/samsara/resources/vehicles/stats.py">list</a>(\*\*<a href="src/samsara/types/vehicles/stat_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicles/vehicle_stats_response.py">VehicleStatsResponse</a></code>

## Safety

Methods:

- <code title="get /v1/fleet/vehicles/{vehicleId}/safety/harsh_event">client.vehicles.safety.<a href="./src/samsara/resources/vehicles/safety.py">harsh_event</a>(vehicle_id, \*\*<a href="src/samsara/types/vehicles/safety_harsh_event_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicles/v1_vehicle_harsh_event_response.py">V1VehicleHarshEventResponse</a></code>
- <code title="get /v1/fleet/vehicles/{vehicleId}/safety/score">client.vehicles.safety.<a href="./src/samsara/resources/vehicles/safety.py">score</a>(vehicle_id, \*\*<a href="src/samsara/types/vehicles/safety_score_params.py">params</a>) -> <a href="./src/samsara/types/fleet/vehicles/v1_vehicle_safety_score_response.py">V1VehicleSafetyScoreResponse</a></code>

# FormSubmissions

Types:

```python
from samsara.types import (
    FormSubmissionsGetFormSubmissionsResponseBody,
    FormSubmissionsPatchFormSubmissionResponseBody,
    FormSubmissionsPostFormSubmissionResponseBody,
    FormSubmissionStreamResponse,
)
```

Methods:

- <code title="post /form-submissions">client.form_submissions.<a href="./src/samsara/resources/form_submissions/form_submissions.py">create</a>(\*\*<a href="src/samsara/types/form_submission_create_params.py">params</a>) -> <a href="./src/samsara/types/form_submissions_post_form_submission_response_body.py">FormSubmissionsPostFormSubmissionResponseBody</a></code>
- <code title="patch /form-submissions">client.form_submissions.<a href="./src/samsara/resources/form_submissions/form_submissions.py">update</a>(\*\*<a href="src/samsara/types/form_submission_update_params.py">params</a>) -> <a href="./src/samsara/types/form_submissions_patch_form_submission_response_body.py">FormSubmissionsPatchFormSubmissionResponseBody</a></code>
- <code title="get /form-submissions">client.form_submissions.<a href="./src/samsara/resources/form_submissions/form_submissions.py">list</a>(\*\*<a href="src/samsara/types/form_submission_list_params.py">params</a>) -> <a href="./src/samsara/types/form_submissions_get_form_submissions_response_body.py">FormSubmissionsGetFormSubmissionsResponseBody</a></code>
- <code title="get /form-submissions/stream">client.form_submissions.<a href="./src/samsara/resources/form_submissions/form_submissions.py">stream</a>(\*\*<a href="src/samsara/types/form_submission_stream_params.py">params</a>) -> <a href="./src/samsara/types/form_submission_stream_response.py">FormSubmissionStreamResponse</a></code>

## PdfExports

Types:

```python
from samsara.types.form_submissions import (
    FormSubmissionsGetFormSubmissionsPdfExportsResponseBody,
    FormSubmissionsPostFormSubmissionsPdfExportsResponseBody,
)
```

Methods:

- <code title="post /form-submissions/pdf-exports">client.form_submissions.pdf_exports.<a href="./src/samsara/resources/form_submissions/pdf_exports.py">create</a>(\*\*<a href="src/samsara/types/form_submissions/pdf_export_create_params.py">params</a>) -> <a href="./src/samsara/types/form_submissions/form_submissions_post_form_submissions_pdf_exports_response_body.py">FormSubmissionsPostFormSubmissionsPdfExportsResponseBody</a></code>
- <code title="get /form-submissions/pdf-exports">client.form_submissions.pdf_exports.<a href="./src/samsara/resources/form_submissions/pdf_exports.py">retrieve</a>(\*\*<a href="src/samsara/types/form_submissions/pdf_export_retrieve_params.py">params</a>) -> <a href="./src/samsara/types/form_submissions/form_submissions_get_form_submissions_pdf_exports_response_body.py">FormSubmissionsGetFormSubmissionsPdfExportsResponseBody</a></code>

# FuelPurchases

Types:

```python
from samsara.types import FuelPurchasePostFuelPurchaseResponseBody
```

Methods:

- <code title="post /fuel-purchase">client.fuel_purchases.<a href="./src/samsara/resources/fuel_purchases.py">create</a>(\*\*<a href="src/samsara/types/fuel_purchase_create_params.py">params</a>) -> <a href="./src/samsara/types/fuel_purchase_post_fuel_purchase_response_body.py">FuelPurchasePostFuelPurchaseResponseBody</a></code>

# Gateways

Types:

```python
from samsara.types import GatewaysGetGatewaysResponseBody, GatewaysPostGatewayResponseBody
```

Methods:

- <code title="get /gateways">client.gateways.<a href="./src/samsara/resources/gateways.py">list</a>(\*\*<a href="src/samsara/types/gateway_list_params.py">params</a>) -> <a href="./src/samsara/types/gateways_get_gateways_response_body.py">GatewaysGetGatewaysResponseBody</a></code>
- <code title="post /gateways">client.gateways.<a href="./src/samsara/resources/gateways.py">activate</a>(\*\*<a href="src/samsara/types/gateway_activate_params.py">params</a>) -> <a href="./src/samsara/types/gateways_post_gateway_response_body.py">GatewaysPostGatewayResponseBody</a></code>
- <code title="delete /gateways/{id}">client.gateways.<a href="./src/samsara/resources/gateways.py">deactivate</a>(id) -> None</code>

# IftaDetails

Types:

```python
from samsara.types import IftaCreateIftaDetailJobResponseBody, IftaGetIftaDetailJobResponseBody
```

Methods:

- <code title="post /ifta-detail/csv">client.ifta_details.<a href="./src/samsara/resources/ifta_details.py">create_csv_job</a>(\*\*<a href="src/samsara/types/ifta_detail_create_csv_job_params.py">params</a>) -> <a href="./src/samsara/types/ifta_create_ifta_detail_job_response_body.py">IftaCreateIftaDetailJobResponseBody</a></code>
- <code title="get /ifta-detail/csv/{id}">client.ifta_details.<a href="./src/samsara/resources/ifta_details.py">retrieve_csv_job</a>(id) -> <a href="./src/samsara/types/ifta_get_ifta_detail_job_response_body.py">IftaGetIftaDetailJobResponseBody</a></code>

# Industrial

## Assets

Types:

```python
from samsara.types.industrial import (
    InlineResponse200,
    ListIndustrialAssetsResponse,
    AssetDeleteResponse,
)
```

Methods:

- <code title="post /industrial/assets">client.industrial.assets.<a href="./src/samsara/resources/industrial/assets/assets.py">create</a>(\*\*<a href="src/samsara/types/industrial/asset_create_params.py">params</a>) -> <a href="./src/samsara/types/industrial/inline_response_200.py">InlineResponse200</a></code>
- <code title="patch /industrial/assets/{id}">client.industrial.assets.<a href="./src/samsara/resources/industrial/assets/assets.py">update</a>(id, \*\*<a href="src/samsara/types/industrial/asset_update_params.py">params</a>) -> <a href="./src/samsara/types/industrial/inline_response_200.py">InlineResponse200</a></code>
- <code title="get /industrial/assets">client.industrial.assets.<a href="./src/samsara/resources/industrial/assets/assets.py">list</a>(\*\*<a href="src/samsara/types/industrial/asset_list_params.py">params</a>) -> <a href="./src/samsara/types/industrial/list_industrial_assets_response.py">ListIndustrialAssetsResponse</a></code>
- <code title="delete /industrial/assets/{id}">client.industrial.assets.<a href="./src/samsara/resources/industrial/assets/assets.py">delete</a>(id) -> str</code>

### DataOutputs

Types:

```python
from samsara.types.industrial.assets import AssetDataOutputsPatchAssetDataOutputsResponseBody
```

Methods:

- <code title="patch /industrial/assets/{id}/data-outputs">client.industrial.assets.data_outputs.<a href="./src/samsara/resources/industrial/assets/data_outputs.py">update</a>(id, \*\*<a href="src/samsara/types/industrial/assets/data_output_update_params.py">params</a>) -> <a href="./src/samsara/types/industrial/assets/asset_data_outputs_patch_asset_data_outputs_response_body.py">AssetDataOutputsPatchAssetDataOutputsResponseBody</a></code>

## DataInputs

Types:

```python
from samsara.types.industrial import DataInputsTinyResponse
```

Methods:

- <code title="get /industrial/data-inputs">client.industrial.data_inputs.<a href="./src/samsara/resources/industrial/data_inputs/data_inputs.py">list</a>(\*\*<a href="src/samsara/types/industrial/data_input_list_params.py">params</a>) -> <a href="./src/samsara/types/industrial/data_inputs_tiny_response.py">DataInputsTinyResponse</a></code>

### DataPoints

Types:

```python
from samsara.types.industrial.data_inputs import DataInputListResponse, DataInputSnapshotResponse
```

Methods:

- <code title="get /industrial/data-inputs/data-points">client.industrial.data_inputs.data_points.<a href="./src/samsara/resources/industrial/data_inputs/data_points.py">retrieve</a>(\*\*<a href="src/samsara/types/industrial/data_inputs/data_point_retrieve_params.py">params</a>) -> <a href="./src/samsara/types/industrial/data_inputs/data_input_snapshot_response.py">DataInputSnapshotResponse</a></code>
- <code title="get /industrial/data-inputs/data-points/feed">client.industrial.data_inputs.data_points.<a href="./src/samsara/resources/industrial/data_inputs/data_points.py">feed</a>(\*\*<a href="src/samsara/types/industrial/data_inputs/data_point_feed_params.py">params</a>) -> <a href="./src/samsara/types/industrial/data_inputs/data_input_list_response.py">DataInputListResponse</a></code>
- <code title="get /industrial/data-inputs/data-points/history">client.industrial.data_inputs.data_points.<a href="./src/samsara/resources/industrial/data_inputs/data_points.py">history</a>(\*\*<a href="src/samsara/types/industrial/data_inputs/data_point_history_params.py">params</a>) -> <a href="./src/samsara/types/industrial/data_inputs/data_input_list_response.py">DataInputListResponse</a></code>

## Vision

### Cameras

#### Programs

Types:

```python
from samsara.types.industrial.vision.cameras import ProgramListResponse
```

Methods:

- <code title="get /v1/industrial/vision/cameras/{camera_id}/programs">client.industrial.vision.cameras.programs.<a href="./src/samsara/resources/industrial/vision/cameras/programs.py">list</a>(camera_id) -> <a href="./src/samsara/types/industrial/vision/cameras/program_list_response.py">ProgramListResponse</a></code>

### Runs

Types:

```python
from samsara.types.industrial.vision import (
    RunRetrieveResponse,
    RunListResponse,
    RunRetrievebycameraResponse,
    RunRetrievebycameraprogramResponse,
)
```

Methods:

- <code title="get /v1/industrial/vision/run/camera/{camera_id}">client.industrial.vision.runs.<a href="./src/samsara/resources/industrial/vision/runs.py">retrieve</a>(camera_id, \*\*<a href="src/samsara/types/industrial/vision/run_retrieve_params.py">params</a>) -> <a href="./src/samsara/types/industrial/vision/run_retrieve_response.py">RunRetrieveResponse</a></code>
- <code title="get /v1/industrial/vision/runs">client.industrial.vision.runs.<a href="./src/samsara/resources/industrial/vision/runs.py">list</a>(\*\*<a href="src/samsara/types/industrial/vision/run_list_params.py">params</a>) -> <a href="./src/samsara/types/industrial/vision/run_list_response.py">RunListResponse</a></code>
- <code title="get /v1/industrial/vision/runs/{camera_id}">client.industrial.vision.runs.<a href="./src/samsara/resources/industrial/vision/runs.py">retrievebycamera</a>(camera_id, \*\*<a href="src/samsara/types/industrial/vision/run_retrievebycamera_params.py">params</a>) -> <a href="./src/samsara/types/industrial/vision/run_retrievebycamera_response.py">RunRetrievebycameraResponse</a></code>
- <code title="get /v1/industrial/vision/runs/{camera_id}/{program_id}/{started_at_ms}">client.industrial.vision.runs.<a href="./src/samsara/resources/industrial/vision/runs.py">retrievebycameraprogram</a>(started_at_ms, \*, camera_id, program_id, \*\*<a href="src/samsara/types/industrial/vision/run_retrievebycameraprogram_params.py">params</a>) -> <a href="./src/samsara/types/industrial/vision/run_retrievebycameraprogram_response.py">RunRetrievebycameraprogramResponse</a></code>

# Issues

Types:

```python
from samsara.types import (
    IssuesGetIssuesResponseBody,
    IssuesGetIssuesStreamResponseBody,
    IssuesPatchIssueResponseBody,
)
```

Methods:

- <code title="patch /issues">client.issues.<a href="./src/samsara/resources/issues.py">update</a>(\*\*<a href="src/samsara/types/issue_update_params.py">params</a>) -> <a href="./src/samsara/types/issues_patch_issue_response_body.py">IssuesPatchIssueResponseBody</a></code>
- <code title="get /issues">client.issues.<a href="./src/samsara/resources/issues.py">list</a>(\*\*<a href="src/samsara/types/issue_list_params.py">params</a>) -> <a href="./src/samsara/types/issues_get_issues_response_body.py">IssuesGetIssuesResponseBody</a></code>
- <code title="get /issues/stream">client.issues.<a href="./src/samsara/resources/issues.py">stream</a>(\*\*<a href="src/samsara/types/issue_stream_params.py">params</a>) -> <a href="./src/samsara/types/issues_get_issues_stream_response_body.py">IssuesGetIssuesStreamResponseBody</a></code>

# LiveShares

Types:

```python
from samsara.types import LiveShareCreateResponse, LiveShareUpdateResponse, LiveShareListResponse
```

Methods:

- <code title="post /live-shares">client.live_shares.<a href="./src/samsara/resources/live_shares.py">create</a>(\*\*<a href="src/samsara/types/live_share_create_params.py">params</a>) -> <a href="./src/samsara/types/live_share_create_response.py">LiveShareCreateResponse</a></code>
- <code title="patch /live-shares">client.live_shares.<a href="./src/samsara/resources/live_shares.py">update</a>(\*\*<a href="src/samsara/types/live_share_update_params.py">params</a>) -> <a href="./src/samsara/types/live_share_update_response.py">LiveShareUpdateResponse</a></code>
- <code title="get /live-shares">client.live_shares.<a href="./src/samsara/resources/live_shares.py">list</a>(\*\*<a href="src/samsara/types/live_share_list_params.py">params</a>) -> <a href="./src/samsara/types/live_share_list_response.py">LiveShareListResponse</a></code>
- <code title="delete /live-shares">client.live_shares.<a href="./src/samsara/resources/live_shares.py">delete</a>(\*\*<a href="src/samsara/types/live_share_delete_params.py">params</a>) -> None</code>

# OrganizationInfo

Types:

```python
from samsara.types import OrganizationInfoResponse
```

Methods:

- <code title="get /me">client.organization_info.<a href="./src/samsara/resources/organization_info.py">retrieve</a>() -> <a href="./src/samsara/types/organization_info_response.py">OrganizationInfoResponse</a></code>

# Preview

## Cameras

### Media

Types:

```python
from samsara.types.preview.cameras import MediaRetrievalListUploadedMediaResponseBody
```

Methods:

- <code title="get /preview/cameras/media">client.preview.cameras.media.<a href="./src/samsara/resources/preview/cameras/media.py">list</a>(\*\*<a href="src/samsara/types/preview/cameras/media_list_params.py">params</a>) -> <a href="./src/samsara/types/preview/cameras/media_retrieval_list_uploaded_media_response_body.py">MediaRetrievalListUploadedMediaResponseBody</a></code>

## CustomReports

### Configs

Types:

```python
from samsara.types.preview.custom_reports import CustomReportsGetCustomReportConfigsResponseBody
```

Methods:

- <code title="get /preview/custom-reports/configs">client.preview.custom_reports.configs.<a href="./src/samsara/resources/preview/custom_reports/configs.py">list</a>(\*\*<a href="src/samsara/types/preview/custom_reports/config_list_params.py">params</a>) -> <a href="./src/samsara/types/preview/custom_reports/custom_reports_get_custom_report_configs_response_body.py">CustomReportsGetCustomReportConfigsResponseBody</a></code>

### Runs

Types:

```python
from samsara.types.preview.custom_reports import (
    CustomReportsGetCustomReportRunsResponseBody,
    CustomReportsPostCustomReportRunResponseBody,
)
```

Methods:

- <code title="post /preview/custom-reports/runs">client.preview.custom_reports.runs.<a href="./src/samsara/resources/preview/custom_reports/runs/runs.py">create</a>(\*\*<a href="src/samsara/types/preview/custom_reports/run_create_params.py">params</a>) -> <a href="./src/samsara/types/preview/custom_reports/custom_reports_post_custom_report_run_response_body.py">CustomReportsPostCustomReportRunResponseBody</a></code>
- <code title="get /preview/custom-reports/runs">client.preview.custom_reports.runs.<a href="./src/samsara/resources/preview/custom_reports/runs/runs.py">list</a>(\*\*<a href="src/samsara/types/preview/custom_reports/run_list_params.py">params</a>) -> <a href="./src/samsara/types/preview/custom_reports/custom_reports_get_custom_report_runs_response_body.py">CustomReportsGetCustomReportRunsResponseBody</a></code>

#### Data

Types:

```python
from samsara.types.preview.custom_reports.runs import (
    CustomReportsGetCustomReportRunDataResponseBody,
)
```

Methods:

- <code title="get /preview/custom-reports/runs/data">client.preview.custom_reports.runs.data.<a href="./src/samsara/resources/preview/custom_reports/runs/data.py">retrieve</a>(\*\*<a href="src/samsara/types/preview/custom_reports/runs/data_retrieve_params.py">params</a>) -> <a href="./src/samsara/types/preview/custom_reports/runs/custom_reports_get_custom_report_run_data_response_body.py">CustomReportsGetCustomReportRunDataResponseBody</a></code>

## DriverEfficiency

### Drivers

Types:

```python
from samsara.types.preview.driver_efficiency import (
    DriverEfficiencyGetDriverEfficiencyByDriversResponseBody,
)
```

Methods:

- <code title="get /preview/driver-efficiency/drivers">client.preview.driver_efficiency.drivers.<a href="./src/samsara/resources/preview/driver_efficiency/drivers.py">list</a>(\*\*<a href="src/samsara/types/preview/driver_efficiency/driver_list_params.py">params</a>) -> <a href="./src/samsara/types/preview/driver_efficiency/driver_efficiency_get_driver_efficiency_by_drivers_response_body.py">DriverEfficiencyGetDriverEfficiencyByDriversResponseBody</a></code>

### Vehicles

Types:

```python
from samsara.types.preview.driver_efficiency import (
    DriverEfficiencyGetDriverEfficiencyByVehiclesResponseBody,
)
```

Methods:

- <code title="get /preview/driver-efficiency/vehicles">client.preview.driver_efficiency.vehicles.<a href="./src/samsara/resources/preview/driver_efficiency/vehicles.py">list</a>(\*\*<a href="src/samsara/types/preview/driver_efficiency/vehicle_list_params.py">params</a>) -> <a href="./src/samsara/types/preview/driver_efficiency/driver_efficiency_get_driver_efficiency_by_vehicles_response_body.py">DriverEfficiencyGetDriverEfficiencyByVehiclesResponseBody</a></code>

## FormTemplates

Types:

```python
from samsara.types.preview import FormTemplatesGetFormTemplatesResponseBody
```

Methods:

- <code title="get /preview/form-templates">client.preview.form_templates.<a href="./src/samsara/resources/preview/form_templates.py">list</a>(\*\*<a href="src/samsara/types/preview/form_template_list_params.py">params</a>) -> <a href="./src/samsara/types/preview/form_templates_get_form_templates_response_body.py">FormTemplatesGetFormTemplatesResponseBody</a></code>

## TrainingAssignments

Types:

```python
from samsara.types.preview import TrainingAssignmentsPatchTrainingAssignmentsResponseBody
```

Methods:

- <code title="patch /preview/training-assignments">client.preview.training_assignments.<a href="./src/samsara/resources/preview/training_assignments.py">update</a>(\*\*<a href="src/samsara/types/preview/training_assignment_update_params.py">params</a>) -> <a href="./src/samsara/types/preview/training_assignments_patch_training_assignments_response_body.py">TrainingAssignmentsPatchTrainingAssignmentsResponseBody</a></code>
- <code title="delete /preview/training-assignments">client.preview.training_assignments.<a href="./src/samsara/resources/preview/training_assignments.py">delete</a>(\*\*<a href="src/samsara/types/preview/training_assignment_delete_params.py">params</a>) -> None</code>

## TrainingCourses

Types:

```python
from samsara.types.preview import TrainingCoursesGetTrainingCoursesResponseBody
```

Methods:

- <code title="get /preview/training-courses">client.preview.training_courses.<a href="./src/samsara/resources/preview/training_courses.py">list</a>(\*\*<a href="src/samsara/types/preview/training_course_list_params.py">params</a>) -> <a href="./src/samsara/types/preview/training_courses_get_training_courses_response_body.py">TrainingCoursesGetTrainingCoursesResponseBody</a></code>

# SpeedingIntervals

Types:

```python
from samsara.types import SpeedingIntervalsGetSpeedingIntervalsResponseBody
```

Methods:

- <code title="get /speeding-intervals/stream">client.speeding_intervals.<a href="./src/samsara/resources/speeding_intervals.py">stream</a>(\*\*<a href="src/samsara/types/speeding_interval_stream_params.py">params</a>) -> <a href="./src/samsara/types/speeding_intervals_get_speeding_intervals_response_body.py">SpeedingIntervalsGetSpeedingIntervalsResponseBody</a></code>

# Tags

Types:

```python
from samsara.types import ListTagsResponse, TagResponse, TagDeleteResponse
```

Methods:

- <code title="post /tags">client.tags.<a href="./src/samsara/resources/tags.py">create</a>(\*\*<a href="src/samsara/types/tag_create_params.py">params</a>) -> <a href="./src/samsara/types/tag_response.py">TagResponse</a></code>
- <code title="get /tags/{id}">client.tags.<a href="./src/samsara/resources/tags.py">retrieve</a>(id) -> <a href="./src/samsara/types/tag_response.py">TagResponse</a></code>
- <code title="put /tags/{id}">client.tags.<a href="./src/samsara/resources/tags.py">update</a>(id, \*\*<a href="src/samsara/types/tag_update_params.py">params</a>) -> <a href="./src/samsara/types/tag_response.py">TagResponse</a></code>
- <code title="get /tags">client.tags.<a href="./src/samsara/resources/tags.py">list</a>(\*\*<a href="src/samsara/types/tag_list_params.py">params</a>) -> <a href="./src/samsara/types/list_tags_response.py">ListTagsResponse</a></code>
- <code title="delete /tags/{id}">client.tags.<a href="./src/samsara/resources/tags.py">delete</a>(id) -> str</code>

# TrainingAssignments

Types:

```python
from samsara.types import (
    TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody,
    TrainingAssignmentsPostTrainingAssignmentsResponseBody,
)
```

Methods:

- <code title="post /training-assignments">client.training_assignments.<a href="./src/samsara/resources/training_assignments.py">create</a>(\*\*<a href="src/samsara/types/training_assignment_create_params.py">params</a>) -> <a href="./src/samsara/types/training_assignments_post_training_assignments_response_body.py">TrainingAssignmentsPostTrainingAssignmentsResponseBody</a></code>
- <code title="get /training-assignments/stream">client.training_assignments.<a href="./src/samsara/resources/training_assignments.py">stream</a>(\*\*<a href="src/samsara/types/training_assignment_stream_params.py">params</a>) -> <a href="./src/samsara/types/training_assignments_get_training_assignments_stream_response_body.py">TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody</a></code>

# Trips

Types:

```python
from samsara.types import TripsGetTripsResponseBody
```

Methods:

- <code title="get /v1/fleet/trips">client.trips.<a href="./src/samsara/resources/trips.py">list</a>(\*\*<a href="src/samsara/types/trip_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/v1_trip_response.py">V1TripResponse</a></code>
- <code title="get /trips/stream">client.trips.<a href="./src/samsara/resources/trips.py">stream</a>(\*\*<a href="src/samsara/types/trip_stream_params.py">params</a>) -> <a href="./src/samsara/types/trips_get_trips_response_body.py">TripsGetTripsResponseBody</a></code>

# UserRoles

Types:

```python
from samsara.types import ListUserRolesResponse
```

Methods:

- <code title="get /user-roles">client.user_roles.<a href="./src/samsara/resources/user_roles.py">list</a>(\*\*<a href="src/samsara/types/user_role_list_params.py">params</a>) -> <a href="./src/samsara/types/list_user_roles_response.py">ListUserRolesResponse</a></code>

# Users

Types:

```python
from samsara.types import ListUsersResponse, UserResponse, UserDeleteResponse
```

Methods:

- <code title="post /users">client.users.<a href="./src/samsara/resources/users.py">create</a>(\*\*<a href="src/samsara/types/user_create_params.py">params</a>) -> <a href="./src/samsara/types/user_response.py">UserResponse</a></code>
- <code title="get /users/{id}">client.users.<a href="./src/samsara/resources/users.py">retrieve</a>(id) -> <a href="./src/samsara/types/user_response.py">UserResponse</a></code>
- <code title="patch /users/{id}">client.users.<a href="./src/samsara/resources/users.py">update</a>(id, \*\*<a href="src/samsara/types/user_update_params.py">params</a>) -> <a href="./src/samsara/types/user_response.py">UserResponse</a></code>
- <code title="get /users">client.users.<a href="./src/samsara/resources/users.py">list</a>(\*\*<a href="src/samsara/types/user_list_params.py">params</a>) -> <a href="./src/samsara/types/list_users_response.py">ListUsersResponse</a></code>
- <code title="delete /users/{id}">client.users.<a href="./src/samsara/resources/users.py">delete</a>(id) -> str</code>

# HosAuthenticationLogs

Types:

```python
from samsara.types import V1HosAuthenticationLogsResponse
```

Methods:

- <code title="get /v1/fleet/hos_authentication_logs">client.hos_authentication_logs.<a href="./src/samsara/resources/hos_authentication_logs.py">list</a>(\*\*<a href="src/samsara/types/hos_authentication_log_list_params.py">params</a>) -> <a href="./src/samsara/types/v1_hos_authentication_logs_response.py">V1HosAuthenticationLogsResponse</a></code>

# Maintenance

Methods:

- <code title="get /v1/fleet/maintenance/list">client.maintenance.<a href="./src/samsara/resources/maintenance.py">list</a>() -> <a href="./src/samsara/types/fleet/inline_response_200_4.py">InlineResponse200_4</a></code>

# Messages

Methods:

- <code title="post /v1/fleet/messages">client.messages.<a href="./src/samsara/resources/messages.py">create</a>(\*\*<a href="src/samsara/types/message_create_params.py">params</a>) -> <a href="./src/samsara/types/fleet/inline_response_200_6.py">InlineResponse200_6</a></code>
- <code title="get /v1/fleet/messages">client.messages.<a href="./src/samsara/resources/messages.py">list</a>(\*\*<a href="src/samsara/types/message_list_params.py">params</a>) -> <a href="./src/samsara/types/fleet/inline_response_200_5.py">InlineResponse200_5</a></code>

# Vision

## Cameras

Types:

```python
from samsara.types.vision import V1VisionCamerasResponse
```

Methods:

- <code title="get /v1/industrial/vision/cameras">client.vision.cameras.<a href="./src/samsara/resources/vision/cameras.py">list</a>() -> <a href="./src/samsara/types/vision/v1_vision_cameras_response.py">V1VisionCamerasResponse</a></code>

# Machines

Types:

```python
from samsara.types import Machine
```

Methods:

- <code title="post /v1/machines/list">client.machines.<a href="./src/samsara/resources/machines/machines.py">retrieve</a>() -> <a href="./src/samsara/types/machine.py">Machine</a></code>

## History

Types:

```python
from samsara.types.machines import HistoryCreateResponse
```

Methods:

- <code title="post /v1/machines/history">client.machines.history.<a href="./src/samsara/resources/machines/history.py">create</a>(\*\*<a href="src/samsara/types/machines/history_create_params.py">params</a>) -> <a href="./src/samsara/types/machines/history_create_response.py">HistoryCreateResponse</a></code>

# Sensors

Types:

```python
from samsara.types import Cargo, Door, Humidity, Sensor, Temperature
```

Methods:

- <code title="post /v1/sensors/list">client.sensors.<a href="./src/samsara/resources/sensors/sensors.py">list</a>() -> <a href="./src/samsara/types/sensor.py">Sensor</a></code>
- <code title="post /v1/sensors/cargo">client.sensors.<a href="./src/samsara/resources/sensors/sensors.py">createcargostatus</a>(\*\*<a href="src/samsara/types/sensor_createcargostatus_params.py">params</a>) -> <a href="./src/samsara/types/cargo.py">Cargo</a></code>
- <code title="post /v1/sensors/door">client.sensors.<a href="./src/samsara/resources/sensors/sensors.py">createdoorstatus</a>(\*\*<a href="src/samsara/types/sensor_createdoorstatus_params.py">params</a>) -> <a href="./src/samsara/types/door.py">Door</a></code>
- <code title="post /v1/sensors/humidity">client.sensors.<a href="./src/samsara/resources/sensors/sensors.py">humidity</a>(\*\*<a href="src/samsara/types/sensor_humidity_params.py">params</a>) -> <a href="./src/samsara/types/humidity.py">Humidity</a></code>
- <code title="post /v1/sensors/temperature">client.sensors.<a href="./src/samsara/resources/sensors/sensors.py">temperature</a>(\*\*<a href="src/samsara/types/sensor_temperature_params.py">params</a>) -> <a href="./src/samsara/types/temperature.py">Temperature</a></code>

## History

Types:

```python
from samsara.types.sensors import HistoryCreateResponse
```

Methods:

- <code title="post /v1/sensors/history">client.sensors.history.<a href="./src/samsara/resources/sensors/history.py">create</a>(\*\*<a href="src/samsara/types/sensors/history_create_params.py">params</a>) -> <a href="./src/samsara/types/sensors/history_create_response.py">HistoryCreateResponse</a></code>

# Webhooks

Types:

```python
from samsara.types import Webhook, WebhookCreateResponse, WebhookUpdateResponse, WebhookListResponse
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/samsara/resources/webhooks.py">create</a>(\*\*<a href="src/samsara/types/webhook_create_params.py">params</a>) -> <a href="./src/samsara/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /webhooks/{id}">client.webhooks.<a href="./src/samsara/resources/webhooks.py">retrieve</a>(id) -> <a href="./src/samsara/types/webhook.py">Webhook</a></code>
- <code title="patch /webhooks/{id}">client.webhooks.<a href="./src/samsara/resources/webhooks.py">update</a>(id, \*\*<a href="src/samsara/types/webhook_update_params.py">params</a>) -> <a href="./src/samsara/types/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/samsara/resources/webhooks.py">list</a>(\*\*<a href="src/samsara/types/webhook_list_params.py">params</a>) -> <a href="./src/samsara/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /webhooks/{id}">client.webhooks.<a href="./src/samsara/resources/webhooks.py">delete</a>(id) -> None</code>
