import pytest
import pandas as pd

from tweets.tweets import tweets_analysis as ta


def test_global_import():
    from tweets.tweets import tweets_analysis


@pytest.mark.parametrize("test_input,expected", [
    ({"path": "/not/valid/path"}, {"error": OSError,
                                   "value": "File /not/valid/path not found"}),
    ({"path": "./tweets/tweets.json", "tags": ['#coffee', '#beans']}, {
     "error": ValueError, "value": "Tags #coffee, #beans do not exist in a dataset"}),
    ({"path": "./tweets/tweets.json", "tags": ['#coffee']}, {
     "error": ValueError, "value": "Tag #coffee does not exist in a dataset"}),
])
def test_wrong_input(test_input, expected):
    with pytest.raises(expected["error"]) as e:
        ta(**test_input)
    assert expected["value"] in str(e.value)


@pytest.mark.parametrize("test_input,expected", [
    ({
        "path": "./tweets/tweets.json",
        "tags": ['#ai', '#bigdata']
    }, float),
    ({
        "path": "./tweets/tweets.json",
        "tags": ['#ai', '#bigdata', '#acquisition']
    }, pd.DataFrame),
])
def test_output_type(test_input, expected):
    output = ta(**test_input)
    assert isinstance(output, expected)


def assert_equal(x, y):
    assert x == y


@pytest.mark.parametrize("test_input,fn_call,expected", [
    (
        {
            "path": "./tweets/tweets.json",
            "tags": ['#ai', '#bigdata']
        },
        assert_equal,
        0.5603877123165414
    ),
    (
        {
            "path": "./tweets/tweets.json",
            "tags": ['#ai', '#bigdata', '#acquisition']
        },
        pd.testing.assert_frame_equal,
        pd.read_pickle('./tests/tweets/test_df.pkl')
    ),
])
def test_corr_value(test_input, fn_call, expected):
    output = ta(**test_input)

    fn_call(output, expected)
