# Rocket.Chat Omnichannel Rooms Info Downloader

Before running the code, increase the number of results per request at settings -> general -> REST API -> Max Record Amount, otherwise it will only return 50 results.
[Documentation](https://docs.rocket.chat/guides/administration/admin-panel/settings/general#rest-api) for the topic above.

Do not forget to get the Personal Access Token at account -> personal access token, it is required.

External libraries: requests and pandas

APIs Documentation: 
- Rocket.Chat Rooms info: https://developer.rocket.chat/reference/api/rest-api/endpoints/omnichannel/omnichannel-endpoints/rooms/livechat-rooms-list
