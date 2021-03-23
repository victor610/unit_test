import unittest

input_value = {
    'hired': {
        'be': {
            'to': {
                'deserve': 'I'
            }
        }
    }
}

output_value = {
    'I': {
        'deserve': {
            'to': {
                'be': 'hired'
            }
        }
    }
}


class TestFun(unittest.TestCase):
    def setUp(self):
        self.result = None
        self.dataList = list()

    def Get_sort_value(self, data):

        for key, value in data.items():
            if isinstance(value, dict):
                self.Get_sort_value(data[key])
                self.dataList.append(key)
            else:
                self.dataList.append(value)
                self.dataList.append(key)

    def build_Output_value(self, index=0):
        if len(self.dataList) == index + 1:
            return self.dataList[index]
        else:
            output_value_dict = dict()
            result = self.build_Output_value(index=index + 1)
            output_value_dict[self.dataList[index]] = result
            return output_value_dict

    def test_run(self):
        self.Get_sort_value(input_value)
        self.result = self.build_Output_value()
        self.assertEqual(output_value, self.result)

    def tearDown(self):
        print("output_value = ", self.result)


if __name__ == '__main__':
    unittest.main()
