from fman import DirectoryPaneCommand
import subprocess

class OpenBash(DirectoryPaneCommand):
    def __call__(self):
        subprocess.call('C:/Program Files/Git/git-bash.exe --cd="{cd}"'.format(cd=self.pane.get_path()))
