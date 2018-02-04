'''
Open Bash window
'''

import subprocess
from fman import DirectoryPaneCommand, show_alert
from fman.url import splitscheme, as_human_readable

class OpenBash(DirectoryPaneCommand):
    '''
    Open Bash
    '''
    def __call__(self):
        url = self.pane.get_path()
        scheme, path = splitscheme(url)
        if scheme != 'file://':
            show_alert('Not supported.')
            return
        local_path = as_human_readable(url)
        subprocess.call('C:/Program Files/Git/git-bash.exe --cd="{cd}"'.format(
            cd=local_path))
