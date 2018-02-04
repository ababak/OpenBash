import subprocess
from fman import DirectoryPaneCommand
from fman.url import splitscheme, as_human_readable

class OpenBash(DirectoryPaneCommand):
    def __call__(self):
        url = self.pane.get_path()
        scheme, path = splitscheme(url)
        if scheme != 'file://':
            show_alert('Not supported.')
			return
        local_path = as_human_readable(url)
        subprocess.call('C:/Program Files/Git/git-bash.exe --cd="{cd}"'.format(cd=local_path))
