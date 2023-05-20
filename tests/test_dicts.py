import pytest
from utils.dicts import get_val


def test_dicts(dicts_fixture):
    assert get_val(dicts_fixture, 'vcs') == 'mercurial'
    assert get_val(dicts_fixture, 'vcs', 'git') == 'mercurial'
    assert get_val(dicts_fixture, '2', 'git') == 'git'
    assert get_val({}, 'vcs') == 'git'
    assert get_val({}, 'vcs', default='bazaar') == 'bazaar'
