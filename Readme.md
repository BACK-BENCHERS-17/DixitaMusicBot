# 🎵 Dixita Music Bot

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=bisug&style=flat-square&color=blue" />
  <img src="https://img.shields.io/github/stars/bisug/DixitaMusicBot?style=flat-square&color=yellow" />
  <img src="https://img.shields.io/github/forks/bisug/DixitaMusicBot?style=flat-square&color=green" />
  <img src="https://img.shields.io/github/issues/bisug/DixitaMusicBot?style=flat-square&color=red" />
  <img src="https://img.shields.io/github/last-commit/bisug/DixitaMusicBot?style=flat-square&color=purple" />
  <img src="https://img.shields.io/github/license/bisug/DixitaMusicBot?style=flat-square&color=orange" />
  <img src="https://img.shields.io/github/repo-size/bisug/DixitaMusicBot?style=flat-square&color=lightgrey" />
</p>

<h1 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=30&duration=4000&pause=1000&color=FF69B4&center=true&vCenter=true&width=600&height=80&lines=🎶+Dixita+Music+Bot+🎵;🚀+Ultimate+Telegram+Music+Bot;⚡+High+Quality+Audio+Streaming;🎯+Multi-Platform+Support;🔥+24%2F7+Active+Development" />
</h1>

<p align="center">
  <a href="https://t.me/DixitaMusicBot">
    <img src="https://i.ibb.co/tTh3xRD6/f6d4dd92e9b4.jpg" width="400">
  </a>
</p>

## 🤖 Live Bot
[![Try Bot](https://img.shields.io/badge/🤖_Try_Bot-@DixitaMusicBot-blue?style=for-the-badge&logo=telegram)](https://t.me/DixitaMusicBot)

## 📖 About

**Dixita Music Bot** is a high-performance Telegram music streaming bot built with **Pyrogram** and **PyTgCalls**. It delivers crystal-clear audio quality in group voice chats with support for multiple music platforms.

> ⚡ **Originally developed by** [Certified Coders](https://github.com/CertifiedCoders)

## 🚀 Quick Deploy

### 🔑 Generate String Session First
[![Generate String](https://img.shields.io/badge/Generate_String_Session-Telegram_Tools-blue?style=for-the-badge&logo=telegram)](https://telegram.tools)

### ☁️ One-Click Deployment

| Platform | Deploy Button |
|----------|---------------|
| **Heroku** | [![Deploy to Heroku](https://img.shields.io/badge/Deploy_to-Heroku-430098?style=for-the-badge&logo=heroku)](https://dashboard.heroku.com/new?template=https://github.com/bisug/DixitaMusicBot) |
| **Render** | [![Deploy to Render](https://img.shields.io/badge/Deploy_to-Render-46B3B3?style=for-the-badge&logo=render)](https://render.com/deploy?repo=https://github.com/bisug/DixitaMusicBot) |
| **Koyeb** | [![Deploy to Koyeb](https://img.shields.io/badge/Deploy_to-Koyeb-121212?style=for-the-badge&logo=koyeb)](https://app.koyeb.com/deploy?type=git&repository=https://github.com/bisug/DixitaMusicBot) |

## 🎯 Features

### 🎵 Music Streaming
- High Quality Audio (320kbps)
- YouTube, Spotify, Apple Music Support  
- 24/7 Playback
- Queue Management
- Multi-group Support

### ⚡ Performance
- Lightning Fast Responses
- Low Resource Usage
- Stable Connection
- Auto-restart Capability

### 🔧 Technical
- Pyrogram & PyTgCalls
- MongoDB Database
- Docker Support
- Multi-platform Deployment

## 🔑 Environment Variables

Below are the required and optional environment variables for deployment.

```env
API_ID=              # Required - Get from https://my.telegram.org
API_HASH=            # Required - From https://my.telegram.org
BOT_TOKEN=           # Required - Get t.me/BotFather
OWNER_ID=            # Required - Your Telegram user ID
LOGGER_ID=           # Required - Log group/channel ID
STRING_SESSION=      # Required - Generate from https://telegram.tools
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
        <td><a href="https://telegram.tools/session-string-generator" target="_blank">Telegram Tools</a></td>
        <td>
          1) Start bot →
          2) Provide <code>API_ID</code>/<code>API_HASH</code> →
          3) Complete login →
          4) Copy string
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

## 🛠️ Manual Installation

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
### 🔖 Credits

* <b> *sᴩᴇᴄɪᴀʟ ᴛʜᴀɴᴋs ᴛᴏ <a href="https://github.com/binamralamsal">Binamralamsal</a> ғᴏʀ <a href="https://github.com/binamralamsal/TuneViaBot">TuneViaBot</a>* </b>
* <b> *sᴩᴇᴄɪᴀʟ ᴛʜᴀɴᴋs ᴛᴏ <a href="https://github.com/AnonymousX1025">ᴀɴᴏɴʏ</a> ғᴏʀ <a href="https://github.com/AnonymousX1025/AnonXMusic">ᴀɴᴏɴxᴍᴜsɪᴄ</a>* </b>

* <b> *ORIGINAL REPOSITORY BY <a href="https://github.com/CertifiedCoders">ᴄᴇʀᴛɪғɪᴇᴅ ᴄᴏᴅᴇʀs</a>* </b>
