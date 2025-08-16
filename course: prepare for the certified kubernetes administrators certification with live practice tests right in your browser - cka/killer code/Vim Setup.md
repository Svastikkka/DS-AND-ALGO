First create or open (if already exists) file .vimrc
```
vim ~/.vimrc
```

Now enter (in insert-mode activated with i) the following lines:
```
set expandtab
set tabstop=2
set shiftwidth=2
```

Save and close the file by pressing Esc followed by :x and Enter.


Explanation
Whenever you open Vim now as the current user, these settings will be used.

If you ssh onto a different server, these settings will not be transferred.

Settings explained:
expandtab: use spaces for tab
tabstop: amount of spaces used for tab
shiftwidth: amount of spaces used during indentation