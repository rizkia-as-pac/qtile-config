#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias v='nvim .'
alias workdir='cd ~/Desktop/work'
alias gitlog='git log --all --decorate --oneline --graph'
PS1='[\u@\h \W]\$ '

