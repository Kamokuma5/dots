# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ${XDG_CONFIG_HOME:-$HOME/.config}/zsh/.p10k.zsh ]] || source ${XDG_CONFIG_HOME:-$HOME/.config}/zsh/.p10k.zsh

HISTFILE=${XDG_CONFIG_HOME:-$HOME/.config}/zsh/.histfile
HISTSIZE=100000
SAVEHIST=100000

# Ignore commands that start with spaces and duplicates.
export HISTCONTROL=ignoreboth

# Don't add certain commands to the history file.
export HISTIGNORE="&:[bf]g:c:clear:history:exit:q:pwd:* --help"

# Use custom `less` colors for `man` pages.
export LESS_TERMCAP_md="$(tput bold 2> /dev/null; tput setaf 2 2> /dev/null)"
export LESS_TERMCAP_me="$(tput sgr0 2> /dev/null)"

# Make new shells get the history lines from all previous
# shells instead of the default "last window closed" history.
export PROMPT_COMMAND="history -a; $PROMPT_COMMAND"


# powerlevel10k theme
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme

# zsh-syntax-highlighting
if [[ ! -d "/usr/share/zsh/plugins/zsh-syntax-highlighting" ]]; then
  echo "Cannot find zsh-syntax-highlighting..."
else
  source "/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"
fi

# zsh-autosuggestions
if [[ ! -d "/usr/share/zsh/plugins/zsh-autosuggestions" ]]; then
  echo "Cannot find zsh-autosuggestions..."
else
  source "/usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh"
fi

# zsh-history-substring-search
if [[ ! -d "/usr/share/zsh/plugins/zsh-history-substring-search" ]]; then
  echo "Cannot find zsh-history-substring-search..."
else
  source "/usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh"
fi

### Aliases
if [ -x "$(command -v eza)" ]; then
    alias la='eza -a'
    alias ll='eza -lah'
    alias ls='eza --color=auto'
else
    echo "eza is not installed"
fi

### Exports
# Editor
if command -v nvim > /dev/null 2>&1; then
  export EDITOR="nvim"
elif command -v vim > /dev/null 2>&1; then
  #echo "Could not find neovim, but vim detected. Setting EDITOR to vim..."
  export EDITOR="vim"
else
  echo "Neovim/vim not found. EDITOR variable remains unset."
fi
