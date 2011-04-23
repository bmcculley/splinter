import unittest
from fake_webapp import EXAMPLE_APP
from nose.tools import assert_equals, raises
from splinter.request_handler.request_handler import RequestHandler, PageNotFound

class RequestHandlerTestCase(unittest.TestCase):
    def setUp(self):
        self.request = RequestHandler(EXAMPLE_APP)

    def test_should_receive_an_url_and_get_an_200_response(self):
        assert_equals(self.request.status_code, 200)

    def test_should_start_a_request_and_with_localhost_and_get_localhost_as_hostname(self):
        assert_equals(self.request.host, "localhost")

    @raises(PageNotFound)
    def test_should_get_an_absent_url_and_raise_an_exception(self):
        request = RequestHandler(EXAMPLE_APP + "page-that-doesnt-exists")
        assert_equals(request.status_code, 404)
