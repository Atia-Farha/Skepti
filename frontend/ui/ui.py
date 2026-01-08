from textual.containers import VerticalScroll, Container, Grid
from textual.widgets import Header, Footer, TabbedContent, TabPane, Label, Input, Button, ProgressBar, DataTable
from textual.app import App, ComposeResult


class MainUI(VerticalScroll):
	@staticmethod
	def compose():
		yield Header(show_clock=True)
		yield Footer()

		with TabbedContent():
			with TabPane("Scan Image", id="tab_scan"):
				with Container():
					yield Input(id="media_file", placeholder="Enter the absolute path of an image file (e.g., \"C:/Downloads/river.png\")...")

				with Container(id="button_container"):
					yield Button("SCAN NOW", id="submit_btn")

				with Container(id="loading_container"):
					yield ProgressBar(id="loading_bar", show_percentage=False, show_eta=False)

				with Grid(id="result_container"):
					yield Label("Real")
					yield ProgressBar(id="result_real", total=100, show_percentage=True, show_eta=False)

					yield Label("Fake")
					yield ProgressBar(id="result_fake", total=100, show_percentage=True, show_eta=False)

			with TabPane("History", id="tab_history"):
				yield DataTable(id="history_table")