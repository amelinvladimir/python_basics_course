# Создание и активация виртуального окружения
### Windows
```bash
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

### Mac OS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

# Install httpie
### Windows
```bash
python -m pip install --upgrade pip wheel
python -m pip install httpie
```

### Mac OS
```bash
brew update
brew install httpie
```

# Скачивание исходных кодов
### [Адрес репозитория](https://github.com/httpie/cli)
### Если установелн git
```bash
git clone git@github.com:httpie/cli.git
```

### Альтернативный вариант - установить [GitHub Desktop](https://desktop.github.com/download/)
### И в нем скачать проект, указав адрес 
```
git@github.com:httpie/cli.git
```
