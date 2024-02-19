# Discord Bot Deployment
Firstly, ensure that the bot has the correct permissions and scope set. It only needs to be able to read/send messages from the channel designated.


#### 1. Set the correct values in the `.env` file.
```bash
DISCORD_TOKEN=your_actual_bot_token
DISCORD_CHANNEL_ID=your_actual_channel_id 
```

#### 2. Build the container
```bash
docker build -t discord-flag-bot . 
```
#### 3. Run the container 
```bash
docker run -d --name discord-flag-bot --env-file .env discord-flag-bot

```