from unittest import TestCase
from aenum import bin, bits


class TestSEPBin(TestCase):
    def test_bin_positive(self):
        assert bin(10) == "0b0 1010"

    def test_bin_negative(self):
        assert bin(-10) == "0b1 0110"

    def test_bin_zero(self):
        assert bin(0) == "0b0 0"

    def test_bin_max_bits(self):
        assert bin(10, max_bits=8) == "0b0 00001010"


class TestSEPBits(TestCase):
    def test_bits_zero(self):
        assert bits(0) == "0"

    def test_bits_positive(self):
        assert bits(10) == "1010"

    def test_bits_negative(self):
        assert bits(-10) == "10110"
