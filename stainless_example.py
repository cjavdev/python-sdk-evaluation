import asyncio
from datetime import datetime
import os
from dotenv import load_dotenv
from stainless_samsara import Samsara, AsyncSamsara

load_dotenv()

client = Samsara(access_token=os.getenv("SAMSARA_API_KEY"))

# Synchronous
# Fetch an individual organization
organization = client.organization_info.retrieve()
print(organization)

# List vehicles
addresses = client.addresses.list()
address = addresses.data[0]

print(address.formatted_address)
print(address.geofence)

# Add type annotations to variables
org_info = client.organization_info.retrieve()

sync_timer_start = datetime.now()
configurations = client.alerts.configurations.list()
for configuration in configurations.data:
  print("Submissions for configuration: ", configuration.id)
  incidents = client.alerts.incidents.stream(
    configuration_ids=[configuration.id],
    start_time="2025-01-01T00:00:00Z",
    end_time=datetime.now().isoformat() + "Z",
  )
  for incident in incidents.data:
    print(incident.incident_url)

sync_timer_end = datetime.now()
print("Sync Time taken: ", sync_timer_end - sync_timer_start)



# Asynchronous:
async def main():
    async with AsyncSamsara(
        access_token=os.getenv('SAMSARA_API_KEY'),
    ) as client:
      async_timer_start = datetime.now()

      incident_list = []
      configurations = await client.alerts.configurations.list()
      for configuration in configurations.data:
        print("Submissions for configuration: ", configuration.id)
        incidents = client.alerts.incidents.stream(
          configuration_ids=[configuration.id],
          start_time="2025-01-01T00:00:00Z",
          end_time=datetime.now().isoformat() + "Z",
        )
        incident_list.append(incidents)

      gathered_incidents = await asyncio.gather(*incident_list)
      for incidents in gathered_incidents:
        for incident in incidents.data:
          print(incident.incident_url)

      async_timer_end = datetime.now()
      print("Async Time taken: ", async_timer_end - async_timer_start)
      print("Sync Time taken: ", sync_timer_end - sync_timer_start)

if __name__ == "__main__":
    asyncio.run(main())
