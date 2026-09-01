from arxit.reference_parser import extract_arxiv_id, extract_year


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



from arxit.reference_parser import extract_arxiv_id, extract_year


def test_extract_modern_arxiv_id():
    raw_text = "Goodfellow et al. Maxout Networks. arXiv:1302.4389, 2013."

    assert extract_arxiv_id(raw_text) == "1302.4389"


def test_extract_versioned_arxiv_id():
    raw_text = "Example paper. arXiv:2404.01349v2."

    assert extract_arxiv_id(raw_text) == "2404.01349v2"


def test_extract_arxiv_id_from_url():
    raw_text = "Available at https://arxiv.org/abs/1706.03762."

    assert extract_arxiv_id(raw_text) == "1706.03762"


def test_extract_legacy_arxiv_id():
    raw_text = "Example paper. arXiv:hep-th/9901001."

    assert extract_arxiv_id(raw_text) == "hep-th/9901001"


def test_extract_arxiv_id_returns_none_when_missing():
    raw_text = "Example Author. Example Paper. 2024."

    assert extract_arxiv_id(raw_text) is None