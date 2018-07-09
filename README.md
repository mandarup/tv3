# Terminal Velocity 3

Terminal Velocity 3 is a TUI application for managing-plain text notes.
It combines finding and creating notes in a single minimal interface and
delegates the note-taking itself to your `$EDITOR`.

![Terminal Velocity 3 Screencast](./tv3.gif)

The interface concept is taken from [Notational
Velocity](http://notational.net/).

This is an active fork of
[terminal-velocity-notes/terminal_velocity](https://github.com/terminal-velocity-notes/terminal_velocity)
and a port from Legacy Python to **Python 3**.

## Installation

### User site installation

This installs to `~/.local/`.  It doesn't need root privileges and keeps
your systemwide Python installation clean.  If you want to install
systemwide just drop the `--user` flag and prepend the last line with
`sudo -H`.

```bash
git clone https://github.com/aramiscd/tv3
cd tv3
pip3 install --user .
cd ..
rm -rf tv3
```

### Installation in a virtual environment

The code currently depends on an older version of Urwid (1.1.1) and
isn't (yet) fully compatibile with more recent versions of Urwid .  So,
if you have other stuff depending on a more recent Urwid in the same
Python environment, you will get a dependency conflict, because Python
doesn't support multiple versions of a Package in the same environment.

The solution is to install tv3 in its own virtual Python environment and
then simlink it to `~/.local/bin/` (or any other directory in your
`$PATH`).  If you are a pythonista you probably already know how to do
this, otherwise just follow the instructions bellow.

```bash
bash
sudo -h pip3 install virtualenv
git clone https://github.com/aramiscd/tv3 ~/.tv3
cd ~/.tv3
virtualenv -p python3 env
env/bin/activate
pip3 install .
deactivate
mkdir -p ~/.local/bin/
ln -s ~/.tv3/env/bin/tv3 ~/.local/bin/
exit
```
