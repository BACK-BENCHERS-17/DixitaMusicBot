

<!-- 👁 Visitor Counter -->

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=bisug&style=flat-square" />
</p>

<h1 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=FF69B4&width=500&lines=This+is+Dixita Music Bot+%F0%9F%8E%B6;The+Ultimate+Telegram+Music+Bot" />
</h1>


<p align="center">
  <a href="https://t.me/dear_sumi">
    <img src="https://files.catbox.moe/d0ynvn.jpg" width="600">
  </a>
</p>

<p align="center">
  <a href="https://t.me/DixitaMusicBot"><img src="https://img.shields.io/badge/Try%20Bot-@DixitaMusicBot-blue?style=for-the-badge&logo=telegram" /></a>
</p>


<p align="center">
  <a href="https://github.com/bisug/DixitaMusicBot/stargazers"><img src="https://img.shields.io/github/stars/bisug/DixitaMusicBot?style=flat-square"/></a>
  <a href="https://github.com/bisug/DixitaMusicBot/network/members"><img src="https://img.shields.io/github/forks/CertifiedCoders/TuneViaBot?style=flat-square"/></a>
  <a href="https://github.com/CertifiedCoders/TuneViaBot/issues"><img src="https://img.shields.io/github/issues/CertifiedCoders/TuneViaBot?style=flat-square"/></a>
  <a href="https://github.com/CertifiedCoders/TuneViaBot/commits/main"><img src="https://img.shields.io/github/last-commit/CertifiedCoders/TuneViaBot?style=flat-square"/></a>
  <a href="https://github.com/CertifiedCoders/TuneViaBot/actions"><img src="https://img.shields.io/badge/CI-Status-grey?style=flat-square"/></a>
</p>

## 🌟 What is 𝘿𝙞𝙭𝙞𝙩𝙖 ✘ 𝙈𝙪𝙨𝙞𝙘 🎶?

𝘿𝙞𝙭𝙞𝙩𝙖 ✘ 𝙈𝙪𝙨𝙞𝙘 🎶 is a blazing fast, modern Telegram music bot built with **Pyrogram** and **PyTgCalls**. It streams high-quality music into your group voice chats and supports various platforms like YouTube, Spotify, Apple Music, and more.
Originally made by <a href="https://github.com/CertifiedCoders">ᴄᴇʀᴛɪғɪᴇᴅ ᴄᴏᴅᴇʀs</a>

## 🚀 Features
<table>
<tr>
<td>
  <img src="https://files.catbox.moe/la0sxq.jpg" width="300" />
</td>
<td>

| 🌟 Feature                | 🔎 Description                              |
| ------------------------- | ------------------------------------------- |
| 🎶 HQ Music Streaming     | Lag‑free HD audio in group voice chats      |
| 🌐 Multi‑Platform Sources | YouTube, Spotify, Apple Music, Resso, etc.  |
| ⚡ Fast Setup              | One‑click Heroku, VPS, or Docker deployment |
| 🔄 Auto Config            | Quick setup script with pre‑checks          |

</td>
</tr>
</table>

## 🔑 Environment Variables

Below are the required and optional environment variables for deployment.

```env
API_ID=              # Required - Get from https://my.telegram.org
API_HASH=            # Required - From https://my.telegram.org
BOT_TOKEN=           # Required - Get t.me/BotFather
OWNER_ID=            # Required - Your Telegram user ID
LOGGER_ID=           # Required - Log group/channel ID
STRING_SESSION=      # Required - Generate from @SessionBuilderbot
MONGO_DB_URI=        # Required - MongoDB connection string
COOKIE_URL=          # Required - YT Cookies url

API_KEY=             # Optional - External API key for music Download
API_URL=             # Optional - External API url for music Download
```

⚠️ **Never expose raw cookies or tokens in public repos.** Use safe paste services like [Pastebin](https://pastebin.com) or [Batbin](https://batbin.me).

##

<details>
  <summary><b>Where do I get each key?</b></summary>

  <!-- Added: Well‑organized helper table -->

  <br/>

  <table>
    <thead>
      <tr>
        <th>Key</th>
        <th>Where to Get It</th>
        <th>Steps</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>API_ID</code> &amp; <code>API_HASH</code></td>
        <td><a href="https://my.telegram.org" target="_blank">my.telegram.org</a> → <i>API Development Tools</i></td>
        <td>
          1) Log in with Telegram →
          2) Open <b>API Development Tools</b> →
          3) Create app →
          4) Copy values
        </td>
        <td>Keep these private. Needed by both userbot &amp; bot client.</td>
      </tr>
      <tr>
        <td><code>BOT_TOKEN</code></td>
        <td><a href="https://t.me/BotFather" target="_blank">@BotFather</a></td>
        <td>
          1) <b>/newbot</b> →
          2) Set name &amp; username →
          3) Copy the token
        </td>
        <td>Rotate if leaked. Store in <code>.env</code>.</td>
      </tr>
      <tr>
        <td><code>STRING_SESSION</code></td>
        <td><href="https://telegram.tools/session-string-generator#pyrogram"t</a></td>
        <td>        
          1) Provide <code>API_ID</code>/<code>API_HASH</code> →
          2) Complete login →
          3) Copy string
        </td>
        <td>Userbot auth for Pyrogram.</td>
      </tr>
      <tr>
        <td><code>LOGGER_ID</code></td>
        <td>Telegram <b>Channel/Group</b> you own</td>
        <td>
          1) Create private channel/group →
          2) Add your bot as admin →
          3) Get ID via <code>@MissRose_Bot</code>
        </td>
        <td>Use a private space so logs aren’t public.</td>
      </tr>
      <tr>
        <td><code>MONGO_DB_URI</code></td>
        <td><a href="https://www.mongodb.com/atlas/database" target="_blank">MongoDB Atlas</a></td>
        <td>
          1) Create free cluster →
          2) Add database user &amp; IP allowlist →
          3) Copy connection string (<code>mongodb+srv://...</code>)
        </td>
        <td>Required for persistence (queues, configs, etc.).</td>
      </tr>
      <tr>
        <td><code>COOKIE_URL</code></td>
        <td>Any secure host (e.g., <a href="https://pastebin.com" target="_blank">Pastebin</a>, <a href="https://batbin.me" target="_blank">Batbin</a>)</td>
        <td>
          1) Upload your <code>cookies.txt</code> privately →
          2) Set paste visibility to <b>Unlisted</b> →
          3) Copy the <b>raw</b> URL
        </td>
        <td>Improves YouTube reliability. Never commit raw cookies.</td>
      </tr>
      <tr>
        <td><code>API_KEY</code> / <code>API_URL</code></td>
        <td>Provider of your choice</td>
        <td>generate key → paste here</td>
        <td>Optional integrations.</td>
      </tr>
    </tbody>
  </table>

  <br/>
</details>

##

### ☕ VPS Setup Guide

<img src="https://img.shields.io/badge/Show%20/Hide-VPS%20Steps-0ea5e9?style=for-the-badge" alt="Toggle VPS Steps"/>
<div align="left">
  <details>

```bash
🎵 Deploy 𝘿𝙞𝙭𝙞𝙩𝙖 ✘ 𝙈𝙪𝙨𝙞𝙘 🎶 on VPS

### Step 1: Update & Install Packages
sudo apt update && sudo apt upgrade -y
sudo apt install git curl python3-pip python3-venv ffmpeg -y
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
npm install -g npm

### Step 2: Clone Repo
git clone https://github.com/bisug/DixitaMusicBot
cd TuneViaBot
tmux new -s tune

### Step 3: Setup & Run
python3 -m venv venv
source venv/bin/activate
pip install -U pip && pip install -r requirements.txt
bash setup   # Fill environment variables
bash start   # Start bot

### Useful Commands
tmux detach         # Use Ctrl+B, then D
tmux attach-session -t tune # Attach to Running Bot session
tmux kill-session -t tune # to kill the running bot session
rm -rf TuneViaBot  # Uninstall the repo
```

  </details>
</div>

##

### 🐳 Docker Deployment

<img src="https://img.shields.io/badge/Show%20/Hide-Docker%20Steps-10b981?style=for-the-badge" alt="Toggle Docker Steps"/>

<div align="left">
  <details>

```bash
### Step 1: Clone Repo
git clone https://github.com/bisug/DixitaMusicBot
cd TuneViaBot

### Step 2: Create .env File
nano .env
# Paste your environment variables here and save (Ctrl+O, Enter, Ctrl+X)

### Step 3: Build Image
docker build -t tuneviabot .

### Step 4: Run Container
docker run -d --name tune --env-file .env --restart unless-stopped tuneviabot

### Step 5: Manage Container
docker logs -f tune        # View logs (Ctrl+C to exit)
docker stop tune           # Stop container
docker start tune          # Start again
docker rm -f tune          # Remove container
docker rmi tuneviabot      # Remove image
```

  </details>
</div>



##
### 🔗 String Session 

#### 🔑 Generate String Session Safely 
<a href="https://telegram.tools/session-string-generator#pyrogram"><img src="https://img.shields.io/badge/Generate%20Pyrogram%20String-Telegram%20Tools-blue?style=for-the-badge&logo=telegram" alt="Generate Pyrogram String"/></a>

#### 🚀 Quick Deploy
| Platform | Deploy Button |
|----------|-------------|
| **Heroku** | <a href="https://dashboard.heroku.com/new?template=https://github.com/bisug/DixitaMusicBot"><img src="https://img.shields.io/badge/Deploy%20to-Heroku-430098?style=for-the-badge&logo=heroku" alt="Deploy to Heroku"/></a> |
| **Render** | <a href="https://render.com/deploy?repo=https://github.com/bisug/DixitaMusicBot"><img src="https://img.shields.io/badge/Deploy%20to-Render-46B3B3?style=for-the-badge&logo=render" alt="Deploy to Render"/></a> |
| **Koyeb** | <a href="https://app.koyeb.com/deploy?type=git&repository=https://github.com/bisug/DixitaMusicBot"><img src="https://img.shields.io/badge/Deploy%20to-Koyeb-121212?style=for-the-badge&logo=koyeb" alt="Deploy to Koyeb"/></a> |
##
### 🔖 Credits

* <b> *sᴩᴇᴄɪᴀʟ ᴛʜᴀɴᴋs ᴛᴏ <a href="https://github.com/AnonymousX1025">ᴀɴᴏɴʏ</a> ғᴏʀ <a href="https://github.com/AnonymousX1025/AnonXMusic">ᴀɴᴏɴxᴍᴜsɪᴄ</a>* </b>
* <b> *ᴄʀᴀғᴛᴇᴅ ᴡɪᴛʜ ᴘᴀssɪᴏɴ ʙʏ <a href="https://github.com/CertifiedCoders">ᴄᴇʀᴛɪғɪᴇᴅ ᴄᴏᴅᴇʀs</a>* </b>
