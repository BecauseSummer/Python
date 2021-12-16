# –*–coding:utf-8 –*–
# 2021-12-20 14:38
import pytest


@pytest.fixture()
@pytest.mark.skip()
def test1():
    print('run function')

@pytest.mark.usefixtures('test1', autouse=True)
def test_a():
    print('case a run')

@pytest.mark.usefixtures('test1')
class TestCase:
    def test_b(self):
        print('case b run')

    def test_c(self):
        print('case c run')

if __name__ == '__main__':
    pytest.main([ 'test._fixture1.py'])