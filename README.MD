# Sublime Text View Settings Freely

Put Sublime Text on Free Distraction Mode when editing Sublime Text settings.

It requires the package `DistractionFreeWindow` installed and configured to hide the SideBar and
the Mini Map.

The dirt trick here is to put the current window on the `distraction_free_window` mode on the
`on_window_command` pre command hook, then the new setting windows will inherited it.

Later on the `on_post_window_command` post command hook, we set the current window back from
the `distraction_free_window` mode.

How to hook the new show settings event?
1. https://forum.sublimetext.com/t/how-to-hook-the-new-show-settings-event/23793/2
1. http://docs.sublimetext.info/en/latest/extensibility/commands.html

Add option to disable the minimap and/or lines numbers (if actived) when opening the new Settings
1. https://github.com/evandrocoan/SublimeTextStudio/issues/12

