import unittest.mock


class MockMixin(object):
    @staticmethod
    def mock(*args, **kwargs):
        return unittest.mock.Mock(*args, **kwargs)

    @property
    def sentinel(self):
        return unittest.mock.sentinel

    @staticmethod
    def patch(*args, **kwargs):
        return unittest.mock.patch(*args, **kwargs)

    def patched(self, *args, **kwargs):
        patcher = self.patch(*args, **kwargs)
        mock = patcher.start()
        self.addCleanup(patcher.stop)
        return mock
