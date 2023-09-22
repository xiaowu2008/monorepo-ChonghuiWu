import unittest
import jsonapi

class TestJSONAPI(unittest.TestCase):

    def test_complex_serialization(self):
        complex_number = 3 + 4j
        serialized = jsonapi.dumps(complex_number)
        deserialized = jsonapi.loads(serialized)

        self.assertEqual(complex_number, deserialized)

    def test_range_serialization(self):
        r = range(5, 10)
        serialized = jsonapi.dumps(r)
        deserialized = jsonapi.loads(serialized)

        self.assertEqual(list(r), list(deserialized))

    def test_dumps(self):
            complex_number = 3 + 4j
            serialized = jsonapi.dumps(complex_number)
            self.assertEqual(serialized, '{"real": 3.0, "imag": 4.0, "__extended_json_type__": "complex"}')


if __name__ == "__main__":
    unittest.main()
