"""config.modules 单元测试。"""
from config.modules import (
    MODULE_FIELD_MAPPING,
    MODULE_WHITELISTS,
    SIDE_EFFECT_GET_BLACKLIST,
    is_endpoint_allowed,
    is_side_effect_get,
)


class TestIsSideEffectGet:
    def test_blacklisted_endpoint(self):
        assert is_side_effect_get("/api/Complaint/ConfigureComplaintVerifyUsers") is True
        assert is_side_effect_get("/api/Complaint/RemoveComplaintType") is True

    def test_normal_endpoint(self):
        assert is_side_effect_get("/api/Repair/GetRepairInfos") is False

    def test_unknown_endpoint(self):
        assert is_side_effect_get("/api/Unknown/Whatever") is False


class TestIsEndpointAllowed:
    def test_repair_whitelist_allowed(self):
        assert is_endpoint_allowed("Repair", "/api/Repair/GetRepairInfos") is True

    def test_repair_whitelist_denied(self):
        assert is_endpoint_allowed("Repair", "/api/Repair/UnknownEndpoint") is False

    def test_complaint_no_whitelist_allows_all(self):
        """Complaint 白名单为空 → 所有接口都允许"""
        assert is_endpoint_allowed("Complaint", "/api/Complaint/Anything") is True

    def test_unknown_module_allows_all(self):
        """未配置白名单的模块 → 所有接口都允许"""
        assert is_endpoint_allowed("UnknownModule", "/api/Unknown/Anything") is True


class TestConfigConsistency:
    def test_whitelist_modules_cover_test_modules(self):
        """TEST_MODULES 中的模块都应在 MODULE_WHITELISTS 中有配置"""
        from config.settings import TEST_MODULES
        for module in TEST_MODULES:
            assert module in MODULE_WHITELISTS, f"模块 {module} 未在 MODULE_WHITELISTS 配置"

    def test_field_mapping_covers_detail_modules(self):
        """有详情接口的模块应在 MODULE_FIELD_MAPPING 中有配置。

        Report 模块只有聚合/统计接口，无详情接口，不需要字段映射。
        """
        from config.settings import TEST_MODULES
        # Report 是纯聚合模块，无需字段映射
        detail_modules = [m for m in TEST_MODULES if m != "Report"]
        for module in detail_modules:
            assert module in MODULE_FIELD_MAPPING, f"模块 {module} 未在 MODULE_FIELD_MAPPING 配置"

    def test_blacklist_not_empty(self):
        """副作用黑名单应有内容"""
        assert len(SIDE_EFFECT_GET_BLACKLIST) > 0
