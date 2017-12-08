=================
Unit Test Helpers
=================

About
=====

Unit Test Helpers (*uth*) is a simple library for Python containing some helper methods for unit testing.

I found myself writing a lot of setup code using *unittest.mock.patch* and *unittest.TestCase.addCleanup*:

.. code:: python

  class MyTestCase(unittest.TestCase):
      def setUp(self):
          patcher = unittest.mock.patch('module.function')
          patcher.start()
          self.addCleanup(patcher.stop)

          # Or if there was many functions and/or objects to patch
          # something like:
          for patcher in (
              unittest.mock.patch('function_a'),
              unittest.mock.patch('function_b'),
          ):
              patcher.start()
              self.addCleanup(patcher.stop)

Adding helper methods to TestCase classes (via mixin class) allows easier patching:

.. code:: python

  import unittest
  import unittest.mock

  import uth


  def function_a():
      return None


  class MyTestCase(unittest.TestCase, uth.MockMixin):
      def setUp(self):
          # The function function_a is immediately patched and patching is stopped
          # automatically after the test has run (using unittest.TestCase.addCleanup).
          mock = self.patched('{}.function_a'.format(__name__), return_value=self.sentinel.retval)

      def test_function_a(self):
          self.assertEqual(function_a(), self.sentinel.retval)

      def test_sentinel(self):
          self.assertEqual(self.sentinel.value, unittest.mock.sentinel.value)

      def test_mock(self):
          mock = self.mock(return_value=self.sentinel.retval)
          self.assertIsInstance(mock, unittest.mock.Mock)

The *patched* method is the only one that actually provides functionality not directly present in *unittest.mock*. The
members *mock*, *patch* and *sentinel* are provided for convenience; you don't need to import *unittest.mock* and you
can access mock related functionality through *self*.

API
===

uth.MockMixin
-------------

A mixin class for *unittest.TestCase* (or any other class from which you want to use Mock, sentinel and/or patch).

The following members are added:

* **ANY**

  unittest.mock.ANY

* **sentinel** (property)

  Access to *unittest.mock.sentinel*

* **mock(*args, \*\*kwargs)**

  Calls *unittest.mock.Mock* with given arguments

* **magic_mock(*args, \*\*kwargs)**

  Calls *unittest.mock.MagicMock* with given arguments

* **patch(*args, \*\*kwargs)**

  Calls *unittest.mock.patch* with given arguments

* **patched(*args, \*\*kwargs)**

  Calls *unittest.mock.patch* with given arguments, starts the returned patcher, registers stopping the patcher
  using *self.addCleanup* and returns the return value of *patcher.start* (the *Mock* object).
