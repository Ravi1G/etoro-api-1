# coding: utf-8

"""
    eToro Trading API

    The Trading API allows the development of the full trading capabilities in the eToro platform  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import etoro_trading
from api.default_api import DefaultApi  # noqa: E501
from etoro_trading.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_exit_order(self):
        """Test case for create_exit_order

        Exit Order<span> </span>  # noqa: E501
        """
        pass

    def test_delete_exit_order(self):
        """Test case for delete_exit_order

        Exit Order<span></span>  # noqa: E501
        """
        pass

    def test_delete_order(self):
        """Test case for delete_order

        Entry Order<span></span>  # noqa: E501
        """
        pass

    def test_do_login(self):
        """Test case for do_login

        Account  # noqa: E501
        """
        pass

    def test_do_logout(self):
        """Test case for do_logout

        Account<span></span>    # noqa: E501
        """
        pass

    def test_edit_position(self):
        """Test case for edit_position

        Trade<span></span>  # noqa: E501
        """
        pass

    def test_get_credit(self):
        """Test case for get_credit

        Credit  # noqa: E501
        """
        pass

    def test_get_equity(self):
        """Test case for get_equity

        Equity  # noqa: E501
        """
        pass

    def test_get_equity_history(self):
        """Test case for get_equity_history

        Equity History  # noqa: E501
        """
        pass

    def test_get_exit_orders(self):
        """Test case for get_exit_orders

        Exit Order  # noqa: E501
        """
        pass

    def test_get_fees(self):
        """Test case for get_fees

        Fees  # noqa: E501
        """
        pass

    def test_get_instrument_metadata(self):
        """Test case for get_instrument_metadata

        Metadata  # noqa: E501
        """
        pass

    def test_get_orders(self):
        """Test case for get_orders

        Entry Order  # noqa: E501
        """
        pass

    def test_get_trade_history(self):
        """Test case for get_trade_history

        Trade History  # noqa: E501
        """
        pass

    def test_get_trades(self):
        """Test case for get_trades

        Trade  # noqa: E501
        """
        pass

    def test_place_order(self):
        """Test case for place_order

        Entry Order<span> </span>  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
