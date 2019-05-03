#!/usr/bin/env bash

pip3 install boto3
pip3 install iterfzf
pip3 install -e .

# create awsi configs
mkdir -p ~/.awsi/
cp  default.cfg ~/.awsi/default.cfg
touch -a ~/.awsi/user.cfg # create if not exists, but do not overwrite

# create zsh bindings
LINE="function _awsi-instances { zle -U \`awsi -instances\` }; zle -N _awsi-instances; bindkey '\ei' _awsi-instances"
[ -f ~/.zshrc ] && (grep -qF -- "$LINE" ~/.zshrc || echo "$LINE" >> ~/.zshrc)

LINE="function _awsi-loggroups { zle -U \`awsi -loggroups\` }; zle -N _awsi-loggroups; bindkey '\eg' _awsi-loggroups"
[ -f ~/.zshrc ] && (grep -qF -- "$LINE" ~/.zshrc || echo "$LINE" >> ~/.zshrc)

# create bash bindings
CMD="bind -x '\"\ei\":\"awsi -instances\"'"
[ -f ~/.bashrc ] && (grep -qF -- "$CMD" ~/.bashrc || echo "$CMD" >> ~/.bashrc)

CMD="bind -x '\"\eg\":\"awsi -loggroups\"'"
[ -f ~/.bashrc ] && (grep -qF -- "$CMD" ~/.bashrc || echo "$CMD" >> ~/.bashrc)

printf "\n\nThank you for installing awsi"
printf "\nSharing is caring:\nIf you like awsi, please 'star' it here: https://github.com/jochen-oko/awsi"
printf "\n\nPlease source your rc-file once (e.g. run . ~/zshrc or . ~/bashrc) or open a new shell in order to make the following shortcuts available:"
printf "\n\n\tAlt+i: Select from a list of instances"
printf "\n\tAlt+g: Select from a list of log groups"
