# ali
__Create aliases in ~/.zshrc from the command line__
(no bash support yet sry)

---

### You might ask... is something like this really necessary if adding aliases is already really easy?
No

---

### how to use:
- First add ali to your `.zshrc` file as an alias:
`alias ali='source path/to/ali`

For help:
- `ali -h`

To add an alias to your .zshrc:
`ali --add alias command`
- Make sure command is in a string e.g. ali --add gc "git commit -m"

To remove an alias from your .zshrc:
`ali --remove alias`
