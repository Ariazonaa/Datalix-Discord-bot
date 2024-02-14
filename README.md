
# Datalix Server Control Bot

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Project Status](#project-status)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is a Discord bot built with Nextcord, designed for managing server operations via Discord commands. It enables specific users to start, stop, reboot, and shut down servers, alongside fetching information on DDoS attacks. The bot integrates with servers managed by the Datalix backend for seamless operation control.

## Features

- **Server Control**: Execute server start, stop, reboot, and shutdown operations from Discord.
- **DDoS Attack Monitoring**: Retrieve and display data on DDoS attacks.
- **Latency Measurement**: Present the bot's current latency in milliseconds.
- **Permission Management**: Limit access to sensitive commands to a predefined user ID.

## Requirements

- Python 3.8 or newer
- Nextcord
- aiohttp

## Installation

1. Ensure Python 3.8+ is installed.
 
2. Install dependencies:

   ```
   pip install nextcord aiohttp
   ```

3. Set your service ID, API token, and allowed user ID in the script.

4. Execute the bot:

   ```
   python main.py
   ```

## Usage

Deploy the bot on a server with appropriate permissions and use the slash commands it registers to manage your server and view DDoS attack information.

## Commands

- `/start` - Initiates the server.
- `/stop` - Halts the server.
- `/shutdown` - Powers down the server.
- `/reboot` - Restarts the server.
- `/ping` - Displays bot latency.
- `/ddos` - Shows recent DDoS attack details.

## Project Status

This is the initial release of the project and, likely, the final update. **No support will be provided**, and the repository is shared as-is for anyone interested in server management via Discord. The community is welcome to fork and extend the project as needed.

## Contributing

While this project is not actively maintained, contributions are still welcome. If you have suggestions or enhancements, feel free to fork the repository, apply your changes, and submit a pull request.

## License

Released under the [MIT License](LICENSE).

