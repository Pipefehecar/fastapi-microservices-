import os


import httpx

MANUFACTURER_SERVICE_HOST_URL = "http://localhost:8002/api/v1/manufacturer/"
url = os.environ.get("MANUFACTURER_SERVICE_HOST_URL", MANUFACTURER_SERVICE_HOST_URL)


def is_manufacturer_present(manufacturer_id: int):
    r = httpx.get(f"{url}{manufacturer_id}")
    return True if r.status_code == 200 else False
