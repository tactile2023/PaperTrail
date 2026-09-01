from arxit.reference_parser import extract_year


def test_extract_year_from_reference():
    raw_text = (
        "K. He, X. Zhang, S. Ren, and J. Sun. "
        "Deep residual learning for image recognition. 2016."
    )
    assert extract_year(raw_text) == 2016


def test_extract_year_from_parantheses():
    raw_text = (
        "Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. "
        "(2019). BERT."
    )
    assert extract_year(raw_text) == 2019


def test_extract_year_returns_none_when_missing():
    raw_text = "OpenAI. An example paper without publication date."

    assert extract_year(raw_text) is None

def test_extract_year_rejects_unreasonable_year():
    raw_text = "Example Author. Example Paper. 3025."

    assert extract_year(raw_text) is None