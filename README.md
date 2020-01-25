# Command Line
A simple discord bot affectionately known as Cline that allows people to run shell commands in chat. Also comes with functionality for fortunes and python code.


# **WARNING**

This bot is ***extremely*** dangerous! It allows access to a "sort-of-shell" on your system (each command gets its own shell) that could be used to get the bot's token, or worse.

Never share a public invite to your instance of this bot, and only use it in servers where you can fully, 100% trust that nobody will delete/harm/do other bad things to anything on your hosting machine!

I nor my friends are liable for any harm caused to anything in relation to this project!

Now that that's out of the way...

# Instructions

Run the bot with `python3 bot.py`.

Once you do that, the bot will create its own config folder.

The bot, however, *cannot* create its own `config.json` file.

Make a config.json file in the bot's config folder (shown in the output) with this template:

```
{
    "token": "bot account token here"
}
```

Run the bot again.
