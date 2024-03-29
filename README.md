# 🚀 Rocket.Chat - Omnichannel Rooms Info Downloader

This Python script extracts all the information from the omnichannel rooms and save as a CSV file for further analysis and investigation.

Before running the code, [increase the number of results per request](https://docs.rocket.chat/guides/administration/admin-panel/settings/general#rest-api), otherwise it will only return 50 results per request call.

Do not forget to get the [Personal Access Token](https://docs.rocket.chat/guides/user-guides/user-panel/managing-your-account/personal-access-token), it is required.

External libraries: [requests](https://requests.readthedocs.io/en/latest/), [pandas](https://pandas.pydata.org/) and [tqdm](https://tqdm.github.io/).

Rocket.Chat APIs used: 
- [Livechat Rooms list](https://developer.rocket.chat/reference/api/rest-api/endpoints/omnichannel/omnichannel-endpoints/rooms/livechat-rooms-list)
