import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    expected_result = [
            ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2), 
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]
        
    results = []
    for quote in quotes:
        result = getDataPoint(quote)  
        results.append(result)
    self.assertEqual(results, expected_result)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    expected_result = [
      ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),  
      ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
    ]
    
    results = []
    for quote in quotes:
        result = getDataPoint(quote)
        results.append(result)
    self.assertEqual(results, expected_result)


  def test_positive_ratio(self):
    
      price_a = 10
      price_b = 5
      expected_ratio = 2.0
      self.assertEqual(getRatio(price_a, price_b), expected_ratio)

  def test_zero_denominator(self):
     
      price_a = 10
      price_b = 0
      self.assertIsNone(getRatio(price_a, price_b))

  def test_zero_numerator(self):
      
      price_a = 0
      price_b = 5
      expected_ratio = 0.0
      self.assertEqual(getRatio(price_a, price_b), expected_ratio)






if __name__ == '__main__':
    unittest.main()
