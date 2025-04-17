# Discord Bot Minecraft Server Controller

## English section

### Table of Contents

- [Presentation](#presentation)
- [Disclaimer](#disclaimer)
- [Step 1 - Making you a developer](#step-1--making-you-a-developper)
- [Step 2 - Diving into the Project](#step-2--diving-into-the-project)
- [Step 3 - Make your environement ready!](#step-3--make-your-environment-ready)
- [Final Step - Getting it configurated](#final-step--getting-it-configurated)
- [Getting Deeper](#getting-deeper)


### Presentation

This project an open-source Discord bot for controlling a self-hosted Minecraft server, course. It let you self-host you own version of this bot for making it interacting with your Minecraft server.
In fact, I made this project so that when I am self-hosting a Minecraft server, my friends not forced to send me a message, learn what a linux CLI is, and use some weird custom vpn and homemade derogations to access my proxmox.

The best question is : "Why not just let the server run all the time ?"
This seems like an obvious and reasonable way to solve the issue, but this method have few problems...

First and foremost, a MC server using a LOT of ram, and can use a lot of CPU too if, as me, you have friends fans of redstone machine and redstone computer and I'd like this to be a joke :( 
Moreover, a server running all the time mean, no auto updates, and can lead to weird and verry annoying issue (I had some worlds files corrupted, and I things the 24/7 a lead...)

So I made accessible controlling the server for all my friends using Discord !


### Disclaimer

I AM NOT RESPONSIBLE for any damages, and bugs and every other issues that might damaging data or computer. USE IT AT YOUR OWN RISK (there should'nt be major security risks but we never know...).

And more importantly I AM NOT a programming maniac, I already know that my code could be better, easier, lighter and more reliable (I have ambiguous thought toward the Popen method and my InteractiveShellController class). But if you have suggestion, feel free to tell it to me ! And for the devellopement prodigies, I'll be honored merge your code, knowing mine far from perfect.

You have to understand that you need your own linux server on which you can interact (here we will be using command lines but you can be help by a graphical environment too !). This project can't help you making your free Aternos server compatible with Discord, that is not how it works. 

Last thing, if you read the English section, you might already know that I am a frenchman. So, sorry for the potential mistakes I'll make, or I have already made...

Just, I reserve the right to modify the license, and to exempt certain individuals from the obligations imposed by said license. That was the juridical moment...


### Step 1 : Making you a developper!

If you read this lines, you surely already have a Discord account. If this is not the case, go making you one ! (By yourselves course ;)
You will have to make this lambda discord account a developper one. To make it, go on the app, from the landpage you go to Settings->Advanced->Developper mode

Now, I want you creating your own Discord App. Go on the discord developper portal, on this website : https://discord.com/developers , sign in before hitting the 'Start' button.
You'll be redirected on your own personnal developper space, I need you making a new 'application' by hitting the top-right button. 
You can name, describe and tag the application whatever you want. This is not important. Just let the app to the defaults settings.

Now, the interesting part...
Make sure the right app selected, you can see it on the top left corner. If not, try hitting your application icon.
On the left panel, clic on 'Bot' section. By default, each application has his own pre-built bot.
As the application, no matter how you name it or which icon you choose. Just make sure you like it, this is both the name and the icon you'll see on the discord server. 

Now a VERY IMPORTANT part! Make sure the 'public bot' section UNCHECKED, by default it is enabled and it has to be DISABLED.
WARNING : The project has no security preventing unknown server interacting with the bot. If the bot is public and can be added by anyone, that a MAJOR SECURITY BREACH. (Normally, the bot can not damaging data from a simple discord message, but as I said, I am not responsible)

Now you have to enable ALL the intents. (I think some of them unnescessary but I have not tested, so you can do it at your own risks)
Please, don't mess with bot permission, Instead, return to the top of the page, under the bot name you will see a 'reset token' button. 
Hit it, confirm, enter your password, and now, be careful copying it (the token), you'll need him later and it will not reappear, so make sure you have it !
Last but not least, confirm all you changes by hitting the button on the bottom right, an... that should be done !


### Step 2 : Diving into the project.

Now, the boring thing with Discord finished, let's get into the code.
Go on your linux envirronement, in which your MC server running.
First, make sure the server down and not running.
Make yourselves a folder in which you'll partition the Discord bot and the Minecraft server itself. 
For example, my tree file look like this :


└── home/  
    ├── minecraft-server/  
    │   ├── config/  
    │   │   ├── globals.yml  
    │   │   └── ...  
    │   ├── logs/  
    │   │   ├── 2025-03-24.log.gz  
    │   │   ├── 2025-03-15.log.gz  
    │   │   └── ...  
    │   └── your_minecraft_server_launcher_file.jar        
    └── minecraft-discordBot/  
        ├── bin/  
        ├── logs/  
        │   ├── 2025-04-12/  
        │   │   ├── 2025-04-12T10-48-08+0200.txt  
        │   │   └── 2025-04-12T11-29-38+0200.txt  
        │   ├── 2025-03-23.tar.gz  
        │   ├── 2025-03-24.tar.gz  
        │   └── ...  
        ├── src/  
        │   ├── commands.py  
        │   ├── logger.py  
        │   ├── bot.py  
        │   └── ...  
        ├── run.py  
        └── config.json  

We can see two distinct folder, very important for not getting confused. But you can name them whatever you want. If I chosed 'minecraft-server' and 'minecraft-DiscordBot', this is because it's better to have clear and explicit folder name. Please do not have folders with a space inside. Even if it is accepted by your folder system, please understand that these spaces are not friends at all with programmation. That could lead to irritating errors latter.

Ok so we have a folder contain all the Minecraft server, and a brand new folder ready to serve ! If you read the english section, select the lastest release and download the 'Production-En' folder (I'll maybe add an all in one installation script in the future). 
Now extract all the files from the downloaded folder to your personal folder.

Please don't be tempted by executing the run.py and focus on the next step.


### Step 3 : Make your environment ready!

Ok, I have the folder system, all the code, what should I do next?

First, the code is writen in python, and your computer may need to install this language.
It is not a bad thing getting your system up to date. I am on Debian, I use the command `sudo apt update && sudo apt upgrade -y`. 
This command not always the same depending on your exploitation system, so feel free to ask your best friend, Google.
Now, the python language not always installed natively. On Debian, I use `sudo apt get-install python3`. 
Again, the command may differ depending on your exploitation system...

Even in python, you'll need to install few more things.
Some of you know how to use virtual environement, python venv. If you dont know about that, no panic we wont need it, that just a special way to install things when you are a developper (a true one), and want partitioned python installation for your projects. However, you might have to do one, if it is the case, the web full of guide if you type : venv python <your_distribution/os_name>

To make the project work, we need first to go into our directory.
The command look like that : `cd /enter_the_path_of_you_folder/enter_the_name_of_an_inside_folder/...`
On my side, it looks like that : `cd /home/minecraft-discordBot`.
You might have to enter first the `cd /` command before all of that, in the case you encounter an error.
If it does not solve the issue, please check you enter PERFECTLY the folders name.
To be sure you are on the right folder, you can now enter the `ls` command, it will display you all the files the folder contains.
You should see both the 'run.py' and the 'requirements.txt' files.
That the last ones interesting us.

So we are ready installing what we called 'requirements'.
First, launch python with the command `Python3`.
A new type of shell appear, and then you can enter `pip install -r requirements.txt`.
Then exit python using `exit()` command.
If you had an issue, you can try (after exited the python3 shell), typing `python3 -m pip install requirements.txt`.

Ok, the hardest behind us, let's get into the final step.


### Final Step : Getting it configurated.

The code ready to be launched. 
Still in the folder, you can finally use the command `python3 run.py`.

And it won't works. That is perfectly normal. If you look carefully at the shell you'll see the message : 'Please fill the configuration file'.
We will do it together.

In fact, the code generates a new file for you.
If you type 'ls', you'll see that a new file appeared, named 'config.json'.
You can open the file by typing 'nano config.json'.
Get prepared.

| Variable name        | Role                                                                                                       | Variable type | Default                                      | Exemple                   |
|----------------------|------------------------------------------------------------------------------------------------------------|---------------|----------------------------------------------|---------------------------|
| token                | Let the discord api connect to your specific bot                                                           | string        | You have to enter yours                      | "thds7FDc:x..."           |
| log_level            | Express which events you want your logs to be made of                                                      | list          | Production (both INFO, ERROR and WARNING)    | ["ERROR", "DEBUG"]        |
| javaFileName         | The name of your Minecraft server .jar file                                                                | string        | You have to enter your own                   | "mojang-1.21.5.jar"       |
| pathToFile           | The path of your Minecraft server folder                                                                   | string        | Here again... Enter your own                 | "/home/minecraft-server/" |
| serverIP             | The IP of your server, prefer the external IP                                                              | string        | And again...                                 | "198.153.254.87"          |
| timezoneName         | Your timezone for the log files' date, include in tzdata library                                           | string        | Again, enter your own from : [tzdata list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)                                                                                                                                                                    | "Europe/Paris"            |
| logCompression       | The system compressing the logs folder for more space                                                      | bool          | true, no quotes                              | true                      |
| botStatus            | Enable or disable the bot status indication                                                                | bool          | true, no quotes                              | false                     |
| baseUserRole         | The role allowing Discord users interacting with the bot                                                   | string        | "Minecraft"                                  | "Minecraft"               |
| adminRole            | The same as the baseUserRole, it allow the stop command                                                    | string        | "Admin"                                      | "Admin"                   |
| pingCommand          | A classic command to check the bot online, he responds pong                                                | string        | "ping"                                       | "ping"                    |
| helpCommand          | The command listing all the... commands                                                                    | string        | "help"                                       | "help"                    |
| ipServerCommand      | The command giving the ip you inserted earlier                                                             | string        | "ip"                                         | "ip"                      |
| startServerCommand   | The command enabling the users starting the server                                                         | string        | "start server"                               | "start server"            |
| stopServerCommand    | The admin command to stop the server                                                                       | string        | "stop server"                                | "stop server"             |
| restartServerCommand | The command allowing users to restart the server in caso of issues                                         | string        | "restart server"                             | "restart server"          |
| whitelistCommand     | The command enabling users to get themselves into the whitelist, please use the help command for the syntax| string        | "add me"                                     | "add me"                  |

Normally, you should be good to go !

### Getting deeper

Be aware the script does not launch automatically when the computer starts. There is a lot of guides online teaching you how making a command line persistent depending on your exploitation system.

Have fun !






