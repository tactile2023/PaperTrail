import subprocess

def test_cli_accepts_paper_id():

    result = subprocess.run(
        ["papertrail", "2401.12345"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout == "Paper requested: 2401.12345\n"



def test_cli_accepts_paper_url():
    result = subprocess.run(
        ["papertrail", "https://arxiv.org/abs/2401.12345"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout == "Paper requested: 2401.12345\n"



def test_cli_rejects_invalid_input_without_traceback():
    result = subprocess.run(
        ["papertrail", "invalid_input"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "Traceback" not in result.stderr
    assert "Invalid arXiv identifier" in result.stderr