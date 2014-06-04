import sublime, sublime_plugin

class SwitchWindowJsCommand(sublime_plugin.WindowCommand):

    def run(self):

        self.window.run_command("set_layout", {

        	"rows": [0.0, 0.02, 1.0],
	        "cols": [0.0, 0.02, 1.0],
	        "cells": [
	            [1, 0, 2, 1],
	            [1, 1, 2, 2],
	            [0, 0, 1, 2]
	        ]

        })

        self.window.focus_group(1)

class SwitchWindowCssCommand(sublime_plugin.WindowCommand):

    def run(self):

        self.window.run_command("set_layout", {

        	"cols": [0.0, 0.02, 1.0],
	        "rows": [0.0, 0.95, 1.0],
	        "cells": [
	            [1, 0, 2, 1],
	            [1, 1, 2, 2],
	            [0, 0, 1, 2]
	        ]

        })

        self.window.focus_group(0)

class SwitchWindowNormalCommand(sublime_plugin.WindowCommand):

    def run(self):

        self.window.run_command("set_layout", {

        	"cols": [0.0, 0.98, 1.0],
	        "rows": [0.0, 0.5, 1.0],
	        "cells": [
	            [1, 0, 2, 1],
	            [1, 1, 2, 2],
	            [0, 0, 1, 2]
	        ]

        })

        self.window.focus_group(2)