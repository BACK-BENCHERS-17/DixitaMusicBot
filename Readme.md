
<p align="center">
  <img src="https://komarev.com/ghpvc/?username=bisug&style=flat-square" />
</p>

<h1 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=FF69B4&width=500&lines=This+is+DixitaMusicBot+%F0%9F%8E%B6;The+Ultimate+Telegram+Music+Bot" />
</h1>


<p align="center">
  <a href="https://t.me/dear_sumi">
    <img src="https://i.ibb.co/tTh3xRD6/f6d4dd92e9b4.jpg" width="300">
  </a>
</p>

<p align="center">
  <a href="https://t.me/DixitaMusicBot"><img src="https://img.shields.io/badge/Try%20Bot-@DixitaMusicBot-blue?style=for-the-badge&logo=telegram" /></a>
</p>


<p align="center">
  <a href="https://github.com/bisug/DixitaMusicBot/stargazers"><img src="https://img.shields.io/github/stars/bisug/DixitaMusicBot?style=flat-square"/></a>
  <a href="https://github.com/bisug/DixitaMusicBot/network/members"><img src="https://img.shields.io/github/forks/bisug/DixitaMusicBot?style=flat-square"/></a>
  <a href="https://github.com/bisug/DixitaMusicBot/issues"><img src="https://img.shields.io/github/issues/bisug/DixitaMusicBot?style=flat-square"/></a>
  <a href="https://github.com/bisug/DixitaMusicBot/commits/main"><img src="https://img.shields.io/github/last-commit/bisug/DixitaMusicBot?style=flat-square"/></a>
  <a href="https://github.com/bisug/DixitaMusicBot/actions"><img src="https://img.shields.io/badge/CI-Status-grey?style=flat-square"/></a>
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
