import asyncio
from pyrogram import filters
from pyrogram.types import Message

import config
from config import BANNED_USERS
from strings import get_string
from Tune import app
from Tune.utils.database import (
    get_chat_topics,
    set_chat_topic,
    unset_chat_topic,
    is_topic_in_chat,
    get_lang,
    clear_chat_topics
)
from Tune.utils.decorators.admins import AdminRightsCheck
from Tune.utils.decorators.language import LanguageStart


@app.on_message(
    filters.command(["setmusictopic", "addmusictopic"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
@LanguageStart
async def set_music_topic_command(client, message: Message, _, chat_id):
    # Get topic ID from the message (forum topic)
    if not message.message_thread_id:
        return await message.reply_text(_["settopic_1"])  # "This command can only be used in forum topics."
    
    topic_id = message.message_thread_id
    
    # Check if topic already exists
    if await is_topic_in_chat(chat_id, topic_id):
        return await message.reply_text(_["settopic_2"].format(topic_id))  # "Topic ID {0} is already enabled for music"
    
    # Add topic
    success = await set_chat_topic(chat_id, topic_id)
    
    if success:
        await message.reply_text(_["settopic_3"].format(topic_id))  # "✅ Successfully enabled music for this topic"
        
        # Log to logger chat if enabled
        if await is_on_off(2):
            await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴇɴᴀʙʟᴇᴅ ᴍᴜsɪᴄ ғᴏʀ ᴛᴏᴘɪᴄ <b>{topic_id}</b> ɪɴ {message.chat.title}\n\n"
                     f"<b>ᴄʜᴀᴛ ɪᴅ:</b> <code>{chat_id}</code>\n"
                     f"<b>ᴛᴏᴘɪᴄ ɪᴅ:</b> <code>{topic_id}</code>\n"
                     f"<b>ᴜsᴇʀ ɪᴅ:</b> <code>{message.from_user.id}</code>\n"
                     f"<b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{message.from_user.username}",
            )
    else:
        await message.reply_text(_["settopic_4"])  # "❌ Failed to enable music for this topic"


@app.on_message(
    filters.command(["unsetmusictopic", "removemusictopic"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
@LanguageStart
async def unset_music_topic_command(client, message: Message, _, chat_id):
    # Get topic ID from the message (forum topic)
    if not message.message_thread_id:
        return await message.reply_text(_["unsettopic_1"])  # "This command can only be used in forum topics."
    
    topic_id = message.message_thread_id
    
    # Check if topic exists
    if not await is_topic_in_chat(chat_id, topic_id):
        return await message.reply_text(_["unsettopic_2"].format(topic_id))  # "Topic ID {0} is not enabled for music"
    
    # Remove topic
    success = await unset_chat_topic(chat_id, topic_id)
    
    if success:
        await message.reply_text(_["unsettopic_3"].format(topic_id))  # "✅ Successfully disabled music for this topic"
        
        # Log to logger chat if enabled
        if await is_on_off(2):
            await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴅɪsᴀʙʟᴇᴅ ᴍᴜsɪᴄ ғᴏʀ ᴛᴏᴘɪᴄ <b>{topic_id}</b> ɪɴ {message.chat.title}\n\n"
                     f"<b>ᴄʜᴀᴛ ɪᴅ:</b> <code>{chat_id}</code>\n"
                     f"<b>ᴛᴏᴘɪᴄ ɪᴅ:</b> <code>{topic_id}</code>\n"
                     f"<b>ᴜsᴇʀ ɪᴅ:</b> <code>{message.from_user.id}</code>\n"
                     f"<b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{message.from_user.username}",
            )
    else:
        await message.reply_text(_["unsettopic_4"])  # "❌ Failed to disable music for this topic"


@app.on_message(
    filters.command(["musictopics", "listmusictopics"]) & filters.group & ~BANNED_USERS
)
@LanguageStart
async def list_music_topics_command(client, message: Message, _):
    chat_id = message.chat.id
    topics = await get_chat_topics(chat_id)
    
    if not topics:
        return await message.reply_text(_["listtopics_1"])  # "📋 No music topics are set for this chat."
    
    topics_text = "\n".join([f"• <code>{topic_id}</code>" for topic_id in topics])
    
    await message.reply_text(
        _["listtopics_2"].format(len(topics), topics_text)  # "📋 **Music Topics for this chat:**\n\nTotal: {0}\n\n{1}"
    )


# Additional command for admins to clear all topics
@app.on_message(
    filters.command(["clearmusictopics"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
@LanguageStart
async def clear_music_topics_command(client, message: Message, _, chat_id):
    topics = await get_chat_topics(chat_id)
    
    if not topics:
        return await message.reply_text(_["cleartopics_1"])  # "📋 No music topics are set for this chat."
    
    # Clear all topics
    success = await clear_chat_topics(chat_id)
    
    if success:
        await message.reply_text(_["cleartopics_2"].format(len(topics)))  # "✅ Successfully cleared all {0} music topics from this chat."
        
        # Log to logger chat if enabled
        if await is_on_off(2):
            await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴄʟᴇᴀʀᴇᴅ ᴀʟʟ ᴍᴜsɪᴄ ᴛᴏᴘɪᴄs ɪɴ {message.chat.title}\n\n"
                     f"<b>ᴄʜᴀᴛ ɪᴅ:</b> <code>{chat_id}</code>\n"
                     f"<b>ᴛᴏᴘɪᴄs ᴄʟᴇᴀʀᴇᴅ:</b> {len(topics)}\n"
                     f"<b>ᴜsᴇʀ ɪᴅ:</b> <code>{message.from_user.id}</code>\n"
                     f"<b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{message.from_user.username}",
            )
    else:
        await message.reply_text(_["cleartopics_3"])  # "❌ Failed to clear topics. Please try again."