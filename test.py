""" Module for unittests """

import unittest
import main
import data.scooters
import db.db as db
# from unittest.mock import MagicMock

class Testcase(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    # def setUp(self):
    #     """ Create object for all tests """
    #     #Arrange
    #     self.customers = main.get_customers()
    #     result = data.scooters.scooter_sthlm("Test_kund_sthlm")
    #     self.scootersgbg = data.scooters.scooter_gbg("Test_kund_gbg")
    #     self.scootersmalmo = data.scooters.scooter_malmo("Test_kund_malmo")
    #     resDbSthlm = db.create_scooter(self.scooterssthlm)
    #     resDbGbg = db.create_scooter(self.scootersgbg)
    #     resDbMalmo = db.create_scooter(self.scootersmalmo)

    # def tearDown(self):
    #     """ Remove dependencies after test """
    #     self.customers = None
    #     self.scooterssthlm = None
    #     self.scootersgbg = None
    #     self.scootersmalmo = None
    #     self.resDbSthlm = None
    #     self.resDbGbg = None
    #     self.resDbMalmo = None

    def test_get_customers(self):
        """ Test get customers """
        result = main.get_customers()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 100)

    def test_create_delete_scooter_sthlm(self):
        """ Test create and delete scooter sthlm """
        result = data.scooters.scooter_sthlm("Test_kund_sthlm")
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('active_user'), "Test_kund_sthlm")
        self.assertEqual(result.get('city_location'), "Stockholm")

        resDbSthlm = db.create_scooter(result)
        self.assertIsNotNone(resDbSthlm)
        self.assertIsInstance(resDbSthlm, dict)
        self.assertTrue(resDbSthlm.get('acknowledged'))

        _idSthlm = resDbSthlm.get('insertedId')
        resSthlm = db.delete_scooter(_idSthlm)
        self.assertEqual(resSthlm, '{"data":{"result":"Object: ' + _idSthlm + ' deleted"}}')

    def test_create_delete_scooter_gbg(self):
        """ Test create and delete scooter gbg """
        result = data.scooters.scooter_gbg("Test_kund_gbg")
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('active_user'), "Test_kund_gbg")
        self.assertEqual(result.get('city_location'), "Göteborg")

        resDbGbg = db.create_scooter(result)
        print(db.create_scooter(result))
        print(type(resDbGbg))
        self.assertIsNotNone(resDbGbg)
        self.assertIsInstance(resDbGbg, dict)
        self.assertTrue(resDbGbg.get('acknowledged'))

        _idGbg = resDbGbg.get('insertedId')
        resGbg = db.delete_scooter(_idGbg)
        self.assertEqual(resGbg, '{"data":{"result":"Object: ' + _idGbg + ' deleted"}}')

    def test_create_delete_scooter_malmo(self):
        """ Test create and delete scooter malmö """
        result = data.scooters.scooter_malmo("Test_kund_malmo")
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('active_user'), "Test_kund_malmo")
        self.assertEqual(result.get('city_location'), "Malmö")

        resDbMalmo = db.create_scooter(result)
        self.assertIsNotNone(resDbMalmo)
        self.assertIsInstance(resDbMalmo, dict)
        self.assertTrue(resDbMalmo.get('acknowledged'))

        _idMalmo = resDbMalmo.get('insertedId')
        resMalmo = db.delete_scooter(_idMalmo)
        self.assertEqual(resMalmo, '{"data":{"result":"Object: ' + _idMalmo + ' deleted"}}')

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

    def test_update_scooter_done(self):
        """ Test update scooter when done """
        result = data.scooters.update_scooter_done('61dc666b1d854d307195d11c',
        'Stockholm', 75, 55.575206286000416, 12.97877633795938)
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('battery'), 75)
        self.assertEqual(result.get('speed'), 0)

if __name__ == '__main__':
    unittest.main()
