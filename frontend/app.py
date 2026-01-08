import os

from textual.app import App, ComposeResult, on
from textual.containers import Container, Grid
from textual.widgets import Button, Input
from textual import work

from frontend.ui.ui import MainUI
from backend.imagedetect import detect_imagefake


class Skepti(App):
	CSS_PATH = "styles/styles.tcss"

	@staticmethod
	def compose() -> ComposeResult:
		yield MainUI()

	def on_mount(self) -> None:
		self.query_one("#media_file", Input).border_title = "File Path"
		self.query_one("#result_container", Grid).border_title = "Result"
		self.query_one("#result_real").progress = 0
		self.query_one("#result_fake").progress = 0

	@on(Input.Changed, "#media_file")
	def on_media_file_change(self) -> None:
		self.query_one("#result_container").styles.display = "none"
		self.query_one("#result_real").progress = 0
		self.query_one("#result_fake").progress = 0
		self.query_one("#submit_btn", Button).label = "SCAN NOW"

	supported_extensions = [".png", ".jpg", ".jpeg", ".svg", ".tiff", ".webp"]

	@work(thread=True)
	def process_media(self, file_path: str) -> str:
		return detect_imagefake(file_path)

	@on(Button.Pressed, "#submit_btn")
	async def on_submit(self):
		self.query_one("#result_container").styles.display = "none"
		self.query_one("#result_real").progress = 0
		self.query_one("#result_fake").progress = 0
		self.query_one("#loading_container").styles.display = "block"

		file_path = self.query_one("#media_file", Input).value.strip()

		if not file_path:
			self.query_one("#loading_container").styles.display = "none"
			self.query_one("#result_container").styles.display = "none"
			self.query_one("#result_real").progress = 0
			self.query_one("#result_fake").progress = 0
			self.notify("Please enter a correct image file path.", title="Empty File Path!", severity="warning", timeout=1.5)
			return

		if not any(file_path.lower().endswith(ext) for ext in self.supported_extensions):
			self.query_one("#loading_container").styles.display = "none"
			self.query_one("#result_container").styles.display = "none"
			self.query_one("#result_real").progress = 0
			self.query_one("#result_fake").progress = 0
			self.notify("Unsupported file format. Please use an image file.\n\nSupported image formats:\n.png, .jpg, .jpeg, .svg, .tiff, .webp", title="Error!", severity="error", timeout=1.5)
			return

		if not os.path.isfile(file_path):
			self.query_one("#loading_container").styles.display = "none"
			self.query_one("#result_container").styles.display = "none"
			self.query_one("#result_real").progress = 0
			self.query_one("#result_fake").progress = 0
			self.notify("File does not exist.", title="Error!", severity="error", timeout=1.5)
			return

		worker = self.process_media(file_path)
		result = await worker.wait()

		if result:
			real, fake = result
			self.query_one("#result_real").progress = real
			self.query_one("#result_fake").progress = fake
			self.query_one("#loading_container").styles.display = "none"
			self.query_one("#result_container").styles.display = "block"
			self.query_one("#submit_btn", Button).label = "RESCAN"
			self.notify("Result generated successfully.", title="Generated!", timeout=1.5)
		else:
			self.query_one("#loading_container").styles.display = "none"
			self.query_one("#result_container").styles.display = "none"
			self.query_one("#result_real").progress = 0
			self.query_one("#result_fake").progress = 0
			self.notify("Failed to detect.", title="Error!", severity="error", timeout=1.5)
