from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
import subprocess

class RunExtension(Extension):

    def __init__(self):
        super(RunExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        command = event.query.split(" ", 1)[1]
        items = [
                ExtensionResultItem(
                    icon="images/icon.png",
                    name="Run a shell command",
                    description="Run '%s'" % command,
                    on_enter=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT),
                    ),
                ]

        return RenderResultListAction(items)

if __name__ == '__main__':
    RunExtension().run()

