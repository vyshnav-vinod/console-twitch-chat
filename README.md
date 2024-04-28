# TWITCH CHAT IN THE TERMINAL

Use this program to get the chat messages of your twitch chat directly to your terminal. Easy to setup and use. Provides some basic configurations like displaying with timestamps and colors.

## Installation and Usage

- Clone the repository

```bash
git clone https://github.com/vyshnav-vinod/console-twitch-chat.git
```
- Navigate to the directory
- Rename `.env_example` into `.env`
- To get your access token
  - Go to [twitchtokengenerator](https://twitchtokengenerator.com/) or any similar sites
  - Click on Bot Chat Token
  - And copy the Access Token
  - Paste it into the `ACCESS_TOKEN` field inside the newly made `.env`

>[!NOTE]
>You can use your own account or a newly made account
- Open `cfg.json` and add your channel name or the channel whose chat you want in your terminal to the `CHANNELS` value. Also configure the other options
- Create a virtual environment (Recommended) and activate it
```python3 -m venv .venv```
- Install required packages ```pip install -r requirements.txt```
- Run `main.py`
```bash
python main.py
```

Thats it, you should get your messages in the terminal.

## Issues
If you run into any issues, feel free to raise a issue in our [issues](https://github.com/vyshnav-vinod/console-twitch-chat/issues) page.