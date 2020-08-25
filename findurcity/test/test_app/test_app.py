import flask

TEST_APP = flask.Flask(__name__)


class TestAPP:
    
    def test_APP():
        with TEST_APP.test_request_context('/?name=Peter'):
            assert flask.request.path == '/'
            assert flask.request.args['name'] == 'Peter'

if __name__ == "__main__":
    TestAPP()
