import requests, sys, html5lib, os, random, time, platform, socket
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore, Style
import socket

class BotNik:
  def download():
    file_url=input('Enter Full File URL:\t')
    print(Fore.WHITE + '━'*115)
    file_name = file_url.split('/')[-1]   
    r = requests.get(file_url, stream = True) 
      
    with open(file_name,"wb") as file:
      for chunk in r.iter_content(chunk_size=1024): 
        # writing one chunk at a time to pdf file 
        if chunk: 
          file.write(chunk)

  def explore():
    interesting = input('Enter file extension to search for:\t')
    t = time.process_time()
    base = input('enter base URL:\t')
    links = BotNik.get_links(base)
    while len(links) > 0:
      if len(links) > 1:
        link = random.choice(links)
        if link.endswith(interesting):
          BotNik.download(link)
        elif link.endswith('.html') or link.endswith('.htm') or not '.' in link.split('/')[-1]:
          nlinks = BotNik.get_links(link)
          for ll in nlinks:
            links.append(ll)
        else:
            continue
      else:
        BotNik.download(links[0])
      t = time.process() - t
      print(t)

  def get_links(archive_url): 
        
      # create response object 
      r = requests.get(archive_url) 
        
      # create beautiful-soup object 
      soup = BeautifulSoup(r.content,'html5lib') 
        
      # find all links on web-page 
      links = soup.findAll('a') 
    
      # filter the link sending with .mp4 
      links = [archive_url + link['href'] for link in links if link['href']] 
    
      return links
  def trakr(ip='1.1.1.1'):
      r = requests.get('https://api.hackertarget.com/geoip/?q=' + ip).text
      return r
  def ping(ip='1.1.1.1'):
      r = requests.get('https://api.hackertarget.com/nping/?q=' + ip).text
      return r
  def nmap(ip='1.1.1.1'):
      r = requests.get('http://api.hackertarget.com/nmap/?q=' + ip).text
      return r
  def headers(domain='hackthissite.org'):
      r = requests.get('https://api.hackertarget.com/httpheaders/?q=' + domain).text
      return r
  def dnsLookup(domain='hackthissite.org'):
      r = requests.get('http://api.hackertarget.com/dnslookup/?q=' + domain).text
      return r
  def censys(ip='1.1.1.1'):
      dirty_response = requests.get('https://censys.io/ipv4/%s/raw' % ip).text
      clean_response = dirty_response.replace('&#34;', '"')
      response = clean_response.split('<code class="json">')[1].split('</code>')[0]
      return response + '\n'
  def whois(domain='1.1.1.1'):
      r = requests.get('http://api.hackertarget.com/whois/?q=' + domain).text
      return r

class core: 
    end = Fore.WHITE 
    green = Fore.GREEN  
    good = Fore.GREEN + '[+]' + end
    bad = Fore.RED + '[-]' + end
    warning = Fore.RED + '[!]'
    run = end + '[~]' + Fore.GREEN
    info = Fore.BLUE + '[i]' + end
    host = socket.gethostname()
    plat = platform.platform()
    def menu():
      print('''
[%s1%s] Download File.
[%s2%s] Explore.
[%s3%s] Extract Links.
[%s4%s] GeoIP.
[%s5%s] Ping.
[%s6%s] Nmap.
[%s7%s] Headers.
[%s8%s] DNSLookup.
[%s9%s] CenSYS.
[%s10%s] whois.
[%s11%s] Clear Console.
''' % (core.green, core.end, core.green, core.end, core.green, core.end, core.green, core.end, core.green, core.end, core.green, core.end, core.green, core.end, core.green, core.end, core.green, core.end, core.green, core.end, core.green, core.end))

    def logo():
      print(Fore.GREEN + '''                                                   
                  .-://++++//:-.`                                                                                  
             .:oydNNNMMMMMMMMNNNmhs/-`                                                                             
         `-+hNMMMNmhysssssoosyhdNMMMNds:`         ........                       ...       ...  ... `..`           
       `/hNMMNho:...+hmNNd.   ``.-+ymMMNmo.      .NNNNNNNmms.              .od.  hNNs`     mNh  mNy /NN:           
     `+mMMNh+.`  `+mMMMMM+         `.:yNMMNs.    .MMd::::+mMm`    `...`   `sMM:` dMMMd-    NMd  ss/ /MM/   ...`    
    :dMMNy:`     oMMMMMMMh`           `.omMMNo`  .MMh````.dMN.  /hmmmmmy- hNMMmm`dMMdMN/   NMd  mmy /MM/ -hmd+`    
   oNMMd:`      `NMMMMMMMMd/-...:-       .sMMMh` .MMNmmmmNMMo  oMMs--:yMN/-yMM/- dMN`yMMs` NMd  MMh /MMoyNNs.      
   sMMMh-       .MMMMMMMMMMMNmmNM+       `+MMMd. .MMd++++odMN+`MMd    `NMd oMM.  dMN  +NMd-NMd  MMh /MMMMMs        
   `+mMMNo.`     yMMMMMMMMMMMMMMm.     `/dMMNs.  .MMy     .MMN`NMd    `NMd oMM.  dMN   -mMNMMd  MMh /MMysNMs`      
     .sNMMNy:.   `sNMMMMMMMMMMMh-   `-odMMNh:`   .MMd++++ohMMo oMMs--:hMN/ oMMo/ dMN    `yMMMd  MMh /MM/ /NMd-     
       .omMMMmy/-.`-sdNNMMNNmy/``.:sdNMMmy:`     .mmmmmmmmds:   :ymmmmds-  .hmmm.hmd      +mmh  mms :mm:  -dmd-    
         `:smNMMMmhyo+oossso+oshdNMMMmh+.         ```````         `...       ``` ```       ```  ```  ``     ```    
            `-+ydmNMMMMMMMMMMMMNNmho:.                                                                             
                `.-:/+ossssoo+/-.`                                                                 v2.8               
''')
      print(Fore.WHITE + '━'*115)
    def __copyright__():
      print(core.info, '(c) RaidTheWeb 2020, MIT Licensed.')
    def __version__():
      print(core.info, 'BotNik 2.8 on', core.plat)
    def console():
      core.logo()
      core.__copyright__()
      core.__version__()
      print(Fore.WHITE + '━'*115)
      core.menu()
      print(Fore.WHITE + '━'*115)
      while True:
        ex = input(core.end + 'BN2@' + core.host + ' ~ # ')
        if ex == '1':
          print(Fore.WHITE + '━'*115)
          print(BotNik.download())
        if ex == '2':
          print(Fore.WHITE + '━'*115)
          BotNik.explore()
        if ex == '3':
          print(Fore.WHITE + '━'*115)
          url = input('Target URL:\t')
          print(Fore.WHITE + '━'*115)
          links = BotNik.get_links(url)
          for link in links:
            print(link)
        if ex == '4':
          print(Fore.WHITE + '━'*115)
          ip = input('Enter Target IP:\t')
          print(Fore.WHITE + '━'*115)
          print(BotNik.trakr(ip))
        if ex == '5':
          print(Fore.WHITE + '━'*115)
          ip = input('Target IP:\t')
          print(BotNik.ping(ip))
        if ex == '6':
          print(Fore.WHITE + '━'*115)
          ip = input('Enter Target IP:\t')
          print(BotNik.nmap(ip))
        if ex == '7':
          print(Fore.WHITE + '━'*115)
          domain = input('Enter Target Domain:\t')
          print(BotNik.headers(domain))
        if ex == '8':
          print(Fore.WHITE + '━'*115)
          domain = input('Enter Target Domain:\t')
          print(BotNik.dnsLookup(domain))
        if ex == '9':
          print(Fore.WHITE + '━'*115)
          op = input('Enter I for IP or D for Domain:\t')
          if op.lower().startswith('i'):
            ip = input('Enter Target IP:\t')
            with open(ip + '-BotNik-2.8', 'w') as f:
              f.write(BotNik.censys(ip))
              f.close()
            print(core.info, 'Saved Output To', ip + '-BotNik-2.8')
          elif op.lower().startswith('d'):
            rm = input('Enter Target Domain:\t')
            ip = socket.gethostbyname(rm)
            with open(rm + '-BotNik-2.8', 'w') as f:
              f.write(BotNik.censys(ip))
              f.close()
            print(core.info, 'Saved Output To', rm + '-BotNik-2.8')
          else:
            print(core.bad, 'Unrecognized Input!')
        print(Fore.WHITE + '━'*115)
        core.menu()
        print(Fore.WHITE + '━'*115)
