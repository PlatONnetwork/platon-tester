from __future__ import unicode_literals

import pytest

from platon_tester import (
    PlatonTester,
    MockBackend,
)

from platon_tester.utils.backend_testing import (
    BaseTestBackendDirect,
)


@pytest.fixture
def platon_tester():
    backend = MockBackend()
    return PlatonTester(backend=backend)


class TestMockBackendDirect(BaseTestBackendDirect):
    supports_evm_execution = False

    @pytest.mark.skip(reason="receipt status not supported in MockBackend")
    def test_get_transaction_receipt_byzantium(self, platon_tester, test_transaction):
        pass

    @pytest.mark.skip(reason="receipt status not supported in MockBackend")
    def test_get_transaction_receipt_byzantium(self, platon_tester, test_transaction):
        pass
