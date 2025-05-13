Upgrade Linux Release Upgrade using the Terminal

sudo apt upgrade (upgrades packages in current)
sudo apt dist-upgrade (upgrades dist)
lsb_release -a (check version)
sudo apt autoremove
sudo do-release-upgrade
make ask for reboot: sudo reboot (for packages)
redo: sudo do-release-upgrade (release upgrade)

restart and check version
lsb_release -a
sudo apt update->update 
sudo apt upgrade->upgrade
sudo apt autoremove->clear space

should be new version

However bug: screen goes blank while entering passwd
Fix as per https://www.stephenwagner.com/2019/05/05/ubuntu-linux-black-screen-frozen-system-after-upgrade-install/
Temporary fix:
> Press right shift button upon restart
> Once GRUB is open, press the “e” key to edit the first highlighted entry “Ubuntu”.
> Move your cursor down to the line that starts with “linux”, and use the right arrow key to find the section with the words “ro quiet splash”.
> Add “nomodeset” after these words.
nomodeset
> Feel free to remove “quiet” and “splash” for more verbosity to troubleshoot the boot process.
> Press “CTRL + X” or “F10” to boot.
> The system should now boot.
> May need multiple attempts

Permanent fix:
> Once the system has booted using the temporary fix, log in.
> Open a terminal window (Applications -> Terminal, or press the “Start” button and type terminal).
> Either “su” in to root, or use “sudo” to open your favorite text editor and edit the file “/etc/default/grub” (I use nano which can be install by running “apt install nano”):
nano /etc/default/grub
> Locate the line with the variable “GRUB_CMDLINE_LINUX_DEFAULT”, and add “nomodeset” to the variables. Feel free to remove “splash” and “quiet” if you’d like text boot. Here’s an example of my line after editing (yours will look different):
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"
> Save the file and exit the text editor (CTRL+X to quit, the press “y” and enter to save).
> At the bash prompt, execute the following command to regenerate the grub.conf file on the /boot partition from your new default file:
update-grub
> Restart your system, it should now boot!

Setup T530: In progress
Moved to thinkpad, for easier steps (vs Ideapad)
Thinkpad configuration: Intel i7 Pro (4-core), 8GB RAM, 128GB SSD