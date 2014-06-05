import sublime_plugin
import os

class file_open(sublime_plugin.EventListener):

	def on_load(self, view):
		
		file_name = view.file_name()
		window = view.window()

		if file_name.find('.js') > 0 or file_name.find('.json'):
			window.set_view_index(view, 1, 0)
			window.focus_group(1)
			window.run_command('switch_window_js')

		elif file_name.find('.scss') > 0 or file_name.find('.css') > 0 or file_name.find('.less') > 0:
			window.set_view_index(view, 0, 0)
			window.focus_group(0)
			window.run_command('switch_window_css')

		else:

			window.set_view_index(view, 2, 0)
			window.focus_group(2)
			window.run_command('switch_window_normal')