import unittest

from lost_hat_smoke_tests import LostHatSmokeTests
from unittest.loader import makeSuite


def smoke_suite():
    test_suite = unittest.TestSuite()
    # adding test classes:
    test_suite.addTest(makeSuite(LostHatSmokeTests))    # wszystkie testy z tej klasy
    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
suit = smoke_suite()
runner.run(suit)





