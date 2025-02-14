import asyncio
from datetime import datetime
import os
from dotenv import load_dotenv
from fern_samsara import Samsara as FernSamsara, AsyncSamsara as AsyncFernSamsara
from stainless_samsara import Samsara as StainlessSamsara, AsyncSamsara as AsyncStainlessSamsara
from samsara import Samsara as SpeakeasySamsara

load_dotenv()

# Synchronous benchmarks
def run_fern_sync():
    print("\nStarting Fern sync benchmark...")
    client = FernSamsara(token=os.getenv("SAMSARA_API_KEY"))
    start = datetime.now()

    configurations = client.alerts.configurations.get()
    print(f"Retrieved {len(configurations.data)} configurations")
    for configuration in configurations.data:
        incidents = client.alerts.incidents.stream(
            configuration_ids=[configuration.id],
            start_time="2024-12-01T00:00:00Z",
            end_time=datetime.now().isoformat() + "Z",
        )
        for incident in incidents.data:
            pass

    return datetime.now() - start

def run_stainless_sync():
    print("\nStarting Stainless sync benchmark...")
    client = StainlessSamsara(access_token=os.getenv("SAMSARA_API_KEY"))
    start = datetime.now()

    configurations = client.alerts.configurations.list()
    print(f"Retrieved {len(configurations.data)} configurations")
    for configuration in configurations.data:
        incidents = client.alerts.incidents.stream(
            configuration_ids=[configuration.id],
            start_time="2024-12-01T00:00:00Z",
            end_time=datetime.now().isoformat() + "Z",
        )
        for incident in incidents.data:
            pass

    return datetime.now() - start

def run_speakeasy_sync():
    print("\nStarting Speakeasy sync benchmark...")
    client = SpeakeasySamsara(access_token_header=f"Bearer {os.getenv('SAMSARA_API_KEY')}")
    start = datetime.now()

    configurations = client.alerts.get_configurations()
    print(f"Retrieved {len(configurations.data)} configurations")
    for configuration in configurations.data:
        incidents = client.alerts.get_incidents(
            configuration_ids=[configuration.id],
            start_time="2024-12-01T00:00:00Z",
            end_time=datetime.now().isoformat() + "Z",
        )
        for incident in incidents.data:
            pass

    return datetime.now() - start

# Async benchmarks
async def run_fern_async():
    print("\nStarting Fern async benchmark...")
    client = AsyncFernSamsara(token=os.getenv('SAMSARA_API_KEY'))
    start = datetime.now()

    incident_list = []
    configurations = await client.alerts.configurations.get()
    print(f"Retrieved {len(configurations.data)} configurations")
    for configuration in configurations.data:
        incidents = client.alerts.incidents.stream(
            configuration_ids=[configuration.id],
            start_time="2024-12-01T00:00:00Z",
            end_time=datetime.now().isoformat() + "Z",
        )
        incident_list.append(incidents)

    vehicle_stats = client.vehicle_stats.get_history(
        types=["gps"],
        start_time="2024-12-01T00:00:00Z",
        end_time=datetime.now().isoformat() + "Z",
    )
    incident_list.append(vehicle_stats)

    gathered_results = await asyncio.gather(*incident_list)
    for result in gathered_results[:-1]:  # Process incidents
        for incident in result.data:
            pass

    # Process vehicle stats
    vehicle_stats_result = gathered_results[-1]
    print(f"Retrieved vehicle stats history")

    return datetime.now() - start

async def run_stainless_async():
    print("\nStarting Stainless async benchmark...")
    async with AsyncStainlessSamsara(access_token=os.getenv('SAMSARA_API_KEY')) as client:
        start = datetime.now()

        incident_list = []
        configurations = await client.alerts.configurations.list()
        print(f"Retrieved {len(configurations.data)} configurations")
        for configuration in configurations.data:
            incidents = client.alerts.incidents.stream(
                configuration_ids=[configuration.id],
                start_time="2024-12-01T00:00:00Z",
                end_time=datetime.now().isoformat() + "Z",
            )
            incident_list.append(incidents)

        vehicle_stats = client.fleet.vehicles.stats.history(
            start_time="2024-12-01T00:00:00Z",
            end_time=datetime.now().isoformat() + "Z",
            types=["gps"],
        )
        incident_list.append(vehicle_stats)

        gathered_results = await asyncio.gather(*incident_list)
        for result in gathered_results[:-1]:  # Process incidents
            for incident in result.data:
                pass

        # Process vehicle stats
        vehicle_stats_result = gathered_results[-1]
        print(f"Retrieved vehicle stats history")

        return datetime.now() - start

async def run_speakeasy_async():
    print("\nStarting Speakeasy async benchmark...")
    async with SpeakeasySamsara(access_token_header=f"Bearer {os.getenv('SAMSARA_API_KEY')}") as client:
        start = datetime.now()

        incident_list = []
        configurations = await client.alerts.get_configurations_async()
        print(f"Retrieved {len(configurations.data)} configurations")
        for configuration in configurations.data:
            incidents = client.alerts.get_incidents_async(
                configuration_ids=[configuration.id],
                start_time="2024-12-01T00:00:00Z",
                end_time=datetime.now().isoformat() + "Z",
            )
            incident_list.append(incidents)

        vehicle_stats = client.vehicle_stats.get_vehicle_stats_history_async(
            start_time="2024-12-01T00:00:00Z",
            end_time=datetime.now().isoformat() + "Z",
            types=["gps"]
        )
        incident_list.append(vehicle_stats)

        gathered_results = await asyncio.gather(*incident_list)
        for result in gathered_results[:-1]:  # Process incidents
            for incident in result.data:
                pass

        # Process vehicle stats
        vehicle_stats_result = gathered_results[-1]
        print(f"Retrieved vehicle stats history")

        return datetime.now() - start

async def main():
    print("Starting benchmarks...")

    # Run sync benchmarks
    fern_sync_time = run_fern_sync()
    stainless_sync_time = run_stainless_sync()
    speakeasy_sync_time = run_speakeasy_sync()

    # Run async benchmarks
    fern_async_time = await run_fern_async()
    stainless_async_time = await run_stainless_async()
    speakeasy_async_time = await run_speakeasy_async()

    # Print report
    print("\nBenchmark Results:")
    print("-----------------")
    print(f"Fern Sync: {fern_sync_time}")
    print(f"Fern Async: {fern_async_time}")
    print(f"\nStainless Sync: {stainless_sync_time}")
    print(f"Stainless Async: {stainless_async_time}")
    print(f"\nSpeakeasy Sync: {speakeasy_sync_time}")
    print(f"Speakeasy Async: {speakeasy_async_time}")

if __name__ == "__main__":
    asyncio.run(main())
