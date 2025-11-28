import discord
from discord import app_commands
from discord.ext import commands

TOKEN = 

# -----------------------
# PRODUSUL UNIC: VIA
# -----------------------
VIA_PRODUCT = {
    "website": "https://t2.hammafia.us/register",
    "loader": "https://gofile.io/d/FYOL2N"
}

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Slash commands synced: {len(synced)}")
    except Exception as e:
        print(e)


# -----------------------------------------------------
# SLASH COMMAND: /sendkey
# -----------------------------------------------------
@bot.tree.command(name="sendkey", description="Trimite produsul VIA cu cheia introdusă.")
async def sendkey(interaction: discord.Interaction):

    await interaction.response.send_message(
        "Introdu cheia pentru produsul **VIA**:",
        ephemeral=True
    )

    def check(msg):
        return msg.author == interaction.user and msg.channel == interaction.channel

    try:
        key_msg = await bot.wait_for("message", timeout=60, check=check)
        product_key = key_msg.content

        # Mesaj final
        embed = discord.Embed(
            title="Here is your Product!",
            description="These are your Product(s). Make sure to keep them.",
            color=0x00b2ff
        )
        embed.add_field(name="Key:", value=f"```\n{product_key}\n```", inline=False)
        embed.add_field(name="Website:", value=VIA_PRODUCT["website"], inline=False)
        embed.add_field(name="Loader:", value=VIA_PRODUCT["loader"], inline=False)
        embed.set_image(url="https://i.imgur.com/z5dB9Dl.png")  # poți pune bannerul tău

        await interaction.followup.send(embed=embed)

    except Exception:
        await interaction.followup.send("⏰ Timpul a expirat. Încearcă din nou!", ephemeral=True)


bot.run(TOKEN)
