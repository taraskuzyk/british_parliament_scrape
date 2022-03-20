import pytest as pytest
from bs4 import BeautifulSoup

import scrape


def test_soup():
    with open("petition_example.html", mode="rb") as file:
        html_binary_list = file.readlines()
        html_strings_list = [html_bin.decode("utf-8") for html_bin in html_binary_list]
        html_text = "\n".join(html_strings_list)
        soup = BeautifulSoup(html_text, "html.parser")

    h1 = soup.find("h1")
    assert h1.text == """Protect the Environment – support carbon neutral energy alternatives"""


@pytest.fixture
def soup():
    with open("petition_example.html", mode="rb") as file:
        html_binary_list = file.readlines()
        html_strings_list = [html_bin.decode("utf-8") for html_bin in html_binary_list]
        html_text = "\n".join(html_strings_list)
        return BeautifulSoup(html_text, "html.parser")


def test_get_petition_name(soup: BeautifulSoup):
    assert scrape.get_petition_name(soup) == """Protect the Environment – support carbon neutral energy alternatives"""

