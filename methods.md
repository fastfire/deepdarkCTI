**TWITTER**

Look for ransomware related resources on the dark web

(url:onion) "ransomware"

ransomware AND (url:onion -filter:retweets)

(hxxp:// OR http://) [.] AND url:onion


Look for vulnerability PoC

PoC and CVE-20xx-xxxxx


Look for leaks on pastebin or ghostbin

target OR dump OR combo OR password OR leak OR breach OR databreach OR credential OR steal AND (url:pastebin.com OR url:ghostbin.co)


**GOOGLE**

Look for onion sites on AnonFiles shared
intext:.onion site:anonfiles.com

Look for vulnerability PoC in GitHub
CVE-20xx-xxxxx site:GitHub.com


**DARK WEB SITE ANALYSIS**

https://www.neteye-blog.com/2021/07/analysis-of-a-dark-web-site/


**TELEGRAM**

Search for onion links in Telegram groups and channels


**DISCORD**

Search for onion links in Discord channels


**SHODAN**

Use these filters:
ssl:".onion"
".onion"
"linkxyz.onion"

**REDDIT**

join to r/onions


**VARIOUS**

**How to download large files from Tor or anonymize yourself while downloading files**
- Install torsocks `sudo apt install torsocks`
- Use torsocks chained with wget `torsocks wget --tries=0 --retry-connrefused --continue --timeout=90 --progress=bar --show-progress --random-wait --append-output=/tmp/wget_background <YOUR DOWNLOAD LINK>`

**How to download files via cmdline from Raidforums**
- On your favorite browser go to raidforums website
- Open developer tools (for firefox CTRL+SHIFT+i)
- Go to network (if no data do CTRL+r to reload)
- Right click on a request and copy cURL (this cURL should contain your session cookies)
- Paste copied on your favorite text editor
- Replace url with download link (usually it's something like https://db.raidforums.com/z/down.php?id=259554)
- Append --output to your cURL cmd with a filename like (curl ... --output thisisatest.7z)
- Enjoy

**SEARCH INVITATION LINKS (thanks to IntelligenceX https://intelx.io/dorks)**
- Skype: https://www.google.com/search?q=%22join.skype.com%22%20-site:google.com%20-site:microsoft.com
- Zoom: https://www.google.com/search?q=%22zoom.us%2Fj%2F%22
- Google Hangouts: https://www.google.com/search?q=%22hangouts.google.com%2Fgroup%2F%22%20-site:google.com
- Telegram: https://www.google.com/search?q=%22t.me%2Fjoinchat%22
- Whatsapp: https://www.bing.com/search?q=site%3Achat.whatsapp.com
