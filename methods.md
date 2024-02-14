# Twitter

Search for ransomware related resources on the dark web

```(url:onion) "ransomware"```

```ransomware AND (url:onion -filter:retweets)```

```(hxxp:// OR http://) [.] AND url:onion```

Search for PoC of vulnerabilities

```PoC and CVE-20xx-xxxxx```

Search for leaks on pastebin or ghostbin

```target OR dump OR combo OR password OR leak OR breach OR databreach OR credential OR steal AND (url:pastebin.com OR url:ghostbin.co)```

# Google

Search for onion sites on AnonFiles shared
```intext:.onion site:anonfiles.com```

Search for vulnerability PoC in GitHub
```CVE-20xx-xxxxx site:GitHub.com```

# Shodan

Use these filters:
```ssl:".onion"```
```".onion"```
```"linkxyz.onion"```

# Interesting urls

[r/onions](https://www.reddit.com/r/onions/) on reddit
In an [article](https://www.neteye-blog.com/2021/07/analysis-of-a-dark-web-site/) at Neteye blog we can see how to perform an analysis of a site present on the Dark Web


# Other

## How to Download Large Files Using Tor for Enhanced Anonymity

This guide walks you through the process of downloading large files while anonymizing your connection using the Tor network. Keep in mind that while Tor provides anonymity, using it for resource-intensive activities can impact the network's performance. Use this method responsibly and consider other options if efficiency is a top priority.

### Prerequisites

- Linux-based operating system (e.g., Ubuntu)
- Basic command line proficiency

### Steps

1. **Install torsocks:**
    
    Open a terminal window and run the following command to install the torsocks utility:
    
    bash
    

- `sudo apt install torsocks`
    
- **Download with Torsocks and Wget:**
    
    Torsocks allows you to route your download through the Tor network while maintaining some level of anonymity. The following command uses torsocks in combination with wget to download a file:
    
    bash
    

1. `torsocks wget --tries=0 --retry-connrefused --retry-on-host-error --retry-on-http-error=500,502 --continue --timeout=90 --progress=bar --show-progress --random-wait --append-output=/tmp/wget_background <YOUR_DOWNLOAD_LINK>`
    
    Breakdown of options used:
    
    - `--tries=0`: Retry indefinitely.
    - `--retry-connrefused`: Retry on connection refused errors.
    - `--retry-on-host-error`: Retry on host errors.
    - `--retry-on-http-error=500,502`: Retry on certain HTTP errors.
    - `--continue`: Continue a partially downloaded file.
    - `--timeout=90`: Set a timeout of 90 seconds.
    - `--progress=bar --show-progress`: Show a progress bar and detailed progress information.
    - `--random-wait`: Introduce random waiting times to avoid overloading the server.
    - `--append-output=/tmp/wget_background`: Append output to a log file in the specified path.

### Additional Considerations

- **Security**: Ensure you're using a secure operating system, keeping it up to date, and using strong authentication methods.
    
- **Tor Browser**: For enhanced security, consider using the Tor Browser for downloads. It's designed to work seamlessly with the Tor network and provides additional privacy features.
    
- **VPN**: To add an extra layer of security, consider using a reputable Virtual Private Network (VPN) alongside Tor. This can help mask your IP address.
    
- **Source Authenticity**: Verify the authenticity of the download source to avoid potential security risks.
    
- **Limitations of Tor**: Understand that Tor provides anonymity, but it's not foolproof. It's important to educate yourself about its limitations.
    
- **Impact on the Tor Network**: Remember that downloading large files over Tor can strain the network. Use Tor responsibly and consider other options for resource-intensive tasks.
    

`torsocks wget --tries=0 --retry-connrefused --retry-on-host-error --retry-on-http-error=500,502 --continue --timeout=90 --progress=bar --show-progress --random-wait --append-output=/tmp/wget_background <YOUR_DOWNLOAD_LINK>
`

## How to download large and numerous files from Tor at high speed trough multi-threading and downloads fragmentation
Aria2-onion-downloader docker image is composed by an aria2ng webinterface as well as an downloader, which creates up to 99 tor-services and allows to load-balance downloads between these via an local nginx instance. This means you can download at an really high speed, since Aria2 fragments the downloads by default to 10 connections, which get load-balanced to Tor-Services.
https://github.com/sn0b4ll/aria2-onion-downloader

## How to download files via cmdline from Raidforums
- On your favorite browser go to raidforums website
- Open developer tools (for firefox CTRL+SHIFT+i)
- Go to network (if no data do CTRL+r to reload)
- Right click on a request and copy cURL (this cURL should contain your session cookies)
- Paste copied on your favorite text editor
- Replace url with download link (usually it's something like https://db.raidforums.com/z/down.php?id=259554)
- Append --output to your cURL cmd with a filename like (curl ... --output thisisatest.7z)
- Enjoy

## Search for invitation links
Thanks to [IntelligenceX](https://intelx.io/dorks)
- Skype: https://www.google.com/search?q=%22join.skype.com%22%20-site:google.com%20-site:microsoft.com
- Zoom: https://www.google.com/search?q=%22zoom.us%2Fj%2F%22
- Google Hangouts: https://www.google.com/search?q=%22hangouts.google.com%2Fgroup%2F%22%20-site:google.com
- Telegram: https://www.google.com/search?q=%22t.me%2Fjoinchat%22
- Whatsapp: https://www.bing.com/search?q=site%3Achat.whatsapp.com
