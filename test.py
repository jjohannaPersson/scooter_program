""" Module for unittests """

import unittest
import main
import data.scooters
import db.db as db

class Testcase(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

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

        res_db_sthlm = db.create_scooter(result)
        self.assertIsNotNone(res_db_sthlm)
        self.assertIsInstance(res_db_sthlm, dict)
        self.assertTrue(res_db_sthlm.get('acknowledged'))

        id_sthlm = res_db_sthlm.get('insertedId')
        res_sthlm = db.delete_scooter(id_sthlm)
        self.assertEqual(res_sthlm, '{"data":{"result":"Object: ' + id_sthlm + ' deleted"}}')

    def test_create_delete_scooter_gbg(self):
        """ Test create and delete scooter gbg """
        result = data.scooters.scooter_gbg("Test_kund_gbg")
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('active_user'), "Test_kund_gbg")
        self.assertEqual(result.get('city_location'), "Göteborg")

        res_db_gbg = db.create_scooter(result)
        self.assertIsNotNone(res_db_gbg)
        self.assertIsInstance(res_db_gbg, dict)
        self.assertTrue(res_db_gbg.get('acknowledged'))

        id_gbg = res_db_gbg.get('insertedId')
        res_gbg = db.delete_scooter(id_gbg)
        self.assertEqual(res_gbg, '{"data":{"result":"Object: ' + id_gbg + ' deleted"}}')

    def test_create_delete_scooter_malmo(self):
        """ Test create and delete scooter malmö """
        result = data.scooters.scooter_malmo("Test_kund_malmo")
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('active_user'), "Test_kund_malmo")
        self.assertEqual(result.get('city_location'), "Malmö")

        res_db_malmo = db.create_scooter(result)
        self.assertIsNotNone(res_db_malmo)
        self.assertIsInstance(res_db_malmo, dict)
        self.assertTrue(res_db_malmo.get('acknowledged'))

        id_malmo = res_db_malmo.get('insertedId')
        res_malmo = db.delete_scooter(id_malmo)
        self.assertEqual(res_malmo, '{"data":{"result":"Object: ' + id_malmo + ' deleted"}}')

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
