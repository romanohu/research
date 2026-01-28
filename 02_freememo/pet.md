# pet
シンプルなコマンドラインスニペット管理ツール

---
コマンドを登録する
Command: 保存したいコマンドを入力
Description: 説明を入力
```sh
pet new
# <>で囲んだ部分は呼び出すときに入力できる
```

---
コマンドを編集する
```sh
pet edit
```

---
tips1
以下を.zshrcに貼り付けるとCtrl+sで呼び出せる
```zshrc
function pet-select() {
  BUFFER=$(pet search --query "$LBUFFER")
  CURSOR=$#BUFFER
  zle redisplay
}
zle -N pet-select
stty -ixon
bindkey '^s' pet-select

function pet-select() {
  BUFFER=$(pet search --query "$LBUFFER")
  CURSOR=$#BUFFER
  zle redisplay
}
zle -N pet-select
stty -ixon
bindkey '^s' pet-select

function _pet_move_cursor_to_next_parameter() {
    match="$(echo "$BUFFER" | perl -nle 'print $& if /<.*?>/')"
    if [ -n "$match" ]; then
      default="$(echo "$match" | perl -nle 'print $& if /(?<==).*(?=>)/')"
      match_len=${#match}
      default_len=${#default}
      parameter_offset=${#BUFFER%%$match*}

      CURSOR="$((${parameter_offset} + ${default_len}))"
      BUFFER="${BUFFER[1,$parameter_offset]}${default}${BUFFER[$parameter_offset+$match_len+1,-1]}"
    fi        
}
zle -N _pet_move_cursor_to_next_parameter
bindkey '^n' _pet_move_cursor_to_next_parameter 
```

---
tips2
Gistで端末間でコマンドを共有できる
```sh
pet configure
# [Gist]のaccess_tokenに
```
