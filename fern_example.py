import asyncio
from datetime import datetime
import os
from dotenv import load_dotenv
from fern_samsara import Samsara, AsyncSamsara

load_dotenv()

client = Samsara(token=os.getenv("SAMSARA_API_KEY"))

org_info = client.organization_info.list()
print(org_info)

sync_timer_start = datetime.now()
configurations = client.alerts.configurations.get()
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
    client = AsyncSamsara(token=os.getenv('SAMSARA_API_KEY'))
    async_timer_start = datetime.now()

    incident_list = []
    configurations = await client.alerts.configurations.get()
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
