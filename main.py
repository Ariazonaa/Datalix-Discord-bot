import nextcord
from nextcord.ext import tasks, commands
from nextcord import Interaction, SlashOption
import itertools
import aiohttp
import random

intents = nextcord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(intents=intents)

service_id = "YOUR SERVICE ID"
api_token = "YOUR API TOKEN"
allowed_user_id = 1118861313108615168  #YOUR DISCORD USER ID


statuses = [
    "BOT IS ONLINE"

]


async def execute_api_action(action):
    async with aiohttp.ClientSession() as session:
        api_url = f"https://backend.datalix.de/v1/service/{service_id}/{action}?token={api_token}"
        async with session.post(api_url) as response:
            return await response.text()

@bot.slash_command(name="start", description="Start the server") 
async def start(interaction: Interaction):
    if interaction.user.id == allowed_user_id:
        await interaction.response.send_message("Start Server....")
        response = await execute_api_action("start")
        await interaction.followup.send(f"Server started: {response}")
    else:
        await interaction.response.send_message("no permission")

@bot.slash_command(name="stop", description="Stops the server")
async def stop(interaction: Interaction):
    if interaction.user.id == allowed_user_id:
        await interaction.response.send_message("Stop server....")
        response = await execute_api_action("stop")
        await interaction.followup.send(f"Server stopped: {response}")
    else:
        await interaction.response.send_message("no permission")

@bot.slash_command(name="shutdown", description="Shuts down the server")
async def shutdown(interaction: Interaction):
    if interaction.user.id == allowed_user_id:
        await interaction.response.send_message("Shut down server...")
        response = await execute_api_action("shutdown")
        await interaction.followup.send(f"Server shut down: {response}")
    else:
        await interaction.response.send_message("no permission")


@bot.slash_command(name="reboot", description="reboot the Server")
async def start(interaction: Interaction):
    if interaction.user.id == allowed_user_id:
        await interaction.response.send_message("reboot Server...")
        response = await execute_api_action("restart")
        await interaction.followup.send(f"Server reboot: {response}")
    else:
        await interaction.response.send_message("no permission")

@bot.slash_command(name="ping", description="Shows the latency of the bot")
async def ping(interaction: Interaction):
    latency = round(bot.latency * 1000)  
    await interaction.response.send_message(f'Latenz: {latency}ms')

@bot.slash_command(name="ddos", description="Shows information about DDOS attacks")
async def ddos(interaction: Interaction):
    if interaction.user.id == allowed_user_id:
        await interaction.response.defer() 
        async with aiohttp.ClientSession() as session:
            api_url = f"https://backend.datalix.de/v1/service/{service_id}/incidents?token={api_token}"
            async with session.get(api_url) as response:
                if response.status == 200:
                    data = await response.json()
                    incidents = data.get("data", [])
                    if incidents:
                       
                        sorted_incidents = sorted(incidents, key=lambda x: float(x['mbps']), reverse=True)
                        
                        biggest_attack = sorted_incidents[0]
                        last_attack = incidents[-1]
                        weakest_attack = sorted_incidents[-1]

                    
                        embed = nextcord.Embed(title="DDOS", description="DDOS-Angriffe", color=nextcord.Color.blue())
                        embed.add_field(name="Big Attack", value=f"IP: {biggest_attack['ip']}\nMBps: {biggest_attack['mbps']}\nPPS: {biggest_attack['pps']}\nMethode: {biggest_attack['method']}", inline=False)
                        embed.add_field(name="Latest Attack", value=f"IP: {last_attack['ip']}\nMBps: {last_attack['mbps']}\nPPS: {last_attack['pps']}\nMethode: {last_attack['method']}", inline=False)
                        embed.add_field(name="SKID Attack", value=f"IP: {weakest_attack['ip']}\nMBps: {weakest_attack['mbps']}\nPPS: {weakest_attack['pps']}\nMethode: {weakest_attack['method']}", inline=False)
                        await interaction.followup.send(embed=embed)

                        last_embed = nextcord.Embed(title="Latest DDOS Attack", description="Details of the last attack", color=nextcord.Color.green())
                        last_embed.add_field(name="IP", value=last_attack['ip'], inline=True)
                        last_embed.add_field(name="MBps", value=last_attack['mbps'], inline=True)
                        last_embed.add_field(name="PPS", value=last_attack['pps'], inline=True)
                        last_embed.add_field(name="Methode", value=last_attack['method'], inline=True)
                        await interaction.followup.send(embed=last_embed)
                    else:
                        await interaction.followup.send("There is currently no DDOS attack data available.")
                else:
                    await interaction.followup.send("Error retrieving the DDOS attack data. Please try again later.")
    else:
        await interaction.response.send_message("You are not authorised to execute this command.", ephemeral=True)


@tasks.loop(seconds=10) 
async def change_status():
    current_status = next(bot.status_cycle)  
    await bot.change_presence(activity=nextcord.Game(name=current_status))

@bot.event
async def on_ready():
    print(f'Bot ist eingewählt als {bot.user.name}')
    bot.status_cycle = itertools.cycle(statuses)  
    change_status.start()  


# Fügen Sie Ihren echten Token hier ein
bot.run("YOUR DISCORD BOT TOKEN")

