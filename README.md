# Discord Bot Minecraft Server Controller

# English section

- Presentation

This project an open source Discord bot for controlling a self-hosted Minecraft server, course. It let you self-host you own iteration of this bot for making it interacting with your Minecraft server.
In fact, I made this project so that when I am self-hosting a Minecraft server, my friends not forced to send me a message, learn what a linux CLI is, and use some weird custom vpn and homemade derogations to access my proxmox.

The best question is : "Why not just let the server run all the time ?"
This seems and obvious and reasonnable way to solve the issue, but this method have few problems...

First and foremost, a MC server using a LOT of ram, and can use a lot of CPU too if, as me, you have friends fans of redstone machine and redstone computer and I'd like this to be a joke :( 
Moreover, a server running all the time mean, no auto updates, and can lead to some weird and verry annoying issue (I had some worlds files corrupted, and I things the 24/7 a lead...)

So I made accessible controlling the server for all my friends using Discord !


- Disclaimer

I AM NOT RESPONSIBLE for any damages, and bugs and every other issues that might damaging data or computer. USE IT AT YOUR OWN RISK (there should'nt be major security risks but we never know...).

And more importantly I AM NOT a programmation maniac, I already know that my code could be better, easier, lighter and more reliable (I have ambiguous thought toward the Popen method and my InteractiveShellController class). But if you have suggestion, feel free to tell it to me ! And for the devellopement prodigys, I'll be honored merge your code, knowing mine far from perfect.

You have to understand that you need your own linux server on which you can interact (here we will be using command lines but you can be help by a graphic environement too !). This project can't help you making your free Aternos server compatible with Discord, that is not how it works. 

Last thing, if you read the English section, you might already know that I am a frenchman. So, sorry for the potential mistakes I'll make, or I have alredy made...


- Step 1 : Making you a developper !

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


- Step 2 : Diving into the project.

Now, the boring thing with Discord finished, let's get into the code.
Go on your linux envirronement, in which your MC server running.
First, make sure the server down and not running.
Make yourselves a folder in which you'll partition the Discord bot and the Minecraft server itself. 
For example, my tree file look like this :

.
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
        ├── bin
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

We can see two distinct folder, very important for not getting confused. But you can name them whatever you want. If I chosed 'minecraft-server' and 'minecraft-DiscordBot', this is because you prefer having explicit and straight to the point folder names. Please do not have folders with a space inside. Even if it is accepted by your folder system, please understand that these spaces are not friends at all with programmation. That could lead to irritating errors latter.

Ok so we have a folder contain all the Minecraft server, and a brand new folder ready to serve ! If you read the english section, select the lastest release and download the 'Production-En' folder (I'll maybe add an all in one installation script in the future). 
Now extract all the files from the downloaded folder to your personal folder.

Please don't be tempted by executing the run.py and focus on the next step.


- Step 3 : Make your environement ready !

Ok, I have the folder system, all the code, what should I do next?

First, the code is writed in python, and your computer may need to install this language.
It is not a bad thing getting your system up to date. I am on Debian, I use the command 'sudo apt update && sudo apt upgrade -y'. 
This command not always the same depending on your exploitation system, so feel free to ask your best friend, Google.
Now, the python language not always installed natively. On Debian, I use 'sudo apt get-install python3'. 
Again, the command may fiffer depending on your exploitation system...

Now, even in python, you may ne





