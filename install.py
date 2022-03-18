#!bin/python3
import os
import datetime as dt
import time
''' i3wm install scrip
    Copyright (C) 2022 anomic-cr

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''
now =str(dt.datetime.now())
cowsay.daemon('welcome' + now)

def update():
    print('updating system')
    os.system('sudo pacman -Syu')
    print('done moving to next phase(it may take a while please grab a coffee) ;-;')

def helper_install():
    il = int(input('Do you have a aur helper installed?\n1.Yes\n2.No\n(repsond with 1 or 2):'))
    if il == 1:
        print('okay..skiping')
    else:
        os.system('git clone https://aur.archlinux.org/yay.git')
        os.system('cd yay && makepkg -si')
        os.system('cd .. && rm -rf yay')



def dep_install():
    os.system('yay -S --noconfirm --needed i3-gaps sddm betterlockscreen i3status-git i3blocks-git alacritty rofi-git neofetch-git polybar-git dunst-git feh-git nitrogen picom lxappearance')
    os.system('yay -S xorg xorg-xinit zsh xorg-server qt5')


def extra():
    ins = int(input('do you want to install some more extra packages?\n1.Yes\n2.No\n(respond with 1 or 2):'))
    if ins == 1:
        os.system('yay -S --noconfirm --needed neovim visual-studio-code-bin-git python-pynvim zsh zsh-completions zsh-syntax-highlighting zsh-autosuggestions zsh-history-substring-search zsh-history-substring-search-git xclip maim')
        print('installing *moreeee* extra packages')
        os.system('yay -S --noconfirm --needed neofetch uwufetch awesome-fonts-git htop nerd-fonts-complete-git noto-fonts-emoji-git noto-fonts-cjk-git noto-fonts-extra-git noto-fonts-extra-cjk-git noto-fonts-mono-git noto-fonts-symbols-git')
    else:
        print("ok ;-;")



def tip():
    print("I assume you have pulseaudio installed, it often creates problem on my system so I'd recommend instlling pipewire instead")
    pipe = int(input('do you want to install pipewire?\n1.Yes\n2.No\n(respond with 1 or 2):'))
    if pipe == 1:
        os.system('yay -S --noconfirm --needed pipewire pipewire-alsa pipewire-bluetooth')
        os.system('sudo pacman -Rns pulseaudio pulseaudio-alsa')


def copy_config():
    print('copying config files')
    os.system('cp -r .config/ ~/.config/')
    os.system('cp .bashrc ~/.bashrc')
    os.system('cp .zshrc ~/.zshrc')
    os.system('cp .Xresources ~/.Xresources')
    #os.system('cp .xinitrc ~/.xinitrc')
    os.system('cp .local ~/.local')
    os.system('cp -r .icons ~/.icons')
    os.system('cp -r gtkrc-2.0 ~/.gtkrc-2.0')

 
def set_sddm():
    print('setting sddm theme')
    os.system('git clone https://github.com/keyitdev/sddm-astronaut-theme.git')
    os.system('sudo cp -fdr sddm-astronaut-theme /usr/share/sddm/themes/')
    os.system('sudo cp /usr/share/sddm/themes/sddm-astronaut-theme/Fonts/* /usr/share/fonts/')
    os.system('''
    echo "[Theme]
    Current = sddm-astronaut-theme" | sudo tee /etc/sddm.conf
    "''')


def try_en():
    print('trying to enable sddm service, if you already have a dispaly manager installed, you can skip this and disbale your current DM and then enable sddm')
    q = int(input('do you want to enable sddm?\n1.Yes\n2.No\n(respond with 1 or 2):'))
    if q == 1:
        os.system('sudo systemctl enable sddm.service')
    else:
        print('everything is done')

ing = 0
nt = 5
def reboot():
    for ing in range(5):
        print(f'restarting after{nt}')
        time.sleep(secs=1)
        nt-=1
        ing+=1


print('done installing')

if __name__ == '__main__':
    update()
    helper_install()
    dep_install()
    extra()
    tip()
    copy_config()
    set_sddm()
    try_en()
    reboot()