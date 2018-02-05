'''
Open Bash window
'''

import subprocess
import platform
import os.path
from fman import DirectoryPaneCommand, show_alert, run_application_command, get_application_commands
from fman.url import splitscheme, as_human_readable

class OpenBash(DirectoryPaneCommand):
    '''
    Open Bash
    '''

    GIT_BASH = 'C:/Program Files/Git/git-bash.exe'

    def __call__(self):
        url = self.pane.get_path()
        scheme, path = splitscheme(url)
        if scheme != 'file://':
            show_alert('Not supported.')
            return
        local_path = as_human_readable(url)
        if platform.system() == 'Windows' and os.path.isfile(self.GIT_BASH):
            subprocess.call('{bash_exe} --cd="{cd}"'.format(
                bash_exe=self.GIT_BASH,
                cd=local_path))
        else:
            self.pane.run_command('open_terminal')
