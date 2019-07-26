import unittest

from lost_hat_login_page_tests import LostHatLoginPageTests
from lost_hat_search_test import LostHatSearchTest
from lost_hat_front_page_tests import LostHatFrontPageTests
from unittest.loader import makeSuite


def sanity_suite():
    test_suite = unittest.TestSuite()
    # adding test classes:
    test_suite.addTest(LostHatLoginPageTests('test_correct_login'))  # pojedynczy test z klasy
    test_suite.addTest(LostHatSearchTest('test_sanity_search_on_main_page'))
    test_suite.addTest(LostHatFrontPageTests('test_featured_product_price_in_pl'))
    # test_suite.addTest(makeSuite(LostHatSearchTest))   - cala klasa
    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
suit = sanity_suite()
runner.run(suit)
