from functools import partial

from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

import navsw

class MyMainWindow(VCPMainWindow):
	"""Main window class for the VCP."""
	def __init__(self, *args, **kwargs):
		super(MyMainWindow, self).__init__(*args, **kwargs)

		self.setConnections()

	def setConnections(self):
		self.leftNavBG.buttonClicked.connect(partial(navsw.leftpage, self))
