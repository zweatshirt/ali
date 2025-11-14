import os
import argparse
import subprocess

def find_zshrc():
    home_dir = os.path.expanduser("~")
    zshrc = os.path.join(home_dir, ".zshrc")

    if not (os.path.exists(zshrc)):
        return None
    return zshrc

def append_alias(alias, command):
    zshrc = find_zshrc()
    
    with open(zshrc, "a") as zshrc_file:
        zshrc_file.write(f'\nalias {alias}="{command}"\n')
    print("Run source ~/.zshrc or restart your terminal to apply the changes.")

def remove_alias(alias):
    zshrc = find_zshrc()
    with open(zshrc, 'r') as file:
        lines = file.readlines()

    without_alias = [line for line in lines if not line.strip().startswith(f'alias {alias}=')]

    with open(zshrc, 'w') as file:
        file.writelines(without_alias)
    print("Run source ~/.zshrc or restart your terminal to apply the changes.")

def get_args():
    parser = argparse.ArgumentParser(description="Create aliases quickly.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--add",
                        nargs=2,
                        metavar=('ALIAS', 'COMMAND'),
                        help="Used to create an alias with two following arguments." \
                        " e.g. `ali --add <alias> <command>\n" \
                        "Ensure the <command> arg is a string")
    group.add_argument("--remove",
                        nargs=1,
                        metavar='ALIAS',
                        help="Used to remove an alias from .zshrc." \
                        " e.g. `ali --remove <alias>")
    return parser.parse_args()

def main():
    args = get_args()

    if (args.add):
        alias = args.add[0]
        command = args.add[1]
        append_alias(alias, command)

    if (args.remove):
        alias = args.remove[0]
        remove_alias(alias)


if __name__ == "__main__":
    main()
