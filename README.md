# TWITCH CHAT IN THE TERMINAL

Use this program to get the chat messages of your twitch chat directly to your terminal. Easy to setup and use. Provides some basic configurations like displaying with timestamps and colors.

## Installation

- Clone the repository

```bash
git clone https://github.com/vyshnav-vinod/console-twitch-chat.git
```
- Navigate to the directory
- Rename `.env_example` into `.env`
- To get your access token
>[!NOTE]
>You can use your own account or a newly made account
  - Go to [twitchtokengenerator](https://twitchtokengenerator.com/) or any similar sites
  - Click on Bot Chat Token
  - And copy the Access Token
  - Paste it into the `ACCESS_TOKEN` field inside the newly made `.env`
- Open `config.json` and add your channel name or the channel whose chat you want in your terminal to the `CHANNELS` value.
- 