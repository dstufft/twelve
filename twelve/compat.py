try:
    import extensions
except ImportError:
    import os

    if not "TWELVE_ALLOW_NO_EXTENSIONS" in os.environ:
        raise
    else:
        extensions = None
