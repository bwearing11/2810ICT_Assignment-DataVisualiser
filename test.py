
def add(a, b, c):
    c = a + b
    return c

def test_add_float(self):
    result = add(10.5, 5, 1)
    self.assertEqual(result, 15.6)


test_add_float()
