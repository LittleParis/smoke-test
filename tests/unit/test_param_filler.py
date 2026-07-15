"""core.param_filler 单元测试。"""
from core.param_filler import fill_params_from_cache, inject_list_filter_params


class TestFillParamsFromCache:
    def test_cache_placeholder_replaced(self):
        """__cache__ 占位符被缓存值替换"""
        cache = {"Repair": {"repairId": 123}}
        params = {"RepairId": "__cache__RepairId", "Platform": "MyEhi"}
        result = fill_params_from_cache(params, "Repair", cache, case_type="positive")
        assert result["RepairId"] == 123

    def test_cache_placeholder_missing_deleted(self):
        """__cache__ 占位符缓存未命中 → 删除参数"""
        cache = {"Repair": {}}
        params = {"RepairId": "__cache__RepairId"}
        result = fill_params_from_cache(params, "Repair", cache, case_type="positive")
        assert "RepairId" not in result

    def test_positive_detail_no_cache_deleted(self):
        """正向详情接口：非占位符参数缓存未命中 → 删除（避免传假值）"""
        cache = {"Complaint": {}}
        params = {"id": 52, "Platform": "MyEhi"}
        result = fill_params_from_cache(params, "Complaint", cache, case_type="positive")
        assert "id" not in result
        assert "Platform" in result  # COMMON_PARAMS 保留

    def test_positive_list_keeps_params(self):
        """正向列表接口：非占位符参数缓存未命中 → 保留（不删除）"""
        cache = {"Complaint": {}}
        params = {"SkipCount": 0, "MaxResultCount": 10, "Platform": "MyEhi"}
        result = fill_params_from_cache(params, "Complaint", cache, case_type="positive")
        assert "SkipCount" in result
        assert "MaxResultCount" in result

    def test_positive_detail_cache_hit_replaces(self):
        """正向详情接口：非占位符参数缓存命中 → 替换"""
        cache = {"Complaint": {"id": 100}}
        params = {"id": 52, "Platform": "MyEhi"}
        result = fill_params_from_cache(params, "Complaint", cache, case_type="positive")
        assert result["id"] == 100

    def test_pairwise_only_replaces_placeholders(self):
        """组合查询：只替换 __cache__ 占位符，保留其他参数"""
        cache = {"Repair": {"carNo": "京A123"}}
        params = {
            "CarNo": "__cache__CarNo",
            "IsAuth": True,  # BOOL_DEFAULT_TRUE，保留
            "Platform": "MyEhi",
            "SkipCount": 0,
        }
        result = fill_params_from_cache(params, "Repair", cache, case_type="pairwise")
        assert result["CarNo"] == "京A123"
        assert result["IsAuth"] is True

    def test_common_params_preserved(self):
        """COMMON_PARAMS 始终保留，不走缓存逻辑"""
        cache = {}
        params = {"Platform": "MyEhi", "SkipCount": 0, "MaxResultCount": 10}
        result = fill_params_from_cache(params, "Repair", cache, case_type="positive")
        assert result["Platform"] == "MyEhi"

    def test_bool_default_true_preserved(self):
        """BOOL_DEFAULT_TRUE 保留"""
        cache = {}
        params = {"IsAuth": True}
        result = fill_params_from_cache(params, "Repair", cache, case_type="positive")
        assert result["IsAuth"] is True


class TestInjectListFilterParams:
    def test_inject_carno_when_missing(self):
        """缺少 CarNo 时从缓存注入"""
        cache = {"Repair": {"carNo": "京A123"}}
        params = {"Platform": "MyEhi"}
        result = inject_list_filter_params(params, "Repair", cache)
        assert result["CarNo"] == "京A123"

    def test_keep_existing_carno(self):
        """已有 CarNo 时不覆盖"""
        cache = {"Repair": {"carNo": "京A123"}}
        params = {"CarNo": "沪B456"}
        result = inject_list_filter_params(params, "Repair", cache)
        assert result["CarNo"] == "沪B456"

    def test_inject_keyno_when_missing(self):
        """缺少 KeyNo 时从缓存注入（缓存键为 keyNo，值来自 repairId 响应字段）"""
        cache = {"Repair": {"keyNo": 100}}
        params = {}
        result = inject_list_filter_params(params, "Repair", cache)
        assert result["KeyNo"] == 100

    def test_no_inject_when_cache_empty(self):
        """缓存为空 → 不注入"""
        cache = {"Repair": {}}
        params = {}
        result = inject_list_filter_params(params, "Repair", cache)
        assert "CarNo" not in result
        assert "KeyNo" not in result
