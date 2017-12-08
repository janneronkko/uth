import unittest.mock


class MockMixin(object):
    ANY = unittest.mock.ANY

    @staticmethod
    def mock(*args, **kwargs):
        return unittest.mock.Mock(*args, **kwargs)

    @staticmethod
    def magic_mock(*args, **kwargs):
        return unittest.mock.MagicMock(*args, **kwargs)

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
