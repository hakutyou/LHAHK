from . import keyboardReal
from . import keyboardHwnd
from . import mouseReal
from . import mouseHwnd


keyboard = keyboardReal.KeyboardReal()
keyboardBack = keyboardHwnd.KeyboardHwnd()
mouse = mouseReal.MouseReal()
mouseBack = mouseHwnd.MouseHwnd()
