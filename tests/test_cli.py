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