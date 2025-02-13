import os
from dotenv import load_dotenv
from samsara import Samsara

load_dotenv()

samsara = Samsara(
    access_token_header=f"Bearer {os.getenv('SAMSARA_API_KEY')}",
)

print(samsara.organization_info.get_organization_info())