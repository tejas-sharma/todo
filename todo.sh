python3 "$HOME/bin/todo.py" "$HOME/config/todo.config"
read -r today<"$HOME/config/todo.config"
vim $today

