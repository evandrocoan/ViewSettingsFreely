

import sublime
import sublime_plugin


class SampleListener(sublime_plugin.EventListener):

    def on_window_command(self, window, command, args):
        
        # print ("About to execute " + command)
        
        if command == "edit_settings":
            
            # print ("EXECUTING...")
            window.run_command("distraction_free_window")


    def on_post_window_command(self, window, command, args):
        
        # print ("Finished executing " + command)
        
        if command == "edit_settings":
            
            # print ("EXECUTING...")
            window.run_command("distraction_free_window")



