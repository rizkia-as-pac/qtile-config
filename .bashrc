#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias killsidebutton="xmodmap -e 'pointer = 1 2 3 4 5 6 7 0 0 0 0 0 0'"
alias tree="find .  | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"
alias kucing="kitty --detach"
alias ping="ping google.com"

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias v='nvim .'
alias workdir='cd ~/Desktop/work'
alias kuliah='cd ~/Desktop/kuliah'
alias learnspace='cd ~/Desktop/learn'
alias gitlog='git log --all --decorate --oneline --graph'
PS1='[\u@\h \W]\$ '

