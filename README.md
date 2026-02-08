### Firefox Tab Integration (Brotab Setup)
This Qtile configuration includes integration with Firefox tab switching using Brotab, allowing users to search and switch browser tabs directly from Qtile via rofi.

Before using this feature, Brotab must be properly configured.

#### 1. Install Python via asdf (Recommended)
This configuration expects a modern Python version managed via asdf.

Install Python:

```bash
asdf plugin add python https://github.com/asdf-community/asdf-python.git
asdf install python 3.13.0
asdf set -u python 3.13.0
```

Verify installation:

```bash
python3.13 --version
```

#### 2. Install Firefox Brotab Extension
Install the Brotab extension for Firefox:
https://addons.mozilla.org/en-US/firefox/addon/brotab/
After installation, restart Firefox.

#### 3. Install Brotab CLI via pipx
Install Brotab CLI using pipx to keep it isolated from the system Python:

```bash
pipx uninstall brotab
pipx install brotab --python python3.13
```

Verify installation:

```bash
bt --version
bt clients
bt list
```

If bt list shows your Firefox tabs, the setup is working correctly.

#### 4. Additional Dependency (Arch Linux)
On Arch Linux systems, Brotab requires the following package:

```bash
sudo pacman -S python-lz4
```

#### 5. Install pipx (if not installed)

```bash
sudo pacman -S python-pipx
pipx install brotab
pipx ensurepath
```

#### What does pipx ensurepath do?
This command checks whether the directory:

```bash
~/.local/bin
```


is included in your shell's PATH.

If not, pipx automatically adds a line to your shell configuration file such as:

```bash
~/.bashrc
~/.zshrc
or other shell config
```

containing:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

This allows commands like bt to be executed directly in the terminal.

#### 6. Final Verification

Run:

```bash
bt clients
bt list
```

If your Firefox tabs are listed, the Qtile browser picker integration is ready to use.

Troubleshooting

If Firefox is running but bt list shows no tabs:
- Ensure Firefox was restarted after installing the extension.
- Ensure only one Firefox profile instance is running.
- Confirm the Brotab extension is enabled in Firefox.