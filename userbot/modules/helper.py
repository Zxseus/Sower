""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, man_cmd


@man_cmd(pattern="ihelp$")
async def usit(event):
    me = await event.client.get_me()
    await edit_or_reply(
        event,
        f"**Hai {me.first_name} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"✣ **Group Support :** [Sharing Userbot](t.me/Blvckcards)\n"
        f"✣ **Channel Support :** [Verified Account™](t.me/VerifiedAccount_ID)\n"
        f"✣ **Owner Repo :** [Blvckcards](t.me/Blvckcards)\n"
        f"✣ **Repo :** [Blvckcards](https://t.me/blvckcards)\n",
    )


@man_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari Blvckcards-Userbot:** [KLIK DISINI](https://telegra.ph/List-Variabel-Heroku-untuk-Blvckcards-Userbot-09-22)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk Blvckcards-Userbot.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository Blvckcards-Userbot.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String Blvckcards-Userbot.\
    "
    }
)
