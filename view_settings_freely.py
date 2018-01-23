

import sublime
import sublime_plugin


class ViewSettingsFreelyListener(sublime_plugin.EventListener):

    def __init__(self):
        super(ViewSettingsFreelyListener, self).__init__()
        self.is_minimap_visible = False

    def on_window_command(self, window, command, args):

        # print ("About to execute " + command)
        if command == "edit_settings":
            self.is_minimap_visible = window.is_minimap_visible()

            # print ("EXECUTING...")
            if self.is_minimap_visible:
                window.run_command("toggle_minimap")


    def on_post_window_command(self, window, command, args):

        # print ("Finished executing " + command)
        if command == "edit_settings":

            # print ("EXECUTING...")
            if self.is_minimap_visible:
                window.run_command("toggle_minimap")


