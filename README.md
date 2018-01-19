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

### Install the cryptocurrency plugin
Download the script from the **Master branch** of this repo. Either using git clone or manually downloading it.

#### Using git clone
* Open up terminal on your mac and change into a directory of your choice (use the [cd command](https://www.macworld.com/article/2042378/master-the-command-line-navigating-files-and-folders.html))
* Once in the correct folder, run the command `git clone https://github.com/malwarelols/CryptocurrencyInfo/`
* A folder will appear called *CryptocurrencyInfo*
* Move into the directory using `cd CryptocurrencyInfo`
* In here is a file called `cryptocurrencies.30s.py`, this needs to be copied to your plugin folder set in BItBar.
* Use the command `cp cryptocurrencies.30s.py /path/to/bitbar/folder` where the last argument is the path set in BitBar.
* Click on BitBar in your menu bar and click refresh or use `⌘+R`.
* Now you should see the money bag logo and clicking on it will display some information on XLM and XVG. There are instructions below explaining how to customise these to fit your own portfolio.

#### Manually downloading it
instructions here

### Edit the plugin to add your own investments and currencies
Show how to add currencies, potentially add all currencies listed on Coinmarketcap

## Screenshot of v1.0 working
![The plugin (v1.0) shown on macOS High Sierra](https://i.imgur.com/I7lRVQF.png)

## To-Do List
- [x] Begin README fixes
- [x] Add instructions to install BitBar
- [ ] Add all other instructions on using the plugin
- [x] Add screenshots to show how the app looks
- [ ] Ask for user feedback
- [ ] Continual improvement!
