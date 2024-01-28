import requests
from datetime import datetime, timedelta

# Replace 'YOUR_ACCESS_TOKEN' with your actual access token
access_token = 'EAAFeEVFDyu0BO7ULw94tt38RZBvV0gowUHAUaqgOft3QwPoZCILXlxVCrfDa6Doc8ZA3ZAxNoSPZAoYpBX4QN4e5YBMgbLzyXnZASNz50JEydQq3ZCacX8cvhvb5PIAEtKyOVgEb4feeYiur9pTxlkszLkN2rP9YMbuXMXEMrHB8skp0c6VJVHbB1FMX8I4EgU13kgxjHrNAt5440IsO1lmRli9mD94LKel9DZBks9cEr4DH'

# Set the time range for the past 1 week
end_time = datetime.now()
start_time = end_time - timedelta(days=7)
print(f'Time range, {start_time}, {end_time}')

# Convert time to Unix timestamp format
end_time_unix = int(end_time.timestamp())
start_time_unix = int(start_time.timestamp())
print(f'Time range, {start_time_unix}, {end_time_unix}')

# Define the API endpoint for Instagram Ads
api_endpoint = 'https://graph.instagram.com/v12.0/act_786056955538549/ads'

# Set parameters for the API request
params = {
    'access_token': access_token,
    'time_range': f'{start_time_unix},{end_time_unix}',
    'limit': 100,
}

# Make the API request
response = requests.get(api_endpoint, params=params)
print(response.text)
# Check if the request was successful
if response.status_code == 200:
    # Save the ads data to a file (change 'ads.json' to your preferred filename)
    with open('ads.json', 'w') as file:
        file.write(response.text)
    print('Ads successfully downloaded and saved.')
else:
    print(f'Error {response.status_code}: {response.text}')
