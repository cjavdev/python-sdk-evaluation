import os
from dotenv import load_dotenv
from fern_samsara import Samsara

load_dotenv()

samsara = Samsara(token=os.getenv("SAMSARA_API_KEY"))

print(samsara.organization_info.list())
