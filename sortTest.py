import unittest

def listEdit(unedited):
    unedited.sort()
    edited = []
    keepGoing = True

    for element in unedited:
        if element >= 0:
            edited.append(element)

    return edited
class TestListMethods(unittest.TestCase):
    def test_listEdit(self):
        self.assertEqual(listEdit([-1,4,2,0]),[0,2,4])

if __name__ == '__main__':
    unittest.main()
