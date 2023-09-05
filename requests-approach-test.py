import requests
import json

# Your Facebook App ID and App Secret
app_id = '821124516328699'
app_secret = '0d737d5ebfbe09a574a607534db54395'

# Get an access token
def get_access_token(app_id, app_secret):
    url = f'https://graph.facebook.com/v12.0/oauth/access_token?client_id={app_id}&client_secret={app_secret}&grant_type=client_credentials'
    response = requests.get(url)
    data = response.json()
    return data.get('access_token')

access_token = get_access_token(app_id, app_secret)

# Replace with your Reel ID or URL
reel_id = '232880599100376'

# Make an API request to get Reel details
api_url = f'https://graph.facebook.com/v12.0/{reel_id}?access_token={access_token}'
response = requests.get(api_url)
reel_data = response.json()

# Print the entire response for inspection
print(json.dumps(reel_data, indent=4))

# Check if the 'video_url' field is present in the response
if 'video_url' in reel_data:
    video_url = reel_data['video_url']

    # Download the video using requests
    video_response = requests.get(video_url)
    with open('downloaded_reel.mp4', 'wb') as video_file:
        video_file.write(video_response.content)
else:
    print("Video URL not found in the Reel data.")