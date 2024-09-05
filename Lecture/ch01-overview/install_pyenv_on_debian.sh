#!/bin/bash
# 참고 문서1 : https://github.com/pyenv/pyenv?tab=readme-ov-file#unixmacos
# 참고 문서2 : https://github.com/pyenv/pyenv/wiki#suggested-build-environment

printmsg() {
  echo -e "\033[1;34m$1\033[0m"
}

PYTHON_VERSION="3.11.8"
BASHRC_PATH="$HOME/.bashrc"

printmsg "backup zshrc"
if [ -f $BASHRC_PATH ]; then
    BACKUP_PATH=$BASHRC_PATH"_backup_$(date +%Y%m%d_%H%M%S)"
    cp $BASHRC_PATH $BACKUP_PATH
    printmsg "backup path : $BACKUP_PATH"
fi

printmsg "update dependencies of debian"
sudo apt update
sudo apt install -y build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev


printmsg "install pyenv"
curl https://pyenv.run | bash

printmsg "write pyenv configure in bashrc"
if ! grep -q 'export PYENV_ROOT="$HOME/.pyenv"' "$BASHRC_PATH"; then
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $BASHRC_PATH
fi

if ! grep -q 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' "$BASHRC_PATH"; then
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> $BASHRC_PATH
fi

if ! grep -q 'eval "$(pyenv init -)"' "$BASHRC_PATH"; then
    echo 'eval "$(pyenv init -)"' >> $BASHRC_PATH
fi

printmsg "source bashrc"
source "$HOME/.bashrc"

#printmsg "pyenv version : `pyenv --version`"
