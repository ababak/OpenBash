'''
Open Bash window
'''

import subprocess
import platform
from fman import DirectoryPaneCommand, show_alert, run_application_command, get_application_commands
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
        if platform.system() == 'Windows':
            subprocess.call('C:/Program Files/Git/git-bash.exe --cd="{cd}"'.format(
                cd=local_path))
        else:
            show_alert(
                "Sorry, this plugin is supposed to run on Windows. "
                "Use the built-in 'Open terminal' command on other platforms.")
