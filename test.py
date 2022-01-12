""" Module for unittests """

import unittest
import main
import data.scooters
import db.db as db
# from unittest.mock import MagicMock

class Testcase(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Create object for all tests """
        #Arrange
        self.customers = main.get_customers()

    def tearDown(self):
        """ Remove dependencies after test """
        self.customers = None

    def test_get_customers(self):
        """ Test get customers """
        self.assertIsInstance(self.customers, list)
        self.assertEqual(len(self.customers), 100)

    # def test_create_scooters(self):
    #     """ Test create scooters """
    #     self.assertTrue(main.create_scooters())

    def test_create_scooter_sthlm(self):
        """ Test create scooter sthlm """
        result = data.scooters.scooter_sthlm("Test_kund")
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('active_user'), "Test_kund")
        self.assertEqual(result.get('city_location'), "Stockholm")

        # db.createScooter(result) = MagicMock()
        # db.createScooter(result).assert_called()
        # self.assertIsNotNone(resDb)
        # self.assertIsInstance(resDb, dict)
        # self.assertTrue(resDb.get('acknowledged'))

    def test_create_scooter_gbg(self):
        """ Test create scooter gbg """
        result = data.scooters.scooter_gbg("Test_kund")
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('active_user'), "Test_kund")
        self.assertEqual(result.get('city_location'), "Göteborg")

        # resDb = db.createScooter(result)
        # self.assertIsNotNone(resDb)
        # self.assertIsInstance(resDb, dict)
        # self.assertTrue(resDb.get('acknowledged'))

    def test_create_scooter_malmo(self):
        """ Test create scooter malmö """
        result = data.scooters.scooter_malmo("Test_kund")
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('active_user'), "Test_kund")
        self.assertEqual(result.get('city_location'), "Malmö")
        #
        # resDb = db.createScooter(result)
        # self.assertIsNotNone(resDb)
        # self.assertIsInstance(resDb, dict)
        # self.assertTrue(resDb.get('acknowledged'))

    def test_update_scooter(self):
        """ Test update scooter """
        result = data.scooters.update_scooter('61dc666b1d854d307195d11c', 55.575206286000416, +
        12.97877633795938, 90, 55.589747971198285, 12.987239311985748)
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('battery'), 89)
        self.assertTrue(result.get('lat') > 55.575206286000416 and +
        result.get('lat') < 55.589747971198285)
        self.assertTrue(result.get('lng') > 12.97877633795938 and +
        result.get('lng') < 12.987239311985748)

    def test_add_ten_sek(self):
        """ Test add 10 sek """
        result = data.scooters.add_ten_sec("10:14:05")
        self.assertIsInstance(result, str)
        self.assertEqual(result, "10:14:15")

    # def test_update_scooter_done(self):
    #     """ Test update scooter when done """
    #     result = data.scooters.update_scooter_done('61dc666b1d854d307195d11c', +
    #'Stockholm', 75, 55.575206286000416, 12.97877633795938)
    #     self.assertIsInstance(result, dict)
    #     self.assertEqual(result.get('battery'), 75)
    #     self.assertEqual(result.get('speed'), 0)

if __name__ == '__main__':
    unittest.main()
