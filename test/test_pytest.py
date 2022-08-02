import pytest
from main import check_document_existance, get_doc_owner_name
from main_2 import *

class TestSomething:
    def setup(self):
        print("method setup")
    def teardown(self):
        print("method teardown")
    def test_number_doc(self):
        assert check_document_existance('00000000') == False
    def test_owner_name(self):
        assert get_doc_owner_name('11-2') == 'Геннадий Покемонов'
    def test_yaUpLoader(self):
        assert str(YaUploader("TOKEN").create_folder("ZXC")) == '<Response [200]>'