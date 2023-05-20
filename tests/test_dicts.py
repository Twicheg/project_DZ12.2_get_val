import pytest
from utils.dicts import get_val


def test_dicts():
    assert get_val({'vcs': 'mercurial'}, 'vcs') == 'mercurial'
    assert get_val({'vcs': 'mercurial'}, 'vcs', 'git') == 'mercurial'
    assert get_val({}, 'vcs') == 'git'
    assert get_val({}, 'vcs', default='bazaar') == 'bazaar'
