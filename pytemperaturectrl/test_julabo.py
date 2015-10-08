import julabo
import unittest


class TestFonctionGet(unittest.TestCase):
	def test_getVersion(self):
		tc = julabo.Julabo()
		tc.open('COM5')
		ver = tc.getVersion()
		self.assertEqual(ver, 'JULABO CORIO CD - 200F 230V 50Hz Version 2.4.1')
		tc.close()

	def test_getStatus(self):
		tc = julabo.Julabo()
		tc.open('COM5')
		status = tc.getStatus()
		self.assertRegexpMatches(status, '^\d[2]\s.*')
		tc.close()		
		
	def test_getsetWorkTemperature(self):
		tc = julabo.Julabo()
		tc.open('COM5')
		tc.setWorkTemperature( 12.3 )
		tmp = tc.getWorkTemperature()
		self.assertEqual(tmp, 12.3)
		tc.close()	

	def test_getCurrentTemperature(self):
		tc = julabo.Julabo()
		tc.open('COM5')
		t = tc.getCurrentTemperature()
		self.assertTrue( t > 0.0 and t < 30.0 )
		tc.close()	
		
	def test_notOpen(self):
		tc = julabo.Julabo()
		with self.assertRaises(Exception):
			tc.getCurrentTemperature()
		
if __name__ == '__main__':
    unittest.main()		