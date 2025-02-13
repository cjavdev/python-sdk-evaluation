import os
from dotenv import load_dotenv
from stainless_samsara import Samsara

load_dotenv()

samsara = Samsara(
    access_token=os.getenv("SAMSARA_API_KEY"),
)

# Fetch an individual organization
print(samsara.organization_info.retrieve())