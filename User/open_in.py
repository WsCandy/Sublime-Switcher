import sublime_plugin
import os

class file_open(sublime_plugin.EventListener):

	def on_load(self, view):
		
		file_name = view.file_name()
		window = view.window()

		if file_name.find('.js') > 0:
			window.set_view_index(view, 1, 0)
			window.focus_group(1)
			window.run_command('switch_window_js', {

				"rows": [0.0, 0.02, 1.0],
		        "cols": [0.0, 0.02, 1.0],
		        "cells": [
		            [1, 0, 2, 1],
		            [1, 1, 2, 2],
		            [0, 0, 1, 2]
		        ]
			
			})

		elif file_name.find('.scss') > 0 or file_name.find('.css') > 0 or file_name.find('.less') > 0:
			window.set_view_index(view, 0, 0)
			window.focus_group(0)
			window.run_command('set_layout', {

				"cols": [0.0, 0.02, 1.0],
		        "rows": [0.0, 0.95, 1.0],
		        "cells": [
		            [1, 0, 2, 1],
		            [1, 1, 2, 2],
		            [0, 0, 1, 2]
		        ]

			})

		else:

			window.set_view_index(view, 2, 0)
			window.focus_group(2)
			window.run_command('set_layout', {

				"cols": [0.0, 0.98, 1.0],
		        "rows": [0.0, 0.5, 1.0],
		        "cells": [
		            [1, 0, 2, 1],
		            [1, 1, 2, 2],
		            [0, 0, 1, 2]
		        ]

			})