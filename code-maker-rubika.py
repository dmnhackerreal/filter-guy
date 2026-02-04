import random
import sys
from subprocess import call
from sys import platform
import time
import datetime
from colorama import Fore, init # Added init

# Initializes colorama to support colors in various terminals (especially Windows).
# autoreset=True automatically resets the color to the default after each print.
init(autoreset=True)

# This function clears the terminal screen for better display.
def clear():
    """Clears the terminal screen."""
    if platform not in ('win32', 'cygwin'):
        command = 'clear'
    else:
        command = 'cls'
    try:
        call(command, shell=True)
    except OSError as e:
        print(f"Error clearing screen: {type(e).__name__}, {e}")

# Define color codes using colorama for cross-platform support
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
pink = Fore.MAGENTA
white = Fore.WHITE
yellow = Fore.YELLOW
light_green = Fore.LIGHTGREEN_EX
light_blue = Fore.LIGHTBLUE_EX
light_yellow = Fore.LIGHTYELLOW_EX
# reset = Fore.RESET # With autoreset=True, this is often not strictly needed, but kept for reference.
# Sample data lists (Note: some of the original links and words may be flagged as malicious or inappropriate by some systems)
drkwblnk = [
    'http://s4k4ceiapwwgcm3mkb6e4diqecpo7kvdnfr5gg7sph7jjppqkvwwqtyd.onion',
    'http://6nhmgdpnyoljh5uzr5kwlatx2u3diou4ldeommfxjz3wkhalzgjqxzqd.onion',
    'http://2jwcnprqbugvyi6ok2h2h7u26qc6j5wxm7feh3znlh2qu3h6hjld4kyd.onion',
    'http://jgwe5cjqdbyvudjqskaajbfibfewew4pndx52dye7ug3mt3jimmktkid.onion',
    'http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page',
    'http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion',
    'http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion',
    'http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion',
    'http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion',
    'http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion',
    'http://wbz2lrxhw4dd7h5t2wnoczmcz5snjpym4pr7dzjmah4vi6yywn37bdyd.onion',
    'http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion',
    'http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion',
    'http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion',
    'http://guzjgkpodzshso2nohspxijzk5jgoaxzqioa7vzy6qdmwpz3hq4mwfid.onion',
    'http://n6qisfgjauj365pxccpr5vizmtb5iavqaug7m7e4ewkxuygk5iim6yyd.onion',
    'http://kl4gp72mdxp3uelicjjslqnpomqfr5cbdd3wzo5klo3rjlqjtzhaymqd.onion',
    'http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion',
    'http://2ln3x7ru6psileh7il7jot2ufhol4o7nd54z663xonnnmmku4dgkx3ad.onion',
    'http://usmost4cbpesx552s2s4ti3c4nk2xgiu763vhcs3b4uc4ppp3zwnscyd.onion',
    'http://xf2gry25d3tyxkiu2xlvczd3q7jl6yyhtpodevjugnxia2u665asozad.onion',
    'http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion',
    'http://prjd5pmbug2cnfs67s3y65ods27vamswdaw2lnwf45ys3pjl55h2gwqd.onion',
    'http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion',
    'http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion',
    'http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion',
    'http://jhi4v5rjly75ggha26cu2eeyfhwvgbde4w6d75vepwxt2zht5sqfhuqd.onion',
    'http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion',
    'http://vhlehwexxmbnvecbmsk4ormttdvhlhbnyabai4cithvizzaduf3gmayd.onion',
    'http://ymvhtqya23wqpez63gyc3ke4svju3mqsby2awnhd3bk2e65izt7baqad.onion',
    'http://k6m3fagp4w4wspmdt23fldnwrmknse74gmxosswvaxf3ciasficpenad.onion',
    'http://lqcjo7esbfog5t4r4gyy7jurpzf6cavpfmc4vkal4k2g4ie66ao5mryd.onion',
    'http://qazkxav4zzmt5xwfw6my362jdwhzrcafz7qpd5kugfgx7z7il5lyb6ad.onion',
    'http://gd5x24pjoan2pddc2fs6jlmnqbawq562d2qyk6ym4peu5ihzy6gd4jad.onion']
dscripts = [
     'https://github.com/Msramirreza/mrhackergod/blob/main/Filter.py',
    'https://github.com/Msramirreza/mrhackergod/blob/main/Sexy.py',
    'https://github.com/Msramirreza/mrhackergod/blob/main/Yftt100k',
    'https://github.com/Msramirreza/mrhackergod/blob/main/Yftt12k.py',
    'https://github.com/Msramirreza/mrhackergod/blob/main/Yftt15k',
    'https://github.com/Msramirreza/mrhackergod/blob/main/Yftt15k.py',
    'https://github.com/Msramirreza/mrhackergod/blob/main/traport.rubika.reset.yttks58k.im009',
    'https://github.com/Ytthacker/dscript-rubika/blob/main/Filterlinks.txt',
    'https://github.com/Ytthacker/dscript-rubika/blob/main/Rubikaviru3.txt',
    'https://github.com/Ytthacker/dscript-rubika/blob/main/Servers.py',
    'https://github.com/Ytthacker/dscript-rubika/blob/main/Viru34.txt',
    'https://github.com/Ytthacker/dscript-rubika/blob/main/Yftt149.txt',
    'https://github.com/Ytthacker/dscript-rubika/blob/main/filtr.txt',
    'https://github.com/Ytthacker/dscript-rubika/blob/main/torlinks.txt',
    'https://github.com/Ytthacker/dscript-rubika/blob/main/yrrf19.apx',
    'https://github.com/Msramirreza/amirreza/blob/main/Dxprit.py',
    'https://github.com/Msramirreza/amirreza/blob/main/Filter.py',
    'https://github.com/Msramirreza/amirreza/blob/main/Sexy.py',
    'https://github.com/Msramirreza/amirreza/blob/main/Yftt100k',
    'https://github.com/Msramirreza/amirreza/blob/main/Yftt12k.py',
    'https://github.com/Msramirreza/amirreza/blob/main/Yftt15k',
    'https://github.com/Msramirreza/amirreza/blob/main/Yftt15k.pv',
    'https://github.com/Msramirreza/amirreza/blob/main/Yftt15k.py',
    'https://github.com/Msramirreza/amirreza/blob/main/rat.py',
    'https://github.com/Msramirreza/amirreza/blob/main/traport.rubika.reset.yttks58k.im009]',
    'https://github.com/Rubika-hacker/http-dxprit-filtering-rubika-sxs.gigfa.com-dxprit.html/blob/main/http%3A/dxprit-saleh-king99-55-39-hackers.phpnet.us/dxprit.html',
    'https://github.com/Rubika-hacker/http-dxprit-filtering-rubika-sxs.gigfa.com-dxprit.html',
    'https://github.com/Amirhackerweb/Hacker/blob/main/index.html',
    'https://github.com/Amirhackerweb/Filtering-rubika-sex-hack-virus-hacker-filter-rubika.com/blob/main/index.html',
    'https://github.com/Amirhackerweb/Filtering-rubika-sex-hack-virus-hacker-filter-rubika.com/blob/main/Filter.py',
    'https://github.com/Amirhackerweb/Filtering-rubika-sex-hack-virus-hacker-filter-rubika.com/blob/main/Filter-rubika.sh',
    'https://github.com/Amirhackerweb/Filtering-rubika-sex-hack-virus-hacker-filter-rubika.com/blob/main/police-cyber-rubika.io',
    'https://github.com/script-amir/supportbot-filtering-rubika/blob/main/index.html',
    'https://github.com/Amirhackerweb/Bug-server-rubika-yftts27-porn-filter--account-rubika-ir/blob/main/index.html',
    'https://github.com/amirsiahchal/DS/blob/main/%23c%3D%DA%AF%D9%88%DB%8C%D8%AF.html',
    'https://github.com/Rubika-hacker/http-dxprit-filtering-rubika-sxs.gigfa.com-dxprit.html/blob/main/index.html']
linksxs = ['https://github.com/Msramirreza/mrhackergod/blob/main/4f453f300c2fe-full-6.jpg',
           'https://github.com/Msramirreza/mrhackergod/blob/main/IMG-20220704-WA0032.jpg',
           'https://github.com/Msramirreza/mrhackergod/blob/main/IMG-20220823-WA0054.jpg',
           'https://github.com/Msramirreza/mrhackergod/blob/main/IMG_20220726_041439_396.jpg',
           'https://github.com/Msramirreza/mrhackergod/blob/main/IMG_20220825_030904_525.jpg',
           'https://github.com/Msramirreza/mrhackergod/blob/main/VID-20220712-WA0020.mp4',
           'https://github.com/Msramirreza/mrhackergod/blob/main/VID-20220712-WA0020.mp4',
           'https://github.com/Msramirreza/mrhackergod/blob/main/VID-20220712-WA0054.mp4',
           'https://github.com/Msramirreza/mrhackergod/blob/main/VID-20220712-WA0057.mp4',
           'https://github.com/Msramirreza/mrhackergod/blob/main/VID-20220824-WA0072.mp4',
           'https://github.com/Msramirreza/mrhackergod/blob/main/casey-kisses-grooby-girls-06.jpg',
           'https://github.com/Msramirreza/mrhackergod/blob/main/images%20(1)%20(3).jpeg',
           'https://github.com/Msramirreza/mrhackergod/blob/main/images%20(24).jpeg',
           'https://github.com/Msramirreza/mrhackergod/blob/main/images%20(31).jpeg',
           'https://github.com/site4767-debug/Report-Rubika-filtering-Hack-virus-Report-netReport-github.io/blob/main/1639580371_4-babatop-xyz-p-porno-spyat-zhopami-k-verkhu-v-trusakh-10.jpg',
           'https://github.com/site4767-debug/Report-Rubika-filtering-Hack-virus-Report-netReport-github.io/blob/main/1640652333_5-babatop-xyz-p-erotika-v-krasivie-popki-seks-szadi-9.jpg',
           'https://github.com/site4767-debug/Report-Rubika-filtering-Hack-virus-Report-netReport-github.io/blob/main/1640652334_11-babatop-xyz-p-erotika-v-krasivie-popki-seks-szadi-20.jpg',
           'https://github.com/site4767-debug/Report-Rubika-filtering-Hack-virus-Report-netReport-github.io/blob/main/1640652371_6-babatop-xyz-p-erotika-v-krasivie-popki-seks-szadi-11.jpg',
           'https://uploadkon.ir/uploads/972e21_25IMG-20250121-193626-382.jpg',
           'https://uploadkon.ir/uploads/2f2521_25IMG-20250121-193617-704.jpg',
           'https://imgurl.ir/uploads/l402377_IMG_20241029_235008_194.jpg',
           'https://uploadkon.ir/uploads/972e21_25IMG-20250121-193626-382.jpg',
           'https://uploadkon.ir/uploads/94ad21_25IMG-20250121-193615-006.jpg',
           'https://uploadkon.ir/uploads/2f2521_25IMG-20250121-193617-704.jpg',
           'https://imgurl.ir/uploads/l402377_IMG_20241029_235008_194.jpg',
           'https://imgurl.ir/uploads/e207364_IMG_20241029_234816_983.jpg',
           'https://imgurl.ir/uploads/z34919_-5838150527672759350_121.jpg',
           'https://imgurl.ir/uploads/c337473_1_1.jpg',
           'https://uploadkon.ir/uploads/635c21_25IMG-20250121-193621-864.jpg'] 
num = ['0','1','2','3','4','5','6','7','8','9','10']
bug_num = ['05','13','62','63','49','l5','64','67','38','39','46','87','4','56','568','795','368','85','658','254','345','775','355','754','447','745','357']
letter = ['a','f','e','n','h','x','u','t','w','m','z']
slashes = ['/', '//', '///']
letterhss = ['sex',
             'xxx',
             'porn',
             'spam',
             'hack',
             'fil',
             'filter',
             'scamming-users',
             'violent-content',
             'threaten',
             'intimidate',
             'harass-users',
             'Violation-of-Islamic',
             'fuck-Islamic-Republic',
             'pornhub',
             'fuck-rubika',
             'Malicious-link',
             'trolling',
             'publishing',
             'sexual-content',
             'hackxxx',
             'drug',
             'abuse',
             'fuck-islam',
             'violation-rubika',
             'virus']
adad_hasas = 'https://'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+''+random.choice(slashes)+''+random.choice(letter)+''+random.choice(slashes)+''+random.choice(letter)+''+random.choice(slashes)+''+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(bug_num) 
bug = 'https://'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'/'+random.choice(letter)+'//'+random.choice(letter)+'/'+random.choice(letter)+'/'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'/)\''
ltterhss = random.choice(letterhss)+'.'+random.choice(letterhss)+'.'+random.choice(letterhss)+'.'+random.choice(letterhss)
codereal = bug+ltterhss+' '+random.choice(dscripts)+' '+random.choice(linksxs)+' '+ random.choice(drkwblnk)

# Print banner with colorama
# With autoreset=True, there's no need to manually reset at the end of lines; colors reset automatically.
print(green)
print(f" ")
print (white)
print(blue)
print ("    ")
print (yellow)
print(pink)
x = f"""
█▀▀ █▀█ █▀▄ █▀▀  █▀▀ █ █░░ ▀█▀ █▀▀ █▀█  █▀█ █░█ █▄▄ █ █▄▀ ▄▀█
█▄▄ █▄█ █▄▀ ██▄  █▀░ █ █▄▄ ░█░ ██▄ █▀▄  █▀▄ █▄█ █▄█ █ █░█ █▀█ v1.2
"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.0000001)

# Display current time
print(green + str(datetime.datetime.now()))
print(red)
# Display welcome messages
print(green + "Welcome ")
print(light_green + "Programming by DMNHACKER")
print(blue + "Supports Rubika v3.9.8 ")
print(red + " Servers.....ON     ")
print(white + '\n' + light_blue)
print(blue)
time.sleep(2.5)
print("")

# Progress animation
progress = [".........", "........", ".......", "......", ".....", "....", "...", "..", "."]
for i in range(len(progress)):
    print(progress[i])
    time.sleep(0.1 + i * 0.05)
print(light_yellow + "Installed!")
time.sleep(3)
print("")

# Corrected input line with a closing parenthesis
try:
     print(red + "1.code with ID")
     print(red + "2.code normal")
     get = int(input(red + "Enter 1 or 2 >>> "))   
     
     if get == 1:
        idtar4get = input("Enter ID target with out @ >>>")
        rubiktg = idtar4get+')'
        print(pink + codereal + "(https://rubika.ir/" + rubiktg)
        time.sleep(5)
        print('20 gozaresh, 30 mostahgan')
        time.sleep(1)
    
     if get == 2:
        print(blue + codereal)
        time.sleep(5)
        print('20 gozaresh, 30 mostahgan')
        time.sleep(1)

     time.sleep(0.6)
     exit1 = input(green + "Press Enter to go back >>> ")
     print('OK')
     time.sleep(2)
     clear()
     time.sleep(2)
except ValueError:
     print(red + "Invalid input. Please enter a number")
except NameError:
     # Handle the case where 'system' is not defined. The original code had `system("clear")` which is not a standard Python function.
     # The `clear()` function I've defined at the top handles this.
     print(red + "An error occurred. Please check the script.")
     exit()
