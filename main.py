import discord
from discord import app_commands
from discord.ext import commands

TOKEN = "PUNE_TOKENUL_TAU_AICI"

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


@bot.tree.command(name="sendkey", description="Trimite un produs complet cu key, website și loader.")
async def sendkey(interaction: discord.Interaction):

    await interaction.response.send_message(
        "Ce produs vrei să trimiți?",
        ephemeral=True
    )

    def check(msg):
        return msg.author == interaction.user and msg.channel == interaction.channel

    try:
        # 1. Produs
        product_msg = await bot.wait_for("message", timeout=60, check=check)
        product_name = product_msg.content

        # 2. Key
        await interaction.followup.send("Introdu cheia produsului:", ephemeral=True)
        key_msg = await bot.wait_for("message", timeout=60, check=check)
        product_key = key_msg.content

        # 3. Website
        await interaction.followup.send("Introdu link-ul website-ului produsului:", ephemeral=True)
        website_msg = await bot.wait_for("message", timeout=60, check=check)
        product_website = website_msg.content

        # 4. Loader
        await interaction.followup.send("Introdu link-ul loader-ului produsului:", ephemeral=True)
        loader_msg = await bot.wait_for("message", timeout=60, check=check)
        product_loader = loader_msg.content

        # Embed final
        embed = discord.Embed(
            title="Here is your Product!",
            description="These are your Product(s). Make sure to keep them.",
            color=0x00b2ff
        )
        embed.add_field(name="Product:", value=product_name, inline=False)
        embed.add_field(name="Key:", value=f"```\n{product_key}\n```", inline=False)
        embed.add_field(name="Website:", value=product_website, inline=False)
        embed.add_field(name="Loader:", value=product_loader, inline=False)
        embed.set_image(url="https://i.imgur.com/z5dB9Dl.png")  # poți pune bannerul tău

        await interaction.followup.send(embed=embed)

    except Exception as e:
        await interaction.followup.send("⏰ Timpul a expirat. Încearcă din nou!", ephemeral=True)
        print(e)


bot.run(TOKEN)
