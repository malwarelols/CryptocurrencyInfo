# Cryptocurrency Info
A plugin that will print a user's cryptocurrency investments onto their menubar on macOS using [bitbar](https://github.com/matryer/bitbar).

## Requirements
### Install Bitbar
* Download the [latest version of BitBar](https://github.com/matryer/bitbar/releases/download/v1.9.2/BitBar-v1.9.2.zip) from their Github (it is a .zip file).
* On your mac, go to *Finder > Downloads* and double click the file downloaded.
![BitBar download as it appears in the Download folder](https://i.imgur.com/xNjOE7H.png)
* Another item will appear named **"BitBar"** and will be listed as an application under "Kind".
![BitBar appearing after being unzipped](https://i.imgur.com/6gNmWkm.png)
* Drag this to your Applications folder.
![Dragging BitBar into the Applications folder](https://i.imgur.com/0bi0lHU.gif)
* Launch BitBar by double clicking on the BitBar app found on your launchpad!
* You need to set the plugin folder, choose anywhere you like. I use *Documents/dev/bitbar-plugins/* as an example.

## Install the cryptocurrency plugin
* Open up terminal on your mac and change into a directory of your choice (use the [cd command](https://www.macworld.com/article/2042378/master-the-command-line-navigating-files-and-folders.html))
* Once in the correct folder, run the command `git clone https://github.com/malwarelols/CryptocurrencyInfo/`
* A folder will appear called *CryptocurrencyInfo*
* Move into the directory using `cd CryptocurrencyInfo`
* In here is a file called `cryptocurrencies.30s.py`, this needs to be copied to your plugin folder set in BItBar.
* Use the command `cp cryptocurrencies.30s.py /path/to/bitbar/folder` where the last argument is the path set in BitBar.
* Click on BitBar in your menu bar and click refresh or use `⌘+R`.
* Now you should see the money bag logo and clicking on it will display some information on XLM and XVG. There are instructions below explaining how to customise these to fit your own portfolio.

### Edit the plugin to add your figures
Now the plugin is downloaded, we want to edit its contents to show numbers relating to your own portfolio.

1. Open up the file `cryptocurrencies.30s.py` in a text editor of your choice. If you don't have a favourite code editor using TextEdit *(installed by default)* is fine.
2. Find the line `# insert information about each currency here -- the number of tokens/coins you hodl and the total cost in your currency`
3. Underneath here is `a) XLM Information`. It lists the number of XLM and the total cost. The number is just the number of tokens you have - enter this with 2 decimal places. The total cost is the fiat you've invested (in USD or GBP) - again this with 2 decimal places.
4. Save the file once you have added the information you need about XLM. 
5. Click on BitBar in your menu bar and click refresh or use `⌘+R`.

### Add more currencies to the plugin
As you can see in the code it runs with Stellar Lumens (XLM) as the currencies - mainly as I developed this for [their subreddit](https://www.reddit.com/r/Stellar/). However, there is a code block commented out *(lines beginning with # are comments and not code)* that relates to XVG. To use XVG, remove the `#` from the start of the lines relating to XVG and folloe the steps above to add your custom amounts. This will add new currencies to your plugin. 

If you want to add any other currency, all you need to do is replicate the XLM part of the code and substitue the API link and some of the variable names, if you are unsure give it a try - don't worry about breaking things!


## Screenshot of v1.0 working
![The plugin (v1.0) shown on macOS High Sierra](https://i.imgur.com/I7lRVQF.png)

## To-Do List
- [x] Begin README fixes
- [x] Add instructions to install BitBar
- [x] Add all other instructions on using the plugin
- [x] Add screenshots to show how the app looks
- [ ] Ask for user feedback?
- [ ] Add an install script to avoid users having to install BitBar and the plugin manually.
- [ ] Continual improvement!
