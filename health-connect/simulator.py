import random
import time

import requests

# Configuration InfluxDB  
url = "http://localhost:8086/api/v2/write?org=health_org&bucket=health_metrics&precision=s"
headers = {
    "Authorization": "Token my-super-secret-auth-token",
    "Content-Type": "text/plain"
}

print("Beginning simulation of data sending to InfluxDB. Press Ctrl+C to stop.")

while True:
    # Create simulated metrics according to the project documentation catalogue
    db_size = random.randint(500, 2000)
    cache_eff = round(random.uniform(70.0, 99.9), 2)
    timestamp = int(time.time())

    # Prepare Line Protocol string
    payload = f"""healthconnect_metrics,host=myserver.com,instance=HEALTHCONNECT,environment=prod,database=HL7,metric=DatabaseSize value={db_size} {timestamp}
healthconnect_metrics,host=myserver.com,instance=HEALTHCONNECT,environment=prod,metric=CacheEfficiency value={cache_eff} {timestamp}"""

    # Send HTTP POST request to InfluxDB
    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code == 204:
        print(f"[{timestamp}] Data sent successfully: DatabaseSize={db_size}, CacheEfficiency={cache_eff}")
    else:
        print(f"Error sending data: {response.status_code} - {response.text}")

    # Wait 5 seconds before sending the next batch
    time.sleep(5)