<!-- Start SDK Example Usage [usage] -->
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