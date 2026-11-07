import unittest

import esphome.config_validation as cv
from esphome.const import CONF_LENGTH

from components.vitoconnect.sensor import (
    CONFIG_SCHEMA,
    SENSOR_LENGTH_SCHEMA,
)


class SensorLengthSchemaTest(unittest.TestCase):
    def test_supported_lengths_are_accepted_by_sensor_schema(self):
        length_validator = next(
            validator
            for key, validator in CONFIG_SCHEMA.schema.items()
            if getattr(key, "schema", key) == CONF_LENGTH
        )

        self.assertIs(length_validator, SENSOR_LENGTH_SCHEMA)
        for length in (1, 2, 4):
            with self.subTest(length=length):
                self.assertEqual(length, length_validator(length))

    def test_unsupported_lengths_are_rejected(self):
        for length in (0, 3, 5, 9, 10, 255):
            with self.subTest(length=length):
                with self.assertRaises(cv.Invalid):
                    SENSOR_LENGTH_SCHEMA(length)


if __name__ == "__main__":
    unittest.main()
