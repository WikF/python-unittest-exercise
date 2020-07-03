from employee import Employee
import pytest


@pytest.fixture()
def employee():
    return Employee(first="Walter", last="Smith", pay=1000)


def test_email(employee):
    assert '{}.{}@email.com'.format(employee.first, employee.last) == 'Walter.Smith@email.com'


def test_fullname(employee):
    assert '{} {}'.format(employee.first, employee.last) == 'Walter Smith'



def test_apply_raise(employee):
    employee.apply_raise()
    assert 1050 == employee.pay
