import unittest
import unittest.mock

import uth


def _func(*args, **kwargs):
    return args, kwargs


class MockMixinTest(unittest.TestCase, uth.MockMixin):
    def setUp(self):
        super().setUp()

        add_cleanup = self.addCleanup
        self.addCleanup = unittest.mock.Mock(
            side_effect=add_cleanup,
        )

    def test_any(self):
        self.assertIs(self.ANY, unittest.mock.ANY)

    def test_mock(self):
        mock = self.mock(name='test mock', return_value=unittest.mock.sentinel.retval)

        self.assertIsInstance(mock, unittest.mock.Mock)
        self.assertEqual(mock(), unittest.mock.sentinel.retval)

        self.assertFalse(self.addCleanup.called)

    def test_magic_mock(self):
        mock = self.magic_mock(name='test mock', return_value=unittest.mock.sentinel.retval)

        self.assertIsInstance(mock, unittest.mock.MagicMock)
        self.assertEqual(mock(), unittest.mock.sentinel.retval)

        self.assertFalse(self.addCleanup.called)

    def test_sentinel(self):
        self.assertIs(self.sentinel, unittest.mock.sentinel)
        self.assertEqual(self.sentinel.sentinel_object, unittest.mock.sentinel.sentinel_object)

        self.assertFalse(self.addCleanup.called)

    def test_patch(self):
        patcher = self.patch('{}._func'.format(__name__), return_value=self.sentinel.retval)
        self.assertIsInstance(patcher, type(unittest.mock.patch('{}._func'.format(__name__))))

        # Make sure the function is not patched implicitly
        self.assertEqual(
            ((self.sentinel.a1, self.sentinel.a2), {'kw': self.sentinel.kwarg}),
            _func(self.sentinel.a1, self.sentinel.a2, kw=self.sentinel.kwarg),
        )

        with patcher:
            self.assertEqual(_func(self.sentinel.arg), self.sentinel.retval)

        self.assertFalse(self.addCleanup.called)

    def test_patched(self):
        mock = self.patched('{}._func'.format(__name__), return_value=self.sentinel.retval)

        self.assertIsInstance(mock, unittest.mock.Mock)

        self.assertEqual(_func(self.sentinel.arg), self.sentinel.retval)

        self.addCleanup.assert_called_once_with(unittest.mock.ANY)
