import unittest

from lost_hat_smoke_tests import LostHatSmokeTests
from lost_hat_product_page_tests import LostHatProductPageTests
from lost_hat_login_page_tests import LostHatLoginPageTests
from lost_hat_front_page_tests import LostHatFrontPageTests
from lost_hat_search_test import LostHatSearchTest

from unittest.loader import makeSuite


def all_suite():
    tests = unittest.TestSuite()
    tests.addTest(makeSuite(LostHatSmokeTests))
    tests.addTest(makeSuite(LostHatProductPageTests))
    tests.addTest(makeSuite(LostHatLoginPageTests))
    tests.addTest(makeSuite(LostHatFrontPageTests))
    tests.addTest(makeSuite(LostHatSearchTest))
    return tests


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suit = all_suite()
    runner.run(suit)
