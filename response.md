{
  "openapi": "3.0.4",
  "info": {
    "title": "CorpAfterSaleApi",
    "description": "\n该平台Id `1011100`，团队 `Eo`，维护人 ``，Tags `售后系统`，Library版本：`7.3.5` `.NET 10.0.8`，[BuildUrl](https://tfs.1hai.cn/tfs/Front.Dev/eHi/_build/results?buildId=447436)， 配置前往[itwork](http://itwork.demo.ehi.com.cn/System/Team)\n",
    "version": "2026052016"
  },
  "paths": {
    "/api/Accident/AddAccidentLog": {
      "post": {
        "tags": [
          "Accident"
        ],
        "summary": "事故查询 添加日志",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.AddAccidentLogInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.AddAccidentLogInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.AddAccidentLogInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00010"
            ]
          }
        ]
      }
    },
    "/api/Accident/EditFollowState": {
      "post": {
        "tags": [
          "Accident"
        ],
        "summary": "修改事故跟进状态",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.EditFollowStateInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.EditFollowStateInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.EditFollowStateInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00029"
            ]
          }
        ]
      }
    },
    "/api/Accident/ExportAccidentInfoExcel": {
      "get": {
        "tags": [
          "Accident"
        ],
        "summary": "事故记录导出Excel",
        "parameters": [
          {
            "name": "IsAuth",
            "in": "query",
            "description": "是否来自分离后的前端项目",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "AcctId",
            "in": "query",
            "description": "政企ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AccidentId",
            "in": "query",
            "description": "事故单号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AccidentType",
            "in": "query",
            "description": "事故类型",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AccidentLevel",
            "in": "query",
            "description": "车损等级",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer",
                "format": "int32"
              }
            }
          },
          {
            "name": "IncludeRs",
            "in": "query",
            "description": "是否包含人伤事故 是true 否false",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "AmountRange",
            "in": "query",
            "description": "事故等级对应车损 金额 范围",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/System.Collections.Generic.KeyValuePair`2[[System.Decimal, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Decimal, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
              }
            }
          },
          {
            "name": "EnterprisetName",
            "in": "query",
            "description": "政企名称",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "StatusFlag",
            "in": "query",
            "description": "事故状态",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ChildStatusFlag",
            "in": "query",
            "description": "事故子状态",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OprNo",
            "in": "query",
            "description": "跟进入编号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UseCity",
            "in": "query",
            "description": "用车城市",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "NextFlowTimeStart",
            "in": "query",
            "description": "下次跟进时间 开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "NextFlowTimeEnd",
            "in": "query",
            "description": "下次跟进时间 结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "AccTimeStart",
            "in": "query",
            "description": "事故时间 开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "AccTimeEnd",
            "in": "query",
            "description": "事故时间 结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "IsNoFollow",
            "in": "query",
            "description": "是否跟进",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "AccidentPhone",
            "in": "query",
            "description": "事故人手机号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ClientType",
            "in": "query",
            "description": "客户类型",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "BizType",
            "in": "query",
            "description": "事故归属类型 1 自驾零单，2代驾零单，3长包自驾，3长包代驾",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
            }
          },
          {
            "name": "FollowStates",
            "in": "query",
            "description": "跟进状态",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AccidentFollowState"
              }
            }
          },
          {
            "name": "DutyType",
            "in": "query",
            "description": "事故责任划分",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.DutyTypes"
            }
          },
          {
            "name": "UserAdvanceFollowState",
            "in": "query",
            "description": "客户垫付费用跟进状态 1.无 2.待退还 3.已退还（报销） 4.已退还（退款） 5.已退还（直赔）",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.UserAdvanceFollowStateType"
            }
          },
          {
            "name": "CarMaintainDepositFollowState",
            "in": "query",
            "description": "本车维修押金跟进状态 1.无 2.待收取 3.已收取待结算 4.已支付已结算",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.CarMaintainDepositFollowStateType"
            }
          },
          {
            "name": "DerogatoryFollowState",
            "in": "query",
            "description": "贬损费用跟进状态 1.无 2.待收取 3.已收取",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.DerogatoryFollowStateType"
            }
          },
          {
            "name": "CarMaintainFollowState",
            "in": "query",
            "description": "本车维修费用跟进状态 1.无 2.待支付 3.已支付（退款） 4.已支付（直赔）",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.CarMaintainFollowStateType"
            }
          },
          {
            "name": "ThreeCostFollowState",
            "in": "query",
            "description": "三者费用跟进状态 1.无 2.待支付 3.已支付（退款） 4.已支付（直赔）",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.ThreeCostFollowStateType"
            }
          },
          {
            "name": "IsOutsideMaintain",
            "in": "query",
            "description": "是否在外维修",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "AppraisalLawsuit",
            "in": "query",
            "description": "公估诉讼 0.否 1.公估 2.诉讼",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AppraisalLawsuitType"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.ExportAccidentInfoExcelOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00041;False"
            ]
          }
        ]
      }
    },
    "/api/Accident/GetAccidentAnnualInspectionCount": {
      "get": {
        "tags": [
          "Accident"
        ],
        "summary": "事故查询数据订单类型分类汇总列表",
        "parameters": [
          {
            "name": "IsAuth",
            "in": "query",
            "description": "是否来自分离后的前端项目",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "AcctId",
            "in": "query",
            "description": "政企ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AccidentId",
            "in": "query",
            "description": "事故单号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AccidentType",
            "in": "query",
            "description": "事故类型",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AccidentLevel",
            "in": "query",
            "description": "车损等级",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer",
                "format": "int32"
              }
            }
          },
          {
            "name": "IncludeRs",
            "in": "query",
            "description": "是否包含人伤事故 是true 否false",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "AmountRange",
            "in": "query",
            "description": "事故等级对应车损 金额 范围",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/System.Collections.Generic.KeyValuePair`2[[System.Decimal, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Decimal, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
              }
            }
          },
          {
            "name": "EnterprisetName",
            "in": "query",
            "description": "政企名称",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "StatusFlag",
            "in": "query",
            "description": "事故状态",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ChildStatusFlag",
            "in": "query",
            "description": "事故子状态",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OprNo",
            "in": "query",
            "description": "跟进入编号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UseCity",
            "in": "query",
            "description": "用车城市",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "NextFlowTimeStart",
            "in": "query",
            "description": "下次跟进时间 开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "NextFlowTimeEnd",
            "in": "query",
            "description": "下次跟进时间 结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "AccTimeStart",
            "in": "query",
            "description": "事故时间 开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "AccTimeEnd",
            "in": "query",
            "description": "事故时间 结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "IsNoFollow",
            "in": "query",
            "description": "是否跟进",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "AccidentPhone",
            "in": "query",
            "description": "事故人手机号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ClientType",
            "in": "query",
            "description": "客户类型",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "BizType",
            "in": "query",
            "description": "事故归属类型 1 自驾零单，2代驾零单，3长包自驾，3长包代驾",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentAnnualInspectionCountOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00008"
            ]
          }
        ]
      }
    },
    "/api/Accident/GetAccidentInfo": {
      "get": {
        "tags": [
          "Accident"
        ],
        "summary": "获取事故详情",
        "parameters": [
          {
            "name": "AccidentId",
            "in": "query",
            "description": "事故Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentInfoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Accident/GetAccidentInfos": {
      "get": {
        "tags": [
          "Accident"
        ],
        "summary": "获取 事故查询 数据",
        "parameters": [
          {
            "name": "IsAuth",
            "in": "query",
            "description": "是否来自分离后的前端项目",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "AcctId",
            "in": "query",
            "description": "政企ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AccidentId",
            "in": "query",
            "description": "事故单号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AccidentType",
            "in": "query",
            "description": "事故类型",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AccidentLevel",
            "in": "query",
            "description": "车损等级",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer",
                "format": "int32"
              }
            }
          },
          {
            "name": "IncludeRs",
            "in": "query",
            "description": "是否包含人伤事故 是true 否false",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "AmountRange",
            "in": "query",
            "description": "事故等级对应车损 金额 范围",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/System.Collections.Generic.KeyValuePair`2[[System.Decimal, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Decimal, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
              }
            }
          },
          {
            "name": "EnterprisetName",
            "in": "query",
            "description": "政企名称",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "StatusFlag",
            "in": "query",
            "description": "事故状态",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ChildStatusFlag",
            "in": "query",
            "description": "事故子状态",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OprNo",
            "in": "query",
            "description": "跟进入编号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UseCity",
            "in": "query",
            "description": "用车城市",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "NextFlowTimeStart",
            "in": "query",
            "description": "下次跟进时间 开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "NextFlowTimeEnd",
            "in": "query",
            "description": "下次跟进时间 结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "AccTimeStart",
            "in": "query",
            "description": "事故时间 开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "AccTimeEnd",
            "in": "query",
            "description": "事故时间 结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "IsNoFollow",
            "in": "query",
            "description": "是否跟进",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "AccidentPhone",
            "in": "query",
            "description": "事故人手机号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ClientType",
            "in": "query",
            "description": "客户类型",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "BizType",
            "in": "query",
            "description": "事故归属类型 1 自驾零单，2代驾零单，3长包自驾，3长包代驾",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
            }
          },
          {
            "name": "FollowStates",
            "in": "query",
            "description": "跟进状态",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AccidentFollowState"
              }
            }
          },
          {
            "name": "DutyType",
            "in": "query",
            "description": "事故责任划分",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.DutyTypes"
            }
          },
          {
            "name": "UserAdvanceFollowState",
            "in": "query",
            "description": "客户垫付费用跟进状态 1.无 2.待退还 3.已退还（报销） 4.已退还（退款） 5.已退还（直赔）",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.UserAdvanceFollowStateType"
            }
          },
          {
            "name": "CarMaintainDepositFollowState",
            "in": "query",
            "description": "本车维修押金跟进状态 1.无 2.待收取 3.已收取待结算 4.已支付已结算",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.CarMaintainDepositFollowStateType"
            }
          },
          {
            "name": "DerogatoryFollowState",
            "in": "query",
            "description": "贬损费用跟进状态 1.无 2.待收取 3.已收取",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.DerogatoryFollowStateType"
            }
          },
          {
            "name": "CarMaintainFollowState",
            "in": "query",
            "description": "本车维修费用跟进状态 1.无 2.待支付 3.已支付（退款） 4.已支付（直赔）",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.CarMaintainFollowStateType"
            }
          },
          {
            "name": "ThreeCostFollowState",
            "in": "query",
            "description": "三者费用跟进状态 1.无 2.待支付 3.已支付（退款） 4.已支付（直赔）",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.ThreeCostFollowStateType"
            }
          },
          {
            "name": "IsOutsideMaintain",
            "in": "query",
            "description": "是否在外维修",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "AppraisalLawsuit",
            "in": "query",
            "description": "公估诉讼 0.否 1.公估 2.诉讼",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AppraisalLawsuitType"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Accident/GetInsuranceCustomer": {
      "get": {
        "tags": [
          "Accident"
        ],
        "summary": "获取跟进客服列表 1跟单客服 2理赔客服",
        "parameters": [
          {
            "name": "Type",
            "in": "query",
            "description": "1--客服跟单人2--理赔跟单人",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.FollowUpStaffs"
            }
          },
          {
            "name": "SearchKey",
            "in": "query",
            "description": "检索关键字(工号或完整姓名)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.CarSupportApi.GetInsuranceCustomerOutPut, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Accident/GetOrderLink": {
      "get": {
        "tags": [
          "Accident"
        ],
        "summary": "获取订单跳转链接",
        "parameters": [
          {
            "name": "AccidentId",
            "in": "query",
            "description": "事故Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetOrderLinkOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00014"
            ]
          }
        ]
      }
    },
    "/api/Accident/PostAssignFollowers": {
      "post": {
        "tags": [
          "Accident"
        ],
        "summary": "事故查询 分配跟进人",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.PostAssignFollowersInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.PostAssignFollowersInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.PostAssignFollowersInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00012"
            ]
          }
        ]
      }
    },
    "/api/Accident/PostCarDamage": {
      "post": {
        "tags": [
          "Accident"
        ],
        "summary": "事故查询 录入车损",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.PostCarDamageAsyncInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.PostCarDamageAsyncInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.PostCarDamageAsyncInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00011"
            ]
          }
        ]
      }
    },
    "/api/Accident/SendAccidentSms": {
      "post": {
        "tags": [
          "Accident"
        ],
        "summary": "发生事故短信",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.SendAccidentSmsInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.SendAccidentSmsInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.SendAccidentSmsInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00027"
            ]
          }
        ]
      }
    },
    "/api/Accident/UpdateAcccidentStateInfo": {
      "post": {
        "tags": [
          "Accident"
        ],
        "summary": "修改事故详细跟进状态",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.UpdateAcccidentStateInfoInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.UpdateAcccidentStateInfoInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.UpdateAcccidentStateInfoInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00040;False"
            ]
          }
        ]
      }
    },
    "/api/Accident/UpdateAccidentStateCurrents": {
      "post": {
        "tags": [
          "Accident"
        ],
        "summary": "批量修改事故跟进状态",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Manager.Dto.UpdateAccidentStateCurrentsInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Manager.Dto.UpdateAccidentStateCurrentsInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Manager.Dto.UpdateAccidentStateCurrentsInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.CoreBusiness.Accident.Manager.Dto.UpdateAccidentStateCurrentsOutput, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00042;False"
            ]
          }
        ]
      }
    },
    "/api/AfterSaleSetting/BatchUpdateRangePrices": {
      "post": {
        "tags": [
          "AfterSaleSetting"
        ],
        "summary": "批量更新官价配置范围",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.BatchUpdateRangePricesInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.BatchUpdateRangePricesInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.BatchUpdateRangePricesInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00044;False"
            ]
          }
        ]
      }
    },
    "/api/AfterSaleSetting/DeleteItemPriceRule": {
      "post": {
        "tags": [
          "AfterSaleSetting"
        ],
        "summary": "删除维保规则配置",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.DeleteItemPriceRuleInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.DeleteItemPriceRuleInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.DeleteItemPriceRuleInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00045;False"
            ]
          }
        ]
      }
    },
    "/api/AfterSaleSetting/ImportItemPriceRule": {
      "post": {
        "tags": [
          "AfterSaleSetting"
        ],
        "summary": "批量导入维保配置",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.ImportItemPriceRuleInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.ImportItemPriceRuleInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.ImportItemPriceRuleInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.CoreBusiness.Repair.Dto.ImportItemPriceRuleOutput, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00046;False"
            ]
          }
        ]
      }
    },
    "/api/AfterSaleSetting/RepairItemPriceRule": {
      "get": {
        "tags": [
          "AfterSaleSetting"
        ],
        "summary": "维保规则详情",
        "parameters": [
          {
            "name": "Id",
            "in": "query",
            "description": "配置项Id",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.CoreBusiness.Repair.Manager.Dto.RepairItemPriceRuleDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00043;False"
            ]
          }
        ]
      }
    },
    "/api/AfterSaleSetting/RepairItemPriceRules": {
      "get": {
        "tags": [
          "AfterSaleSetting"
        ],
        "summary": "获取维保规则配置",
        "parameters": [
          {
            "name": "ItemName",
            "in": "query",
            "description": "维保项名称",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ItemId",
            "in": "query",
            "description": "维保项编号",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.RepairItemPriceRulesDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_P_00010;False"
            ]
          }
        ]
      }
    },
    "/api/AfterSaleSetting/ReserveItemPriceRule": {
      "post": {
        "tags": [
          "AfterSaleSetting"
        ],
        "summary": "保存维保规则配置",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.ReserveItemPriceRuleInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.ReserveItemPriceRuleInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.ReserveItemPriceRuleInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00044;False"
            ]
          }
        ]
      }
    },
    "/api/Annual/AnnualInspection": {
      "post": {
        "tags": [
          "Annual"
        ],
        "summary": "push年检 数据保存",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_PushAnnualInspection",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Annual.Dto.AnnualInspectionInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Annual.Dto.AnnualInspectionInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Annual.Dto.AnnualInspectionInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Annual/GetAnnualInspections": {
      "get": {
        "tags": [
          "Annual"
        ],
        "summary": "需年检车辆",
        "parameters": [
          {
            "name": "IsAuth",
            "in": "query",
            "description": "是否来自分离后的前端项目",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OrderNo",
            "in": "query",
            "description": "订单编号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "DateNextCheckStart",
            "in": "query",
            "description": "下次年检时间-开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "DateNextCheckEnd",
            "in": "query",
            "description": "下次年检时间-结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "AcctIds",
            "in": "query",
            "description": "政企ID",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "BizType",
            "in": "query",
            "description": "业务类型",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Annual.Dto.GetAnnualInspectionsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00007"
            ]
          }
        ]
      }
    },
    "/api/Annual/GetAnnualInspectionsCount": {
      "get": {
        "tags": [
          "Annual"
        ],
        "summary": "需年检车辆数 group=false",
        "parameters": [
          {
            "name": "IsAuth",
            "in": "query",
            "description": "是否来自分离后的前端项目",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "DateNextCheckStart",
            "in": "query",
            "description": "下次年检时间-开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "DateNextCheckEnd",
            "in": "query",
            "description": "下次年检时间-结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Annual.Dto.GetAnnualInspectionsCountOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00007"
            ]
          }
        ]
      }
    },
    "/api/Annual/ModifyMaintainAlarmCurrentKmInfos": {
      "post": {
        "tags": [
          "Annual"
        ],
        "summary": "批量修改当前车辆的表显里程数和最新维保时间",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.AnnualInspection.Dto.ModifyMaintainAlarmCurrentKmInfosInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.AnnualInspection.Dto.ModifyMaintainAlarmCurrentKmInfosInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.AnnualInspection.Dto.ModifyMaintainAlarmCurrentKmInfosInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default"
            ]
          }
        ]
      }
    },
    "/api/Annual/ModifyMaintainAlarmStatuses": {
      "post": {
        "tags": [
          "Annual"
        ],
        "summary": "需保养的车辆数 批量修改跟进状态",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Annual.Dto.ModifyMaintainAlarmStatusesInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Annual.Dto.ModifyMaintainAlarmStatusesInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Annual.Dto.ModifyMaintainAlarmStatusesInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00018"
            ]
          }
        ]
      }
    },
    "/api/Common/CallCenterTask": {
      "post": {
        "tags": [
          "Common"
        ],
        "summary": "创建任务",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/eHi.CallCenter.Dto.Dto.CreateTaskInputDto"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/eHi.CallCenter.Dto.Dto.CreateTaskInputDto"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/eHi.CallCenter.Dto.Dto.CreateTaskInputDto"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/CustomerServiceList": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "查询客服列表",
        "parameters": [
          {
            "name": "input",
            "in": "query",
            "description": "",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.CustomerServiceListInput"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.CustomerServiceDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default;False"
            ]
          }
        ]
      }
    },
    "/api/Common/GetAccs": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "模糊查询政企信息",
        "parameters": [
          {
            "name": "query",
            "in": "query",
            "description": "",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.IList`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetAccDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetAllAccounts": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取政企信息(包含禁用政企的)",
        "parameters": [
          {
            "name": "AccountName",
            "in": "query",
            "description": "政企名称",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetAccountsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetApplyAccountInfo": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取用户售后工单账户信息",
        "parameters": [
          {
            "name": "AccountNo",
            "in": "query",
            "description": "账户号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Phone",
            "in": "query",
            "description": "客户联系方式",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ApplyAccountStatus",
            "in": "query",
            "description": "",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ApplyAccountStatus"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyAccountInfoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default;False"
            ]
          }
        ]
      }
    },
    "/api/Common/GetAreas": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取城市 用车城市",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetAreasDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetBankCities": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "报销城市",
        "parameters": [
          {
            "name": "CityName",
            "in": "query",
            "description": "城市名称",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetCitiesDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetBanks": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取报销银行",
        "parameters": [
          {
            "name": "Id",
            "in": "query",
            "description": "银行code",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetBankDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetDistricts": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "",
        "parameters": [
          {
            "name": "CityId",
            "in": "query",
            "description": "城市Id",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetDistrictsDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetDrivers": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "模糊查询司机工号列表",
        "parameters": [
          {
            "name": "NameOrNo",
            "in": "query",
            "description": "司机姓名或工号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.DriverApi.GetDriverDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetKaolaCities": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取考拉基础数据-城市",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_GetKaolaCitys",
        "parameters": [
          {
            "name": "ProvinceId",
            "in": "query",
            "description": "省份ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CityName",
            "in": "query",
            "description": "城市名称",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AllowQuery",
            "in": "query",
            "description": "",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaCitiesDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetKaolaProvinces": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取考拉基础数据-省份",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaProvincesOriginalDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetKaoLaRepairItems": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取考拉基础数据-维修保养具体项目",
        "parameters": [
          {
            "name": "Name",
            "in": "query",
            "description": "维修项名称",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaoLaRepairItemsDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetKaolaRepeatShops": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取考拉基础数据-考拉维修厂",
        "parameters": [
          {
            "name": "CityId",
            "in": "query",
            "description": "城市ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperationTime",
            "in": "query",
            "description": "操作时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaRepeatShopsDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetKaolaStations": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取考拉基础数据-维修工位",
        "parameters": [
          {
            "name": "ShopId",
            "in": "query",
            "description": "维修厂ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Time",
            "in": "query",
            "description": "",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "RepairTypes",
            "in": "query",
            "description": "1 维修，2保养",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairType"
              }
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetKaolaStationsResultDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetKoalaRepairShopCities": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取考拉和合作修理厂的全部城市",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaCitiesDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetOrderInfo": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "根据车牌号码和事故时间获取订单信息",
        "parameters": [
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "DateTime",
            "in": "query",
            "description": "事故发生时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.GetOrderTypeDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00013"
            ]
          }
        ]
      }
    },
    "/api/Common/GetOrderInfoByCarNoAndTime": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "跟进车牌+时间匹配企业订单信息",
        "parameters": [
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "DateTime",
            "in": "query",
            "description": "事故发生时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.GetOrderInfoByCarNoAndTimeDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetOrderServiceTerm": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "根据订单号获取售后服务条款信息",
        "parameters": [
          {
            "name": "OrderNo",
            "in": "query",
            "description": "订单编号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetOrderType": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "根据车牌号码和预约时间获取订单信息",
        "parameters": [
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ReserveTime",
            "in": "query",
            "description": "预约时间(包含日期时间)",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.CoreBusiness.Repair.Dto.GetOrderTypeExpandDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetReimburseInfo": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "根据报销单号获取报销信息",
        "parameters": [
          {
            "name": "Id",
            "in": "query",
            "description": "报销ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetReimburseInfoOutPut, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetRepairReimburseInfos": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取报销记录",
        "parameters": [
          {
            "name": "BusinessId",
            "in": "query",
            "description": "业务单号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ReimbursementType",
            "in": "query",
            "description": "报销类型",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ReimbursementType"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetRepairReimburseInfosOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetRepairshopsConditions": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "根据城市id,区域id,维修厂类型查询维修厂信息",
        "parameters": [
          {
            "name": "CityId",
            "in": "query",
            "description": "",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "DistrinctId",
            "in": "query",
            "description": "",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ShopType",
            "in": "query",
            "description": "",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetRepairshopsConditionsDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetStocks": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "根据维修厂时间查询剩余工位",
        "parameters": [
          {
            "name": "CarRepairShopId",
            "in": "query",
            "description": "店铺id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Date",
            "in": "query",
            "description": "日期",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "IsRepair",
            "in": "query",
            "description": "是否维修",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "IsMaintain",
            "in": "query",
            "description": "是否保养",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetStocksDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetSubBanks": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取报销分行",
        "parameters": [
          {
            "name": "BankCategoryCode",
            "in": "query",
            "description": "银行ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "BankCityCode",
            "in": "query",
            "description": "银行所在城市ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetSubBankDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Common/GetTempLateFile": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取模板文件相对路径",
        "parameters": [
          {
            "name": "TemplateType",
            "in": "query",
            "description": "模板类型",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.TemplateType"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Microsoft.AspNetCore.Mvc.ActionResult, Microsoft.AspNetCore.Mvc.Core, Version=10.0.0.0, Culture=neutral, PublicKeyToken=adb9793829ddae60]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default;False"
            ]
          }
        ]
      }
    },
    "/api/Common/GetUserInfo": {
      "get": {
        "tags": [
          "Common"
        ],
        "summary": "获取当前登录用户信息",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetUserInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default"
            ]
          }
        ]
      }
    },
    "/api/Common/ResolveSensitiveInfo": {
      "post": {
        "tags": [
          "Common"
        ],
        "summary": "解析脱敏信息",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfoInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfoInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfoInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default;False"
            ]
          }
        ]
      }
    },
    "/api/Common/ResolveSensitiveInfos": {
      "post": {
        "tags": [
          "Common"
        ],
        "summary": "批量解析脱敏信息",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfosInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfosInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfosInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default;False"
            ]
          }
        ]
      }
    },
    "/api/Common/UploadFiles": {
      "post": {
        "tags": [
          "Common"
        ],
        "summary": "批量上传文件 FormData 形式",
        "parameters": [
          {
            "name": "CategoryId",
            "in": "query",
            "description": "文件上传操作 类型ID",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.FileCenter.FileCategoryType"
            }
          },
          {
            "name": "UseAegisService",
            "in": "query",
            "description": "使用aeigs文件上传服务",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "type": "object",
                "properties": {
                  "file": {
                    "type": "string",
                    "format": "binary"
                  }
                }
              },
              "encoding": {
                "Form": {
                  "style": "form"
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.UpLoadFilesOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Complaint/AddOrUpdateComplaintType": {
      "post": {
        "tags": [
          "Complaint"
        ],
        "summary": "添加/修改投诉类型（id为0时，则为新增投诉类型）",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.AddOrUpdateComplaintTypeInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.AddOrUpdateComplaintTypeInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.AddOrUpdateComplaintTypeInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintTypeDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/CancelComplaint": {
      "post": {
        "tags": [
          "Complaint"
        ],
        "summary": "取消客诉",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_PostCancelComplaint",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.CancelComplaintInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.CancelComplaintInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.CancelComplaintInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00033;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/ComplaintThreeVerifyUsers": {
      "get": {
        "tags": [
          "Complaint"
        ],
        "summary": "获取客诉三级审核人",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintThreeVerifyUsersOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_P_00008;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/ComplaintTypes": {
      "get": {
        "tags": [
          "Complaint"
        ],
        "summary": "获取客诉类型",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintTypeDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/ComplaintVerifyLogs": {
      "get": {
        "tags": [
          "Complaint"
        ],
        "summary": "获取客诉审核记录日志",
        "parameters": [
          {
            "name": "ComplaintId",
            "in": "query",
            "description": "客诉Id",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintVerifyLogsOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00036;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/CompleteComplaint": {
      "post": {
        "tags": [
          "Complaint"
        ],
        "summary": "完成客诉",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_PostCompleteComplaint",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.CompleteComplaintInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.CompleteComplaintInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.CompleteComplaintInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00034;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/ConfigureComplaintVerifyUsers": {
      "get": {
        "tags": [
          "Complaint"
        ],
        "summary": "配置客诉三级审核人",
        "parameters": [
          {
            "name": "VerifyNo",
            "in": "query",
            "description": "当前审核人工号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "NewVerifyNo",
            "in": "query",
            "description": "新审核人工号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/ExportComplaintInfoExcel": {
      "get": {
        "tags": [
          "Complaint"
        ],
        "summary": "客诉记录导出Excel",
        "parameters": [
          {
            "name": "AcctId",
            "in": "query",
            "description": "政企ID集合",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Id",
            "in": "query",
            "description": "客诉ID",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OrderNo",
            "in": "query",
            "description": "订单号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "BizType",
            "in": "query",
            "description": "业务类型： 0：其他 1:政企自驾零单 2:政企代驾零单 3:政企自驾长包 4:政企代驾长包5：个人代驾",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ComplaintType",
            "in": "query",
            "description": "投诉类型：1.事故 2.保养",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ComplaintState",
            "in": "query",
            "description": "投诉状态：1.待提交2.待提交【已退回】3.待复核4.待审核5.审核中6.待复核【已退回】7.待审核【已退回】8.取消9.已通过",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ComplainedStartTime",
            "in": "query",
            "description": "投诉开始日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "ComplainedEndTime",
            "in": "query",
            "description": "投诉结束日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "ComplainantPhone",
            "in": "query",
            "description": "投诉人联系方式",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "IsSalesIntervention",
            "in": "query",
            "description": "销售介入",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ExportExcelBaseDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00037;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/GetComplaintInfo": {
      "get": {
        "tags": [
          "Complaint"
        ],
        "summary": "获取客诉详情",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_GetComplaintInfo",
        "parameters": [
          {
            "name": "id",
            "in": "query",
            "description": "",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00038;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/GetComplaints": {
      "get": {
        "tags": [
          "Complaint"
        ],
        "summary": "客诉记录查询",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_GetComplaints",
        "parameters": [
          {
            "name": "AcctId",
            "in": "query",
            "description": "政企ID集合",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Id",
            "in": "query",
            "description": "客诉ID",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OrderNo",
            "in": "query",
            "description": "订单号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "BizType",
            "in": "query",
            "description": "业务类型： 0：其他 1:政企自驾零单 2:政企代驾零单 3:政企自驾长包 4:政企代驾长包5：个人代驾",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ComplaintType",
            "in": "query",
            "description": "投诉类型：1.事故 2.保养",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ComplaintState",
            "in": "query",
            "description": "投诉状态：1.待提交2.待提交【已退回】3.待复核4.待审核5.审核中6.待复核【已退回】7.待审核【已退回】8.取消9.已通过",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ComplainedStartTime",
            "in": "query",
            "description": "投诉开始日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "ComplainedEndTime",
            "in": "query",
            "description": "投诉结束日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "ComplainantPhone",
            "in": "query",
            "description": "投诉人联系方式",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "IsSalesIntervention",
            "in": "query",
            "description": "销售介入",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_P_00008;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/GetComplaintVerifyInfos": {
      "get": {
        "tags": [
          "Complaint"
        ],
        "summary": "客诉管理-客诉审核-查询",
        "parameters": [
          {
            "name": "Id",
            "in": "query",
            "description": "客诉Id",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OrderNo",
            "in": "query",
            "description": "订单号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AcctId",
            "in": "query",
            "description": "政企Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ComplainedStartTime",
            "in": "query",
            "description": "投诉开始日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "ComplainedEndTime",
            "in": "query",
            "description": "投诉结束日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "ComplaintType",
            "in": "query",
            "description": "投诉类型",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "BizType",
            "in": "query",
            "description": "业务类型",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ComplaintState",
            "in": "query",
            "description": "客诉状态",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Complaint.Enums.ComplaintStates"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintVerifyInfosOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00035;CORPAF_I_00035<>审核所有:Complaint.VerifyAll;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/GetOrderInfoByOrderNo": {
      "get": {
        "tags": [
          "Complaint"
        ],
        "summary": "根据订单号加载客诉信息上所需的订单信息",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_GetOrderInfoByOrderNo",
        "parameters": [
          {
            "name": "OrderNo",
            "in": "query",
            "description": "订单号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.GetOrderInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Complaint/GetUserOrderCount": {
      "get": {
        "tags": [
          "Complaint"
        ],
        "summary": "获取客户一年的订单量",
        "parameters": [
          {
            "name": "ComplainantName",
            "in": "query",
            "description": "投诉人姓名",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ComplainantPhone",
            "in": "query",
            "description": "投诉人联系方式",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.GetUserOrderCountDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Complaint/RemoveComplaintType": {
      "get": {
        "tags": [
          "Complaint"
        ],
        "summary": "删除投诉类型",
        "parameters": [
          {
            "name": "Id",
            "in": "query",
            "description": "id",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/ReserveComplaintInfo": {
      "post": {
        "tags": [
          "Complaint"
        ],
        "summary": "登记客诉",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_PostReserveComplaintInfo",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.ReserveComplaintInfoInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.ReserveComplaintInfoInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.ReserveComplaintInfoInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00030;CORPAF_I_00032;False"
            ]
          }
        ]
      }
    },
    "/api/Complaint/VerifyComplaintInfos": {
      "post": {
        "tags": [
          "Complaint"
        ],
        "summary": "客诉管理-客诉审核-审核",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.VerifyComplaintInfosInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.VerifyComplaintInfosInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.VerifyComplaintInfosInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00035;CORPAF_I_00035<>审核所有:Complaint.VerifyAll;False"
            ]
          }
        ]
      }
    },
    "/api/ForAccount/GetAfterSaleAccidentInfo/GetAfterSaleAccidentInfo": {
      "post": {
        "tags": [
          "ForAccount"
        ],
        "summary": "售后-事故管理",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.GetAfterSaleAccidentInfoInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.GetAfterSaleAccidentInfoInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.GetAfterSaleAccidentInfoInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetAfterSaleAccidentInfoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForCrm/AddRepairApplyLicenseAttaches": {
      "post": {
        "tags": [
          "ForCrm"
        ],
        "summary": "添加工单凭证接口",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/eHi.Common.AfterSale.Dto.AddRepairApplyLicenseAttachesInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/eHi.Common.AfterSale.Dto.AddRepairApplyLicenseAttachesInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/eHi.Common.AfterSale.Dto.AddRepairApplyLicenseAttachesInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForCrm/RepairApplyLicenseAttaches": {
      "get": {
        "tags": [
          "ForCrm"
        ],
        "summary": "查询凭证类型列表",
        "parameters": [
          {
            "name": "RepairId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[eHi.Common.AfterSale.Dto.RepairApplyLicenseAttachDto, eHi.Common.AfterSale, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForCrm/RepairCreatorInfos": {
      "get": {
        "tags": [
          "ForCrm"
        ],
        "summary": "查询工单下单人信息",
        "parameters": [
          {
            "name": "RepairIds",
            "in": "query",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[eHi.Common.AfterSale.Dto.RepairCreatorDto, eHi.Common.AfterSale, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForDriver/GetJgAccidentDetail": {
      "get": {
        "tags": [
          "ForDriver"
        ],
        "summary": "架管 获取事故详情",
        "parameters": [
          {
            "name": "AccidentId",
            "in": "query",
            "description": "事故编号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OprNo",
            "in": "query",
            "description": "操作人ID 必输",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForDriver/GetJgAccidentDetails": {
      "post": {
        "tags": [
          "ForDriver"
        ],
        "summary": "驾管 获取事故列表",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForDriver/GetJgAccidentSummary": {
      "post": {
        "tags": [
          "ForDriver"
        ],
        "summary": "驾管 获取汇总列表",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentSummaryInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentSummaryInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentSummaryInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentSummaryDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForDriver/GetRepairDetailInfosByRepairId": {
      "get": {
        "tags": [
          "ForDriver"
        ],
        "summary": "根据维保编号获取维保详情",
        "parameters": [
          {
            "name": "RepairId",
            "in": "query",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairDetailInfosByRepairIdOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForDriver/GetRepairInfosByDriverNo": {
      "get": {
        "tags": [
          "ForDriver"
        ],
        "summary": "根据司机工号检索维保信息",
        "parameters": [
          {
            "name": "DriverNo",
            "in": "query",
            "description": "",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosByDriverNoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForDriver/JgAccidentInfo": {
      "post": {
        "tags": [
          "ForDriver"
        ],
        "summary": "驾管 更新事故信息",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.JgAccidentInfoInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.JgAccidentInfoInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.JgAccidentInfoInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForEo/GetMaintenanceRecordByCarLicense": {
      "post": {
        "tags": [
          "ForEo"
        ],
        "summary": "根据车牌获取车辆的机油滤芯保养记录",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintenanceRecordByCarLicenseInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintenanceRecordByCarLicenseInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintenanceRecordByCarLicenseInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.MaintenanceRecordDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/AfterSaleCancel": {
      "post": {
        "tags": [
          "ForH5"
        ],
        "summary": "H5取消工单",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AfterSaleCancelInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AfterSaleCancelInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AfterSaleCancelInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/ApplyMaintenance": {
      "post": {
        "tags": [
          "ForH5"
        ],
        "summary": "H5 维保单 预约/修改",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_PostApplyMaintenance",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ApplyMaintenanceInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ApplyMaintenanceInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ApplyMaintenanceInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ApplyMaintenanceOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/CityNameByLocation": {
      "post": {
        "tags": [
          "ForH5"
        ],
        "summary": "根据经纬度返回城市名称",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.CityNameByLocationInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.CityNameByLocationInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.CityNameByLocationInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Common.Dto.CityNameByLocationOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/GetAccidentsForH5": {
      "get": {
        "tags": [
          "ForH5"
        ],
        "summary": "检索当前登录人所属事故订单，区分内部工号和客户Id",
        "parameters": [
          {
            "name": "UserId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserInfoSourceType",
            "in": "query",
            "schema": {
              "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
            }
          },
          {
            "name": "OpenId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Phone",
            "in": "query",
            "description": "手机号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "StatusFlag",
            "in": "query",
            "description": "1 已完成 0 待处理",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.GetAccidentsForH5InPutStatusFlag"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAccidentsForH5OutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/GetAfterSaleRepairItems": {
      "get": {
        "tags": [
          "ForH5"
        ],
        "summary": "获取售后自己维护的维保项列表",
        "parameters": [
          {
            "name": "UserId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserInfoSourceType",
            "in": "query",
            "schema": {
              "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
            }
          },
          {
            "name": "OpenId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAfterSaleRepairItemsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/GetApplyAccountInfo": {
      "get": {
        "tags": [
          "ForH5"
        ],
        "summary": "获取用户售后工单账户信息",
        "parameters": [
          {
            "name": "AccountNo",
            "in": "query",
            "description": "账户号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserId",
            "in": "query",
            "description": "用户ID 密文 非cookie来源时使用",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserInfoSourceType",
            "in": "query",
            "description": "用来信息来源区分 0 cookie 1 原始密文",
            "schema": {
              "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
            }
          },
          {
            "name": "OpenId",
            "in": "query",
            "description": "微信OpenId",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ApplyAccountStatus",
            "in": "query",
            "description": "",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ApplyAccountStatus"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyAccountInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/GetApplyMaintenance": {
      "get": {
        "tags": [
          "ForH5"
        ],
        "summary": "获取我的预约工单记录",
        "parameters": [
          {
            "name": "UserId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserInfoSourceType",
            "in": "query",
            "schema": {
              "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
            }
          },
          {
            "name": "OpenId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserCode",
            "in": "query",
            "description": "明文 用户编号(用户Id)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "PhoneNumber",
            "in": "query",
            "description": "用户手机号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyMaintenanceOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/GetApplyMaintenanceInfo": {
      "get": {
        "tags": [
          "ForH5"
        ],
        "summary": "H5 获取维保单详情",
        "parameters": [
          {
            "name": "Id",
            "in": "query",
            "description": "主键",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "UserId",
            "in": "query",
            "description": "用户ID 密文 非cookie来源时使用",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserInfoSourceType",
            "in": "query",
            "description": "用来信息来源区分 0 cookie 1 原始密文",
            "schema": {
              "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
            }
          },
          {
            "name": "OpenId",
            "in": "query",
            "description": "微信OpenId",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyMaintenanceInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/GetApplyUserInfo": {
      "get": {
        "tags": [
          "ForH5"
        ],
        "summary": "获取售后工单用户信息",
        "parameters": [
          {
            "name": "UserId",
            "in": "query",
            "description": "用户ID 密文 非cookie来源时使用",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserInfoSourceType",
            "in": "query",
            "description": "用来信息来源区分 0 cookie 1 原始密文",
            "schema": {
              "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
            }
          },
          {
            "name": "OpenId",
            "in": "query",
            "description": "微信OpenId",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyUserInfoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/GetCarNoIsEnterprise": {
      "get": {
        "tags": [
          "ForH5"
        ],
        "summary": "获取车牌当前是否正在被长包政企用户使用",
        "description": "true 政企在用 false 政企未用",
        "parameters": [
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ReserveTime",
            "in": "query",
            "description": "预约时间(包含日期时间)",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "UserId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserInfoSourceType",
            "in": "query",
            "schema": {
              "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
            }
          },
          {
            "name": "OpenId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/GetLicenseInfo": {
      "get": {
        "tags": [
          "ForH5"
        ],
        "summary": "H5 获取凭证上传详情",
        "parameters": [
          {
            "name": "ApplyId",
            "in": "query",
            "description": "维保编号",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "UserId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserInfoSourceType",
            "in": "query",
            "schema": {
              "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
            }
          },
          {
            "name": "OpenId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetLicenseInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/GetRepairInfoForWx": {
      "get": {
        "tags": [
          "ForH5"
        ],
        "summary": "一嗨出行,获取预约详情",
        "parameters": [
          {
            "name": "RepairId",
            "in": "query",
            "description": "预约编号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserInfoSourceType",
            "in": "query",
            "schema": {
              "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
            }
          },
          {
            "name": "OpenId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfoForWxDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/GetRepairInfosForWx": {
      "get": {
        "tags": [
          "ForH5"
        ],
        "summary": "一嗨出行，获取当前用户的预约记录列表",
        "parameters": [
          {
            "name": "UserId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserInfoSourceType",
            "in": "query",
            "schema": {
              "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
            }
          },
          {
            "name": "OpenId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosForWxOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/GetRepairKmInfo": {
      "get": {
        "tags": [
          "ForH5"
        ],
        "summary": "获取维保里程和时间信息",
        "parameters": [
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Km",
            "in": "query",
            "description": "当前里程数",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "UserId",
            "in": "query",
            "description": "用户ID 密文 非cookie来源时使用",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserInfoSourceType",
            "in": "query",
            "description": "用来信息来源区分 0 cookie 1 原始密文",
            "schema": {
              "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
            }
          },
          {
            "name": "OpenId",
            "in": "query",
            "description": "微信OpenId",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarId",
            "in": "query",
            "description": "车辆Id",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairKmInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/GetUserFirstAccess": {
      "get": {
        "tags": [
          "ForH5"
        ],
        "summary": "判断 用户是否首次访问 true 首次登陆 false 非首次登陆",
        "parameters": [
          {
            "name": "UserId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserInfoSourceType",
            "in": "query",
            "schema": {
              "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
            }
          },
          {
            "name": "OpenId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/OcrCarCarNo": {
      "post": {
        "tags": [
          "ForH5"
        ],
        "summary": "ocr服务识别图片中的车牌",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarCarNoInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarCarNoInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarCarNoInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarCarNoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/OcrCarKilometer": {
      "post": {
        "tags": [
          "ForH5"
        ],
        "summary": "ocr服务识别图片中的车辆公里数",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarKilometerInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarKilometerInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarKilometerInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarKilometerDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/ReserveApplyUserInfo": {
      "post": {
        "tags": [
          "ForH5"
        ],
        "summary": "保存/更新售后工单用户信息",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReserveApplyUserInfoInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReserveApplyUserInfoInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReserveApplyUserInfoInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/ReserveRepairFromWeChat": {
      "post": {
        "tags": [
          "ForH5"
        ],
        "summary": "微信(H5)预约考拉",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReserveRepairFromWeChatInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReserveRepairFromWeChatInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReserveRepairFromWeChatInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/UpLoadLicense": {
      "post": {
        "tags": [
          "ForH5"
        ],
        "summary": "一嗨出行，H5 上传凭证,修改凭证，重新上传",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.UpLoadLicenseInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.UpLoadLicenseInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.UpLoadLicenseInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForH5/VerifyApplyLicense": {
      "post": {
        "tags": [
          "ForH5"
        ],
        "summary": "判断上传的凭证是否正确",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyApplyLicenseInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyApplyLicenseInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyApplyLicenseInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForSupport/CheckAddMaintenance": {
      "get": {
        "tags": [
          "ForSupport"
        ],
        "summary": "判断是否允许预约工单",
        "parameters": [
          {
            "name": "OrderId",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarInDateTime",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "CarInMileage",
            "in": "query",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "CarOutMileage",
            "in": "query",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[eHi.Common.AfterSale.Dto.CheckAddMaintenanceOutput, eHi.Common.AfterSale, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/ForSupport/RepairInfoByRescueId": {
      "get": {
        "tags": [
          "ForSupport"
        ],
        "summary": "查询救援Id对应的维修单信息",
        "parameters": [
          {
            "name": "rescueId",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[eHi.CarSupport.Dto.AccidentRescue.ModelAccidentOrderOdto, eHi.CarSupport.Dto, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Home/Token/Token": {
      "post": {
        "tags": [
          "Home"
        ],
        "summary": "手动设置api 请求时的token",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.TokenInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.TokenInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.TokenInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Job/ApplyLicenseAutoVerify": {
      "post": {
        "tags": [
          "Job"
        ],
        "summary": "工单凭证自动审核",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.ApplyLicenseAutoVerifyInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.ApplyLicenseAutoVerifyInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.ApplyLicenseAutoVerifyInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Job/DueMaintenanceEmailReminder": {
      "post": {
        "tags": [
          "Job"
        ],
        "summary": "到期保养邮件提醒",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.DueMaintenanceEmailReminderInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.DueMaintenanceEmailReminderInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.DueMaintenanceEmailReminderInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Job/RefreshAfterSaleCarNoInfo": {
      "get": {
        "tags": [
          "Job"
        ],
        "summary": "刷新长包在用车辆数据",
        "parameters": [
          {
            "name": "_",
            "in": "query",
            "description": "",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.RefreshAfterSaleCarNoInfoInPut"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Job/SendApologyMail1": {
      "post": {
        "tags": [
          "Job"
        ],
        "summary": "发送致歉信",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SendMailInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SendMailInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SendMailInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Job/SendApologyMail2": {
      "post": {
        "tags": [
          "Job"
        ],
        "summary": "发送致歉信",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SendMailInputSecond"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SendMailInputSecond"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SendMailInputSecond"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Job/SendRepairApplyLicenseAuditEmail": {
      "post": {
        "tags": [
          "Job"
        ],
        "summary": "工单凭证超24小时未审核通知",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SendRepairApplyLicenseAuditEmailInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SendRepairApplyLicenseAuditEmailInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SendRepairApplyLicenseAuditEmailInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Job/SendRepairOrderNotifyMessages": {
      "post": {
        "tags": [
          "Job"
        ],
        "summary": "工单预约功能后短信通知客户",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SendRepairOrderNotifyMessagesInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SendRepairOrderNotifyMessagesInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SendRepairOrderNotifyMessagesInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Job/SyncMaintainAlarm": {
      "post": {
        "tags": [
          "Job"
        ],
        "summary": "同步或更新 车辆最近两次维保信息记录",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SyncMaintainAlarmInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SyncMaintainAlarmInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Job.Dto.SyncMaintainAlarmInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Repair/AfterSaleCancel": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "取消工单 维保工单取消",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AfterSaleCancelInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AfterSaleCancelInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AfterSaleCancelInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00004"
            ]
          }
        ]
      }
    },
    "/api/Repair/AfterSaleReserveCancel": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "取消工单 预约单取消",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AfterSaleCancelInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AfterSaleCancelInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AfterSaleCancelInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00028"
            ]
          }
        ]
      }
    },
    "/api/Repair/AssignCustomerService": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "分配客服",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AssignCustomerServiceInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AssignCustomerServiceInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AssignCustomerServiceInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00050;False"
            ]
          }
        ]
      }
    },
    "/api/Repair/CancelKaolaReserve": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "考拉预约取消",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_CancelReserve",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.CancelReserveInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.CancelReserveInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.CancelReserveInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00004"
            ]
          }
        ]
      }
    },
    "/api/Repair/ExportEarlyApplyInfosExcel": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "保养记录查询-工单凭证审核查询-凭证审核记录导出Excel",
        "parameters": [
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Phone",
            "in": "query",
            "description": "手机号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "VerifyStatus",
            "in": "query",
            "description": "审核状态",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.VerifyStatusFlag"
            }
          },
          {
            "name": "From",
            "in": "query",
            "description": "预约时间开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "To",
            "in": "query",
            "description": "预约时间结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "RepairId",
            "in": "query",
            "description": "维修单号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "LicenseVerifyStatus",
            "in": "query",
            "description": "凭证审核状态",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.LicenseVerifyStatusFlag"
              }
            }
          },
          {
            "name": "ApplyId",
            "in": "query",
            "description": "申请Id",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "BusinessType",
            "in": "query",
            "description": "业务类型",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
              }
            }
          },
          {
            "name": "ReimburseReviewState",
            "in": "query",
            "description": "报销审核状态",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "ReimbursePaymentState",
            "in": "query",
            "description": "报销打款状态",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "ChannelType",
            "in": "query",
            "description": "下单渠道 1客户 2员工",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "CustomerServiceCode",
            "in": "query",
            "description": "客服工号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "PendingReimbursement",
            "in": "query",
            "description": "待提交报销",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ExportExcelBaseDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00047;False"
            ]
          }
        ]
      }
    },
    "/api/Repair/GetAccessLogs": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取日志 详情列表",
        "parameters": [
          {
            "name": "KeyNo",
            "in": "query",
            "description": "业务关键字",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Request",
            "in": "query",
            "description": "请求内容",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Page",
            "in": "query",
            "description": "页面",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Action",
            "in": "query",
            "description": "接口内容",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "StartDateTime",
            "in": "query",
            "description": "开始时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EndDateTime",
            "in": "query",
            "description": "结束时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAccessLogsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Repair/GetActionLogs": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取操作日志",
        "parameters": [
          {
            "name": "KeyNo",
            "in": "query",
            "description": "主键值",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "TableName",
            "in": "query",
            "description": "表名",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "FieldKeies",
            "in": "query",
            "description": "字段名",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.IEnumerable`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOperationLogsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default"
            ]
          }
        ]
      }
    },
    "/api/Repair/GetContractMainRepairInfo": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取要素基本条款维修/保养地点信息",
        "parameters": [
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ReserveTime",
            "in": "query",
            "description": "预约时间(包含日期时间)",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.GetRepairInfoOutPut, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Repair/GetEarlyApplyInfo": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "售后系统 维保单详情查看（维保单主体信息,客户信息,审核信息）",
        "parameters": [
          {
            "name": "Id",
            "in": "query",
            "description": "Apply Id",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "RepairId",
            "in": "query",
            "description": "维保工单Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ActionType",
            "in": "query",
            "description": "",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Enums.EarlyApplyInfoQueryType"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetEarlyApplyInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00022"
            ]
          }
        ]
      }
    },
    "/api/Repair/GetEarlyApplyInfos": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "售后系统 维保单申请记录查询",
        "parameters": [
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Phone",
            "in": "query",
            "description": "手机号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "VerifyStatus",
            "in": "query",
            "description": "审核状态",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.VerifyStatusFlag"
            }
          },
          {
            "name": "From",
            "in": "query",
            "description": "预约时间开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "To",
            "in": "query",
            "description": "预约时间结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "RepairId",
            "in": "query",
            "description": "维修单号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "LicenseVerifyStatus",
            "in": "query",
            "description": "凭证审核状态",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.LicenseVerifyStatusFlag"
              }
            }
          },
          {
            "name": "ApplyId",
            "in": "query",
            "description": "申请Id",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "BusinessType",
            "in": "query",
            "description": "业务类型",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
              }
            }
          },
          {
            "name": "ReimburseReviewState",
            "in": "query",
            "description": "报销审核状态",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "ReimbursePaymentState",
            "in": "query",
            "description": "报销打款状态",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "ChannelType",
            "in": "query",
            "description": "下单渠道 1客户 2员工",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "CustomerServiceCode",
            "in": "query",
            "description": "客服工号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "PendingReimbursement",
            "in": "query",
            "description": "待提交报销",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetEarlyApplyInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00021"
            ]
          }
        ]
      }
    },
    "/api/Repair/GetExportMaintainAlarmsExcel": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "需保养车辆导出Excel",
        "parameters": [
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "StartDateTime",
            "in": "query",
            "description": "开始时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EndDateTime",
            "in": "query",
            "description": "结束时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EarlyWarningType",
            "in": "query",
            "description": "预警类型 0 全部 1 预警中 2 已预警",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.EarlyWarningType"
            }
          },
          {
            "name": "StatusFlag",
            "in": "query",
            "description": "状态0未进入预警，1未跟进，2跟进中，3已跟进,4已完成",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.StatusFlag"
            }
          },
          {
            "name": "StartWarnTime",
            "in": "query",
            "description": "开始预警时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EndWarnTime",
            "in": "query",
            "description": "结束预警时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ExportExcelBaseDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default"
            ]
          }
        ]
      }
    },
    "/api/Repair/GetExportRepairInfoExcel": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "保养记录导出Excel",
        "parameters": [
          {
            "name": "AcctIds",
            "in": "query",
            "description": "政企ID集合",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "RepairId",
            "in": "query",
            "description": "维保ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarInStartTime",
            "in": "query",
            "description": "进厂时间开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "CarInEndTime",
            "in": "query",
            "description": "进厂时间结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "RepairType",
            "in": "query",
            "description": "订单来源类型",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairFactoryType"
            }
          },
          {
            "name": "StatusFlag",
            "in": "query",
            "description": "--R,预约中（未接单） C,预约中（已接单） G,已登记(待预检) E,已预检(待审核) A,已审核 D, 审核中 J,已拒绝 L, 维修中 K,已完成 F, 已取消",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "BizType",
            "in": "query",
            "description": "1自驾，2代驾，3自驾长包，4代驾长包，6耀东方自驾零单",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "UserPhone",
            "in": "query",
            "description": "用户联系方式",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ChannelType",
            "in": "query",
            "description": "下单渠道 1客户 2员工",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "IsAuth",
            "in": "query",
            "description": "",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "LicenseVerifyStatus",
            "in": "query",
            "description": "0 待上传 1 待审核 3 已拒绝",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "AuditStatusFlag",
            "in": "query",
            "description": "{ \"N\", \"初始\" }, { \"R\", \"待审核\" }, { \"D\", \"已审核\" }, { \"J\", \"被拒绝\" }, { \"C\", \"已取消\" }, { \"S\",\n\"待确认\" }, { \"M\", \"草稿\" }",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "FinanceStatusFlag",
            "in": "query",
            "description": "{ \"R\", \"等待预审\" }, { \"J\", \"预审被拒\" }, { \"O\", \"未打款\" }, { \"K\", \"已打款\" }, { \"C\", \"单据接收\" }, {\n\"N\", \"拒绝\" }",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AppointmentProjects",
            "in": "query",
            "description": "维保类型",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairType"
              }
            }
          },
          {
            "name": "CoverageTypes",
            "in": "query",
            "description": "保障类型\n105:基本保障 215.乘客守护 232:尊享保障 233:百万守护  255:尊享守护  256.全程无忧",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.CoverageType"
              }
            }
          },
          {
            "name": "CreateTimeStart",
            "in": "query",
            "description": "下单开始时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "CreateTimeEnd",
            "in": "query",
            "description": "下单结束时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "RepeatApplyAuditState",
            "in": "query",
            "description": "维保单审核状态 0.待审核1.已通过2.已拒绝3.无需审核",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairAuditState"
            }
          },
          {
            "name": "CustomerServiceCode",
            "in": "query",
            "description": "客服工号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "RescueReviewStatus",
            "in": "query",
            "description": "救援单审核状态",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RescueReviewStatus"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ExportExcelBaseDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00003"
            ]
          }
        ]
      }
    },
    "/api/Repair/GetFields": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取 操作日志 表字段 配置",
        "parameters": [
          {
            "name": "TableName",
            "in": "query",
            "description": "表名",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "FieldName",
            "in": "query",
            "description": "字段名",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "FieldDesc",
            "in": "query",
            "description": "字段描述",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Id",
            "in": "query",
            "description": "主键Id",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetFieldsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Repair/GetJgTicketDetail": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取违章详情",
        "parameters": [
          {
            "name": "TicketId",
            "in": "query",
            "description": "违章ID",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetJgTicketDetailsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Repair/GetJgTicketDetails": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取违章列表",
        "parameters": [
          {
            "name": "TicketId",
            "in": "query",
            "description": "事故编号",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "StartDate",
            "in": "query",
            "description": "事故日期 开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EndDate",
            "in": "query",
            "description": "事故日期 结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "TickType",
            "in": "query",
            "description": "违章分类 1违停、2超速、3不按车道行驶、4逆向行驶、5使用手机、6不系安全带、7闯红灯、8使用应急通道、9不礼让、10限行、11其它",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.TickType"
            }
          },
          {
            "name": "TicketDjStatus",
            "in": "query",
            "description": "违章处理状态 1待处理,2公司处理，3审核中，4自缴完成，5代缴未完成",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.TicketDjStatus"
            }
          },
          {
            "name": "TicketDjStatuses",
            "in": "query",
            "description": "违章处理状态 1待处理,2公司处理，3审核中，4自缴完成，5代缴未完成",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer",
                "format": "int32"
              }
            }
          },
          {
            "name": "Drivers",
            "in": "query",
            "description": "司机 组别 列表 必输项",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgDriverDto"
              }
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetJgTicketDetailsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Repair/GetMaintainAlarmLogs": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取需保养车辆预警修改日志",
        "parameters": [
          {
            "name": "Key",
            "in": "query",
            "description": "主键值",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.IEnumerable`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOperationLogsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default"
            ]
          }
        ]
      }
    },
    "/api/Repair/GetMaintainAlarms": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取需保养的车辆数",
        "parameters": [
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "StartDateTime",
            "in": "query",
            "description": "开始时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EndDateTime",
            "in": "query",
            "description": "结束时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EarlyWarningType",
            "in": "query",
            "description": "预警类型 0 全部 1 预警中 2 已预警",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.EarlyWarningType"
            }
          },
          {
            "name": "StatusFlag",
            "in": "query",
            "description": "状态0未进入预警，1未跟进，2跟进中，3已跟进,4已完成",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.StatusFlag"
            }
          },
          {
            "name": "StartWarnTime",
            "in": "query",
            "description": "开始预警时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EndWarnTime",
            "in": "query",
            "description": "结束预警时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintainAlarmsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Repair/GetMaintenanceInfos": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "政企服务 获取车辆维保信息",
        "parameters": [
          {
            "name": "OrderNo",
            "in": "query",
            "description": "长包订单编号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "SelfOrderNo",
            "in": "query",
            "description": "自驾订单编号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CheckType",
            "in": "query",
            "description": "年检状态 待定",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "MaintenanceType",
            "in": "query",
            "description": "保养状态 待定",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintenanceInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Repair/GetOperationLogs": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取操作日志",
        "parameters": [
          {
            "name": "KeyNo",
            "in": "query",
            "description": "",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOperationLogsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Repair/GetOrderDetailLink": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取订单详情跳转链接",
        "parameters": [
          {
            "name": "RepairId",
            "in": "query",
            "description": "维修单编号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOrderDetailLinkOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default"
            ]
          }
        ]
      }
    },
    "/api/Repair/GetReimburseMiddlePageUrl": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取报销系统跳转中间页",
        "parameters": [
          {
            "name": "UserCode",
            "in": "query",
            "description": "操作人工号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Key",
            "in": "query",
            "description": "主键值",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Type",
            "in": "query",
            "description": "报销类型：1客户申请工单报销，2员工发起维保工单报销",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.DjEoWork.GetReimburseMiddlePageUrlOutPut, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00026"
            ]
          }
        ]
      }
    },
    "/api/Repair/GetReimburseMiddleResponse": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "报销系统 用 获取售后维保工单报销申请所需信息",
        "parameters": [
          {
            "name": "RepairId",
            "in": "query",
            "description": "维保编号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "UserCode",
            "in": "query",
            "description": "用户code",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReimburseMiddleResponseDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Repair/GetRepairInfo": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取维保",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_GetrepairInfo",
        "parameters": [
          {
            "name": "repairId",
            "in": "query",
            "description": "",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "actionType",
            "in": "query",
            "description": "ActionType 1查看 预约2 修改3",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetrepairInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00003"
            ]
          }
        ]
      }
    },
    "/api/Repair/GetRepairInfoGroupCount": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取订单类型分类汇总列表",
        "parameters": [
          {
            "name": "AcctIds",
            "in": "query",
            "description": "政企ID集合",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "RepairId",
            "in": "query",
            "description": "维保ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarInStartTime",
            "in": "query",
            "description": "进厂时间开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "CarInEndTime",
            "in": "query",
            "description": "进厂时间结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "RepairType",
            "in": "query",
            "description": "订单来源类型",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairFactoryType"
            }
          },
          {
            "name": "StatusFlag",
            "in": "query",
            "description": "--R,预约中（未接单） C,预约中（已接单） G,已登记(待预检) E,已预检(待审核) A,已审核 D, 审核中 J,已拒绝 L, 维修中 K,已完成 F, 已取消",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "BizType",
            "in": "query",
            "description": "1自驾，2代驾，3自驾长包，4代驾长包",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "UserPhone",
            "in": "query",
            "description": "用户联系方式",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ChannelType",
            "in": "query",
            "description": "下单渠道 1客户 2员工",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "IsAuth",
            "in": "query",
            "description": "",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "LicenseVerifyStatus",
            "in": "query",
            "description": "0 待上传 1 待审核 3 已拒绝",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "AuditStatusFlag",
            "in": "query",
            "description": "{ \"N\", \"初始\" }, { \"R\", \"待审核\" }, { \"D\", \"已审核\" }, { \"J\", \"被拒绝\" }, { \"C\", \"已取消\" }, { \"S\",\n\"待确认\" }, { \"M\", \"草稿\" }",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "FinanceStatusFlag",
            "in": "query",
            "description": "{ \"R\", \"等待预审\" }, { \"J\", \"预审被拒\" }, { \"O\", \"未打款\" }, { \"K\", \"已打款\" }, { \"C\", \"单据接收\" }, {\n\"N\", \"拒绝\" }",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAnnualInspectionCountOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Repair/GetRepairInfos": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "保养记录查询 已预约未保养 数据 查询",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_GetrepairInfos",
        "parameters": [
          {
            "name": "AcctIds",
            "in": "query",
            "description": "政企ID集合",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "RepairId",
            "in": "query",
            "description": "维保ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarNo",
            "in": "query",
            "description": "车牌号码",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "CarInStartTime",
            "in": "query",
            "description": "进厂时间开始",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "CarInEndTime",
            "in": "query",
            "description": "进厂时间结束",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "RepairType",
            "in": "query",
            "description": "订单来源类型",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairFactoryType"
            }
          },
          {
            "name": "StatusFlag",
            "in": "query",
            "description": "--R,预约中（未接单） C,预约中（已接单） G,已登记(待预检) E,已预检(待审核) A,已审核 D, 审核中 J,已拒绝 L, 维修中 K,已完成 F, 已取消",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "BizType",
            "in": "query",
            "description": "1自驾，2代驾，3自驾长包，4代驾长包，6耀东方自驾零单",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "UserPhone",
            "in": "query",
            "description": "用户联系方式",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ChannelType",
            "in": "query",
            "description": "下单渠道 1客户 2员工",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "IsAuth",
            "in": "query",
            "description": "",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "LicenseVerifyStatus",
            "in": "query",
            "description": "0 待上传 1 待审核 3 已拒绝",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "AuditStatusFlag",
            "in": "query",
            "description": "{ \"N\", \"初始\" }, { \"R\", \"待审核\" }, { \"D\", \"已审核\" }, { \"J\", \"被拒绝\" }, { \"C\", \"已取消\" }, { \"S\",\n\"待确认\" }, { \"M\", \"草稿\" }",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "FinanceStatusFlag",
            "in": "query",
            "description": "{ \"R\", \"等待预审\" }, { \"J\", \"预审被拒\" }, { \"O\", \"未打款\" }, { \"K\", \"已打款\" }, { \"C\", \"单据接收\" }, {\n\"N\", \"拒绝\" }",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AppointmentProjects",
            "in": "query",
            "description": "维保类型",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairType"
              }
            }
          },
          {
            "name": "CoverageTypes",
            "in": "query",
            "description": "保障类型\n105:基本保障 215.乘客守护 232:尊享保障 233:百万守护  255:尊享守护  256.全程无忧",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.CoverageType"
              }
            }
          },
          {
            "name": "CreateTimeStart",
            "in": "query",
            "description": "下单开始时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "CreateTimeEnd",
            "in": "query",
            "description": "下单结束时间",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "RepeatApplyAuditState",
            "in": "query",
            "description": "维保单审核状态 0.待审核1.已通过2.已拒绝3.无需审核",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairAuditState"
            }
          },
          {
            "name": "CustomerServiceCode",
            "in": "query",
            "description": "客服工号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "RescueReviewStatus",
            "in": "query",
            "description": "救援单审核状态",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RescueReviewStatus"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00001"
            ]
          }
        ]
      }
    },
    "/api/Repair/GetTicketGroupByBizType": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取订单类型分类汇总列表",
        "parameters": [
          {
            "name": "bizType",
            "in": "query",
            "description": "",
            "schema": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetTicketGroupByBizTypeOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Repair/GetWbOrderInfo": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取考拉方车辆维保信息",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_GetWbOrderInfo",
        "parameters": [
          {
            "name": "orderId",
            "in": "query",
            "description": "订单编号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetWbOrderInfoDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default"
            ]
          }
        ]
      }
    },
    "/api/Repair/InitCheckKoalaRepairItems": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "保养记录查询-预约考拉-验证工单是否重复",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.InitCheckKoalaRepairItemsInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.InitCheckKoalaRepairItemsInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.InitCheckKoalaRepairItemsInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default;False"
            ]
          }
        ]
      }
    },
    "/api/Repair/InitCheckRepairItems": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "保养记录查询-预约工单-验证工单是否重复",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.InitCheckRepairItemsInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.InitCheckRepairItemsInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.InitCheckRepairItemsInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default;False"
            ]
          }
        ]
      }
    },
    "/api/Repair/ModifyApplyInfo": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "编辑工单预约申请",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ModifyApplyInfoInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ModifyApplyInfoInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ModifyApplyInfoInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00025"
            ]
          }
        ]
      }
    },
    "/api/Repair/ModifyApplyLicense": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "修改打款银行卡信息",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ModifyApplyLicenseInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ModifyApplyLicenseInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ModifyApplyLicenseInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00048"
            ]
          }
        ]
      }
    },
    "/api/Repair/RepairRescueUrl": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "获取救援系统链接",
        "parameters": [
          {
            "name": "repairId",
            "in": "query",
            "description": "维保单Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.RepairRescueUrlOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00051"
            ]
          }
        ]
      }
    },
    "/api/Repair/ReserveMaintenance": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "维保预约/修改",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_PostReserveMaintenance",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReserveMaintenanceInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReserveMaintenanceInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReserveMaintenanceInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00002;CORPAF_I_00005;False"
            ]
          }
        ]
      }
    },
    "/api/Repair/RevokeLicenseVerify": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "撤销报销凭证审核状态",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.RevokeLicenseVerifyInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.RevokeLicenseVerifyInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.RevokeLicenseVerifyInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00049"
            ]
          }
        ]
      }
    },
    "/api/Repair/SaveKaolaReserve": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "考拉预约",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_PostSaveKaolaReserve",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.SaveKaolaReserveInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.SaveKaolaReserveInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.SaveKaolaReserveInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00006"
            ]
          }
        ]
      }
    },
    "/api/Repair/UserReimburseNotMatchInfos": {
      "get": {
        "tags": [
          "Repair"
        ],
        "summary": "查询用户材料不符合信息",
        "parameters": [
          {
            "name": "UserPhone",
            "in": "query",
            "description": "手机号",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.UserReimburseNotMatchInfosOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00002"
            ]
          }
        ]
      }
    },
    "/api/Repair/VerifyApplyInfo": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "售后系统 维保单审核",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_VerifyApplyInfo",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyApplyInfoInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyApplyInfoInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyApplyInfoInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00023"
            ]
          }
        ]
      }
    },
    "/api/Repair/VerifyLicense": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "报销凭证审核",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyLicenseInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyLicenseInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyLicenseInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00024"
            ]
          }
        ]
      }
    },
    "/api/Repair/VerifyRepairInfo": {
      "post": {
        "tags": [
          "Repair"
        ],
        "summary": "保养记录查询-工单审核",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyRepairInfoInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyRepairInfoInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyRepairInfoInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "CORPAF_I_00039;False"
            ]
          }
        ]
      }
    },
    "/api/Report/GetAfterSaleIndexInfo": {
      "get": {
        "tags": [
          "Report"
        ],
        "summary": "首页待办事项 汇总(保养，待处理事故，保养车辆，待处理违章，年检车辆数)",
        "description": "首页待办事项 汇总(保养，待处理事故，保养车辆，待处理违章，年检车辆数)",
        "parameters": [
          {
            "name": "IsAuth",
            "in": "query",
            "description": "是否来自分离后的前端项目",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAfterSaleIndexInfoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default"
            ]
          }
        ]
      }
    },
    "/api/Report/GetIndexAccidents": {
      "get": {
        "tags": [
          "Report"
        ],
        "summary": "首页 事故数据",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_GetIndexAccidents",
        "parameters": [
          {
            "name": "StartDate",
            "in": "query",
            "description": "开始日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EndDate",
            "in": "query",
            "description": "结束日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetIndexAccidentsOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default"
            ]
          }
        ]
      }
    },
    "/api/Report/GetIndexAccidentsCount": {
      "get": {
        "tags": [
          "Report"
        ],
        "summary": "首页 事故数据 获取待处理事故数",
        "parameters": [
          {
            "name": "StartDate",
            "in": "query",
            "description": "开始日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EndDate",
            "in": "query",
            "description": "结束日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default"
            ]
          }
        ]
      }
    },
    "/api/Report/GetIndexMaintains": {
      "get": {
        "tags": [
          "Report"
        ],
        "summary": "获取首页维保数据",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_GetIndexMaintains",
        "parameters": [
          {
            "name": "StartDate",
            "in": "query",
            "description": "开始日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EndDate",
            "in": "query",
            "description": "结束日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "DataRanges",
            "in": "query",
            "description": "周期表",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetIndexMaintainsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default"
            ]
          }
        ]
      }
    },
    "/api/Report/GetUnMaintainedCount": {
      "get": {
        "tags": [
          "Report"
        ],
        "summary": "获取首页维保数据 获取已预约未保养车辆数",
        "parameters": [
          {
            "name": "StartDate",
            "in": "query",
            "description": "开始日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EndDate",
            "in": "query",
            "description": "结束日期",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "StatusFlag",
            "in": "query",
            "description": "待办事项 已预约未保养车辆数：汇总状态为R和1 截止目前未保养数：汇总状态为F和1",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "QueryWriteDb",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "JWT": [
              "Default"
            ]
          }
        ]
      }
    },
    "/api/SignalRNotify/GetNotificationDetail": {
      "get": {
        "tags": [
          "SignalRNotify"
        ],
        "parameters": [
          {
            "name": "MessageId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Common.SignalR.Dto.GetNotificationDetailDto, Eo.Common, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/SignalRNotify/GetUnReadNotificationCount": {
      "get": {
        "tags": [
          "SignalRNotify"
        ],
        "parameters": [
          {
            "name": "UserId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/SignalRNotify/GetUserNotifications": {
      "get": {
        "tags": [
          "SignalRNotify"
        ],
        "parameters": [
          {
            "name": "SkipCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "MaxResultCount",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "UserId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "IsRead",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[Eo.Common.SignalR.Dto.GetUserNotificationsOutPut, Eo.Common, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/SignalRNotify/ReadAll": {
      "post": {
        "tags": [
          "SignalRNotify"
        ],
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Eo.Common.SignalR.Dto.ReadAllInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Eo.Common.SignalR.Dto.ReadAllInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Eo.Common.SignalR.Dto.ReadAllInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/SignalRNotify/TargetMessageRead": {
      "post": {
        "tags": [
          "SignalRNotify"
        ],
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Eo.Common.SignalR.Dto.TargetMessageReadInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Eo.Common.SignalR.Dto.TargetMessageReadInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Eo.Common.SignalR.Dto.TargetMessageReadInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Sync/PushAccidentInfo": {
      "post": {
        "tags": [
          "Sync"
        ],
        "summary": "push事故 数据保存",
        "description": "http://djpublicapi.dev.ehi.com.cn//swagger/ui/index#!/AfterSale/AfterSale_PushAccidentInfo http://blockorderapiv2.demo.ehi.com.cn/swagger/ui/index#!/AfterSale/AfterSale_PushAccidentInfo",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "items": {
                  "type": "integer",
                  "format": "int32"
                }
              }
            },
            "text/json": {
              "schema": {
                "type": "array",
                "items": {
                  "type": "integer",
                  "format": "int32"
                }
              }
            },
            "application/*+json": {
              "schema": {
                "type": "array",
                "items": {
                  "type": "integer",
                  "format": "int32"
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Sync/PushAnnualInspection": {
      "post": {
        "tags": [
          "Sync"
        ],
        "summary": "push年检数据同步",
        "description": "http://djpublicapi.dev.ehi.com.cn//swagger/ui/index#!/AfterSale/AfterSale_PushAnnualInspection http://blockorderapiv2.demo.ehi.com.cn/swagger/ui/index#!/AfterSale/AfterSale_PushAnnualInspection",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/eHi.Car.Dto.Base.PushAnnualInspectionInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/eHi.Car.Dto.Base.PushAnnualInspectionInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/eHi.Car.Dto.Base.PushAnnualInspectionInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult"
                }
              }
            }
          }
        }
      }
    },
    "/api/Sync/PushRepairInfo": {
      "post": {
        "tags": [
          "Sync"
        ],
        "summary": "push维保 数据保存",
        "description": "http://djpublicapi.dev.ehi.com.cn//swagger/ui/index#!/AfterSale/AfterSale_PushRepairInfo http://blockorderapiv2.demo.ehi.com.cn/swagger/ui/index#!/AfterSale/AfterSale_PushRepairInfo",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            },
            "text/json": {
              "schema": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            },
            "application/*+json": {
              "schema": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Sync/SyncRepairBxStatus": {
      "post": {
        "tags": [
          "Sync"
        ],
        "summary": "手动维保工单报销信息同步",
        "description": "http://blockorderapi.1hai.cn/v2/swagger/ui/index#!/AfterSale/AfterSale_SyncRepairBxStatus",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Sync.Dto.SyncRepairBxInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Sync.Dto.SyncRepairBxInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Sync.Dto.SyncRepairBxInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Sync/SyncRepairEcCarId": {
      "post": {
        "tags": [
          "Sync"
        ],
        "summary": "手动同步维保工单车辆Id信息",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Sync.Dto.SyncRepairEcCarIdInPut"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Sync.Dto.SyncRepairEcCarIdInPut"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Sync.Dto.SyncRepairEcCarIdInPut"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Sync/SyncRepairTempCarNo": {
      "post": {
        "tags": [
          "Sync"
        ],
        "summary": "根据临牌编号变更铁牌编号",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Sync.Dto.SyncRepairTempCarNoInput"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Sync.Dto.SyncRepairTempCarNoInput"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Sync.Dto.SyncRepairTempCarNoInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult"
                }
              }
            }
          }
        }
      }
    },
    "/api/Test/TestLockForMonopoly": {
      "get": {
        "tags": [
          "Test"
        ],
        "summary": "",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Test/TestLockForSpin": {
      "get": {
        "tags": [
          "Test"
        ],
        "summary": "",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Test/TestLogging": {
      "get": {
        "tags": [
          "Test"
        ],
        "summary": "",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Test/TestThrowException": {
      "get": {
        "tags": [
          "Test"
        ],
        "summary": "测试固定异常抛出",
        "parameters": [
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    },
    "/api/Test/TestUow": {
      "get": {
        "tags": [
          "Test"
        ],
        "summary": "",
        "parameters": [
          {
            "name": "id",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "isThrowException",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "OperatorId",
            "in": "query",
            "description": "操作人Id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Platform",
            "in": "query",
            "description": "平台",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlatformEnum"
            }
          },
          {
            "name": "IsTrack",
            "in": "query",
            "description": "是否追踪",
            "schema": {
              "type": "boolean",
              "default": false
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Corp.AfterSale.Application.Contracts.Accident.Dto.AddAccidentLogInPut": {
        "type": "object",
        "properties": {
          "accidentId": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "事故 ID",
            "nullable": true
          },
          "logContent": {
            "type": "string",
            "description": "日志主体",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "添加事故跟进日志"
      },
      "Corp.AfterSale.Application.Contracts.Accident.Dto.EditFollowStateInput": {
        "required": [
          "followState",
          "id"
        ],
        "type": "object",
        "properties": {
          "id": {
            "minLength": 1,
            "type": "string",
            "description": "事故Id"
          },
          "followState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AccidentFollowState"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Accident.Dto.ExportAccidentInfoExcelOutput": {
        "type": "object",
        "properties": {
          "isAsync": {
            "type": "boolean",
            "description": "本次下载启用了异步通知模型"
          },
          "notifyMessage": {
            "type": "string",
            "description": "例外通知",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentAnnualInspectionCountOutPut": {
        "type": "object",
        "properties": {
          "selfDrivingSingle": {
            "type": "integer",
            "description": "政企自驾 1",
            "format": "int32",
            "nullable": true
          },
          "insteadDrivingSingle": {
            "type": "integer",
            "description": "政企代驾 2",
            "format": "int32",
            "nullable": true
          },
          "selfSubscribe": {
            "type": "integer",
            "description": "长包代驾 3",
            "format": "int32",
            "nullable": true
          },
          "insteadSubscribe": {
            "type": "integer",
            "description": "长包自驾 4",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentInfoOutPut": {
        "type": "object",
        "properties": {
          "accidentId": {
            "type": "string",
            "description": "事故Id",
            "nullable": true
          },
          "userAdvanceFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.UserAdvanceFollowStateType"
          },
          "carMaintainDepositFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.CarMaintainDepositFollowStateType"
          },
          "derogatoryFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.DerogatoryFollowStateType"
          },
          "carMaintainFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.CarMaintainFollowStateType"
          },
          "threeCostFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.ThreeCostFollowStateType"
          },
          "isOutsideMaintain": {
            "type": "boolean",
            "description": "是否在外维修",
            "nullable": true
          },
          "appraisalLawsuit": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AppraisalLawsuitType"
          },
          "clientType": {
            "type": "integer",
            "description": "客户类型",
            "format": "int32",
            "nullable": true
          },
          "acctId": {
            "type": "string",
            "description": "政企ID，用户在前端调用第三方接口不全政企名称",
            "nullable": true
          },
          "acctName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "logOn": {
            "type": "string",
            "description": "政企帐号",
            "nullable": true
          },
          "enterprisetName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "订单编号",
            "nullable": true
          },
          "ecCarId": {
            "type": "integer",
            "description": "当前车牌所属车辆ID",
            "format": "int32",
            "nullable": true
          },
          "carUseCity": {
            "type": "string",
            "description": "用车城市",
            "nullable": true
          },
          "accidentName": {
            "type": "string",
            "description": "事故人姓名",
            "nullable": true
          },
          "accidentPhone": {
            "type": "string",
            "description": "事故人手机号",
            "nullable": true
          },
          "accidentDate": {
            "type": "string",
            "description": "事故发生时间",
            "format": "date-time",
            "nullable": true
          },
          "accidentLocation": {
            "type": "string",
            "description": "事故发生地点",
            "nullable": true
          },
          "accidentType": {
            "type": "integer",
            "description": "事故类型",
            "format": "int32",
            "nullable": true
          },
          "statusFlag": {
            "type": "integer",
            "description": "事故状态",
            "format": "int32",
            "nullable": true
          },
          "oprNo": {
            "type": "string",
            "description": "跟进人工号",
            "nullable": true
          },
          "oprName": {
            "type": "string",
            "description": "跟进人姓名",
            "nullable": true
          },
          "proAmount": {
            "type": "number",
            "description": "预估车损",
            "format": "double",
            "nullable": true
          },
          "amount": {
            "type": "number",
            "description": "实际车损",
            "format": "double",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "driverNo": {
            "type": "string",
            "description": "司机编号",
            "nullable": true
          },
          "driverName": {
            "type": "string",
            "description": "司机名称 由前段拼接",
            "nullable": true
          },
          "nextFlowTime": {
            "type": "string",
            "description": "下次跟进日期",
            "format": "date-time",
            "nullable": true
          },
          "childStatusFlag": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ChildStatusFlag"
          },
          "followState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AccidentFollowState"
          },
          "carUseCityId": {
            "type": "integer",
            "description": "用车城市Id",
            "format": "int32",
            "nullable": true
          },
          "dutyType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.DutyTypes"
          },
          "dutyTypeDesc": {
            "type": "string",
            "description": "责任划分类型描述",
            "nullable": true,
            "readOnly": true
          },
          "businessProperty": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Other.Enums.AccountBusinessProperty"
          },
          "extraProperties": {
            "type": "object",
            "additionalProperties": {
              "nullable": true
            },
            "description": "",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": "获取事故详情出参"
      },
      "Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentInfosDto": {
        "type": "object",
        "properties": {
          "clientType": {
            "type": "integer",
            "description": "客户类型",
            "format": "int32",
            "nullable": true
          },
          "acctId": {
            "type": "string",
            "description": "政企ID，用户在前端调用第三方接口不全政企名称",
            "nullable": true
          },
          "acctName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "logOn": {
            "type": "string",
            "description": "政企帐号",
            "nullable": true
          },
          "enterprisetName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "订单编号",
            "nullable": true
          },
          "ecCarId": {
            "type": "integer",
            "description": "当前车牌所属车辆ID",
            "format": "int32",
            "nullable": true
          },
          "carUseCity": {
            "type": "string",
            "description": "用车城市",
            "nullable": true
          },
          "accidentName": {
            "type": "string",
            "description": "事故人姓名",
            "nullable": true
          },
          "accidentPhone": {
            "type": "string",
            "description": "事故人手机号",
            "nullable": true
          },
          "accidentDate": {
            "type": "string",
            "description": "事故发生时间",
            "format": "date-time",
            "nullable": true
          },
          "accidentLocation": {
            "type": "string",
            "description": "事故发生地点",
            "nullable": true
          },
          "accidentType": {
            "type": "integer",
            "description": "事故类型",
            "format": "int32",
            "nullable": true
          },
          "statusFlag": {
            "type": "integer",
            "description": "事故状态",
            "format": "int32",
            "nullable": true
          },
          "oprNo": {
            "type": "string",
            "description": "跟进人工号",
            "nullable": true
          },
          "oprName": {
            "type": "string",
            "description": "跟进人姓名",
            "nullable": true
          },
          "proAmount": {
            "type": "number",
            "description": "预估车损",
            "format": "double",
            "nullable": true
          },
          "amount": {
            "type": "number",
            "description": "实际车损",
            "format": "double",
            "nullable": true
          },
          "accidentId": {
            "type": "string",
            "description": "事故Id",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "driverNo": {
            "type": "string",
            "description": "司机编号",
            "nullable": true
          },
          "driverName": {
            "type": "string",
            "description": "司机名称 由前段拼接",
            "nullable": true
          },
          "nextFlowTime": {
            "type": "string",
            "description": "下次跟进日期",
            "format": "date-time",
            "nullable": true
          },
          "childStatusFlag": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ChildStatusFlag"
          },
          "followState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AccidentFollowState"
          },
          "carUseCityId": {
            "type": "integer",
            "description": "用车城市Id",
            "format": "int32",
            "nullable": true
          },
          "dutyType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.DutyTypes"
          },
          "dutyTypeDesc": {
            "type": "string",
            "description": "责任划分类型描述",
            "nullable": true,
            "readOnly": true
          },
          "businessProperty": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Other.Enums.AccountBusinessProperty"
          },
          "userAdvanceFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.UserAdvanceFollowStateType"
          },
          "userAdvanceDesc": {
            "type": "string",
            "description": "客户垫付费用跟进状态描述",
            "nullable": true,
            "readOnly": true
          },
          "carMaintainDepositFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.CarMaintainDepositFollowStateType"
          },
          "carMaintainDepositDesc": {
            "type": "string",
            "description": "本车维修押金跟进状态描述",
            "nullable": true,
            "readOnly": true
          },
          "derogatoryFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.DerogatoryFollowStateType"
          },
          "derogatoryDesc": {
            "type": "string",
            "description": "贬损费用跟进状态描述",
            "nullable": true,
            "readOnly": true
          },
          "carMaintainFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.CarMaintainFollowStateType"
          },
          "carMaintainDesc": {
            "type": "string",
            "description": "本车维修费用跟进状态描述",
            "nullable": true,
            "readOnly": true
          },
          "threeCostFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.ThreeCostFollowStateType"
          },
          "threeCostDesc": {
            "type": "string",
            "description": "三者费用跟进状态描述",
            "nullable": true,
            "readOnly": true
          },
          "isOutsideMaintain": {
            "type": "boolean",
            "description": "是否在外维修",
            "nullable": true
          },
          "isOutsideMaintainDesc": {
            "type": "string",
            "description": "是否在外维修描述",
            "nullable": true,
            "readOnly": true
          },
          "appraisalLawsuit": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AppraisalLawsuitType"
          },
          "appraisalLawsuitDesc": {
            "type": "string",
            "description": "公估诉讼描述",
            "nullable": true,
            "readOnly": true
          },
          "extraProperties": {
            "type": "object",
            "additionalProperties": {
              "nullable": true
            },
            "description": "",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Accident.Dto.GetAfterSaleAccidentInfoInPut": {
        "type": "object",
        "properties": {
          "queryWriteDb": {
            "type": "boolean"
          },
          "maxResultCount": {
            "type": "integer",
            "format": "int32"
          },
          "skipCount": {
            "type": "integer",
            "format": "int32"
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "statusFlags": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32"
            },
            "description": "事故状态 1 待处理(0待处理，1缺少资料，2资料更新，9退款信息) 2 处理中(参照子状态) 3 理赔中（3） 4 打款中（4） 5 已完成(5已打款) 6 撤案(6已撤案)\n7 拒赔（7） 8 诉讼中(10) 9 待上报(8) 10 已上报(12) 11 已完成(13)",
            "nullable": true
          },
          "childStatusFlag": {
            "type": "integer",
            "description": "事故子状态\n1-客户处理中 \n2-联系不上 \n3-车辆维修中 \n4-资料收集中\n5-人伤资料收集中",
            "format": "int32",
            "nullable": true
          },
          "materialStatus": {
            "type": "integer",
            "description": "资料收集状态\n0 缺少资料\n1 资料齐全",
            "format": "int32",
            "nullable": true
          },
          "accidentType": {
            "type": "integer",
            "description": "事故类型:1-单车事故 2-双车事故 3-多车事故 4-人伤事故 5-死亡事故",
            "format": "int32",
            "nullable": true
          },
          "acctId": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "政企id",
            "nullable": true
          },
          "accidentStartTime": {
            "type": "string",
            "description": "事故开始时间(比较粒度：天)",
            "nullable": true
          },
          "accidentEndTime": {
            "type": "string",
            "description": "事故结束时间(比较粒度：天)",
            "nullable": true
          },
          "bizTypes": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32"
            },
            "description": "1 零单自驾\n2 零单代驾\n3 长包自驾\n4 长包代驾",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "订单号",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Accident.Dto.GetAfterSaleAccidentInfoOutPut": {
        "type": "object",
        "properties": {
          "accidentId": {
            "type": "string",
            "description": "事故编号 主键",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "accidentName": {
            "type": "string",
            "description": "用车人姓名",
            "nullable": true
          },
          "accidentPhone": {
            "type": "string",
            "description": "用车人电话",
            "nullable": true
          },
          "accidentDate": {
            "type": "string",
            "description": "事故日期",
            "format": "date-time",
            "nullable": true
          },
          "accidentType": {
            "type": "integer",
            "description": "事故类型:1-单车事故 2-双车事故 3-多车事故 4-人伤事故 5-死亡事故",
            "format": "int32"
          },
          "statusFlag": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AfterSaleAccidentStatusFlag"
          },
          "accidentLocation": {
            "type": "string",
            "description": "事故地点",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "订单号",
            "nullable": true
          },
          "dutyType": {
            "type": "integer",
            "description": "事故责任：1全责、2主责、3同责、4次责、5无责、6责任未定",
            "format": "int32"
          },
          "carUseCity": {
            "type": "string",
            "description": "城市",
            "nullable": true
          },
          "bizType": {
            "type": "integer",
            "description": "事故归属订单业务类型\n1 零单自驾\n2 零单代驾\n3 长包自驾\n4 长包代驾",
            "format": "int32"
          },
          "statusFlagDesc": {
            "type": "string",
            "description": "事故状态描述",
            "nullable": true,
            "readOnly": true
          },
          "carDamagePartDesc": {
            "type": "string",
            "description": "车损部位",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Accident.Dto.GetOrderLinkOutput": {
        "type": "object",
        "properties": {
          "url": {
            "type": "string",
            "description": "跳转链接",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Accident.Dto.PostAssignFollowersInPut": {
        "type": "object",
        "properties": {
          "accidentIds": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "事故工单ID集合",
            "nullable": true
          },
          "roleId": {
            "type": "string",
            "description": "分配角色ID",
            "nullable": true
          },
          "roleName": {
            "type": "string",
            "description": "分配角色名称",
            "nullable": true
          },
          "oprNo": {
            "type": "string",
            "description": "跟进人工号",
            "nullable": true
          },
          "oprName": {
            "type": "string",
            "description": "跟进人姓名",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "事故添加跟进人"
      },
      "Corp.AfterSale.Application.Contracts.Accident.Dto.PostCarDamageAsyncInPut": {
        "type": "object",
        "properties": {
          "accidentId": {
            "type": "string",
            "description": "事故编号",
            "nullable": true
          },
          "amount": {
            "type": "number",
            "description": "事故定损金额",
            "format": "double"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Accident.Dto.UpdateAcccidentStateInfoInPut": {
        "type": "object",
        "properties": {
          "accidentId": {
            "type": "string",
            "description": "事故Id",
            "nullable": true
          },
          "userAdvanceFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.UserAdvanceFollowStateType"
          },
          "carMaintainDepositFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.CarMaintainDepositFollowStateType"
          },
          "derogatoryFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.DerogatoryFollowStateType"
          },
          "carMaintainFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.CarMaintainFollowStateType"
          },
          "threeCostFollowState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.ThreeCostFollowStateType"
          },
          "isOutsideMaintain": {
            "type": "boolean",
            "description": "是否在外维修",
            "nullable": true
          },
          "appraisalLawsuit": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AppraisalLawsuitType"
          }
        },
        "additionalProperties": false,
        "description": "修改事故详细跟进状态入参"
      },
      "Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.DeleteItemPriceRuleInput": {
        "type": "object",
        "properties": {
          "ids": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32"
            },
            "description": "配置项Id",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "删除维保规则配置入参"
      },
      "Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.RepairItemPriceRulesDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "配置项Id",
            "format": "int32"
          },
          "itemId": {
            "type": "integer",
            "description": "维保项Id",
            "format": "int32"
          },
          "itemName": {
            "type": "string",
            "description": "维保项名称",
            "nullable": true
          },
          "checkType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.PriceRuleCheckType"
          },
          "rangeCheckType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RangeCheckTypes"
          },
          "price": {
            "type": "number",
            "description": "规则对应单价",
            "format": "double"
          },
          "rangeStart": {
            "type": "number",
            "description": "区间下限，默认为0",
            "format": "double"
          },
          "rangeEnd": {
            "type": "number",
            "description": "区间上限，默认为0",
            "format": "double"
          },
          "ruleName": {
            "type": "string",
            "description": "规则描述",
            "nullable": true
          },
          "isRepair": {
            "type": "boolean",
            "description": "维修时是否检查 true 检查 false 不检查"
          },
          "isMaintain": {
            "type": "boolean",
            "description": "保养时是否检查 true 检查 false 不检查"
          },
          "quantity": {
            "type": "integer",
            "description": "数量限制",
            "format": "int32"
          },
          "checkTypeDesc": {
            "type": "string",
            "description": "判定类型描述",
            "nullable": true,
            "readOnly": true
          },
          "rangeCheckTypeDesc": {
            "type": "string",
            "description": "区间判定方式",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.ReserveItemPriceRuleInput": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "配置项Id",
            "format": "int32",
            "nullable": true
          },
          "itemId": {
            "type": "integer",
            "description": "维保项目Id",
            "format": "int32"
          },
          "itemName": {
            "type": "string",
            "description": "维保项目Id",
            "nullable": true
          },
          "checkType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.PriceRuleCheckType"
          },
          "rangeCheckType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RangeCheckTypes"
          },
          "price": {
            "type": "number",
            "description": "规则对应单价",
            "format": "double"
          },
          "rangeStart": {
            "type": "number",
            "description": "区间下限，默认为0",
            "format": "double"
          },
          "rangeEnd": {
            "type": "number",
            "description": "区间上限，默认为0",
            "format": "double"
          },
          "ruleName": {
            "type": "string",
            "description": "规则描述",
            "nullable": true
          },
          "isRepair": {
            "type": "boolean",
            "description": "维修时是否检查 true 检查 false 不检查"
          },
          "isMaintain": {
            "type": "boolean",
            "description": "保养时是否检查 true 检查 false 不检查"
          },
          "quantity": {
            "type": "integer",
            "description": "数量限制",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": "保存维护配置入参"
      },
      "Corp.AfterSale.Application.Contracts.Annual.Dto.AnnualInspectionInPut": {
        "type": "object",
        "properties": {
          "ecCarId": {
            "type": "integer",
            "description": "当前所属车辆ID 需要在前端通过第三方接口联查获取",
            "format": "int32"
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "dateNextCheck": {
            "type": "string",
            "description": "下次年检时间",
            "format": "date-time",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Annual.Dto.GetAnnualInspectionsCountOutPut": {
        "type": "object",
        "properties": {
          "selfDrivingSingle": {
            "type": "integer",
            "description": "政企自驾零单",
            "format": "int32",
            "nullable": true
          },
          "insteadDrivingSingle": {
            "type": "integer",
            "description": "政企代驾零单",
            "format": "int32",
            "nullable": true
          },
          "selfSubscribe": {
            "type": "integer",
            "description": "政企自驾长包",
            "format": "int32",
            "nullable": true
          },
          "insteadSubscribe": {
            "type": "integer",
            "description": "政企代驾长包",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Annual.Dto.GetAnnualInspectionsDto": {
        "type": "object",
        "properties": {
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "orderNo": {
            "type": "string",
            "description": "订单号",
            "nullable": true
          },
          "acctId": {
            "type": "string",
            "description": "政企ID",
            "nullable": true
          },
          "acctName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "logOn": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "enterprisetName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "carUseCity": {
            "type": "string",
            "description": "城市",
            "nullable": true
          },
          "takeCarName": {
            "type": "string",
            "description": "用车人姓名",
            "nullable": true
          },
          "takeCarCellPhone": {
            "type": "string",
            "description": "用车人手机号",
            "nullable": true
          },
          "dateNextCheck": {
            "type": "string",
            "description": "下次年检日期",
            "format": "date-time",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌",
            "nullable": true
          },
          "driverNo": {
            "type": "string",
            "description": "司机编号",
            "nullable": true
          },
          "driverName": {
            "type": "string",
            "description": "司机名称",
            "nullable": true
          },
          "driverPhone": {
            "type": "string",
            "description": "司机手机号",
            "nullable": true
          },
          "extraProperties": {
            "type": "object",
            "additionalProperties": {
              "nullable": true
            },
            "description": "",
            "nullable": true,
            "readOnly": true
          },
          "businessProperty": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Other.Enums.AccountBusinessProperty"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Annual.Dto.ModifyMaintainAlarmStatusesInPut": {
        "type": "object",
        "properties": {
          "ids": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32"
            },
            "description": "待更新记录Id集合",
            "nullable": true
          },
          "status": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.AnnualInspection.Enums.MaintainAlarmStatus"
          },
          "remark": {
            "type": "string",
            "description": "备注内容",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.CityNameByLocationInput": {
        "type": "object",
        "properties": {
          "longitude": {
            "type": "number",
            "description": "经度",
            "format": "double"
          },
          "latitude": {
            "type": "number",
            "description": "纬度",
            "format": "double"
          },
          "openId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "userId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "userInfoSourceType": {
            "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.CityNameByLocationOutput": {
        "type": "object",
        "properties": {
          "cityName": {
            "type": "string",
            "description": "城市名称",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.GetAccDto": {
        "type": "object",
        "properties": {
          "acctId": {
            "type": "string",
            "description": "政企Id",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "logOn": {
            "type": "string",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.GetAccountsDto": {
        "type": "object",
        "properties": {
          "value": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "logOn": {
            "type": "string",
            "description": "政企账号",
            "nullable": true
          },
          "activeFlag": {
            "type": "string",
            "description": "是否启用 : 1启用0禁用",
            "nullable": true
          },
          "activation": {
            "type": "boolean",
            "description": ""
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.GetAreasDto": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "displayName": {
            "type": "string",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.GetKaolaStationsResultDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "可预约时间字符串表示形式",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "可预约事件段，用于前端展示",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.GetOtherSystemUrlDto": {
        "type": "object",
        "properties": {
          "systemName": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "systemUrl": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "index": {
            "type": "integer",
            "description": "",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": "ctor"
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.GetRepairReimburseInfosDto": {
        "type": "object",
        "properties": {
          "repairId": {
            "type": "string",
            "description": "维保编号",
            "nullable": true
          },
          "amount": {
            "type": "number",
            "description": "报销总金额",
            "format": "double"
          },
          "bxNo": {
            "type": "string",
            "description": "报销编号",
            "nullable": true
          },
          "financeStatusFlag": {
            "type": "string",
            "description": "报销打款状态{ \"R\", \"等待预审\" }, { \"J\", \"预审被拒\" }, { \"O\", \"未打款\" }, { \"K\", \"已打款\" }, { \"C\", \"单据接收\" },\n{ \"N\", \"拒绝\" }",
            "nullable": true
          },
          "auditStatusFlag": {
            "type": "string",
            "description": "报销审核状态 { \"N\", \"初始\" }, { \"R\", \"待审核\" }, { \"D\", \"已审核\" }, { \"J\", \"被拒绝\" }, { \"C\", \"已取消\" }, {\n\"S\", \"待确认\" }, { \"M\", \"草稿\" }",
            "nullable": true
          },
          "lastModificationTime": {
            "type": "string",
            "description": "",
            "format": "date-time",
            "nullable": true
          },
          "creationTime": {
            "type": "string",
            "description": "",
            "format": "date-time"
          },
          "userCode": {
            "type": "string",
            "description": "操作人工号",
            "nullable": true
          },
          "userName": {
            "type": "string",
            "description": "操作人姓名",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.GetRepairReimburseInfosOutPut": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.GetRepairReimburseInfosDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.GetUserInfoDto": {
        "type": "object",
        "properties": {
          "userCode": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "userName": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "systems": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.GetOtherSystemUrlDto"
            },
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarCarNoDto": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean",
            "description": ""
          },
          "carNo": {
            "type": "string",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarCarNoInput": {
        "type": "object",
        "properties": {
          "imageUrl": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "openId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "userId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "userInfoSourceType": {
            "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarKilometerDto": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean",
            "description": ""
          },
          "kilometer": {
            "type": "integer",
            "description": "识别公里数",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarKilometerInput": {
        "type": "object",
        "properties": {
          "imageUrl": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "openId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "userId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "userInfoSourceType": {
            "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfoInput": {
        "type": "object",
        "properties": {
          "info": {
            "type": "string",
            "description": "密文信息",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfosDto": {
        "type": "object",
        "properties": {
          "field": {
            "type": "string",
            "description": "字段Id",
            "nullable": true
          },
          "info": {
            "type": "string",
            "description": "密文",
            "nullable": true
          },
          "originInfo": {
            "type": "string",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfosInput": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfosDto"
            },
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.TemplateType": {
        "enum": [
          1,
          2
        ],
        "type": "integer",
        "description": "模板类型",
        "format": "int32"
      },
      "Corp.AfterSale.Application.Contracts.Common.Dto.TokenInput": {
        "type": "object",
        "properties": {
          "token": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "domain": {
            "type": "string",
            "description": "cookie 域",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "token 请求"
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.AddOrUpdateComplaintTypeInput": {
        "required": [
          "complaintName"
        ],
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "大于0修改",
            "format": "int32"
          },
          "complaintName": {
            "minLength": 1,
            "type": "string",
            "description": "类型名称"
          },
          "email": {
            "type": "string",
            "description": "邮件",
            "nullable": true
          },
          "isSendEmail": {
            "type": "boolean",
            "description": "是否发送邮件"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.CancelComplaintInput": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "客诉Id",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": "取消客诉入参"
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintThreeVerifyUsersOutput": {
        "type": "object",
        "properties": {
          "reviewUser": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.Hr.UserInfoByCode"
          },
          "firstVerifyUser": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.Hr.UserInfoByCode"
            },
            "description": "第一审核人信息",
            "nullable": true
          },
          "secondVerifyUser": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.Hr.UserInfoByCode"
            },
            "description": "第二审核人信息",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "获取客诉三级审核人-出参"
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintTypeDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Id",
            "format": "int32"
          },
          "complaintName": {
            "type": "string",
            "description": "类型名称",
            "nullable": true
          },
          "email": {
            "type": "string",
            "description": "邮件",
            "nullable": true
          },
          "isSendEmail": {
            "type": "boolean",
            "description": "是否发送邮件"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintVerifyInfoDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "客诉Id",
            "format": "int32"
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "bizTypeDesc": {
            "type": "string",
            "description": "业务类型描述",
            "nullable": true,
            "readOnly": true
          },
          "complaintType": {
            "type": "integer",
            "description": "投诉类型",
            "format": "int32"
          },
          "complaintTypeDesc": {
            "type": "string",
            "description": "投诉类型描述",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "订单号",
            "nullable": true
          },
          "selfOrderNo": {
            "type": "string",
            "description": "自驾订单号",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "accountName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "complainedTime": {
            "type": "string",
            "description": "投诉日期",
            "format": "date-time"
          },
          "complaintState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Complaint.Enums.ComplaintStates"
          },
          "complaintStateDesc": {
            "type": "string",
            "description": "状态描述",
            "nullable": true,
            "readOnly": true
          },
          "creationUserNo": {
            "type": "string",
            "description": "创建人工号",
            "nullable": true
          },
          "creationUserName": {
            "type": "string",
            "description": "创建人姓名",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "客诉审核信息"
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintVerifyLogsDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "唯一标识",
            "format": "int32"
          },
          "complaintId": {
            "type": "integer",
            "description": "客诉ID",
            "format": "int32"
          },
          "operateUserNo": {
            "type": "string",
            "description": "操作人工号",
            "nullable": true
          },
          "operateUserName": {
            "type": "string",
            "description": "操作人姓名",
            "nullable": true
          },
          "operationType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Complaint.Enums.ComplaintOperationType"
          },
          "operationTypeDesc": {
            "type": "string",
            "description": "操作类型描述",
            "nullable": true,
            "readOnly": true
          },
          "preComplaintState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Complaint.Enums.ComplaintStates"
          },
          "preComplaintStateDesc": {
            "type": "string",
            "description": "操作前客诉状态描述",
            "nullable": true,
            "readOnly": true
          },
          "afterComplaintState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Complaint.Enums.ComplaintStates"
          },
          "afterComplaintStateDesc": {
            "type": "string",
            "description": "操作后客诉状态",
            "nullable": true,
            "readOnly": true
          },
          "verifyContent": {
            "type": "string",
            "description": "审核意见",
            "nullable": true
          },
          "creationTime": {
            "type": "string",
            "description": "创建时间",
            "format": "date-time",
            "nullable": true
          },
          "files": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "附件",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "客诉审核记录日志"
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintVerifyLogsOutPut": {
        "type": "object",
        "properties": {
          "complaintVerifyLogs": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintVerifyLogsDto"
            },
            "description": "客诉审核记录日志",
            "nullable": true
          },
          "complaintInfo": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintInfoDto"
          }
        },
        "additionalProperties": false,
        "description": "获取客诉审核记录日志--出参"
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.CompleteComplaintInput": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "客诉Id",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": "完成客诉入参"
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintInfoDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "客诉ID",
            "format": "int32"
          },
          "complaintType": {
            "type": "integer",
            "description": "投诉类型",
            "format": "int32"
          },
          "complaintState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Complaint.Enums.ComplaintStates"
          },
          "selfOrderNo": {
            "type": "string",
            "description": "自驾订单号",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "isMyCar": {
            "type": "boolean",
            "description": "是否本车原因,默认否"
          },
          "complainantName": {
            "type": "string",
            "description": "投诉人姓名",
            "nullable": true
          },
          "complainantPhone": {
            "type": "string",
            "description": "投诉人联系方式",
            "nullable": true
          },
          "complainantDetail": {
            "type": "string",
            "description": "投诉详情",
            "nullable": true
          },
          "afterSalePlan": {
            "type": "string",
            "description": "售后方案",
            "nullable": true
          },
          "salesmanNo": {
            "type": "string",
            "description": "业务员编号",
            "nullable": true
          },
          "salesmanName": {
            "type": "string",
            "description": "业务员姓名",
            "nullable": true
          },
          "acctId": {
            "type": "string",
            "description": "政企Id",
            "nullable": true
          },
          "acctName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "userOrderCount": {
            "type": "integer",
            "description": "客户近一年订单量",
            "format": "int32"
          },
          "userOrderAmount": {
            "type": "number",
            "description": "客户近一年订单金额",
            "format": "double",
            "nullable": true
          },
          "acctOrderAmount": {
            "type": "number",
            "description": "政企近一年订单金额",
            "format": "double",
            "nullable": true
          },
          "orderTotalAmount": {
            "type": "number",
            "description": "订单总价",
            "format": "double"
          },
          "reductionDay": {
            "type": "integer",
            "description": "减免天数",
            "format": "int32"
          },
          "reductionAmount": {
            "type": "number",
            "description": "减免金额",
            "format": "double"
          },
          "coverageType": {
            "type": "string",
            "description": "保障类型",
            "nullable": true
          },
          "complainedTime": {
            "type": "string",
            "description": "投诉日期",
            "format": "date-time",
            "nullable": true
          },
          "orderStartDateTime": {
            "type": "string",
            "description": "订单租期开始时间",
            "format": "date-time",
            "nullable": true
          },
          "orderEndDateTime": {
            "type": "string",
            "description": "订单租期结束时间",
            "format": "date-time",
            "nullable": true
          },
          "isSalesIntervention": {
            "type": "boolean",
            "description": "销售介入"
          },
          "files": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "附件",
            "nullable": true
          },
          "bizTypeDesc": {
            "type": "string",
            "description": "业务类型描述",
            "nullable": true,
            "readOnly": true
          },
          "complaintTypeDesc": {
            "type": "string",
            "description": "投诉类型描述",
            "nullable": true
          },
          "complaintStateDesc": {
            "type": "string",
            "description": "投诉状态描述",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": "客诉信息详情"
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintInfosDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "客诉Id",
            "format": "int32"
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "complaintType": {
            "type": "integer",
            "description": "投诉类型：1.事故 2.保养",
            "format": "int32"
          },
          "selfOrderNo": {
            "type": "string",
            "description": "自驾订单号",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "acctId": {
            "type": "string",
            "description": "政企Id",
            "nullable": true
          },
          "acctName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "verifyOprNo": {
            "type": "string",
            "description": "审核人",
            "nullable": true
          },
          "verifyOprName": {
            "type": "string",
            "description": "审核人姓名",
            "nullable": true
          },
          "salesmanNo": {
            "type": "string",
            "description": "业务员编号",
            "nullable": true
          },
          "salesmanName": {
            "type": "string",
            "description": "业务员姓名",
            "nullable": true
          },
          "complainantName": {
            "type": "string",
            "description": "投诉人姓名",
            "nullable": true
          },
          "complainantPhone": {
            "type": "string",
            "description": "投诉人联系方式",
            "nullable": true
          },
          "coverageType": {
            "type": "string",
            "description": "保障类型",
            "nullable": true
          },
          "isMyCar": {
            "type": "boolean",
            "description": "是否本车原因,默认否"
          },
          "complainedTime": {
            "type": "string",
            "description": "投诉日期",
            "format": "date-time",
            "nullable": true
          },
          "orderStartDateTime": {
            "type": "string",
            "description": "订单租期开始时间",
            "format": "date-time",
            "nullable": true
          },
          "orderEndDateTime": {
            "type": "string",
            "description": "订单租期结束时间",
            "format": "date-time",
            "nullable": true
          },
          "userOrderCount": {
            "type": "integer",
            "description": "客户近一年订单量",
            "format": "int32"
          },
          "userOrderAmount": {
            "type": "number",
            "description": "客户近一年订单金额",
            "format": "double",
            "nullable": true
          },
          "acctOrderAmount": {
            "type": "number",
            "description": "政企近一年订单金额",
            "format": "double",
            "nullable": true
          },
          "reductionDay": {
            "type": "integer",
            "description": "减免天数",
            "format": "int32"
          },
          "reductionAmount": {
            "type": "number",
            "description": "减免金额",
            "format": "double"
          },
          "complainantDetail": {
            "type": "string",
            "description": "投诉详情",
            "nullable": true
          },
          "afterSalePlan": {
            "type": "string",
            "description": "售后方案",
            "nullable": true
          },
          "complaintState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Complaint.Enums.ComplaintStates"
          },
          "isSalesIntervention": {
            "type": "boolean",
            "description": "销售介入"
          },
          "isSalesInterventionDesc": {
            "type": "string",
            "description": "销售是否介入",
            "nullable": true,
            "readOnly": true
          },
          "bizTypeDesc": {
            "type": "string",
            "description": "业务类型描述",
            "nullable": true,
            "readOnly": true
          },
          "complaintTypeDesc": {
            "type": "string",
            "description": "投诉类型描述",
            "nullable": true
          },
          "complaintStateDesc": {
            "type": "string",
            "description": "投诉状态描述",
            "nullable": true,
            "readOnly": true
          },
          "creationUserNo": {
            "type": "string",
            "description": "创建人工号",
            "nullable": true
          },
          "creationUserName": {
            "type": "string",
            "description": "创建人姓名",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintVerifyInfosOutput": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintVerifyInfoDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": "客诉审核查询-出参"
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.GetOrderInfoDto": {
        "type": "object",
        "properties": {
          "acctId": {
            "type": "string",
            "description": "企业编号",
            "nullable": true
          },
          "acctName": {
            "type": "string",
            "description": "企业名称",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "订单编号",
            "nullable": true
          },
          "selfOrderNo": {
            "type": "string",
            "description": "自驾订单编号",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "salesSerialNo": {
            "type": "string",
            "description": "销售编号",
            "nullable": true
          },
          "salesSerialName": {
            "type": "string",
            "description": "销售姓名",
            "nullable": true
          },
          "orderTotalAmount": {
            "type": "number",
            "description": "订单总价",
            "format": "double"
          },
          "complainantName": {
            "type": "string",
            "description": "投诉人姓名",
            "nullable": true
          },
          "complainantPhone": {
            "type": "string",
            "description": "投诉人联系方式",
            "nullable": true
          },
          "actualUseStart": {
            "type": "string",
            "description": "订单实际开始时间",
            "format": "date-time",
            "nullable": true
          },
          "actualUseEnd": {
            "type": "string",
            "description": "订单实际结束时间",
            "format": "date-time",
            "nullable": true
          },
          "coverageTypes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.CoverageType"
            },
            "description": "保障类型",
            "nullable": true
          },
          "bizTypeDesc": {
            "type": "string",
            "description": "业务类型描述",
            "nullable": true,
            "readOnly": true
          },
          "coverageTypeDesc": {
            "type": "string",
            "description": "保障类型描述",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.GetUserOrderCountDto": {
        "type": "object",
        "properties": {
          "entzjOrderCount": {
            "type": "integer",
            "description": "企业自驾零单订单数",
            "format": "int32"
          },
          "blockOrderCount": {
            "type": "integer",
            "description": "长包订单量",
            "format": "int32"
          },
          "userOrderCount": {
            "type": "integer",
            "description": "客户近一年订单量",
            "format": "int32",
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": "客户近一年订单量"
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.ReserveComplaintInfoInPut": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "客诉Id",
            "format": "int32"
          },
          "complaintType": {
            "type": "integer",
            "description": "投诉类型",
            "format": "int32"
          },
          "orderNo": {
            "type": "string",
            "description": "订单号",
            "nullable": true
          },
          "selfOrderNo": {
            "type": "string",
            "description": "自驾订单号",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "isMyCar": {
            "type": "boolean",
            "description": "是否本车原因,默认否"
          },
          "complainantName": {
            "type": "string",
            "description": "投诉人姓名",
            "nullable": true
          },
          "complainantPhone": {
            "type": "string",
            "description": "投诉人联系方式",
            "nullable": true
          },
          "complainantDetail": {
            "type": "string",
            "description": "投诉详情",
            "nullable": true
          },
          "afterSalePlan": {
            "type": "string",
            "description": "售后方案",
            "nullable": true
          },
          "salesmanNo": {
            "type": "string",
            "description": "业务员编号",
            "nullable": true
          },
          "acctId": {
            "type": "string",
            "description": "政企编号",
            "nullable": true
          },
          "userOrderCount": {
            "type": "integer",
            "description": "客户近一年订单量",
            "format": "int32"
          },
          "userOrderAmount": {
            "type": "number",
            "description": "客户近一年订单金额",
            "format": "double",
            "nullable": true
          },
          "acctOrderAmount": {
            "type": "number",
            "description": "政企近一年订单金额",
            "format": "double",
            "nullable": true
          },
          "orderTotalAmount": {
            "type": "number",
            "description": "订单总价",
            "format": "double"
          },
          "reductionDay": {
            "type": "integer",
            "description": "减免天数",
            "format": "int32"
          },
          "reductionAmount": {
            "type": "number",
            "description": "减免金额",
            "format": "double"
          },
          "coverageType": {
            "type": "string",
            "description": "保障类型",
            "nullable": true
          },
          "complainedTime": {
            "type": "string",
            "description": "投诉日期",
            "format": "date-time"
          },
          "orderStartDateTime": {
            "type": "string",
            "description": "订单租期开始时间",
            "format": "date-time"
          },
          "orderEndDateTime": {
            "type": "string",
            "description": "订单租期结束时间",
            "format": "date-time"
          },
          "actionType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Complaint.Enums.ActionType"
          },
          "isReview": {
            "type": "boolean",
            "description": "是否提交复核"
          },
          "isSalesIntervention": {
            "type": "boolean",
            "description": "销售介入"
          },
          "files": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "附件",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "登记客诉入参"
      },
      "Corp.AfterSale.Application.Contracts.Complaint.Dto.VerifyComplaintInfosInput": {
        "type": "object",
        "properties": {
          "ids": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32"
            },
            "description": "客诉Id列表",
            "nullable": true
          },
          "verifyStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Verify.Enums.VerifyStatusEnum"
          },
          "verifyContent": {
            "type": "string",
            "description": "审核意见",
            "nullable": true
          },
          "needSecondVerify": {
            "type": "boolean",
            "description": "需要第二审核人"
          },
          "files": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "附件",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "客诉管理-客诉审核-审核-入参"
      },
      "Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsDto": {
        "type": "object",
        "properties": {
          "accidentId": {
            "type": "string",
            "description": "主键 事故ID",
            "nullable": true
          },
          "isHavePassenger": {
            "type": "boolean",
            "description": "是否有乘客",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "accidentDate": {
            "type": "string",
            "description": "自驾事故时间",
            "format": "date-time",
            "nullable": true
          },
          "acctId": {
            "type": "string",
            "description": "政企ID",
            "nullable": true
          },
          "acctName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "driverNo": {
            "type": "string",
            "description": "司机工号",
            "nullable": true
          },
          "driverName": {
            "type": "string",
            "description": "司机姓名",
            "nullable": true
          },
          "accidentTime": {
            "type": "string",
            "description": "驾管事故时间(事故具体时间)",
            "format": "date-time",
            "nullable": true
          },
          "jgAccidentType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.JgAccidentType"
          },
          "accidentType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.AccidentTypes"
          },
          "jgDutyType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.JgDutyType"
          },
          "dutyType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.DutyTypes"
          },
          "areaType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.AreaType"
          },
          "cityName": {
            "type": "string",
            "description": "工作城市",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "supervisorName": {
            "type": "string",
            "description": "直属主管",
            "nullable": true
          },
          "areaManager": {
            "type": "string",
            "description": "区域经理",
            "nullable": true
          },
          "jgDetail": {
            "type": "string",
            "description": "驾管事故详情",
            "nullable": true
          },
          "jgRemark": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetJgAccidentDetailRemarksDto"
            },
            "description": "驾管备注",
            "nullable": true
          },
          "statusFlag": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AfterSaleAccidentStatusFlag"
          },
          "impactType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ImpactType"
          },
          "scenes": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ScenesType"
          },
          "weather": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.WeatherType"
          },
          "isPerformance": {
            "type": "boolean",
            "description": "是否计入绩效：true是，false否",
            "nullable": true
          },
          "needMemoir": {
            "type": "boolean",
            "description": "是否需要调查报告 true 是 false 不需要",
            "nullable": true
          },
          "proAmount": {
            "type": "number",
            "description": "预估车损",
            "format": "double",
            "nullable": true
          },
          "amount": {
            "type": "number",
            "description": "违章总金额",
            "format": "double",
            "nullable": true
          },
          "punishment": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.PunishmentType"
          },
          "attachs": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "附件集合",
            "nullable": true
          },
          "memoir": {
            "type": "integer",
            "description": "附件 调查报告数量",
            "format": "int32"
          },
          "damageFee": {
            "type": "number",
            "description": "承担车损费",
            "format": "double",
            "nullable": true
          },
          "incomeAmount": {
            "type": "number",
            "description": "收入",
            "format": "double",
            "nullable": true
          },
          "realDamageFee": {
            "type": "number",
            "description": "实际承担车损费",
            "format": "double",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "获取某一区域事故详情列表 详情"
      },
      "Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsInPut": {
        "type": "object",
        "properties": {
          "queryWriteDb": {
            "type": "boolean"
          },
          "maxResultCount": {
            "type": "integer",
            "format": "int32"
          },
          "skipCount": {
            "type": "integer",
            "format": "int32"
          },
          "accidentId": {
            "type": "string",
            "description": "事故编号",
            "nullable": true
          },
          "startDate": {
            "type": "string",
            "description": "事故日期 开始",
            "format": "date-time",
            "nullable": true
          },
          "endDate": {
            "type": "string",
            "description": "事故日期 结束",
            "format": "date-time",
            "nullable": true
          },
          "jgAccidentType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.JgAccidentType"
          },
          "jgDutyType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.JgDutyType"
          },
          "jgDutyTypes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.JgDutyType"
            },
            "description": "责任划分(事故责任)：1全责、2主责、3同责、4次责、5无责、6责任未定",
            "nullable": true
          },
          "impactType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ImpactType"
          },
          "scenes": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ScenesType"
          },
          "isPerformance": {
            "type": "boolean",
            "description": "是否计入绩效：true是，false否",
            "nullable": true
          },
          "punishment": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.PunishmentType"
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "groupIds": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "组别ID",
            "nullable": true
          },
          "isInclude": {
            "type": "boolean",
            "description": "是否包含传入的组别"
          },
          "driverNo": {
            "type": "string",
            "description": "司机工号",
            "nullable": true
          },
          "cities": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "城市",
            "nullable": true
          },
          "accountId": {
            "type": "string",
            "description": "政企编号",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "获取某一区域事故详情列表 输入"
      },
      "Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentSummaryDto": {
        "type": "object",
        "properties": {
          "total": {
            "type": "integer",
            "description": "合计",
            "format": "int32"
          },
          "zrQz": {
            "type": "integer",
            "description": "全责",
            "format": "int32"
          },
          "zrZz": {
            "type": "integer",
            "description": "主责",
            "format": "int32"
          },
          "zrTz": {
            "type": "integer",
            "description": "同责",
            "format": "int32"
          },
          "zrCz": {
            "type": "integer",
            "description": "次责",
            "format": "int32"
          },
          "zrWz": {
            "type": "integer",
            "description": "无责",
            "format": "int32"
          },
          "zrwd": {
            "type": "integer",
            "description": "未定",
            "format": "int32"
          },
          "ywLd": {
            "type": "integer",
            "description": "零单",
            "format": "int32"
          },
          "ywCb": {
            "type": "integer",
            "description": "长包",
            "format": "int32"
          },
          "ywZc": {
            "type": "integer",
            "description": "专车",
            "format": "int32"
          },
          "sjrssg": {
            "type": "integer",
            "description": "涉及人伤事故",
            "format": "int32"
          },
          "cfWxz": {
            "type": "integer",
            "description": "处罚 未选择 1",
            "format": "int32"
          },
          "cfSmjg": {
            "type": "integer",
            "description": "处罚 书面警告 2",
            "format": "int32"
          },
          "cfXg": {
            "type": "integer",
            "description": "处罚 小过 3",
            "format": "int32"
          },
          "cfDg": {
            "type": "integer",
            "description": "处罚 大过 4",
            "format": "int32"
          },
          "cfKc": {
            "type": "integer",
            "description": "处罚 开除 5",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": "列表明细集合"
      },
      "Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentSummaryInPut": {
        "type": "object",
        "properties": {
          "queryWriteDb": {
            "type": "boolean"
          },
          "startDate": {
            "type": "string",
            "description": "开始时间",
            "format": "date-time",
            "nullable": true
          },
          "endDate": {
            "type": "string",
            "description": "结束时间",
            "format": "date-time",
            "nullable": true
          },
          "groupIds": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "组别ID",
            "nullable": true
          },
          "isInclude": {
            "type": "boolean",
            "description": "是否包含传入的组别"
          }
        },
        "additionalProperties": false,
        "description": "获取驾管 时间 区域 汇总 列表 输入"
      },
      "Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgDriverDto": {
        "type": "object",
        "properties": {
          "driverId": {
            "type": "string",
            "description": "司机编号",
            "nullable": true
          },
          "driverType": {
            "type": "string",
            "description": "司机类型",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "驾管获取事故信息 传入 司机信息"
      },
      "Corp.AfterSale.Application.Contracts.ForDriver.Dto.JgAccidentInfoInPut": {
        "type": "object",
        "properties": {
          "accidentId": {
            "type": "string",
            "description": "事故Id",
            "nullable": true
          },
          "jgAccidentType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.JgAccidentType"
          },
          "jgDutyType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.JgDutyType"
          },
          "impactType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ImpactType"
          },
          "scenes": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ScenesType"
          },
          "weather": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.WeatherType"
          },
          "accidentTime": {
            "type": "string",
            "description": "驾管事故时间(事故具体时间)",
            "format": "date-time",
            "nullable": true
          },
          "isHavePassenger": {
            "type": "boolean",
            "description": "是否有乘客",
            "nullable": true
          },
          "isPerformance": {
            "type": "boolean",
            "description": "是否计入绩效：true是，false否",
            "nullable": true
          },
          "punishment": {
            "type": "integer",
            "description": "行政处罚决定：1未选择、2书面警告、3小过、4大过、5开除、6无需处罚",
            "format": "int32",
            "nullable": true
          },
          "jgDetail": {
            "type": "string",
            "description": "驾管事故详情",
            "nullable": true
          },
          "jgRemark": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetJgAccidentDetailRemarksDto"
            },
            "description": "驾管备注",
            "nullable": true
          },
          "needMemoir": {
            "type": "boolean",
            "description": "是否需要调查报告 true是 false 不需要"
          },
          "attachs": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "附件地址集合",
            "nullable": true
          },
          "oprNo": {
            "type": "string",
            "description": "操作人编号",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Job.Dto.ApplyLicenseAutoVerifyInput": {
        "type": "object",
        "properties": {
          "applyIds": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32"
            },
            "description": "工单Id集合，忽略其它条件",
            "nullable": true
          },
          "fromDate": {
            "type": "string",
            "description": "指定开始时间",
            "format": "date-time",
            "nullable": true
          },
          "toDate": {
            "type": "string",
            "description": "指定结束时间",
            "format": "date-time",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Job.Dto.DueMaintenanceEmailReminderInput": {
        "type": "object",
        "properties": {
          "queryWriteDb": {
            "type": "boolean"
          },
          "carNos": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "车牌号",
            "nullable": true
          },
          "orderNos": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "长包订单号",
            "nullable": true
          },
          "customerEmail": {
            "type": "string",
            "description": "测试用邮件接收人",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Job.Dto.RefreshAfterSaleCarNoInfoInPut": {
        "type": "object",
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Job.Dto.SendMailInput": {
        "type": "object",
        "properties": {
          "templateId": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "to": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "cc": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Job.Dto.SendMailInputSecond": {
        "type": "object",
        "properties": {
          "templateId": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "emailTo": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "emailCc": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "emailSubject": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "content": {
            "type": "string",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Job.Dto.SendRepairApplyLicenseAuditEmailInPut": {
        "type": "object",
        "properties": {
          "customerEmail": {
            "type": "string",
            "description": "测试用邮件接收人",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "超过24小时凭证未审核邮件通知-入参"
      },
      "Corp.AfterSale.Application.Contracts.Job.Dto.SendRepairOrderNotifyMessagesInput": {
        "type": "object",
        "properties": {
          "minute": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "repairId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "phoneNo": {
            "type": "string",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Job.Dto.SyncMaintainAlarmInput": {
        "type": "object",
        "properties": {
          "carNos": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AfterSaleCancelInPut": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "保养记录Id或者工单凭证Id",
            "nullable": true
          },
          "cancelReason": {
            "type": "string",
            "description": "取消原因",
            "nullable": true
          },
          "userId": {
            "type": "string",
            "description": "用户ID 密文 非cookie来源时使用",
            "nullable": true
          },
          "userInfoSourceType": {
            "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
          },
          "openId": {
            "type": "string",
            "description": "微信OpenId",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ApplyMaintenanceInPut": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "维保单主键",
            "format": "int32",
            "nullable": true
          },
          "repairShopName": {
            "type": "string",
            "description": "修理厂",
            "nullable": true
          },
          "repairShopType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairShopType"
          },
          "maintenanceTypes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.MaintenanceType"
            },
            "description": "预约项目 1维修 2保养",
            "nullable": true
          },
          "bookTime": {
            "type": "string",
            "description": "预约时间 精确到分",
            "format": "date-time"
          },
          "remark": {
            "type": "string",
            "description": "备注",
            "nullable": true
          },
          "userName": {
            "type": "string",
            "description": "客户姓名/用户姓名",
            "nullable": true
          },
          "userPhone": {
            "type": "string",
            "description": "客户联系方式/用户联系方式",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "inKm": {
            "type": "integer",
            "description": "进厂公里数",
            "format": "int32"
          },
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ApplyMaintenanceItemDto"
            },
            "description": "维修项明细",
            "nullable": true
          },
          "skipVerifiedWarn": {
            "type": "boolean",
            "description": "拒绝建议，转入人工审核"
          },
          "inKmOutOfRange": {
            "type": "boolean",
            "description": "进厂公里数超出范围"
          },
          "dashboardKmImageUrl": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
          },
          "driverNo": {
            "type": "string",
            "description": "司机工号",
            "nullable": true
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否维修",
            "readOnly": true
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否保养",
            "readOnly": true
          },
          "userId": {
            "type": "string",
            "description": "用户ID 密文 非cookie来源时使用",
            "nullable": true
          },
          "userInfoSourceType": {
            "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
          },
          "openId": {
            "type": "string",
            "description": "微信OpenId",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ApplyMaintenanceItemDto": {
        "type": "object",
        "properties": {
          "itemId": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "itemName": {
            "type": "string",
            "description": "维保项目名称",
            "nullable": true
          },
          "num": {
            "type": "integer",
            "description": "数量",
            "format": "int32"
          },
          "price": {
            "type": "number",
            "description": "预估单价",
            "format": "double"
          }
        },
        "additionalProperties": false,
        "description": "维修项明细"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ApplyMaintenanceOutPut": {
        "type": "object",
        "properties": {
          "currentResult": {
            "type": "integer",
            "description": "本次请求保存结果，为申请工单主键",
            "format": "int32"
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否允许发起本次维保申请 false 不允许 true 允许",
            "readOnly": true
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否允许发起本次维修申请 false 不允许 true 允许",
            "readOnly": true
          },
          "checkItems": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.ApplyMaintenanceCheckItemDto"
            },
            "description": "集合验证结果",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.AssignCustomerServiceInput": {
        "type": "object",
        "properties": {
          "applyIds": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32"
            },
            "description": "工单Id集合",
            "nullable": true
          },
          "customerServiceCode": {
            "type": "string",
            "description": "客服工号",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.CancelReserveInPut": {
        "type": "object",
        "properties": {
          "repairId": {
            "type": "string",
            "description": "维保单号",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "考拉预约取消入参"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.CustomerServiceDto": {
        "type": "object",
        "properties": {
          "customerServiceCode": {
            "type": "string",
            "description": "客服工号",
            "nullable": true
          },
          "customerServiceName": {
            "type": "string",
            "description": "客服姓名",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.CustomerServiceListInput": {
        "type": "object",
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ExportExcelBaseDto": {
        "type": "object",
        "properties": {
          "fileUrl": {
            "type": "string",
            "description": "文件url",
            "nullable": true
          },
          "fileName": {
            "type": "string",
            "description": "预下载文件名称",
            "nullable": true
          },
          "mediaType": {
            "type": "string",
            "description": "MediaTypeNames 常量名 主要是常量的属性名 不是常量属性值 可以使用 nameof(MediaTypeNames.Excel2007) 得到",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAccessLogsDto": {
        "type": "object",
        "properties": {
          "keyNo": {
            "type": "string",
            "description": "业务关键字",
            "nullable": true
          },
          "page": {
            "type": "string",
            "description": "请求页面",
            "nullable": true
          },
          "action": {
            "type": "string",
            "description": "请求接口",
            "nullable": true
          },
          "request": {
            "type": "string",
            "description": "请求实体",
            "nullable": true
          },
          "response": {
            "type": "string",
            "description": "响应实体",
            "nullable": true
          },
          "error": {
            "type": "string",
            "description": "错误信息",
            "nullable": true
          },
          "createTime": {
            "type": "string",
            "description": "新增时间",
            "format": "date-time",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "日志详情"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAccidentsForH5Dto": {
        "type": "object",
        "properties": {
          "accidentId": {
            "type": "string",
            "description": "事故编号",
            "nullable": true
          },
          "logon": {
            "type": "string",
            "description": "政企帐号",
            "nullable": true
          },
          "acctName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "事故订单",
            "nullable": true
          },
          "accidentTime": {
            "type": "string",
            "description": "事故时间",
            "format": "date-time",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "accidentLocation": {
            "type": "string",
            "description": "事故地点",
            "nullable": true
          },
          "accidentName": {
            "type": "string",
            "description": "事故联系人姓名",
            "nullable": true
          },
          "accidentPhone": {
            "type": "string",
            "description": "事故联系人电话",
            "nullable": true
          },
          "statusFlag": {
            "type": "integer",
            "description": "主状态 1 已完成 0 处理中",
            "format": "int32"
          },
          "materialStatus": {
            "type": "integer",
            "description": "资料收集状态 0 缺少资料,待凭证上传 1 资料齐全,凭证已上传",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAccidentsForH5OutPut": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAccidentsForH5Dto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAfterSaleIndexInfoOutPut": {
        "type": "object",
        "properties": {
          "unMaintained": {
            "type": "integer",
            "description": "已预约未保养车辆数",
            "format": "int32",
            "nullable": true
          },
          "pendingAccident": {
            "type": "integer",
            "description": "待处理事故数",
            "format": "int32",
            "nullable": true
          },
          "maintenance": {
            "type": "integer",
            "description": "需保养车辆数",
            "format": "int32",
            "nullable": true
          },
          "pendingViolations": {
            "type": "integer",
            "description": "待处理违章数",
            "format": "int32",
            "nullable": true
          },
          "annualInspection": {
            "type": "integer",
            "description": "需年检车辆数",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAfterSaleRepairItemsDto": {
        "type": "object",
        "properties": {
          "itemId": {
            "type": "integer",
            "description": "维保项目Id",
            "format": "int32"
          },
          "itemName": {
            "type": "string",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAnnualInspectionCountOutPut": {
        "type": "object",
        "properties": {
          "selfDrivingSingle": {
            "type": "integer",
            "description": "政企自驾零单",
            "format": "int32",
            "nullable": true
          },
          "insteadDrivingSingle": {
            "type": "integer",
            "description": "政企代驾零单",
            "format": "int32",
            "nullable": true
          },
          "selfSubscribe": {
            "type": "integer",
            "description": "政企自驾长包",
            "format": "int32",
            "nullable": true
          },
          "insteadSubscribe": {
            "type": "integer",
            "description": "政企代驾长包",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyAccountInfoDto": {
        "type": "object",
        "properties": {
          "userId": {
            "type": "string",
            "description": "用户号",
            "nullable": true
          },
          "accountNo": {
            "type": "string",
            "description": "账户号",
            "nullable": true
          },
          "accountName": {
            "type": "string",
            "description": "账户名称",
            "nullable": true
          },
          "bankId": {
            "type": "string",
            "description": "银行编号",
            "nullable": true
          },
          "bankName": {
            "type": "string",
            "description": "银行名称",
            "nullable": true
          },
          "bankSectionId": {
            "type": "string",
            "description": "分行编号",
            "nullable": true
          },
          "bankSectionName": {
            "type": "string",
            "description": "分行名称",
            "nullable": true
          },
          "cityNo": {
            "type": "string",
            "description": "城市编号",
            "nullable": true
          },
          "cityName": {
            "type": "string",
            "description": "城市名称",
            "nullable": true
          },
          "applyAccountStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ApplyAccountStatus"
          }
        },
        "additionalProperties": false,
        "description": "获取用户售后工单账户信息-出参"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyAccountInfoOutPut": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyAccountInfoDto"
            },
            "description": "",
            "nullable": true
          },
          "isSaveAccountInfo": {
            "type": "boolean",
            "description": ""
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyMaintenanceInfoDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "主键",
            "format": "int32"
          },
          "repairShopType": {
            "type": "integer",
            "description": "维修厂栏位 1 4S店 2 非4S店",
            "format": "int32"
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否维修 默认 否"
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否保养 默认 否"
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "bookTime": {
            "type": "string",
            "description": "预约时间 精确到分",
            "format": "date-time"
          },
          "bookTimeTimestamp": {
            "type": "string",
            "description": "预约时间时间戳格式",
            "nullable": true,
            "readOnly": true
          },
          "repairShopName": {
            "type": "string",
            "description": "修理厂",
            "nullable": true
          },
          "verifyStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ApplyMaintenanceStatus"
          },
          "repairDetail": {
            "type": "string",
            "description": "维保明细-文字",
            "nullable": true
          },
          "remark": {
            "type": "string",
            "description": "备注",
            "nullable": true
          },
          "reason": {
            "type": "string",
            "description": "原因",
            "nullable": true
          },
          "licenseReason": {
            "type": "string",
            "description": "凭证拒审原因",
            "nullable": true
          },
          "inKm": {
            "type": "integer",
            "description": "进厂公里数",
            "format": "int32"
          },
          "details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfoDetailDto"
            },
            "description": "维修明细",
            "nullable": true
          },
          "userPhone": {
            "type": "string",
            "description": "用户手机号",
            "nullable": true
          },
          "userName": {
            "type": "string",
            "description": "用户姓名",
            "nullable": true
          },
          "driverNo": {
            "type": "string",
            "description": "司机工号",
            "nullable": true
          },
          "bxNo": {
            "type": "string",
            "description": "报销编号",
            "nullable": true
          },
          "expectedDeliveryTime": {
            "type": "string",
            "description": "预计维修完成时间",
            "nullable": true
          },
          "channelType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairChannelType"
          },
          "rescueReviewStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RescueReviewStatus"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyMaintenanceOutPut": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.GetApplyMaintenanceDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyUserInfoOutPut": {
        "type": "object",
        "properties": {
          "userId": {
            "type": "string",
            "description": "用户编号",
            "nullable": true
          },
          "saveType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.SaveTypes"
          }
        },
        "additionalProperties": false,
        "description": "获取售后工单用户信息-出参"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetEarlyApplyInfoDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "主键",
            "format": "int32"
          },
          "repairShopName": {
            "type": "string",
            "description": "修理厂名称",
            "nullable": true
          },
          "repairShopType": {
            "type": "integer",
            "description": "维修厂栏位:1 4S店,2 非4S店",
            "format": "int32"
          },
          "inKm": {
            "type": "integer",
            "description": "进厂公里数",
            "format": "int32"
          },
          "maintenanceTypes": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32"
            },
            "description": "预约项目1维修2保养",
            "nullable": true,
            "readOnly": true
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否维修 默认 否"
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否保养 默认 否"
          },
          "carNo": {
            "type": "string",
            "description": "车牌",
            "nullable": true
          },
          "bookTime": {
            "type": "string",
            "description": "预约时间",
            "format": "date"
          },
          "repairDetail": {
            "type": "string",
            "description": "维修项明细",
            "nullable": true
          },
          "remark": {
            "type": "string",
            "description": "备注",
            "nullable": true
          },
          "userName": {
            "type": "string",
            "description": "客户姓名",
            "nullable": true
          },
          "userPhone": {
            "type": "string",
            "description": "用户手机号码",
            "nullable": true
          },
          "repairId": {
            "type": "string",
            "description": "维保编号",
            "nullable": true
          },
          "verifyHistories": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyHistoriesDto"
            },
            "description": "审核历史",
            "nullable": true
          },
          "licenseInfo": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetExpenseReimbursementLicenseInfoDto"
          },
          "details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfoDetailDto"
            },
            "description": "维修明细",
            "nullable": true
          },
          "dashBoardInKmImageUrl": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
          },
          "carPrice": {
            "type": "number",
            "description": "车辆官价",
            "format": "double",
            "nullable": true
          },
          "notMatchTypes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairAttachType"
            },
            "description": "不符合报销材料类型",
            "nullable": true
          },
          "fpRecordReason": {
            "type": "string",
            "description": "发票未自动审核通过原因",
            "nullable": true
          },
          "transferAccountsRecordReason": {
            "type": "string",
            "description": "转账凭证未自动审核通过原因",
            "nullable": true
          },
          "maintenanceSiteRecord": {
            "type": "string",
            "description": "维修现场（带车牌）未自动审核通过原因",
            "nullable": true
          },
          "extraProperties": {
            "type": "object",
            "additionalProperties": {
              "nullable": true
            },
            "description": "",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": "获取维保详细出参"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetEarlyApplyInfosDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "repairId": {
            "type": "string",
            "description": "维保编号",
            "nullable": true
          },
          "userPhone": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "userName": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "repairShopName": {
            "type": "string",
            "description": "修理厂名称",
            "nullable": true
          },
          "maintenanceType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.MaintenanceType"
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否维修 默认 否"
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否保养 默认 否"
          },
          "maintenanceTypeDesc": {
            "type": "string",
            "description": "预约项目描述",
            "nullable": true,
            "readOnly": true
          },
          "bookTime": {
            "type": "string",
            "description": "预约时间 精确到分",
            "format": "date-time"
          },
          "verifyStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.VerifyStatusFlag"
          },
          "verifyStatusDesc": {
            "type": "string",
            "description": "工单状态描述",
            "nullable": true,
            "readOnly": true
          },
          "licenseVerifyStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.LicenseVerifyStatusFlag"
          },
          "licenseVerifyStatusDesc": {
            "type": "string",
            "description": "凭证状态描述",
            "nullable": true,
            "readOnly": true
          },
          "bxNo": {
            "type": "string",
            "description": "报销编号",
            "nullable": true
          },
          "financeStatusFlag": {
            "type": "string",
            "description": "打款状态",
            "nullable": true
          },
          "auditStatusFlag": {
            "type": "string",
            "description": "审核状态",
            "nullable": true
          },
          "statusFlag": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "allowReimburse": {
            "type": "boolean",
            "description": "是否允许报销",
            "readOnly": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "bizTypeDesc": {
            "type": "string",
            "description": "业务类型描述",
            "nullable": true,
            "readOnly": true
          },
          "creationUserNo": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "channelType": {
            "type": "integer",
            "description": "渠道",
            "format": "int32",
            "nullable": true
          },
          "channelTypeDesc": {
            "type": "string",
            "description": "渠道描述",
            "nullable": true,
            "readOnly": true
          },
          "details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfoDetailDto"
            },
            "description": "维修明细",
            "nullable": true
          },
          "compensations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.RepairCompensationDto"
            },
            "description": "补偿项细项",
            "nullable": true
          },
          "totalAmount": {
            "type": "number",
            "description": "总计费用",
            "format": "double",
            "nullable": true,
            "readOnly": true
          },
          "extraProperties": {
            "type": "object",
            "additionalProperties": {
              "nullable": true
            },
            "nullable": true,
            "readOnly": true
          },
          "customerServiceCode": {
            "type": "string",
            "description": "客服工号",
            "nullable": true
          },
          "customerServiceName": {
            "type": "string",
            "description": "客服姓名",
            "nullable": true
          },
          "repeatApplyAuditState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairAuditState"
          },
          "verifyUserDesc": {
            "type": "string",
            "description": "审核人描述",
            "nullable": true
          },
          "licenseId": {
            "type": "integer",
            "description": "凭证Id",
            "format": "int32"
          },
          "lastVerifyType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.LicenseLastVerifyType"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetExpenseReimbursementLicenseInfoDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "accountName": {
            "type": "string",
            "description": "账户名称",
            "nullable": true
          },
          "accountNo": {
            "type": "string",
            "description": "账户Id",
            "nullable": true
          },
          "provinceNo": {
            "type": "string",
            "description": "省份Id",
            "nullable": true
          },
          "cityNo": {
            "type": "string",
            "description": "城市Id",
            "nullable": true
          },
          "bankId": {
            "type": "string",
            "description": "银行Id",
            "nullable": true
          },
          "bankSectionId": {
            "type": "string",
            "description": "分行Id",
            "nullable": true
          },
          "expressNo": {
            "type": "string",
            "description": "快递单号",
            "nullable": true
          },
          "verifyStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.VerifyStatus"
          },
          "autoVerifyId": {
            "type": "string",
            "description": "自动审核批次",
            "format": "uuid",
            "nullable": true
          },
          "lastVerifyType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.LicenseLastVerifyType"
          },
          "repairDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "维修单据 至少一张",
            "nullable": true
          },
          "repairImageUrl": {
            "type": "string",
            "description": "默认维修单据首张图片",
            "nullable": true,
            "readOnly": true
          },
          "invoiceDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "发票 至少一张",
            "nullable": true
          },
          "invoiceImageUrl": {
            "type": "string",
            "description": "默认发票首张图片",
            "nullable": true,
            "readOnly": true
          },
          "verifyHistories": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyHistoriesDto"
            },
            "description": "审核历史",
            "nullable": true
          },
          "kmDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "仪表盘公里数\n至少一张",
            "nullable": true
          },
          "transferAccountsDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "转账凭证\n至少一张",
            "nullable": true
          },
          "maintenanceSiteSparePartsDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "维修现场（带零件）",
            "nullable": true
          },
          "maintenanceSiteSpareCarNoDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "维修现场（带车牌）",
            "nullable": true
          },
          "stampReceiptDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "盖章收据",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "工单审核详情"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetFieldsDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "主键",
            "format": "int32",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "姓名",
            "nullable": true
          },
          "desc": {
            "type": "string",
            "description": "描述",
            "nullable": true
          },
          "table": {
            "type": "string",
            "description": "表名",
            "nullable": true
          },
          "enumId": {
            "type": "integer",
            "description": "字段枚举中英对照",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetIndexAccidentsDto": {
        "type": "object",
        "properties": {
          "cycle": {
            "type": "string",
            "description": "事故周期",
            "nullable": true
          },
          "injuredTotalNumber": {
            "type": "integer",
            "description": "总人伤",
            "format": "int32"
          },
          "nonPersonalInjuryTotalNumber": {
            "type": "integer",
            "description": "总非人伤",
            "format": "int32"
          },
          "injuredNumber": {
            "type": "integer",
            "description": "人伤结案量",
            "format": "int32"
          },
          "injuredRate": {
            "type": "number",
            "description": "人伤结案率",
            "format": "double"
          },
          "nonPersonalInjuryNumber": {
            "type": "integer",
            "description": "非人伤结案量",
            "format": "int32"
          },
          "nonPersonalInjuryRate": {
            "type": "number",
            "description": "非人伤结案率",
            "format": "double"
          }
        },
        "additionalProperties": false,
        "description": "首页 事故数据 出参集合模型"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetIndexAccidentsOutPut": {
        "type": "object",
        "properties": {
          "unHandleTotalNumber": {
            "type": "integer",
            "description": "总人伤",
            "format": "int32"
          },
          "indexAccidents": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetIndexAccidentsDto"
            },
            "description": "事故数据集合",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "首页 事故数据 出参模型"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetIndexMaintainsDto": {
        "type": "object",
        "properties": {
          "cycle": {
            "type": "string",
            "description": "保养周期",
            "nullable": true
          },
          "actualMaintenanceAmount": {
            "type": "integer",
            "description": "实际维保量 考拉已完成+非考拉已预约已保养（政企客户在考拉系统中实际维保量，含客户预约和非客户预约。）",
            "format": "int32"
          },
          "manualBooking": {
            "type": "integer",
            "description": "人工预约量 考拉预约量+非考拉预约量 （仅针对人工预约的统计）",
            "format": "int32"
          },
          "actualManualMaintenanceAmount": {
            "type": "integer",
            "description": "人工实际保养量 考拉预约后完成量（仅针对人工预约的统计）",
            "format": "int32"
          },
          "unMaintenanceAmount": {
            "type": "integer",
            "description": "未保养量 周期内已取消维保订单数量",
            "format": "int32"
          },
          "reserveCount": {
            "type": "integer",
            "description": "周期内预约量",
            "format": "int32"
          },
          "maintenanceRate": {
            "type": "number",
            "description": "预约保养率 周期内实际保养量(ActualMaintenanceAmount)/ 周期内预约量(ReserveCount)",
            "format": "double"
          }
        },
        "additionalProperties": false,
        "description": "首页 维保数据 出参列表模型"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetJgAccidentDetailRemarksDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "日志主键ID",
            "format": "int32"
          },
          "logContent": {
            "type": "string",
            "description": "日志内容",
            "nullable": true
          },
          "isDeleted": {
            "type": "boolean",
            "description": "删除区分 false 正常 true 删除"
          },
          "creationTime": {
            "type": "string",
            "description": "创建时间",
            "format": "date-time",
            "nullable": true
          },
          "lastModificationTime": {
            "type": "string",
            "description": "更新时间",
            "format": "date-time",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetJgTicketDetailsDto": {
        "type": "object",
        "properties": {
          "ticketId": {
            "type": "integer",
            "description": "违章ID",
            "format": "int32",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "长包系统订单编号",
            "nullable": true
          },
          "ticketOrderId": {
            "type": "string",
            "description": "自驾违章订单号",
            "nullable": true
          },
          "driverNo": {
            "type": "string",
            "description": "司机工号",
            "nullable": true
          },
          "driverName": {
            "type": "string",
            "description": "司机姓名",
            "nullable": true
          },
          "groupId": {
            "type": "integer",
            "description": "区域ID",
            "format": "int32"
          },
          "groupName": {
            "type": "string",
            "description": "区域名称",
            "nullable": true
          },
          "supervisorName": {
            "type": "string",
            "description": "直属主管",
            "nullable": true
          },
          "areaManager": {
            "type": "string",
            "description": "区域经理",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "ticketTime": {
            "type": "string",
            "description": "违章时间",
            "format": "date-time",
            "nullable": true
          },
          "ticketContent": {
            "type": "string",
            "description": "违章内容",
            "nullable": true
          },
          "ticketCity": {
            "type": "string",
            "description": "违章城市",
            "nullable": true
          },
          "ticketRoad": {
            "type": "string",
            "description": "违章路段",
            "nullable": true
          },
          "ticketAmount": {
            "type": "number",
            "description": "违章罚金",
            "format": "double",
            "nullable": true
          },
          "ticketPoint": {
            "type": "integer",
            "description": "违章扣分",
            "format": "int32",
            "nullable": true
          },
          "tickType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.TickType"
          },
          "ticketDjStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.TicketDjStatus"
          },
          "ticketDjStatusName": {
            "type": "string",
            "description": "违章处理状态名 1待处理,2公司处理，3审核中，4自缴完成，5代缴未完成",
            "nullable": true
          },
          "comments": {
            "type": "string",
            "description": "备注",
            "nullable": true
          },
          "bxSerialNumber": {
            "type": "string",
            "description": "报销流水号",
            "nullable": true
          },
          "pickPrice": {
            "type": "number",
            "description": "已付金额",
            "format": "double"
          },
          "arrearsPrice": {
            "type": "number",
            "description": "未付金额",
            "format": "double"
          },
          "ticketProcessType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.TicketProcessType"
          }
        },
        "additionalProperties": false,
        "description": "加官 违章列表"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetLicenseInfoDto": {
        "type": "object",
        "properties": {
          "accountName": {
            "type": "string",
            "description": "账户名称",
            "nullable": true
          },
          "accountNo": {
            "type": "string",
            "description": "账户号",
            "nullable": true
          },
          "bankId": {
            "type": "string",
            "description": "银行编号",
            "nullable": true
          },
          "bankName": {
            "type": "string",
            "description": "银行名",
            "nullable": true
          },
          "provinceNo": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "province": {
            "type": "string",
            "description": "省份",
            "nullable": true
          },
          "cityNo": {
            "type": "string",
            "description": "城市ID",
            "nullable": true
          },
          "city": {
            "type": "string",
            "description": "城市",
            "nullable": true
          },
          "bankSectionId": {
            "type": "string",
            "description": "分行编号",
            "nullable": true
          },
          "bankSectionName": {
            "type": "string",
            "description": "分行名",
            "nullable": true
          },
          "expressNo": {
            "type": "string",
            "description": "快递单号",
            "nullable": true
          },
          "repairDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "维修单据 至少一张",
            "nullable": true
          },
          "invoiceDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "发票 至少一张",
            "nullable": true
          },
          "kmDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "仪表盘公里数\n至少一张",
            "nullable": true
          },
          "transferAccountsDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "转账凭证\n至少一张",
            "nullable": true
          },
          "maintenanceSiteSparePartsDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "维修现场（带零件）",
            "nullable": true
          },
          "maintenanceSiteSpareCarNoDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "维修现场（带车牌）",
            "nullable": true
          },
          "stampReceiptDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "盖章收据",
            "nullable": true
          },
          "ehiCompanyAddress": {
            "type": "string",
            "description": "ehi公司地址",
            "nullable": true
          },
          "userName": {
            "type": "string",
            "description": "客户姓名",
            "nullable": true
          },
          "phone": {
            "type": "string",
            "description": "客户电话",
            "nullable": true
          },
          "reason": {
            "type": "string",
            "description": "原因",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintainAlarmsDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "需保养记录ID",
            "format": "int32",
            "nullable": true
          },
          "startRemindDate": {
            "type": "string",
            "description": "开始预警时间",
            "format": "date-time",
            "nullable": true,
            "readOnly": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌",
            "nullable": true
          },
          "latestMaintainDate": {
            "type": "string",
            "description": "最近保养时间",
            "format": "date-time",
            "nullable": true
          },
          "latestMaintainMileage": {
            "type": "number",
            "description": "最近保养里程",
            "format": "double",
            "nullable": true
          },
          "currentMileage": {
            "type": "number",
            "description": "当前公里数",
            "format": "double",
            "nullable": true
          },
          "currentTime": {
            "type": "string",
            "description": "人工维护最近保养时间",
            "format": "date-time",
            "nullable": true
          },
          "afterRepairMileage": {
            "type": "number",
            "description": "售后保养里程数",
            "format": "double",
            "nullable": true
          },
          "afterRepairTime": {
            "type": "string",
            "description": "售后保养时间",
            "format": "date-time",
            "nullable": true
          },
          "statusFlag": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.StatusFlag"
          },
          "comments": {
            "type": "string",
            "description": "备注",
            "nullable": true
          },
          "ecCarId": {
            "type": "integer",
            "description": "",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintenanceInfosDto": {
        "type": "object",
        "properties": {
          "orderNo": {
            "type": "string",
            "description": "长包订单编号",
            "nullable": true
          },
          "selfOrderNo": {
            "type": "string",
            "description": "自驾订单编号",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "carTypeId": {
            "type": "integer",
            "description": "车型编号",
            "format": "int32",
            "nullable": true
          },
          "latestMaintainDate": {
            "type": "string",
            "description": "上次维保时间",
            "format": "date-time",
            "nullable": true
          },
          "latestMaintainMileage": {
            "type": "number",
            "description": "上次保养里程",
            "format": "double",
            "nullable": true
          },
          "currentMileage": {
            "type": "number",
            "description": "当前里程",
            "format": "double",
            "nullable": true
          },
          "currentTime": {
            "type": "string",
            "description": "业务手工维护的上次保养时间",
            "format": "date-time",
            "nullable": true
          },
          "afterRepairTime": {
            "type": "string",
            "description": "售后系统维保预约工单最新出厂时间",
            "format": "date-time",
            "nullable": true
          },
          "afterRepairMileage": {
            "type": "number",
            "description": "售后系统维保预约工单最新出厂里程数",
            "format": "double",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintenanceRecordByCarLicenseInput": {
        "type": "object",
        "properties": {
          "queryWriteDb": {
            "type": "boolean"
          },
          "carNos": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "车牌号",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOperationLogsDto": {
        "type": "object",
        "properties": {
          "creationUserNo": {
            "type": "string",
            "description": "创建人",
            "nullable": true
          },
          "creationUserName": {
            "type": "string",
            "description": "创建人姓名",
            "nullable": true
          },
          "creationTime": {
            "type": "string",
            "description": "创建实际",
            "format": "date-time",
            "nullable": true
          },
          "desc": {
            "type": "string",
            "description": "字段描述",
            "nullable": true
          },
          "oldValue": {
            "type": "string",
            "description": "新值",
            "nullable": true
          },
          "newValueDesc": {
            "type": "string",
            "description": "枚举描述",
            "nullable": true
          },
          "oldValueDesc": {
            "type": "string",
            "description": "枚举描述",
            "nullable": true
          },
          "newValue": {
            "type": "string",
            "description": "旧值",
            "nullable": true
          },
          "handleId": {
            "type": "string",
            "description": "操作批次",
            "nullable": true
          },
          "fieldKey": {
            "type": "string",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "GetOperationLogsDto"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOrderDetailLinkOutput": {
        "type": "object",
        "properties": {
          "url": {
            "type": "string",
            "description": "跳转链接",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "订单详情链接输出"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairDetailInfosByRepairIdDto": {
        "type": "object",
        "properties": {
          "itemName": {
            "type": "string",
            "description": "维保明细介绍",
            "nullable": true
          },
          "itemAmount": {
            "type": "string",
            "description": "维保项金额",
            "nullable": true
          },
          "amount": {
            "type": "number",
            "description": "维保项金额",
            "format": "double"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairDetailInfosByRepairIdOutPut": {
        "type": "object",
        "properties": {
          "acctName": {
            "type": "string",
            "description": "企业名称",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "reimbursementNo": {
            "type": "string",
            "description": "报销编号",
            "nullable": true
          },
          "inTime": {
            "type": "string",
            "description": "进厂日期",
            "format": "date-time"
          },
          "amount": {
            "type": "number",
            "description": "总金额",
            "format": "double",
            "readOnly": true
          },
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairDetailInfosByRepairIdDto"
            },
            "description": "维保明细",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfoDetailDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "repairId": {
            "type": "string",
            "description": "维修单号",
            "nullable": true
          },
          "isApproval": {
            "type": "boolean",
            "description": "是否审核"
          },
          "isOutsite": {
            "type": "boolean",
            "description": "是否托外：0-否，1-是 ,"
          },
          "itemCount": {
            "type": "integer",
            "description": "数量",
            "format": "int32"
          },
          "itemName": {
            "type": "string",
            "description": "项目名称",
            "nullable": true
          },
          "maintainStaff": {
            "type": "integer",
            "description": "维修员工工号",
            "format": "int32"
          },
          "materialsId": {
            "type": "integer",
            "description": "材料Id ,",
            "format": "int32"
          },
          "outsiteAmount": {
            "type": "number",
            "description": "托外金额 ,",
            "format": "double"
          },
          "outsiteId": {
            "type": "string",
            "description": "托外商id ,",
            "nullable": true
          },
          "outsiteType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.OutsiteType"
          },
          "priceMaterial": {
            "type": "number",
            "description": "材料费 ,",
            "format": "double"
          },
          "priceService": {
            "type": "number",
            "description": "服务费 ,",
            "format": "double"
          },
          "qualityStatus": {
            "type": "boolean",
            "description": "质检状态：0-不通过，1-通过 ,"
          },
          "qualityTestStaff": {
            "type": "integer",
            "description": "质检人工号 ,",
            "format": "int32"
          },
          "serviceSubItemId": {
            "type": "integer",
            "description": "类别Id ,",
            "format": "int32",
            "nullable": true
          },
          "serviceTypeName": {
            "type": "string",
            "description": "类别名称",
            "nullable": true
          },
          "oprNo": {
            "type": "string",
            "description": "操作人",
            "nullable": true
          },
          "notPassReason": {
            "type": "string",
            "description": "未通过原因",
            "nullable": true
          },
          "notPassReasons": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.NotPassReasonFlag"
            },
            "description": "未通过原因",
            "nullable": true
          },
          "noHasInvoiceDoc": {
            "type": "boolean",
            "description": "是否有发票"
          },
          "isFeeConfirmed": {
            "type": "boolean",
            "description": "费用待确认"
          },
          "invoiceFiles": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.Infrastructure.QueryModel.NameValueDto`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
            },
            "description": "发票附件集合",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "维修明细"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfoForWxDto": {
        "type": "object",
        "properties": {
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否维修 true 是 false 否"
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否保养 true 是 false 否"
          },
          "repairTime": {
            "type": "string",
            "description": "预约时间",
            "format": "date-time"
          },
          "repairContent": {
            "type": "string",
            "description": "维保备注",
            "nullable": true
          },
          "repairShopId": {
            "type": "string",
            "description": "维保门店Id",
            "nullable": true
          },
          "cityId": {
            "type": "string",
            "description": "城市ID",
            "nullable": true
          },
          "statusFlag": {
            "type": "string",
            "description": "--R,预约中（未接单） C,预约中（已接单） G,已登记(待预检) E,已预检(待审核) A,已审核 D,审核中 J,已拒绝 L,维修中 K,已完成 F,已取消 1 已预约(未完成),2已预约(已完成),",
            "nullable": true
          },
          "statusName": {
            "type": "string",
            "description": "状态名称",
            "nullable": true,
            "readOnly": true
          },
          "repairShopName": {
            "type": "string",
            "description": "维保门店名称",
            "nullable": true
          },
          "repairShopPhone": {
            "type": "string",
            "description": "维保门店联系方式",
            "nullable": true
          },
          "repairShopAddress": {
            "type": "string",
            "description": "维保门店地址",
            "nullable": true
          },
          "completeDateTimeEst": {
            "type": "string",
            "description": "预计维修完成时间",
            "format": "date-time",
            "nullable": true
          },
          "expectedDeliveryTime": {
            "type": "string",
            "description": "预计维修完成时间",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosByDriverNoDto": {
        "type": "object",
        "properties": {
          "repairId": {
            "type": "string",
            "description": "维修保养编号",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "inTime": {
            "type": "string",
            "description": "进厂时间/保养时间",
            "nullable": true
          },
          "amount": {
            "type": "number",
            "description": "报销金额",
            "format": "double"
          },
          "reimbursementNo": {
            "type": "string",
            "description": "当前报销编号 从未发起报销时，为空",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosByDriverNoOutPut": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosByDriverNoDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosDto": {
        "type": "object",
        "properties": {
          "statusFlag": {
            "type": "string",
            "description": "维修单状态 R,预约中（未接单） C,预约中（已接单） G,已登记(待预检) E,已预检(待审核) A,已审核 D,审核中 J,已拒绝 L,维修中 K,已完成 F,已取消",
            "nullable": true
          },
          "repairId": {
            "type": "string",
            "description": "维修单号",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "车牌/车架号",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "vinNo": {
            "type": "string",
            "description": "车架号码",
            "nullable": true
          },
          "carTypeName": {
            "type": "string",
            "description": "车型（考拉）",
            "nullable": true
          },
          "city": {
            "type": "string",
            "description": "城市",
            "nullable": true
          },
          "repairShopName": {
            "type": "string",
            "description": "修理厂",
            "nullable": true
          },
          "carInDateTime": {
            "type": "string",
            "description": "进厂时间",
            "format": "date-time",
            "nullable": true
          },
          "carOutDateTime": {
            "type": "string",
            "description": "出厂时间",
            "format": "date-time",
            "nullable": true
          },
          "bookRepairTime": {
            "type": "string",
            "description": "预约维修时间",
            "format": "date-time",
            "nullable": true
          },
          "completeDateTimeEst": {
            "type": "string",
            "description": "预约完成维修时间",
            "format": "date-time",
            "nullable": true
          },
          "carInMileage": {
            "type": "number",
            "description": "进厂公里数",
            "format": "double"
          },
          "carOutMileage": {
            "type": "number",
            "description": "出厂公里数",
            "format": "double"
          },
          "hourAmount": {
            "type": "number",
            "description": "工时费",
            "format": "double",
            "nullable": true,
            "readOnly": true
          },
          "materialAmount": {
            "type": "number",
            "description": "材料费",
            "format": "double",
            "nullable": true,
            "readOnly": true
          },
          "repairContent": {
            "type": "string",
            "description": "维修项明细",
            "nullable": true
          },
          "repairType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairFactoryType"
          },
          "acctId": {
            "type": "string",
            "description": "政企ID",
            "nullable": true
          },
          "acctName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "logOn": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "enterprisetName": {
            "type": "string",
            "description": "政企名称",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "reimbursementNo": {
            "type": "string",
            "description": "报销流水号",
            "nullable": true
          },
          "creationUserNo": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "createrName": {
            "type": "string",
            "description": "下单人",
            "nullable": true
          },
          "creationTime": {
            "type": "string",
            "description": "下单时间",
            "format": "date-time",
            "nullable": true
          },
          "wxUserId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "channelType": {
            "type": "integer",
            "description": "渠道",
            "format": "int32",
            "nullable": true
          },
          "isPostKoala": {
            "type": "boolean",
            "description": "是否已经推送考拉",
            "nullable": true
          },
          "lastModificationTime": {
            "type": "string",
            "description": "最后更新时间",
            "format": "date-time",
            "nullable": true
          },
          "lastModifyUserName": {
            "type": "string",
            "description": "最后操作人姓名",
            "nullable": true
          },
          "lastModifyUserNo": {
            "type": "string",
            "description": "最后操作工号",
            "nullable": true
          },
          "financeStatusFlag": {
            "type": "string",
            "description": "报销打款状态{ \"R\", \"等待预审\" }, { \"J\", \"预审被拒\" }, { \"O\", \"未打款\" }, { \"K\", \"已打款\" }, { \"C\", \"单据接收\" },\n{ \"N\", \"拒绝\" }",
            "nullable": true
          },
          "auditStatusFlag": {
            "type": "string",
            "description": "报销审核状态 { \"N\", \"初始\" }, { \"R\", \"待审核\" }, { \"D\", \"已审核\" }, { \"J\", \"被拒绝\" }, { \"C\", \"已取消\" }, {\n\"S\", \"待确认\" }, { \"M\", \"草稿\" }",
            "nullable": true
          },
          "applyVerifyStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.VerifyStatusFlag"
          },
          "licenseVerifyStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.LicenseVerifyStatusFlag"
          },
          "allowReimburse": {
            "type": "boolean",
            "description": "根据报销审核状态判断是否允许再次提交 未报销或者审核状态为已取消",
            "readOnly": true
          },
          "details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfoDetailDto"
            },
            "description": "维修明细",
            "nullable": true
          },
          "compensations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.RepairCompensationDto"
            },
            "description": "补偿项细项",
            "nullable": true
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否含有保养"
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否含有维修"
          },
          "coverageTypes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.CoverageType"
            },
            "description": "保障类型",
            "nullable": true
          },
          "bizTypeDesc": {
            "type": "string",
            "description": "业务类型",
            "nullable": true,
            "readOnly": true
          },
          "repairTypeDesc": {
            "type": "string",
            "description": "订单分类",
            "nullable": true,
            "readOnly": true
          },
          "coverageTypeDesc": {
            "type": "string",
            "description": "保障类型",
            "nullable": true,
            "readOnly": true
          },
          "isYellowBackground": {
            "type": "boolean",
            "description": "是否黄色背景"
          },
          "extraProperties": {
            "type": "object",
            "additionalProperties": {
              "nullable": true
            },
            "description": "",
            "nullable": true,
            "readOnly": true
          },
          "businessProperty": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Other.Enums.AccountBusinessProperty"
          },
          "repeatApplyAuditState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairAuditState"
          },
          "auditStateDesc": {
            "type": "string",
            "description": "维保单审核状态描述",
            "nullable": true,
            "readOnly": true
          },
          "reimburseReportType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ReimburseReportType"
          },
          "reimburseReportTypeDesc": {
            "type": "string",
            "description": "报销报备类型描述",
            "nullable": true,
            "readOnly": true
          },
          "customerServiceCode": {
            "type": "string",
            "description": "客服工号",
            "nullable": true
          },
          "customerServiceName": {
            "type": "string",
            "description": "客服姓名",
            "nullable": true
          },
          "rescueReviewStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RescueReviewStatus"
          },
          "rescueReviewStatusDesc": {
            "type": "string",
            "description": "救援单审核状态描述",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosForWxDto": {
        "type": "object",
        "properties": {
          "repairId": {
            "type": "string",
            "description": "预约编号",
            "nullable": true
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否维修 true 是 false 否"
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否保养 true 是 false 否"
          },
          "repairTime": {
            "type": "string",
            "description": "",
            "format": "date-time"
          },
          "shopName": {
            "type": "string",
            "description": "门店名称",
            "nullable": true
          },
          "repairType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairFactoryType"
          },
          "statusFlag": {
            "type": "string",
            "description": "--R,预约中（未接单） C,预约中（已接单） G,已登记(待预检) E,已预检(待审核) A,已审核 D,审核中 J,已拒绝 L,维修中 K,已完成 F,已取消\n1 已预约(未完成),2已预约(已完成),",
            "nullable": true
          },
          "statusName": {
            "type": "string",
            "description": "状态名称",
            "nullable": true,
            "readOnly": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosForWxOutPut": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosForWxDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairKmInfoDto": {
        "type": "object",
        "properties": {
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "latestKm": {
            "type": "integer",
            "description": "最近保养里程",
            "format": "int32"
          },
          "latestRepairTime": {
            "type": "string",
            "description": "最近保养时间",
            "format": "date-time",
            "nullable": true
          },
          "carTypeName": {
            "type": "string",
            "description": "车型名称",
            "nullable": true
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否允许保养"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetTicketGroupByBizTypeOutPut": {
        "type": "object",
        "properties": {
          "selfDrivingSingle": {
            "type": "integer",
            "description": "政企自驾零单 1",
            "format": "int32",
            "nullable": true
          },
          "insteadDrivingSingle": {
            "type": "integer",
            "description": "政企代驾零单 2",
            "format": "int32",
            "nullable": true
          },
          "selfSubscribe": {
            "type": "integer",
            "description": "政企自驾长包 3",
            "format": "int32",
            "nullable": true
          },
          "insteadSubscribe": {
            "type": "integer",
            "description": "政企代驾长包 4",
            "format": "int32",
            "nullable": true
          },
          "selfNoDriver": {
            "type": "integer",
            "description": "自驾无人租车 5",
            "format": "int32",
            "nullable": true
          },
          "insteadNoDriver": {
            "type": "integer",
            "description": "代驾无人租车 6",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetrepairInfoDto": {
        "type": "object",
        "properties": {
          "repairId": {
            "type": "string",
            "description": "维修单号",
            "nullable": true
          },
          "carInDateTime": {
            "type": "string",
            "description": "CarInDateTime",
            "format": "date",
            "nullable": true
          },
          "carOutDateTime": {
            "type": "string",
            "description": "CarOutDateTime",
            "format": "date",
            "nullable": true
          },
          "carInMileage": {
            "type": "number",
            "description": "CarInMileage",
            "format": "double",
            "nullable": true
          },
          "carOutMileage": {
            "type": "number",
            "description": "CarOutMileage",
            "format": "double",
            "nullable": true
          },
          "repairShopName": {
            "type": "string",
            "description": "修理厂名",
            "nullable": true
          },
          "repairType": {
            "type": "integer",
            "description": "类型1维修，2保养",
            "format": "int32"
          },
          "materialAmount": {
            "type": "number",
            "description": "材料费",
            "format": "double",
            "nullable": true
          },
          "expressDate": {
            "type": "string",
            "description": "快递到达时间",
            "nullable": true
          },
          "hourAmount": {
            "type": "number",
            "description": "工时费",
            "format": "double",
            "nullable": true
          },
          "reimbursementNo": {
            "type": "string",
            "description": "报销流水号",
            "nullable": true
          },
          "repairContent": {
            "type": "string",
            "description": "维修明细",
            "nullable": true
          },
          "driverNo": {
            "type": "string",
            "description": "司机工号",
            "nullable": true
          },
          "city": {
            "type": "string",
            "description": "维修厂城市",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "maintenanceTypes": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32"
            },
            "description": "预约项目",
            "nullable": true,
            "readOnly": true
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否维修 默认 否"
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否保养 默认 否"
          },
          "repairShopType": {
            "type": "integer",
            "description": "维修厂栏位 1-4S店 2-非4S店",
            "format": "int32",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "userName": {
            "type": "string",
            "description": "客户姓名",
            "nullable": true
          },
          "userPhone": {
            "type": "string",
            "description": "客户联系方式",
            "nullable": true
          },
          "expressCost": {
            "type": "number",
            "description": "快递费用",
            "format": "double"
          },
          "expressNo": {
            "type": "string",
            "description": "快递单号",
            "nullable": true
          },
          "statusFlag": {
            "type": "string",
            "description": "工单状态",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "长包订单编号",
            "nullable": true
          },
          "attachs": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "附件集合",
            "nullable": true
          },
          "details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfoDetailDto"
            },
            "description": "维修明细",
            "nullable": true
          },
          "serviceTerms": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "服务条款",
            "nullable": true
          },
          "compensations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.RepairCompensationDto"
            },
            "description": "补偿项明细",
            "nullable": true
          },
          "extraProperties": {
            "type": "object",
            "additionalProperties": {
              "nullable": true
            },
            "description": "",
            "nullable": true,
            "readOnly": true
          },
          "applyLicense": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.RepairApplyLicenseDto"
          },
          "reimburseReportType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ReimburseReportType"
          },
          "reimburseReportTypeDesc": {
            "type": "string",
            "description": "报销报备类型描述",
            "nullable": true,
            "readOnly": true
          },
          "accidentCity": {
            "type": "string",
            "description": "事故城市（维修厂或事故发生地所在城市）",
            "nullable": true
          },
          "payeeMismatchAttaches": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "打款信息不一致附件地址集合",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "非考拉 维保工单明细"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.MaintenanceRecordDto": {
        "type": "object",
        "properties": {
          "carNo": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "lastMaintenanceDate": {
            "type": "string",
            "description": "最后保养日期",
            "format": "date-time",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ModifyApplyInfoInPut": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "repairShopName": {
            "type": "string",
            "description": "修理厂名称",
            "nullable": true
          },
          "maintenanceTypes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.MaintenanceType"
            },
            "description": "预约项目 1维修 2保养",
            "nullable": true
          },
          "repairShopType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairShopType"
          },
          "bookTime": {
            "type": "string",
            "description": "",
            "format": "date-time"
          },
          "repairDetail": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "remark": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "autoVerify": {
            "type": "boolean",
            "description": "自动审核"
          },
          "details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.PushRepairInfoDto"
            },
            "description": "维修明细项",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ModifyApplyLicenseInput": {
        "type": "object",
        "properties": {
          "repairId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "applyLicense": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.RepairApplyLicenseDto"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.NotMatchTypeDto": {
        "type": "object",
        "properties": {
          "attachType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairAttachType"
          },
          "attachTypeDesc": {
            "type": "string",
            "description": "类型描述",
            "nullable": true,
            "readOnly": true
          },
          "notMatchCount": {
            "type": "integer",
            "description": "不符合次数",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReimburseMiddleResponseDto": {
        "type": "object",
        "properties": {
          "basicInfo": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseBasicInfo"
          },
          "optionInfo": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseOptionInfo"
          },
          "thirdPartInfo": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseThirdPartInfo"
          },
          "ehaiUserInfo": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseUserInfo"
          },
          "auditInfo": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseAuditInfo"
          },
          "splitInfos": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseSplitInfo"
            },
            "nullable": true
          },
          "function": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseFunction"
          },
          "files": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.OA.Dto.FileInfo"
            },
            "nullable": true
          },
          "operationInfo": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMain.OperationInfo"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.RepairRescueUrlOutPut": {
        "type": "object",
        "properties": {
          "rescueSystemUrl": {
            "type": "string",
            "description": "救援系统链接",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "获取救援系统链接出参"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReserveApplyUserInfoInPut": {
        "type": "object",
        "properties": {
          "saveType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.SaveTypes"
          },
          "userId": {
            "type": "string",
            "description": "用户ID 密文 非cookie来源时使用",
            "nullable": true
          },
          "userInfoSourceType": {
            "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
          },
          "openId": {
            "type": "string",
            "description": "微信OpenId",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "保存/更新售后工单信息-入参"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReserveMaintenanceInPut": {
        "type": "object",
        "properties": {
          "repairId": {
            "type": "string",
            "description": "维保ID",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "carInDateTime": {
            "type": "string",
            "description": "进厂时间",
            "format": "date-time"
          },
          "carOutDateTime": {
            "type": "string",
            "description": "出厂时间",
            "format": "date-time",
            "nullable": true
          },
          "carInMileage": {
            "type": "integer",
            "description": "进厂公里数",
            "format": "int32"
          },
          "carOutMileage": {
            "type": "integer",
            "description": "出厂公里数",
            "format": "int32"
          },
          "repairShopName": {
            "type": "string",
            "description": "修理厂",
            "nullable": true
          },
          "maintenanceTypes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.MaintenanceType"
            },
            "description": "预约项目 1维修 2保养",
            "nullable": true
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否维修",
            "readOnly": true
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否保养",
            "readOnly": true
          },
          "expressDate": {
            "type": "string",
            "description": "快递到达时间",
            "format": "date-time",
            "nullable": true
          },
          "repairContent": {
            "type": "string",
            "description": "维修项目明细",
            "nullable": true
          },
          "repairShopType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairShopType"
          },
          "userName": {
            "type": "string",
            "description": "客户姓名",
            "nullable": true
          },
          "userPhone": {
            "type": "string",
            "description": "客户联系方式",
            "nullable": true
          },
          "expressCost": {
            "type": "number",
            "description": "快递费用",
            "format": "double"
          },
          "expressNo": {
            "type": "string",
            "description": "快递单号",
            "nullable": true
          },
          "driverNo": {
            "type": "string",
            "description": "司机工号",
            "nullable": true
          },
          "isAllow": {
            "type": "boolean",
            "description": "验证维保记录是否审核"
          },
          "attachs": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "附件地址集合",
            "nullable": true
          },
          "details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.PushRepairInfoDto"
            },
            "description": "维修明细项",
            "nullable": true
          },
          "compensations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.RepairCompensationDto"
            },
            "description": "补偿项明细",
            "nullable": true
          },
          "isContinue": {
            "type": "boolean",
            "description": "是否生成审核流"
          },
          "applyLicense": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.RepairApplyLicenseDto"
          },
          "afterSaleRepairApplyInDb": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Entities.AfterSaleRepairApply"
          },
          "accidentCity": {
            "type": "string",
            "description": "城市",
            "nullable": true
          },
          "reimburseReportType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ReimburseReportType"
          },
          "payeeMismatchAttaches": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "打款信息不一致附件地址集合",
            "nullable": true
          },
          "repairOperationType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairOperationType"
          }
        },
        "additionalProperties": false,
        "description": "预约维保入参"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReserveRepairFromWeChatInPut": {
        "type": "object",
        "properties": {
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "customerName": {
            "type": "string",
            "description": "客户姓名",
            "nullable": true
          },
          "phone": {
            "type": "string",
            "description": "联系电话",
            "nullable": true
          },
          "cityId": {
            "type": "integer",
            "description": "城市ID",
            "format": "int32"
          },
          "cityName": {
            "type": "string",
            "description": "城市名称",
            "nullable": true
          },
          "repeatShopId": {
            "type": "integer",
            "description": "维修厂ID",
            "format": "int32"
          },
          "repeatShopName": {
            "type": "string",
            "description": "店铺名称",
            "nullable": true
          },
          "types": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairType"
            },
            "description": "类型ID 1 维修 2保养",
            "nullable": true
          },
          "reserveTime": {
            "type": "string",
            "description": "预约日期",
            "format": "date-time"
          },
          "reMark": {
            "type": "string",
            "description": "备注",
            "nullable": true
          },
          "bizType": {
            "type": "integer",
            "description": "业务类型 1 自驾 2 代驾 3 自驾长包 4 代驾长包",
            "format": "int32"
          },
          "period": {
            "type": "string",
            "description": "时段",
            "nullable": true
          },
          "isPost": {
            "type": "boolean",
            "description": "若门店信息不为空则推送",
            "readOnly": true
          },
          "userId": {
            "type": "string",
            "description": "用户ID 密文 非cookie来源时使用",
            "nullable": true
          },
          "userInfoSourceType": {
            "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
          },
          "openId": {
            "type": "string",
            "description": "微信OpenId",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.RevokeLicenseVerifyInput": {
        "type": "object",
        "properties": {
          "applyId": {
            "type": "integer",
            "description": "工单id",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.SendAccidentSmsInPut": {
        "type": "object",
        "properties": {
          "haveUrl": {
            "type": "boolean",
            "description": "是否包含h5网址链接"
          },
          "accidentId": {
            "type": "integer",
            "description": "事故编号",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.UpLoadFilesOutPut": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "批量上传文件"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.UpLoadLicenseInPut": {
        "type": "object",
        "properties": {
          "bankAccountInfoId": {
            "type": "integer",
            "description": "银行账户信息Id",
            "format": "int32"
          },
          "accountName": {
            "type": "string",
            "description": "账户名称",
            "nullable": true
          },
          "accountNo": {
            "type": "string",
            "description": "账户号",
            "nullable": true
          },
          "bankId": {
            "type": "string",
            "description": "银行编号",
            "nullable": true
          },
          "bankName": {
            "type": "string",
            "description": "银行名称",
            "nullable": true
          },
          "provinceNo": {
            "type": "integer",
            "description": "省份编号",
            "format": "int32",
            "nullable": true
          },
          "cityNo": {
            "type": "string",
            "description": "城市编号",
            "nullable": true
          },
          "cityName": {
            "type": "string",
            "description": "城市名称",
            "nullable": true
          },
          "bankSectionId": {
            "type": "string",
            "description": "分行编号",
            "nullable": true
          },
          "bankSectionName": {
            "type": "string",
            "description": "分行名称",
            "nullable": true
          },
          "expressNo": {
            "type": "string",
            "description": "快递单号",
            "nullable": true
          },
          "applyId": {
            "type": "integer",
            "description": "工单申请记录ID",
            "format": "int32"
          },
          "id": {
            "type": "integer",
            "description": "申请记录Id 0表示新增",
            "format": "int32"
          },
          "repairDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "维修单据 至少一张",
            "nullable": true
          },
          "invoiceDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "发票 至少一张",
            "nullable": true
          },
          "kmDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "仪表盘公里数",
            "nullable": true
          },
          "transferAccountsDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "转账凭证",
            "nullable": true
          },
          "maintenanceSiteSparePartsDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "维修现场（带零件）",
            "nullable": true
          },
          "maintenanceSiteSpareCarNoDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "维修现场（带车牌）",
            "nullable": true
          },
          "stampReceiptDocument": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto"
            },
            "description": "盖章收据",
            "nullable": true
          },
          "userId": {
            "type": "string",
            "nullable": true
          },
          "userInfoSourceType": {
            "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
          },
          "openId": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.UserReimburseNotMatchInfosOutput": {
        "type": "object",
        "properties": {
          "reimburseNotMatchCount": {
            "type": "integer",
            "description": "报销材料不符次数",
            "format": "int32"
          },
          "notMatchTypes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.NotMatchTypeDto"
            },
            "description": "报销材料不符类型次数",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyApplyInfoInPut": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "reason": {
            "type": "string",
            "description": "原因",
            "nullable": true
          },
          "verifyUserNo": {
            "type": "string",
            "description": "审核人",
            "nullable": true
          },
          "verifyStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.VerifyStatus"
          },
          "details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.PushRepairInfoDto"
            },
            "description": "维修明细项",
            "nullable": true
          },
          "carOutMileage": {
            "type": "integer",
            "description": "出厂公里数",
            "format": "int32",
            "nullable": true,
            "readOnly": true
          },
          "isAllow": {
            "type": "boolean",
            "description": "表示是否批准该工单审核",
            "readOnly": true
          },
          "isReject": {
            "type": "boolean",
            "description": "表示是否拒绝该工单审核",
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": "维保审核入参"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyApplyLicenseInput": {
        "type": "object",
        "properties": {
          "verifyLicenseType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairAttachType"
          },
          "name": {
            "type": "string",
            "description": "凭证名称",
            "nullable": true
          },
          "url": {
            "type": "string",
            "description": "凭证链接",
            "nullable": true
          },
          "applyId": {
            "type": "integer",
            "description": "工单Id",
            "format": "int32"
          },
          "openId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "userId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "userInfoSourceType": {
            "$ref": "#/components/schemas/Eo.Aegis.Session.UserInfoSourceType"
          }
        },
        "additionalProperties": false,
        "description": "判断上传的凭证是否正确"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyHistoriesDto": {
        "type": "object",
        "properties": {
          "verifyStatus": {
            "type": "integer",
            "description": "审核状态",
            "format": "int32"
          },
          "VerifyUserNo": {
            "type": "string",
            "description": "审核人",
            "nullable": true
          },
          "userName": {
            "type": "string",
            "description": "审核人姓名",
            "nullable": true
          },
          "remark": {
            "type": "string",
            "description": "审核备注",
            "nullable": true
          },
          "verifyTime": {
            "type": "string",
            "description": "审核时间",
            "format": "date-time"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyLicenseInPut": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "reason": {
            "type": "string",
            "description": "原因",
            "nullable": true
          },
          "verifyStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.VerifyStatus"
          },
          "oprNo": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "userPhone": {
            "type": "string",
            "description": "客户联系方式",
            "nullable": true
          },
          "notMatchTypes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairAttachType"
            },
            "description": "不符合报销材料类型",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Dto.VerifyRepairInfoInput": {
        "type": "object",
        "properties": {
          "repairId": {
            "type": "string",
            "description": "维修编号",
            "nullable": true
          },
          "repeatApplyAuditState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Verify.Enums.VerifyStatusEnum"
          },
          "verifyContent": {
            "type": "string",
            "description": "审核意见",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "工单审核入参"
      },
      "Corp.AfterSale.Application.Contracts.RepairInfo.Enums.EarlyApplyInfoQueryType": {
        "enum": [
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "description": "",
        "format": "int32"
      },
      "Corp.AfterSale.Application.Contracts.Sync.Dto.SyncRepairBxInPut": {
        "type": "object",
        "properties": {
          "bxNo": {
            "type": "string",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Sync.Dto.SyncRepairEcCarIdInPut": {
        "type": "object",
        "properties": {
          "carNos": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Application.Contracts.Sync.Dto.SyncRepairTempCarNoInput": {
        "type": "object",
        "properties": {
          "carId": {
            "type": "integer",
            "format": "int32"
          },
          "oldCarNo": {
            "type": "string",
            "nullable": true
          },
          "newCarNo": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Dto.PostAttachDto": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "文件名称",
            "nullable": true
          },
          "url": {
            "type": "string",
            "description": "文件远端地址",
            "nullable": true
          },
          "attachType": {
            "type": "integer",
            "description": "附件类别：维保(1普通附件)，事故(1现场照片，2调查报告),3维保凭证(1维修单据，2发票，3仪表盘公里数，4转账凭证，5维修现场（带零件），6维修现场（带车牌）,7盖章收据),4 H5预约工单(1仪表盘里程数)",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": "附件 模型"
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AccidentFollowState": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          7
        ],
        "type": "integer",
        "description": "事故跟进状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AfterSaleAccidentStatusFlag": {
        "enum": [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11
        ],
        "type": "integer",
        "description": "事故状态 转换关系 1 待处理(0待处理，1缺少资料，2资料更新，9退款信息) 2 处理中(参照子状态) 3 理赔中（3） 4 打款中（4） 5 已完成(5已打款) 6\n撤案(6已撤案) 7 拒赔（7） 8 诉讼中(10) 9 待上报(8) 10 已上报(12) 11 已完成(13)",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Enums.AppraisalLawsuitType": {
        "enum": [
          0,
          1,
          2
        ],
        "type": "integer",
        "description": "公估诉讼",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Enums.CarMaintainDepositFollowStateType": {
        "enum": [
          0,
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "description": "本车维修押金跟进状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Enums.CarMaintainFollowStateType": {
        "enum": [
          0,
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "description": "本车维修费用跟进状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Enums.DerogatoryFollowStateType": {
        "enum": [
          0,
          1,
          2,
          3
        ],
        "type": "integer",
        "description": "贬损费用跟进状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Enums.FollowUpStaffs": {
        "enum": [
          1,
          2
        ],
        "type": "integer",
        "description": "跟进人 跟单人类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Enums.GetAccidentsForH5InPutStatusFlag": {
        "enum": [
          0,
          1
        ],
        "type": "integer",
        "description": "",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Enums.ThreeCostFollowStateType": {
        "enum": [
          0,
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "description": "三者费用跟进状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Enums.UserAdvanceFollowStateType": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5
        ],
        "type": "integer",
        "description": "客户垫付费用跟进状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Manager.Dto.UpdateAccidentStateCurrentsInput": {
        "type": "object",
        "properties": {
          "fileUrl": {
            "type": "string",
            "description": "表单数据集合",
            "nullable": true
          },
          "accidents": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "事故编号集合",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": "批量修改事故跟进状态入参"
      },
      "Corp.AfterSale.Core.CoreBusiness.Accident.Manager.Dto.UpdateAccidentStateCurrentsOutput": {
        "type": "object",
        "properties": {
          "exceptionExcelUrl": {
            "type": "string",
            "description": "导出异常事故跟进状态信息",
            "nullable": true
          },
          "successCount": {
            "type": "integer",
            "description": "导入成功总数",
            "format": "int32"
          },
          "failCount": {
            "type": "integer",
            "description": "导入失败总数",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": "批量修改事故跟进状态出参"
      },
      "Corp.AfterSale.Core.CoreBusiness.AnnualInspection.Dto.ModifyMaintainAlarmCurrentKmInfosDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "车辆需保养记录ID",
            "format": "int32"
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "currentKm": {
            "type": "number",
            "description": "当前公里数",
            "format": "double"
          },
          "currentTime": {
            "type": "string",
            "description": "最新维保时间",
            "format": "date-time"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.CoreBusiness.AnnualInspection.Dto.ModifyMaintainAlarmCurrentKmInfosInPut": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.AnnualInspection.Dto.ModifyMaintainAlarmCurrentKmInfosDto"
            },
            "description": "",
            "nullable": true
          },
          "ids": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32"
            },
            "description": "",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.CoreBusiness.AnnualInspection.Enums.MaintainAlarmStatus": {
        "enum": [
          0,
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "description": "车辆年检跟进状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Complaint.Enums.ActionType": {
        "enum": [
          1,
          2,
          3
        ],
        "type": "integer",
        "description": "操作类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Complaint.Enums.ComplaintOperationType": {
        "enum": [
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "description": "客诉操作类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Complaint.Enums.ComplaintStates": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10
        ],
        "type": "integer",
        "description": "投诉状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Other.Enums.AccountBusinessProperty": {
        "enum": [
          0,
          8
        ],
        "type": "integer",
        "description": "政企类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Reimbursement.Enums.AuditStatusChildType": {
        "enum": [
          0,
          1
        ],
        "type": "integer",
        "description": "报销审核子状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Dto.ApplyMaintenanceCheckItemDto": {
        "type": "object",
        "properties": {
          "itemId": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "verified": {
            "type": "boolean",
            "description": "验证结果 true 通过 false 未通过"
          },
          "verifiedFlag": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.NotPassReasonFlag"
          },
          "verifiedType": {
            "type": "integer",
            "description": "验证类型 1里程，2时间间隔，3官价",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Dto.BatchUpdateRangePricesInput": {
        "type": "object",
        "properties": {
          "rangeCheckType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RangeCheckTypes"
          },
          "rangeStart": {
            "type": "number",
            "description": "区间下限，默认为0",
            "format": "double"
          },
          "rangeEnd": {
            "type": "number",
            "description": "区间上限，默认为0",
            "format": "double"
          },
          "ruleName": {
            "type": "string",
            "description": "规则描述",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Dto.GetApplyMaintenanceDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "预约审核记录主键 或者 维保编号",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "bookTime": {
            "type": "string",
            "description": "预约时间 精确到分",
            "format": "date-time"
          },
          "repairShopName": {
            "type": "string",
            "description": "修理厂",
            "nullable": true
          },
          "verifyStatus": {
            "type": "integer",
            "description": "工单审核状态 1 待审核 2 已通过 3 已拒绝",
            "format": "int32"
          },
          "licenseStatus": {
            "type": "integer",
            "description": "凭证审核状态 1 待审核 2 已通过 3 已拒绝",
            "format": "int32"
          },
          "bxNo": {
            "type": "string",
            "description": "报销编号",
            "nullable": true
          },
          "financeStatusFlag": {
            "type": "string",
            "description": "报销打款状态",
            "nullable": true
          },
          "auditStatusFlag": {
            "type": "string",
            "description": "报销审核状态",
            "nullable": true
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否保养 true 是 false 否"
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否维修 true 是 false 否"
          },
          "wxUserId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "openId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "rescueReviewStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RescueReviewStatus"
          },
          "status": {
            "type": "integer",
            "description": "组合状态 \n1,待审核---工单提交成功 \n2,已拒绝---工单审核未通过--操作：重新提交 \n3,待上传凭证---工单审核通过--操作：上传凭证 \n4,待审核凭证---凭证上传成功\n5,凭证拒绝---凭证审核未通过--操作：重新上传 \n6,待报销---凭证审核通过 \n7,待报销---报销审核拒绝 \n8,已完成---报销完成",
            "format": "int32",
            "readOnly": true
          },
          "channelType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairChannelType"
          },
          "isCanEdit": {
            "type": "boolean",
            "description": "是否允许编辑",
            "readOnly": true
          },
          "isCancel": {
            "type": "boolean",
            "description": "是否允许取消",
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Dto.GetOrderTypeExpandDto": {
        "type": "object",
        "properties": {
          "driverNo": {
            "type": "string",
            "description": "司机工号",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "acctId": {
            "type": "string",
            "description": "政企编号",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "订单编号",
            "nullable": true
          },
          "contractId": {
            "type": "integer",
            "description": "要素编号",
            "format": "int32",
            "nullable": true
          },
          "selfOrderNo": {
            "type": "string",
            "description": "自驾订单编号",
            "nullable": true
          },
          "userId": {
            "type": "string",
            "description": "用户ID",
            "nullable": true
          },
          "actualUseStart": {
            "type": "string",
            "description": "实际取车时间",
            "format": "date-time",
            "nullable": true
          },
          "actualUseEnd": {
            "type": "string",
            "description": "实际还车时间",
            "format": "date-time",
            "nullable": true
          },
          "clientName": {
            "type": "string",
            "description": "客户姓名",
            "nullable": true
          },
          "clientPhone": {
            "type": "string",
            "description": "客户手机",
            "nullable": true
          },
          "driver": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.DriverApi.GetDriverDto"
          },
          "acctName": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "rentUserPhoneNumber": {
            "type": "string",
            "description": "租车人手机号",
            "nullable": true
          },
          "rentUserName": {
            "type": "string",
            "description": "租车人姓名",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Dto.ImportItemPriceRuleInput": {
        "type": "object",
        "properties": {
          "fileUrl": {
            "type": "string",
            "description": "表单数据集合",
            "nullable": true
          },
          "itemIds": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32",
              "nullable": true
            },
            "description": "维修项目编号集合",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": "导入维保配置入参"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Dto.ImportItemPriceRuleOutput": {
        "type": "object",
        "properties": {
          "exceptionExcelUrl": {
            "type": "string",
            "description": "导出异常维保规则配置",
            "nullable": true
          },
          "successCount": {
            "type": "integer",
            "description": "导入成功总数",
            "format": "int32"
          },
          "failCount": {
            "type": "integer",
            "description": "导入失败总数",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": "批量导入维保规则入参"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Dto.InitCheckKoalaRepairItemsInput": {
        "type": "object",
        "properties": {
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "reserveTime": {
            "type": "string",
            "description": "预约日期",
            "format": "date-time"
          },
          "type": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairType"
            },
            "description": "类型ID 1 维修 2保养",
            "nullable": true
          },
          "isContinue": {
            "type": "boolean",
            "description": "是否生成审核流"
          },
          "repairChannel": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairChannelType"
          },
          "repairInfo": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Entities.AfterSaleRepairInfo"
          }
        },
        "additionalProperties": false,
        "description": "验证考拉工单是否重复"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Dto.InitCheckRepairItemsInput": {
        "type": "object",
        "properties": {
          "details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.PushRepairInfoDto"
            },
            "description": "维修明细项",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "carInDateTime": {
            "type": "string",
            "description": "进厂时间",
            "format": "date-time"
          },
          "repairId": {
            "type": "string",
            "description": "维保编号",
            "nullable": true
          },
          "applyId": {
            "type": "integer",
            "description": "工单申请记录Id",
            "format": "int32",
            "nullable": true
          },
          "isContinue": {
            "type": "boolean",
            "description": "是否生成审核流"
          },
          "repairChannel": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairChannelType"
          },
          "repairInfo": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Entities.AfterSaleRepairInfo"
          },
          "rescueReviewStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RescueReviewStatus"
          }
        },
        "additionalProperties": false,
        "description": "验证工单是否重复入参"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Dto.RepairApplyLicenseDto": {
        "type": "object",
        "properties": {
          "bankAccountInfoId": {
            "type": "integer",
            "description": "银行账户信息Id",
            "format": "int32"
          },
          "accountName": {
            "type": "string",
            "description": "账户名称",
            "nullable": true
          },
          "accountNo": {
            "type": "string",
            "description": "账户号",
            "nullable": true
          },
          "bankId": {
            "type": "string",
            "description": "银行编号",
            "nullable": true
          },
          "bankName": {
            "type": "string",
            "description": "银行名称",
            "nullable": true
          },
          "cityNo": {
            "type": "string",
            "description": "城市编码",
            "nullable": true
          },
          "cityName": {
            "type": "string",
            "description": "城市名称",
            "nullable": true
          },
          "bankSectionId": {
            "type": "string",
            "description": "分行编号",
            "nullable": true
          },
          "bankSectionName": {
            "type": "string",
            "description": "分行名称",
            "nullable": true
          },
          "isSaveAccountInfo": {
            "type": "boolean",
            "description": "留存银行卡信息"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Dto.RepairCompensationDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "repairId": {
            "type": "string",
            "description": "维修编号",
            "nullable": true
          },
          "compensationType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.CompensationTypes"
          },
          "compensationAmount": {
            "type": "number",
            "description": "补偿金额",
            "format": "double"
          },
          "remark": {
            "type": "string",
            "description": "备注",
            "nullable": true
          },
          "invoiceFiles": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.Infrastructure.QueryModel.NameValueDto`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
            },
            "description": "发票附件集合",
            "nullable": true
          },
          "compensationTypeDesc": {
            "type": "string",
            "description": "补偿项描述",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": "补偿项明细"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Entities.AfterSaleRepairApply": {
        "type": "object",
        "properties": {
          "extraProperties": {
            "type": "object",
            "additionalProperties": {
              "nullable": true
            },
            "description": "默认扩展字段",
            "nullable": true,
            "readOnly": true
          },
          "id": {
            "type": "integer",
            "description": "主键",
            "format": "int32"
          },
          "repairShopName": {
            "type": "string",
            "description": "修理厂名称",
            "nullable": true
          },
          "repairShopType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairShopType"
          },
          "maintenanceType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.MaintenanceType"
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否维修 默认 否"
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否保养 默认 否"
          },
          "bookTime": {
            "type": "string",
            "description": "预约时间",
            "format": "date-time"
          },
          "repairDetail": {
            "type": "string",
            "description": "维修项明细",
            "nullable": true
          },
          "remark": {
            "type": "string",
            "description": "备注",
            "nullable": true
          },
          "userName": {
            "type": "string",
            "description": "客户姓名",
            "nullable": true
          },
          "userPhone": {
            "type": "string",
            "description": "用户手机号码",
            "nullable": true
          },
          "isDeleted": {
            "type": "boolean",
            "description": "是否删除"
          },
          "deleterUserId": {
            "type": "string",
            "description": "删除操作用户",
            "nullable": true
          },
          "deletionTime": {
            "type": "string",
            "description": "删除操作时间",
            "format": "date-time",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "vinNo": {
            "type": "string",
            "description": "车架号",
            "nullable": true
          },
          "verifyStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.VerifyStatus"
          },
          "openId": {
            "type": "string",
            "description": "微信Openid",
            "nullable": true
          },
          "wxUserId": {
            "type": "string",
            "description": "联合登陆对应的userid",
            "nullable": true
          },
          "repairId": {
            "type": "string",
            "description": "维保ID",
            "nullable": true
          },
          "inKm": {
            "type": "integer",
            "description": "进厂公里数",
            "format": "int32"
          },
          "bxNo": {
            "type": "string",
            "description": "报销编号",
            "nullable": true
          },
          "financeStatusFlag": {
            "type": "string",
            "description": "报销打款状态\nCorp.AfterSale.Core.CoreBusiness.Reimbursement.Enums.FinanceStatusFlags",
            "nullable": true
          },
          "auditStatusFlag": {
            "type": "string",
            "description": "报销审核状态\nCorp.AfterSale.Core.CoreBusiness.Reimbursement.Enums.AuditStatusFlags",
            "nullable": true
          },
          "reminded": {
            "type": "boolean",
            "description": "邮件通知标记"
          },
          "driverNo": {
            "type": "string",
            "description": "司机工号",
            "nullable": true
          },
          "cancelReason": {
            "type": "string",
            "description": "取消原因",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "channelType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairChannelType"
          },
          "customerServiceCode": {
            "type": "string",
            "description": "客服工号",
            "nullable": true
          },
          "lastModificationTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "creationTime": {
            "type": "string",
            "format": "date-time"
          },
          "creationUserNo": {
            "type": "string",
            "nullable": true
          },
          "lastModifyUserNo": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Entities.AfterSaleRepairInfo": {
        "type": "object",
        "properties": {
          "extraProperties": {
            "type": "object",
            "additionalProperties": {
              "nullable": true
            },
            "description": "默认扩展字段",
            "nullable": true,
            "readOnly": true
          },
          "id": {
            "type": "string",
            "description": "维修编号",
            "nullable": true
          },
          "acctId": {
            "type": "string",
            "description": "企业编号",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "orderNo": {
            "type": "string",
            "description": "企业订单",
            "nullable": true
          },
          "ecCarId": {
            "type": "integer",
            "description": "车辆Id",
            "format": "int32"
          },
          "carNo": {
            "type": "string",
            "description": "车牌号",
            "nullable": true
          },
          "vinNo": {
            "type": "string",
            "description": "车架号",
            "nullable": true
          },
          "repairType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairFactoryType"
          },
          "repairDateTime": {
            "type": "string",
            "description": "维修时间",
            "format": "date-time"
          },
          "repairContent": {
            "type": "string",
            "description": "维修明细备注",
            "nullable": true
          },
          "repairShopName": {
            "type": "string",
            "description": "维修厂名称",
            "nullable": true
          },
          "statusFlag": {
            "type": "string",
            "description": "维保工单状态",
            "nullable": true
          },
          "carInDateTime": {
            "type": "string",
            "description": "进厂时间",
            "format": "date-time",
            "nullable": true
          },
          "carOutDateTime": {
            "type": "string",
            "description": "出厂时间",
            "format": "date-time",
            "nullable": true
          },
          "carInMileage": {
            "type": "number",
            "description": "进厂公里数",
            "format": "double",
            "nullable": true
          },
          "carOutMileage": {
            "type": "number",
            "description": "出厂公里数",
            "format": "double",
            "nullable": true
          },
          "city": {
            "type": "string",
            "description": "维修厂城市",
            "nullable": true
          },
          "carTypeName": {
            "type": "string",
            "description": "车型名称",
            "nullable": true
          },
          "hourAmount": {
            "type": "number",
            "description": "工时费",
            "format": "double",
            "nullable": true
          },
          "materialAmount": {
            "type": "number",
            "description": "材料费",
            "format": "double",
            "nullable": true
          },
          "expressDate": {
            "type": "string",
            "description": "快递到达时间",
            "nullable": true
          },
          "reimbursementNo": {
            "type": "string",
            "description": "报销单号",
            "nullable": true
          },
          "oprNo": {
            "type": "string",
            "description": "操作人工号",
            "nullable": true
          },
          "oprName": {
            "type": "string",
            "description": "操作人姓名",
            "nullable": true
          },
          "completeDateTimeEst": {
            "type": "string",
            "description": "预计维修完成时间",
            "format": "date-time",
            "nullable": true
          },
          "completeDateTime": {
            "type": "string",
            "description": "实际维修完成时间",
            "format": "date-time",
            "nullable": true
          },
          "bookRepairTime": {
            "type": "string",
            "description": "预约维修时间",
            "format": "date-time",
            "nullable": true
          },
          "maintenanceType": {
            "type": "integer",
            "description": "预约项目，1维修，2保养",
            "format": "int32",
            "nullable": true,
            "deprecated": true
          },
          "repairShopType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairShopType"
          },
          "channelType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairChannelType"
          },
          "userName": {
            "type": "string",
            "description": "客户姓名",
            "nullable": true
          },
          "userPhone": {
            "type": "string",
            "description": "客户手机号码",
            "nullable": true
          },
          "expressNo": {
            "type": "string",
            "description": "快递单号",
            "nullable": true
          },
          "expressCost": {
            "type": "number",
            "description": "快递费用",
            "format": "double"
          },
          "creationUserNo": {
            "type": "string",
            "description": "创建人工号",
            "nullable": true
          },
          "creationUserName": {
            "type": "string",
            "description": "创建人姓名",
            "nullable": true
          },
          "lastModifyUserNo": {
            "type": "string",
            "description": "更新人工号",
            "nullable": true
          },
          "lastModifyUserName": {
            "type": "string",
            "description": "更新人姓名",
            "nullable": true
          },
          "accidentDuty": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.AccidentDutyType"
          },
          "isPostKoala": {
            "type": "boolean",
            "description": "是否已推送考拉",
            "nullable": true
          },
          "openId": {
            "type": "string",
            "description": "微信Openid",
            "nullable": true
          },
          "wxUserId": {
            "type": "string",
            "description": "联合登陆对应的userid",
            "nullable": true
          },
          "repairShopId": {
            "type": "string",
            "description": "考拉维修门店ID",
            "nullable": true
          },
          "cityId": {
            "type": "string",
            "description": "维修厂城市ID",
            "nullable": true
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否维修"
          },
          "isMaintenance": {
            "type": "boolean",
            "description": "是否保养"
          },
          "lastModificationTime": {
            "type": "string",
            "description": "更新时间",
            "format": "date-time",
            "nullable": true
          },
          "creationTime": {
            "type": "string",
            "description": "创建时间",
            "format": "date-time"
          },
          "driverNo": {
            "type": "string",
            "description": "司机工号",
            "nullable": true
          },
          "isDeleted": {
            "type": "boolean",
            "description": "删除"
          },
          "smsSendCount": {
            "type": "integer",
            "description": "短信通知提醒次数\n负数为失败次数\n正数为成功次数",
            "format": "int32"
          },
          "repeatApplyAuditState": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairAuditState"
          },
          "reimburseReportType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ReimburseReportType"
          },
          "accidentCity": {
            "type": "string",
            "description": "事故城市（维修厂或事故发生地所在城市）",
            "nullable": true
          },
          "financeStatusFlag": {
            "type": "string",
            "description": "报销打款状态\nCorp.AfterSale.Core.CoreBusiness.Reimbursement.Enums.FinanceStatusFlags",
            "nullable": true
          },
          "auditStatusFlag": {
            "type": "string",
            "description": "报销审核状态\nCorp.AfterSale.Core.CoreBusiness.Reimbursement.Enums.AuditStatusFlags",
            "nullable": true
          },
          "rescueReviewStatus": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RescueReviewStatus"
          },
          "rescueId": {
            "type": "integer",
            "description": "救援Id",
            "format": "int32",
            "nullable": true
          },
          "isPushKoala": {
            "type": "boolean",
            "description": "是否可以推送到考拉系统",
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": "维保信息"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.AccidentDutyType": {
        "enum": [
          1,
          2
        ],
        "type": "integer",
        "description": "",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.AccidentTypes": {
        "enum": [
          1,
          2,
          3,
          4,
          5
        ],
        "type": "integer",
        "description": "(自驾)事故性质：1-单车事故 2-双车事故 3-多车事故 4-人伤事故 5-死亡事故",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ApplyAccountStatus": {
        "enum": [
          0,
          1
        ],
        "type": "integer",
        "description": "工单所属银行账户信息有效状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ApplyMaintenanceStatus": {
        "enum": [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8
        ],
        "type": "integer",
        "description": "H5预约工单状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.AreaType": {
        "enum": [
          1,
          2,
          3,
          4,
          5,
          6,
          7
        ],
        "type": "integer",
        "description": "区域",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6
        ],
        "type": "integer",
        "description": "企业售后订单服务类型\n1:零单自驾 2:零单代驾 3:长包自驾 4:长包代驾",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.CarNatures": {
        "enum": [
          1,
          2
        ],
        "type": "integer",
        "description": "车辆性质类型\n1:自驾 2:代驾",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ChildStatusFlag": {
        "enum": [
          0,
          1,
          2,
          9
        ],
        "type": "integer",
        "description": "",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.CompensationTypes": {
        "enum": [
          0,
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "description": "补偿项类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.CoverageType": {
        "enum": [
          0,
          105,
          215,
          231,
          232,
          233,
          255,
          256
        ],
        "type": "integer",
        "description": "保障类型\n105:基本保障 231:尊享保障 232:百万守护 233:全程无忧 215.乘客守护 255.尊享守护 256.全程无忧升级版",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.DutyTypes": {
        "enum": [
          1,
          2,
          3,
          4,
          5,
          6
        ],
        "type": "integer",
        "description": "(自驾)责任划分(事故责任)",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.EarlyWarningType": {
        "enum": [
          0,
          1,
          2
        ],
        "type": "integer",
        "description": "预警类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ImpactType": {
        "enum": [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11,
          12,
          13
        ],
        "type": "integer",
        "description": "碰撞类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.JgAccidentType": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          7
        ],
        "type": "integer",
        "description": "事故性质",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.JgDutyType": {
        "enum": [
          1,
          2,
          3,
          4,
          5,
          6
        ],
        "type": "integer",
        "description": "责任划分(事故责任)",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.LicenseLastVerifyType": {
        "enum": [
          0,
          1,
          2
        ],
        "type": "integer",
        "description": "最近一次审核类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.LicenseVerifyStatusFlag": {
        "enum": [
          0,
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "description": "凭证审核状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.MaintenanceType": {
        "enum": [
          0,
          1,
          2
        ],
        "type": "integer",
        "description": "预约项目",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.NotPassReasonFlag": {
        "enum": [
          1,
          2,
          4,
          5,
          6,
          7
        ],
        "type": "integer",
        "description": "不通过原因",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.OutsiteType": {
        "enum": [
          0,
          1,
          3
        ],
        "type": "integer",
        "description": "托外商类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.PriceRuleCheckType": {
        "enum": [
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "description": "",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.PunishmentType": {
        "enum": [
          1,
          2,
          3,
          4,
          5
        ],
        "type": "integer",
        "description": "行政处罚决定",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RangeCheckTypes": {
        "enum": [
          0,
          1,
          2,
          3
        ],
        "type": "integer",
        "description": "区间判断方式",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ReimburseReportType": {
        "enum": [
          0,
          1,
          2
        ],
        "type": "integer",
        "description": "报销报备类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ReimbursementType": {
        "enum": [
          1
        ],
        "type": "integer",
        "description": "报销申请类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RentTypes": {
        "enum": [
          1,
          2
        ],
        "type": "integer",
        "description": "租凭类型\n1:短租 2:长包",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairAttachType": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          7
        ],
        "type": "integer",
        "description": "维保凭证",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairAuditState": {
        "enum": [
          0,
          1,
          2,
          3
        ],
        "type": "integer",
        "description": "工单审核状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairChannelType": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          7
        ],
        "type": "integer",
        "description": "维保预约渠道",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairFactoryType": {
        "enum": [
          1,
          2
        ],
        "type": "integer",
        "description": "维修厂类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairOperationType": {
        "enum": [
          0,
          1
        ],
        "type": "integer",
        "description": "",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairShopType": {
        "enum": [
          1,
          2
        ],
        "type": "integer",
        "description": "维修厂类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairType": {
        "enum": [
          1,
          2
        ],
        "type": "integer",
        "description": "维修类型 1 维修，2保养",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RescueReviewStatus": {
        "enum": [
          6,
          7,
          8,
          10,
          11
        ],
        "type": "integer",
        "description": "救援单审核状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.SaveTypes": {
        "enum": [
          0,
          1,
          2
        ],
        "type": "integer",
        "description": "是否保存银行信息 0.下次再说 1.同意 2.不同意",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.ScenesType": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6
        ],
        "type": "integer",
        "description": "事故场景",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.StatusFlag": {
        "enum": [
          0,
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "description": "跟进状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.TickType": {
        "enum": [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11
        ],
        "type": "integer",
        "description": "违章分类",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.TicketDjStatus": {
        "enum": [
          1,
          2,
          3,
          4,
          5
        ],
        "type": "integer",
        "description": "违章处理状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.TicketProcessType": {
        "enum": [
          1,
          2,
          3
        ],
        "type": "integer",
        "description": "违章处理状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.VerifyStatus": {
        "enum": [
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "description": "",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.VerifyStatusFlag": {
        "enum": [
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "description": "工单提交成功",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Enums.WeatherType": {
        "enum": [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8
        ],
        "type": "integer",
        "description": "天气",
        "format": "int32"
      },
      "Corp.AfterSale.Core.CoreBusiness.Repair.Manager.Dto.RepairItemPriceRuleDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "业务主键",
            "format": "int32"
          },
          "itemId": {
            "type": "integer",
            "description": "维保项目Id",
            "format": "int32"
          },
          "itemName": {
            "type": "string",
            "description": "维保项目名称",
            "nullable": true
          },
          "checkType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.PriceRuleCheckType"
          },
          "rangeCheckType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RangeCheckTypes"
          },
          "price": {
            "type": "number",
            "description": "规则对应单价",
            "format": "double"
          },
          "rangeStart": {
            "type": "number",
            "description": "区间下限，默认为0",
            "format": "double"
          },
          "rangeEnd": {
            "type": "number",
            "description": "区间上限，默认为0",
            "format": "double"
          },
          "ruleName": {
            "type": "string",
            "description": "规则描述",
            "nullable": true
          },
          "isRepair": {
            "type": "boolean",
            "description": "维修时是否检查 true 检查 false 不检查"
          },
          "isMaintain": {
            "type": "boolean",
            "description": "保养时是否检查 true 检查 false 不检查"
          },
          "quantity": {
            "type": "integer",
            "description": "数量限制",
            "format": "int32"
          },
          "checkTypeDesc": {
            "type": "string",
            "description": "判定类型描述",
            "nullable": true,
            "readOnly": true
          },
          "rangeCheckTypeDesc": {
            "type": "string",
            "description": "区间判定方式",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.CoreBusiness.Verify.Enums.VerifyStatusEnum": {
        "enum": [
          0,
          1,
          2,
          3,
          100,
          -1
        ],
        "type": "integer",
        "description": "通用审核审核状态",
        "format": "int32"
      },
      "Corp.AfterSale.Core.ExternalService.Dto.CarSupportApi.GetInsuranceCustomerOutPut": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "",
            "format": "int32",
            "nullable": true
          },
          "oprNo": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "oprName": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "oprType": {
            "type": "integer",
            "description": "",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "获取跟进客服列表出参"
      },
      "Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.BlockOrderType": {
        "enum": [
          1,
          2,
          4,
          5
        ],
        "type": "integer",
        "description": "长包订单类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.GetOrderInfoByCarNoAndTimeDto": {
        "type": "object",
        "properties": {
          "acctId": {
            "type": "string",
            "description": "企业编号",
            "nullable": true
          },
          "acctName": {
            "type": "string",
            "description": "企业名称",
            "nullable": true
          },
          "contractId": {
            "type": "integer",
            "description": "要素编号",
            "format": "int32",
            "nullable": true
          },
          "driverNo": {
            "type": "string",
            "description": "司机工号",
            "nullable": true
          },
          "fromDate": {
            "type": "string",
            "description": "订单开始时间",
            "format": "date-time",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "订单编号",
            "nullable": true
          },
          "orderStatus": {
            "type": "integer",
            "description": "订单状态",
            "format": "int32"
          },
          "orderType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.BlockOrderType"
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "refConfirmationNo": {
            "type": "string",
            "description": "自驾订单编号",
            "nullable": true
          },
          "salesSerialNo": {
            "type": "string",
            "description": "销售编号",
            "nullable": true
          },
          "takeCarCellPhone": {
            "type": "string",
            "description": "用车人手机",
            "nullable": true
          },
          "takeCarName": {
            "type": "string",
            "description": "用车人姓名",
            "nullable": true
          },
          "toDate": {
            "type": "string",
            "description": "结束时间",
            "format": "date-time",
            "nullable": true
          },
          "actualUseStart": {
            "type": "string",
            "description": "订单实际开始时间",
            "format": "date-time",
            "nullable": true
          },
          "actualUseEnd": {
            "type": "string",
            "description": "订单实际结束时间",
            "format": "date-time",
            "nullable": true
          },
          "carUseCity": {
            "type": "string",
            "description": "用车城市",
            "nullable": true
          },
          "carPrice": {
            "type": "number",
            "description": "车辆官价",
            "format": "double",
            "nullable": true
          },
          "isReplaceCarType": {
            "type": "boolean",
            "description": "是否替代车"
          },
          "replaceCarType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.ReplaceCarType"
          },
          "takeCarEmail": {
            "type": "string",
            "description": "用车人邮箱",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.GetOrderTypeDto": {
        "type": "object",
        "properties": {
          "driverNo": {
            "type": "string",
            "description": "司机工号",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "acctId": {
            "type": "string",
            "description": "政企编号",
            "nullable": true
          },
          "orderNo": {
            "type": "string",
            "description": "订单编号",
            "nullable": true
          },
          "contractId": {
            "type": "integer",
            "description": "要素编号",
            "format": "int32",
            "nullable": true
          },
          "selfOrderNo": {
            "type": "string",
            "description": "自驾订单编号",
            "nullable": true
          },
          "userId": {
            "type": "string",
            "description": "用户ID",
            "nullable": true
          },
          "actualUseStart": {
            "type": "string",
            "description": "实际取车时间",
            "format": "date-time",
            "nullable": true
          },
          "actualUseEnd": {
            "type": "string",
            "description": "实际还车时间",
            "format": "date-time",
            "nullable": true
          },
          "rentUserPhoneNumber": {
            "type": "string",
            "description": "租车人手机号",
            "nullable": true
          },
          "rentUserName": {
            "type": "string",
            "description": "租车人姓名",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.GetRepairInfoOutPut": {
        "type": "object",
        "properties": {
          "serviceTermId": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "serviceTermDesc": {
            "type": "string",
            "description": "描述",
            "nullable": true
          },
          "serviceTermName": {
            "type": "string",
            "description": "名称",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.ReplaceCarType": {
        "enum": [
          101,
          102,
          103,
          104,
          105,
          106,
          107,
          201,
          202,
          203,
          204
        ],
        "type": "integer",
        "description": "替代车类型",
        "format": "int32"
      },
      "Corp.AfterSale.Core.ExternalService.Dto.DjEoWork.GetReimburseMiddlePageUrlOutPut": {
        "type": "object",
        "properties": {
          "allow": {
            "type": "boolean",
            "description": "是否允许跳转报销中间页"
          },
          "url": {
            "type": "string",
            "description": "跳转url",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.DriverApi.GetDriverDto": {
        "type": "object",
        "properties": {
          "driverId": {
            "type": "string",
            "description": "司机工号 ,",
            "nullable": true
          },
          "driverName": {
            "type": "string",
            "description": ": 司机姓名 ,",
            "nullable": true
          },
          "activeStatus": {
            "type": "string",
            "description": "在职状态： 0 离职，1在职，2:提出离职",
            "nullable": true
          },
          "phoneNumber": {
            "type": "string",
            "description": "司机手机号",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "司机绑定的车牌号",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.FileCenter.FileCategoryType": {
        "enum": [
          612,
          621,
          629,
          1204,
          1211,
          1220,
          1228,
          1230,
          1231,
          1239,
          1277,
          1278,
          1298,
          1315,
          1320,
          1326,
          1644,
          1660,
          1675
        ],
        "type": "integer",
        "description": "上传图片 类型ID 对应李潇组 文件中心类别",
        "format": "int32"
      },
      "Corp.AfterSale.Core.ExternalService.Dto.Hr.UserInfoByCode": {
        "type": "object",
        "properties": {
          "userCode": {
            "type": "string",
            "description": "工号",
            "nullable": true
          },
          "userName": {
            "type": "string",
            "description": "姓名",
            "nullable": true
          },
          "certTypeName": {
            "type": "string",
            "description": "证件类型",
            "nullable": true
          },
          "certCode": {
            "type": "string",
            "description": "证件号码",
            "nullable": true
          },
          "phone": {
            "type": "string",
            "description": "手机号",
            "nullable": true
          },
          "status": {
            "type": "string",
            "description": "员工状态：{ \"P\", \"待离职\" }, { \"L\", \"已离职\" },{ \"Y\",\"正常入职\"},{ \"S\",\"试用期\"}, {\"F\",\"放弃录用\" }, { \"D\",\"待录用\"}",
            "nullable": true
          },
          "quit": {
            "type": "boolean",
            "description": "标记员工是否已离职",
            "readOnly": true
          },
          "email": {
            "type": "string",
            "description": "邮箱",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetDistrictsDto": {
        "type": "object",
        "properties": {
          "cityId": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "districtCode": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "enName": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "id": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaoLaRepairItemsDto": {
        "type": "object",
        "properties": {
          "chargeModelSame": {
            "type": "integer",
            "description": "车型收费相同，0-不同，1-相同 ,",
            "format": "int32",
            "nullable": true
          },
          "description": {
            "type": "string",
            "description": "服务项目描述 ,",
            "nullable": true
          },
          "fastRepair": {
            "type": "integer",
            "description": "是否快修结算，0-不是，1-是 ,",
            "format": "int32",
            "nullable": true
          },
          "financeCategory": {
            "type": "integer",
            "description": "财务类别，见字典表 ,",
            "format": "int32",
            "nullable": true
          },
          "id": {
            "type": "integer",
            "description": "自增长，主键 ,",
            "format": "int32",
            "nullable": true
          },
          "imageUrl": {
            "type": "string",
            "description": "图片 ,",
            "nullable": true
          },
          "isDeleted": {
            "type": "boolean",
            "description": "是否隐藏该条记录 ,",
            "nullable": true
          },
          "isMultiselect": {
            "type": "integer",
            "description": "是否多选 ,",
            "format": "int32",
            "nullable": true
          },
          "isPublicVisit": {
            "type": "boolean",
            "description": "是否在对外可以显示 ,",
            "nullable": true
          },
          "isRadioOption": {
            "type": "boolean",
            "description": "是否单选 ,",
            "nullable": true
          },
          "maintenanceMiles": {
            "type": "number",
            "description": "保养公里数 ,",
            "format": "double",
            "nullable": true
          },
          "maintenancePeriod": {
            "type": "number",
            "description": "保养周期 ,",
            "format": "double",
            "nullable": true
          },
          "modify": {
            "type": "boolean",
            "description": "",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "服务项目名称 ,",
            "nullable": true
          },
          "price": {
            "type": "number",
            "description": "服务项目价格 ,",
            "format": "double",
            "nullable": true
          },
          "seats": {
            "type": "integer",
            "description": "座位数 ,",
            "format": "int32",
            "nullable": true
          },
          "serviceCategoryId": {
            "type": "integer",
            "description": "服务类别ID(serviceCatagory.Id) ,",
            "format": "int32",
            "nullable": true
          },
          "serviceItemId": {
            "type": "integer",
            "description": "子服务ID(serviceItem.Id) ,",
            "format": "int32",
            "nullable": true
          },
          "servicePrice": {
            "type": "number",
            "description": "服务费价格 ,",
            "format": "double",
            "nullable": true
          },
          "serviceSubTypeId": {
            "type": "integer",
            "description": "维修子项目ID(serviceSubType.i ,",
            "format": "int32",
            "nullable": true
          },
          "serviceTypeId": {
            "type": "integer",
            "description": "关联服务类型ID (ServiceType.i,",
            "format": "int32",
            "nullable": true
          },
          "starLevel": {
            "type": "integer",
            "description": "对应星级，见字典表 ,",
            "format": "int32",
            "nullable": true
          },
          "workTypeId": {
            "type": "integer",
            "description": "对应工种",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaCitiesDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "isOnline": {
            "type": "boolean",
            "description": ""
          },
          "cityCode": {
            "type": "string",
            "description": "城市代码",
            "nullable": true
          },
          "enName": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "provinceId": {
            "type": "integer",
            "description": "",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaProvincesOriginalDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "省份Id",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "description": "省份名称",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaRepeatShopsDto": {
        "type": "object",
        "properties": {
          "shopId": {
            "type": "integer",
            "description": "门店Id",
            "format": "int32",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "门店名称",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetRepairshopsConditionsDto": {
        "type": "object",
        "properties": {
          "address": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "cooperationId": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "distance": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "id": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "imagePath": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "latitude": {
            "type": "number",
            "description": "",
            "format": "double",
            "nullable": true
          },
          "longitude": {
            "type": "number",
            "description": "",
            "format": "double",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "phoneNo": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "shopType": {
            "type": "integer",
            "description": "",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetStocksDto": {
        "type": "object",
        "properties": {
          "carRepairShopId": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "carRepairShopName": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "cityId": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "cityName": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "id": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "maintainOrderCount": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "maintainRemainCount": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "maintainStationCount": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "orderCount": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "remainCount": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "reserve": {
            "type": "boolean",
            "description": ""
          },
          "stationCount": {
            "type": "integer",
            "description": "",
            "format": "int32"
          },
          "stockDateTime": {
            "type": "string",
            "description": "",
            "format": "date-time",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetWbOrderInfoDto": {
        "type": "object",
        "properties": {
          "carRepairItemInfoList": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetwbOrderInfoRepairInfoItemDto"
            },
            "description": "维修项列表",
            "nullable": true
          },
          "orderCar": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetWbOrderInfoOrderCarDto"
          },
          "orderOperator": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetWbOrderInfoOrderOperatorDto"
          },
          "user": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetWbOrderInfoUserDto"
          },
          "serviceTerms": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "服务条款",
            "nullable": true
          },
          "deal": {
            "type": "boolean",
            "description": "无需通知"
          },
          "userName": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "userPhone": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "companyName": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "extraProperties": {
            "type": "object",
            "additionalProperties": {
              "nullable": true
            },
            "description": "",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetWbOrderInfoOrderCarDto": {
        "type": "object",
        "properties": {
          "brandId": {
            "type": "integer",
            "description": "品牌ID ,",
            "format": "int32"
          },
          "brandName": {
            "type": "string",
            "description": "品牌名 ,",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "description": "车牌号 ,",
            "nullable": true
          },
          "emission": {
            "type": "string",
            "description": "排量 ,",
            "nullable": true
          },
          "miles": {
            "type": "integer",
            "description": "公里数 ,",
            "format": "int32"
          },
          "orderId": {
            "type": "string",
            "description": "维修订单号(订单表中的orderId,o ,",
            "nullable": true
          },
          "seats": {
            "type": "integer",
            "description": "坐位数 ,",
            "format": "int32"
          },
          "seriesId": {
            "type": "integer",
            "description": "车系ID ,",
            "format": "int32"
          },
          "seriesName": {
            "type": "string",
            "description": "车系名 ,",
            "nullable": true
          },
          "year": {
            "type": "string",
            "description": "出厂年份",
            "nullable": true
          },
          "accidentDuty": {
            "type": "integer",
            "description": "事故责任 1 本车原因 2 其他",
            "format": "int32",
            "nullable": true
          },
          "carId": {
            "type": "integer",
            "description": "车辆Id",
            "format": "int32"
          },
          "coopId": {
            "type": "integer",
            "description": "渠道ID，1 表示一嗨，2表示散客，3表示集团",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetWbOrderInfoOrderOperatorDto": {
        "type": "object",
        "properties": {
          "accept": {
            "type": "boolean",
            "description": ""
          },
          "accident": {
            "type": "boolean",
            "description": ""
          },
          "approvalComments": {
            "type": "string",
            "description": "审核备注（审核不通过原因） ,",
            "nullable": true
          },
          "approvalDateTime": {
            "type": "string",
            "description": "审核时间 原表字段：verify_dat ,",
            "nullable": true
          },
          "approvalStatus": {
            "type": "boolean",
            "description": "维修审核状态(所有维修厂都要审,维修中心用户不用审） ,"
          },
          "approvalUserId": {
            "type": "string",
            "description": "审核人工号（维修中心的审核人） ,",
            "nullable": true
          },
          "bookRepairTime": {
            "type": "string",
            "description": "预约维修时间 ,",
            "nullable": true
          },
          "carInDateTime": {
            "type": "string",
            "description": "车辆进入维修厂时间 ,",
            "nullable": true
          },
          "carInFuel": {
            "type": "number",
            "description": "进维修厂油量，原表字段start_f ,",
            "format": "double"
          },
          "carInMiles": {
            "type": "integer",
            "description": "车辆进维修厂里程 ,",
            "format": "int32"
          },
          "carNo": {
            "type": "string",
            "description": "车牌号 ,",
            "nullable": true
          },
          "carOutDateTime": {
            "type": "string",
            "description": "车辆修好后，出维修厂时间 ,",
            "nullable": true
          },
          "carOutFuel": {
            "type": "number",
            "description": "出维修厂油量 原表字段：end_f ,",
            "format": "double"
          },
          "carOutMiles": {
            "type": "integer",
            "description": "车辆出维修厂里程 ,",
            "format": "int32"
          },
          "carRepairShopId": {
            "type": "integer",
            "description": "维修厂ID（carRepairShop.Id） ,",
            "format": "int32"
          },
          "carRepairShopName": {
            "type": "string",
            "description": "修理厂名称 ,",
            "nullable": true
          },
          "cityId": {
            "type": "integer",
            "description": "城市id ,",
            "format": "int32"
          },
          "cityName": {
            "type": "string",
            "description": "城市名 ,",
            "nullable": true
          },
          "companyName": {
            "type": "string",
            "description": "公司名称 ,",
            "nullable": true
          },
          "companyRemark": {
            "type": "string",
            "description": "公司备注 ,",
            "nullable": true
          },
          "completeDateTime": {
            "type": "string",
            "description": "实际维修完成时间 ,",
            "nullable": true
          },
          "completeDateTimeEst": {
            "type": "string",
            "description": "预计维修完成时间 ,",
            "nullable": true
          },
          "coopId": {
            "type": "integer",
            "description": "渠道ID ,",
            "format": "int32"
          },
          "exMileReason": {
            "type": "string",
            "description": "超里程原因(车辆进维修厂和出维 ,",
            "nullable": true
          },
          "feedBack": {
            "type": "integer",
            "description": "是否评价 ,",
            "format": "int32"
          },
          "haveOutsiteOrder": {
            "type": "integer",
            "description": "是否有托外订单：0-没有，1-有 ,",
            "format": "int32"
          },
          "inDateTime": {
            "type": "string",
            "description": "下单时间 ,",
            "nullable": true
          },
          "isAccept": {
            "type": "boolean",
            "description": "供就商是否已接单 ,"
          },
          "isAccident": {
            "type": "boolean",
            "description": "该车是否有事故 ,"
          },
          "isDoorService": {
            "type": "integer",
            "description": "是否上门服务：0-否，1-是 ,",
            "format": "int32",
            "nullable": true
          },
          "isMaintain": {
            "type": "boolean",
            "description": "是否保养 ,"
          },
          "isRepair": {
            "type": "boolean",
            "description": "是否维修 ,"
          },
          "maintain": {
            "type": "boolean",
            "description": "",
            "nullable": true
          },
          "oprUserId": {
            "type": "string",
            "description": "操作人工号(维修厂和维修中心) ,",
            "nullable": true
          },
          "orderId": {
            "type": "string",
            "description": "订单号 ,",
            "nullable": true
          },
          "orderSource": {
            "type": "integer",
            "description": "订单来源：0-自修，1-托外 ,",
            "format": "int32"
          },
          "payBy": {
            "type": "string",
            "description": "支付方式: 客户承担 C ,客户报销B，一嗨 E，保险公司 I ,",
            "nullable": true
          },
          "payPrice": {
            "type": "number",
            "description": "待支付金额 ,",
            "format": "double"
          },
          "paymentType": {
            "type": "string",
            "description": "微信支付方式：现付：C，预付:R ,",
            "nullable": true
          },
          "persionName": {
            "type": "string",
            "description": "维修人姓名 ,",
            "nullable": true
          },
          "persionPhone": {
            "type": "string",
            "description": "维修人电话 ,",
            "nullable": true
          },
          "price": {
            "type": "number",
            "description": "订单总价 ,",
            "format": "double"
          },
          "referId": {
            "type": "string",
            "description": "关联标识（例，一嗨的租车订单号 ,",
            "nullable": true
          },
          "repair": {
            "type": "boolean",
            "description": "",
            "nullable": true
          },
          "repairContent": {
            "type": "string",
            "description": "维修内容或维修项目描述 ,",
            "nullable": true
          },
          "repairDateTime": {
            "type": "string",
            "description": "维修时间 ,",
            "nullable": true
          },
          "repairItemComments": {
            "type": "string",
            "description": "维修内容备注 原表字段：repair ,",
            "nullable": true
          },
          "repairType": {
            "type": "string",
            "description": "维修分类 ,",
            "nullable": true
          },
          "settlementType": {
            "type": "string",
            "description": "结算方式：现付 C,月付 M ,",
            "nullable": true
          },
          "source": {
            "type": "integer",
            "description": "订单来源1. 公众号、2. 维修厂登记、3 维修厂预约、4 批量导入、5 非koala批量导入、6企业预约",
            "format": "int32"
          },
          "sourceOrderId": {
            "type": "string",
            "description": "来源订单号 ,",
            "nullable": true
          },
          "status": {
            "type": "string",
            "description": "'R' THEN '预约中' 'G' THEN '已 ,",
            "nullable": true
          },
          "userId": {
            "type": "integer",
            "description": "用户ID ,",
            "format": "int32"
          },
          "vinNo": {
            "type": "string",
            "description": "车架号",
            "nullable": true
          },
          "enterpriseId": {
            "type": "string",
            "description": "企业ID",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetWbOrderInfoUserDto": {
        "type": "object",
        "properties": {
          "balance": {
            "type": "number",
            "description": "用户余额 ,",
            "format": "double"
          },
          "cellPhone": {
            "type": "string",
            "description": "手机号 ,",
            "nullable": true
          },
          "inDateTime": {
            "type": "string",
            "description": "建档时间 ,",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "用户名 ,",
            "nullable": true
          },
          "points": {
            "type": "integer",
            "description": "用户积分 ,",
            "format": "int32"
          },
          "userId": {
            "type": "integer",
            "description": "用户ID ,",
            "format": "int32"
          },
          "userLevel": {
            "type": "integer",
            "description": "用户等级",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetwbOrderInfoRepairInfoItemDto": {
        "type": "object",
        "properties": {
          "isApproval": {
            "type": "integer",
            "description": "是否审核",
            "format": "int32"
          },
          "isOutsite": {
            "type": "integer",
            "description": "是否托外：0-否，1-是 ,",
            "format": "int32"
          },
          "itemCount": {
            "type": "integer",
            "description": "数量",
            "format": "int32"
          },
          "itemName": {
            "type": "string",
            "description": "项目名称",
            "nullable": true
          },
          "maintainStaff": {
            "type": "integer",
            "description": "维修员工工号",
            "format": "int32"
          },
          "materialsId": {
            "type": "integer",
            "description": "材料Id ,",
            "format": "int32"
          },
          "orderId": {
            "type": "string",
            "description": "订单id ,",
            "nullable": true
          },
          "outSiteAmount": {
            "type": "number",
            "description": "托外金额 ,",
            "format": "double"
          },
          "outSiteId": {
            "type": "integer",
            "description": "托外商id ,",
            "format": "int32"
          },
          "outSiteType": {
            "type": "integer",
            "description": "托外商类型：0-考拉修理厂，1-合作修理厂，3-供应商; ,",
            "format": "int32"
          },
          "priceMaterial": {
            "type": "number",
            "description": "材料费 ,",
            "format": "double"
          },
          "priceService": {
            "type": "number",
            "description": "服务费 ,",
            "format": "double"
          },
          "qualityStatus": {
            "type": "integer",
            "description": "质检状态：0-不通过，1-通过 ,",
            "format": "int32"
          },
          "qualityTestStaff": {
            "type": "integer",
            "description": "质检人工号 ,",
            "format": "int32"
          },
          "serviceSubItemId": {
            "type": "integer",
            "description": "类别Id ,",
            "format": "int32"
          },
          "serviceTypeName": {
            "type": "string",
            "description": "类别名称",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.PushRepairInfoDto": {
        "type": "object",
        "properties": {
          "repairId": {
            "type": "string",
            "description": "维修单号",
            "nullable": true
          },
          "isApproval": {
            "type": "boolean",
            "description": "是否审核"
          },
          "isOutsite": {
            "type": "boolean",
            "description": "是否托外：0-否，1-是 ,"
          },
          "itemCount": {
            "type": "integer",
            "description": "数量",
            "format": "int32"
          },
          "itemName": {
            "type": "string",
            "description": "项目名称",
            "nullable": true
          },
          "maintainStaff": {
            "type": "integer",
            "description": "维修员工工号",
            "format": "int32"
          },
          "materialsId": {
            "type": "integer",
            "description": "材料Id ,",
            "format": "int32"
          },
          "outsiteAmount": {
            "type": "number",
            "description": "托外金额 ,",
            "format": "double"
          },
          "outsiteId": {
            "type": "string",
            "description": "托外商id ,",
            "nullable": true
          },
          "outsiteType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.OutsiteType"
          },
          "priceMaterial": {
            "type": "number",
            "description": "材料费 ,",
            "format": "double"
          },
          "priceService": {
            "type": "number",
            "description": "服务费 ,",
            "format": "double"
          },
          "qualityStatus": {
            "type": "boolean",
            "description": "质检状态：0-不通过，1-通过 ,"
          },
          "qualityTestStaff": {
            "type": "integer",
            "description": "质检人工号 ,",
            "format": "int32"
          },
          "serviceSubItemId": {
            "type": "integer",
            "description": "类别Id ,",
            "format": "int32",
            "nullable": true
          },
          "serviceTypeName": {
            "type": "string",
            "description": "类别名称",
            "nullable": true
          },
          "oprNo": {
            "type": "string",
            "description": "操作人",
            "nullable": true
          },
          "notPassReasons": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.NotPassReasonFlag"
            },
            "description": "未通过原因",
            "nullable": true
          },
          "noHasInvoiceDoc": {
            "type": "boolean",
            "description": "是否有发票"
          },
          "invoiceFiles": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.Infrastructure.QueryModel.NameValueDto`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"
            },
            "description": "发票附件集合",
            "nullable": true
          },
          "isFeeConfirmed": {
            "type": "boolean",
            "description": "费用待确认",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "维保详情"
      },
      "Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.SaveKaolaReserveInPut": {
        "type": "object",
        "properties": {
          "carNo": {
            "type": "string",
            "description": "车牌号码",
            "nullable": true
          },
          "customerName": {
            "type": "string",
            "description": "客户姓名",
            "nullable": true
          },
          "phone": {
            "type": "string",
            "description": "联系电话",
            "nullable": true
          },
          "cityId": {
            "type": "integer",
            "description": "城市ID",
            "format": "int32"
          },
          "cityName": {
            "type": "string",
            "description": "城市名称",
            "nullable": true
          },
          "repeatShopId": {
            "type": "integer",
            "description": "维修厂ID",
            "format": "int32"
          },
          "repeatShopName": {
            "type": "string",
            "description": "店铺名称",
            "nullable": true
          },
          "type": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RepairType"
            },
            "description": "类型ID 1 维修 2保养",
            "nullable": true
          },
          "reserveTime": {
            "type": "string",
            "description": "预约日期",
            "format": "date-time"
          },
          "period": {
            "type": "string",
            "description": "时段",
            "nullable": true
          },
          "reMark": {
            "type": "string",
            "description": "备注",
            "nullable": true
          },
          "bizType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.BizTypes"
          },
          "acctId": {
            "type": "string",
            "description": "政企Id",
            "nullable": true
          },
          "vinNo": {
            "type": "string",
            "description": "车架号",
            "nullable": true
          },
          "carNature": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.CarNatures"
          },
          "rentType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Enums.RentTypes"
          },
          "isContinue": {
            "type": "boolean",
            "description": "是否生成审核流"
          }
        },
        "additionalProperties": false,
        "description": "考拉预约入参"
      },
      "Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetBankDto": {
        "type": "object",
        "properties": {
          "description": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "id": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "extraInfo": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "isSelect": {
            "type": "boolean",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetCitiesDto": {
        "type": "object",
        "properties": {
          "description": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "id": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "extraInfo": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "isSelect": {
            "type": "boolean",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetReimburseInfoAuditsDto": {
        "type": "object",
        "properties": {
          "auditUserName": {
            "type": "string",
            "description": "审核人姓名",
            "nullable": true
          },
          "auditUserCode": {
            "type": "string",
            "description": "审核人编码",
            "nullable": true
          },
          "auditDateTime": {
            "type": "string",
            "description": "审核时间",
            "nullable": true
          },
          "auditStatusName": {
            "type": "string",
            "description": "审核状态名",
            "nullable": true
          },
          "auditComments": {
            "type": "string",
            "description": "审核备注",
            "nullable": true
          },
          "auditTypeName": {
            "type": "string",
            "description": "首选/追加",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "审核历史记录"
      },
      "Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetReimburseInfoOutPut": {
        "type": "object",
        "properties": {
          "audits": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetReimburseInfoAuditsDto"
            },
            "description": "审核记录列表",
            "nullable": true
          },
          "finStatusCode": {
            "type": "string",
            "description": "财务状态编码",
            "nullable": true
          },
          "finStatusName": {
            "type": "string",
            "description": "财务状态名称",
            "nullable": true
          },
          "statusCode": {
            "type": "string",
            "description": "审核状态编码",
            "nullable": true
          },
          "statusName": {
            "type": "string",
            "description": "审核状态名称",
            "nullable": true
          },
          "priceTotal": {
            "type": "number",
            "description": "总额",
            "format": "double",
            "nullable": true
          },
          "bxNo": {
            "type": "string",
            "description": "报销流水号",
            "nullable": true
          },
          "auditStatusChildType": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Reimbursement.Enums.AuditStatusChildType"
          },
          "finaceTime": {
            "type": "string",
            "description": "打款时间",
            "format": "date-time",
            "nullable": true
          },
          "bankRefundStatus": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.BankRefund.enum.BankRefundStatus"
          },
          "creationTime": {
            "type": "string",
            "description": "创建时间",
            "format": "date-time",
            "nullable": true
          },
          "creationUserName": {
            "type": "string",
            "description": "创建人姓名",
            "nullable": true
          },
          "creationUserNo": {
            "type": "string",
            "description": "创建人工号",
            "nullable": true
          },
          "statusChildDesc": {
            "type": "string",
            "description": "打款子状态描述",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false,
        "description": "报销信息"
      },
      "Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetSubBankDto": {
        "type": "object",
        "properties": {
          "description": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "id": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "extraInfo": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "isSelect": {
            "type": "boolean",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Corp.AfterSale.Core.Infrastructure.QueryModel.NameValueDto`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "value": {
            "type": "string",
            "description": "",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": ""
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentInfosDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetAfterSaleAccidentInfoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.GetAfterSaleAccidentInfoOutPut"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.RepairItemPriceRulesDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.RepairItemPriceRulesDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Annual.Dto.GetAnnualInspectionsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Annual.Dto.GetAnnualInspectionsDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintInfosDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAccessLogsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAccessLogsDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetEarlyApplyInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetEarlyApplyInfosDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetFieldsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetFieldsDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetJgTicketDetailsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetJgTicketDetailsDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintainAlarmsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintainAlarmsDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintenanceInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintenanceInfosDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOperationLogsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOperationLogsDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosDto"
            },
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "Eo.Aegis.Session.UserInfoSourceType": {
        "enum": [
          0,
          1
        ],
        "type": "integer",
        "format": "int32"
      },
      "Eo.Common.Enums.MessageContentType": {
        "enum": [
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "format": "int32"
      },
      "Eo.Common.SignalR.Dto.GetNotificationDetailDto": {
        "type": "object",
        "properties": {
          "messageTitle": {
            "type": "string",
            "nullable": true
          },
          "content": {
            "type": "string",
            "nullable": true
          },
          "isRead": {
            "type": "boolean"
          },
          "contentType": {
            "$ref": "#/components/schemas/Eo.Common.Enums.MessageContentType"
          }
        },
        "additionalProperties": false
      },
      "Eo.Common.SignalR.Dto.GetUserNotificationsDto": {
        "type": "object",
        "properties": {
          "messageId": {
            "type": "string",
            "nullable": true
          },
          "isRead": {
            "type": "boolean"
          },
          "messageTitle": {
            "type": "string",
            "nullable": true
          },
          "creationTime": {
            "type": "string",
            "format": "date-time"
          }
        },
        "additionalProperties": false
      },
      "Eo.Common.SignalR.Dto.GetUserNotificationsOutPut": {
        "type": "object",
        "properties": {
          "totalCount": {
            "type": "integer",
            "format": "int32"
          },
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Eo.Common.SignalR.Dto.GetUserNotificationsDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "Eo.Common.SignalR.Dto.ReadAllInput": {
        "type": "object",
        "properties": {
          "userId": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "Eo.Common.SignalR.Dto.TargetMessageReadInput": {
        "type": "object",
        "properties": {
          "messageId": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "Microsoft.AspNetCore.Mvc.ActionResult": {
        "type": "object",
        "additionalProperties": false
      },
      "PlatformEnum": {
        "enum": [
          "HasFlag",
          "Equals",
          "GetHashCode",
          "CompareTo",
          "ToString",
          "ToString",
          "GetTypeCode",
          "GetType",
          "value__",
          "Unknown",
          "MyEhi",
          "Booking",
          "CallCenter",
          "EhiClub",
          "Limo",
          "Mobile",
          "Iphone",
          "Android",
          "Channel",
          "WebService",
          "DriveBackground",
          "ChargeManager",
          "TransferService",
          "None",
          "International",
          "Account",
          "WWW",
          "EnterpriseDrive",
          "AndroidAccountTransferService",
          "IphoneAccountTransferService",
          "StorePad",
          "PaymentCenter",
          "Market",
          "MarketH5",
          "GPSCustomer",
          "FastCar",
          "WeChatApp",
          "InterfaceApi",
          "UserApi",
          "Cms",
          "Test",
          "ApiWork",
          "UserWork",
          "InvoiceApi",
          "EnterpriseCarRental",
          "ThirdPartyApi",
          "NewLongCharter",
          "HcCarWeb",
          "HcCarApi",
          "EnterpriseService",
          "CrmApi",
          "AlipayApp",
          "OldCrm",
          "Crm",
          "App",
          "OpenApi",
          "EnterpriseCarRentalApi",
          "PortalsApi",
          "CarSaleApi",
          "ComputingCenter",
          "RiskControlApi",
          "CsPrice",
          "ChannelApi",
          "PaymentApi",
          "EnterpriseMiniProgram",
          "EnterpriseExchangeCar",
          "ItWork",
          "Bookingmgmt",
          "MCKWeChatApp",
          "FastApp",
          "JobApi",
          "Store",
          "SecurityApi",
          "BiduMiniApp",
          "SalesWorkService",
          "Login",
          "ApiGateway",
          "PortalsService",
          "News",
          "Engilsh",
          "InternationalApi",
          "CrmWork",
          "Bx",
          "MobileApi",
          "PriceApi",
          "TripApi",
          "Zjht",
          "Dj",
          "TouTiaoApp",
          "WinOnlyApi",
          "CsSettlementApi",
          "CarServiceApi",
          "ZjhtStockApi",
          "ManageMgr",
          "InsuranceMgr",
          "VehicleMgr",
          "SettlementMgr",
          "ZjhtOrderApi",
          "ZjhtPriceApi",
          "ZjhtCarApi",
          "ZjhtCarTypeApi",
          "ZjhtStoreApi",
          "StockApi",
          "StockWork",
          "PriceWork",
          "MessageApi",
          "CallCenterApi",
          "CsOrderApi",
          "AppMarket",
          "FrontApiGateway",
          "SpecialCarService",
          "DriverApi",
          "DispatchApi",
          "Pay",
          "PaymentWork",
          "ThirdPartyWork",
          "CredentialSys",
          "ExpenseSys",
          "QqMiniApp",
          "CsAccountApi",
          "SpecialChannelService",
          "DriverMis",
          "MessageWork",
          "PriceSpider",
          "BookingMgmt_DjLong",
          "EnterpriseCarRentalWork",
          "BookingApi",
          "OperationWork",
          "EnglishBooking",
          "CsJobApi",
          "JobManagementApi",
          "DriverWork",
          "OperationApi",
          "CarApi",
          "InvoiceWork",
          "MarketingMessageWork",
          "SettlementApi",
          "SettlementWork",
          "ManageApi",
          "ManageWork",
          "ViolationApi",
          "ViolationWork",
          "StoreApi",
          "EmH5",
          "ZhuanCheWeb",
          "PadH5",
          "AvailabilityManagerApi",
          "KoalaApp",
          "KoalaMp",
          "CarSupportApi",
          "ReimburseApi",
          "Reimburse",
          "ContractApi",
          "Contract",
          "CorpServiceApi",
          "TripApiWorker",
          "SalesWork",
          "GaoDeMiniApp",
          "DjEoWork",
          "PersonnelApi",
          "ReimburseWeb",
          "KouBeiMiniApp",
          "YoukuMiniApp",
          "ReimburseWork",
          "CsSettlementWork",
          "AlipayCarApplet",
          "WechatCarApplet",
          "JdMiniApp",
          "IdentityApi",
          "DjEoJob",
          "ChannelInternalApi",
          "MarketingDataApi",
          "OrderMessageWork",
          "CorpService",
          "StoreWork",
          "PortalServiceWork",
          "CrmCoreApi",
          "DriverPadApi",
          "DjEoApi",
          "UserCoreApi",
          "CarSupport",
          "CorpWeChatApp",
          "CrmMessageWork",
          "RiskControlWork",
          "CrmHangFireWork",
          "UserMessageWork",
          "CarWork",
          "KoalaReimburseApi",
          "KoalaReimburse",
          "KoalaLoginApi",
          "Privilege",
          "ReimburseMentApi",
          "HrApi",
          "QxApi",
          "BxApi",
          "CrmWorkflow",
          "CorpAfterSaleApi",
          "HuaweiApp",
          "EtcCustomerService",
          "UploadFileApi",
          "CsSupplier",
          "CsAccountWork",
          "KoalaContractApi",
          "KoalaContractWork",
          "KoalaContractWeb",
          "KoalaContract",
          "KoalaReimburseWork",
          "KoalaPersonnelApi",
          "OaItApi",
          "KoalaOaCampus",
          "OaCampus",
          "ContractWork",
          "AfterSaleWork",
          "CarLeaseApi",
          "CarLeaseWork",
          "DriverAppApi",
          "ApiGatewayInternal",
          "CsEnterpriseCarRentalApi",
          "CsEnterpriseCarRentalWork",
          "HiCar",
          "ShortLink",
          "UserHangFireWork",
          "ChannelService",
          "ShortLinkAdminApi",
          "GpsApi",
          "GpsWork",
          "Sample",
          "CarClueApp",
          "WorkflowApi",
          "CarSaleWork",
          "RiskApi",
          "Java",
          "KoalaCostControl",
          "KoalaCostControlApi",
          "KoalaCostControlWork",
          "RiskMessageWork",
          "ViolationSystem",
          "CarSaleIOS",
          "CarSaleAndroid",
          "KoalaWorkflowApi",
          "KoalaWorkflowWeb",
          "UserAssetsApi",
          "InsuranceApi",
          "CarCoreApi",
          "InsuranceWork",
          "CarCoreWork",
          "SettlementPay",
          "SettlementPayWork",
          "MyLogin",
          "UserAssetsMessageWork",
          "CorearcHealthcheck",
          "HubApi",
          "HubWork",
          "AzData",
          "KoalaNHComWxApp",
          "KoalaExternalSupplierApi",
          "HiCarWork",
          "FileUp",
          "AppMgmtApi",
          "UserAdminNew",
          "CarSupportWork",
          "LibraryApi",
          "StockDapr",
          "SettlementData",
          "SettlementDataWork",
          "StoreOnlineService",
          "BookingApiWork",
          "ThirdPartyCoreApi",
          "ThirdPartyMessageWork",
          "CsOrderWork",
          "ChannelPortalsApi",
          "CarCoreDapr",
          "OaExternalApi",
          "OaApi",
          "ContractWeb",
          "Mzc",
          "Enterprise",
          "ZcOrderAudit",
          "Supplier",
          "UserManagerApi",
          "UserAuthApi",
          "CmsApi",
          "MessageEmailWork",
          "EnterpriseServiceWork",
          "MarketingDevHealthCheck",
          "MEnterprise",
          "OaExternalWork",
          "FoundationLibrary",
          "SpecialChannelWork",
          "CallCenterWork",
          "eGPTApi",
          "CarAssetsApi",
          "CarAssetsWork",
          "StoreApp",
          "ChannelMessageWork",
          "DispatchWork",
          "DataXApi",
          "DataXSync",
          "DataXScheduler",
          "KoalaReimbursePro",
          "MeiTuanMiniApp",
          "CrmMarketingWork",
          "ClientLogin",
          "MarketingDataWork",
          "Service",
          "HarmonyOS",
          "Report",
          "SignalRHub",
          "MessagingBridge",
          "EnterpriseChannel",
          "InternationalApiWork",
          "KoalaPersonnelWork",
          "CarServiceWork",
          "MarketApi",
          "Operations",
          "MarketWork",
          "ContentApi",
          "ContentWork",
          "QuestionnaireApi",
          "ExternApi",
          "EhiGptApi",
          "QuestionnaireWork",
          "MQuestionnaire",
          "SettlementDataHub",
          "SettlementDataHubWork",
          "OaWork",
          "AssetH5Service",
          "AssetH5",
          "AdminLoginSupplier",
          "IphoneWatch",
          "AndroidWatch",
          "HarmonyOSWatch",
          "DataEngineService",
          "DataEngineH5",
          "FsApi",
          "MessageService",
          "BasicWork",
          "OaOfficeWeb",
          "OaOfficeH5",
          "KoalaRepairWeb",
          "SettlementCenter",
          "SettlementCenterWork",
          "SettlementCenterHangfireWork",
          "MarketingFlowApi",
          "VoipApi",
          "VoipWork",
          "AiGateway",
          "DataEngine",
          "ExternService",
          "CrowdSourcingApp",
          "HiTuApi",
          "OperationAdminApi",
          "OperationAdminWork",
          "HiTuWork"
        ],
        "type": "string",
        "default": "CorpAfterSaleApi"
      },
      "System.Collections.Generic.KeyValuePair`2[[System.Decimal, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Decimal, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "key": {
            "type": "number",
            "format": "double"
          },
          "value": {
            "type": "number",
            "format": "double"
          }
        },
        "additionalProperties": false
      },
      "System.Collections.Generic.KeyValuePair`2[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[Microsoft.Extensions.Primitives.StringValues, Microsoft.Extensions.Primitives, Version=10.0.0.0, Culture=neutral, PublicKeyToken=adb9793829ddae60]]": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "nullable": true
          },
          "value": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "additionalProperties": false
      },
      "eHi.CallCenter.Dto.Dto.CreateTaskInputDto": {
        "type": "object",
        "properties": {
          "customerName": {
            "type": "string",
            "nullable": true
          },
          "taskDesc": {
            "type": "string",
            "nullable": true
          },
          "priority": {
            "$ref": "#/components/schemas/eHi.CallCenter.Dto.Enum.TaskPriority"
          },
          "taskTypeId": {
            "type": "integer",
            "format": "int32"
          },
          "oprNo": {
            "type": "string",
            "nullable": true
          },
          "phoneNumber": {
            "type": "string",
            "nullable": true
          },
          "source": {
            "$ref": "#/components/schemas/eHi.CallCenter.Dto.Enum.TaskSource"
          },
          "orderId": {
            "type": "string",
            "nullable": true
          },
          "mailAddress": {
            "type": "string",
            "nullable": true
          },
          "imagePath": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.CallCenter.Dto.Enum.TaskPriority": {
        "enum": [
          1,
          2,
          3
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.CallCenter.Dto.Enum.TaskSource": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Car.Dto.Base.PushAnnualInspectionInPut": {
        "type": "object",
        "properties": {
          "ecCarId": {
            "type": "integer",
            "format": "int32"
          },
          "carNo": {
            "type": "string",
            "nullable": true
          },
          "dateNextCheck": {
            "type": "string",
            "format": "date-time"
          }
        },
        "additionalProperties": false
      },
      "eHi.Car.Dto.Enum.PowerType": {
        "enum": [
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.CarSupport.Dto.AccidentRescue.AccidentRescueRepairItemOdto": {
        "type": "object",
        "properties": {
          "rescueId": {
            "type": "integer",
            "format": "int32"
          },
          "serviceTypeName": {
            "type": "string",
            "nullable": true
          },
          "itemId": {
            "type": "integer",
            "format": "int32"
          },
          "itemName": {
            "type": "string",
            "nullable": true
          },
          "itemCount": {
            "type": "integer",
            "format": "int32"
          },
          "priceMaterial": {
            "type": "number",
            "format": "double"
          },
          "isCustomerUpload": {
            "type": "boolean"
          },
          "isFeePendingConfirm": {
            "type": "boolean",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.CarSupport.Dto.AccidentRescue.ModelAccidentOrderOdto": {
        "type": "object",
        "properties": {
          "accidentRescueId": {
            "type": "integer",
            "format": "int32"
          },
          "rescueId": {
            "type": "integer",
            "format": "int32"
          },
          "rescueNo": {
            "type": "string",
            "nullable": true
          },
          "faultDescription": {
            "type": "string",
            "nullable": true
          },
          "rescueStoreId": {
            "type": "integer",
            "format": "int32"
          },
          "rescueStoreName": {
            "type": "string",
            "nullable": true
          },
          "faultCityId": {
            "type": "integer",
            "format": "int32"
          },
          "faultLocation": {
            "type": "string",
            "nullable": true
          },
          "faultLocationLong": {
            "type": "number",
            "format": "double"
          },
          "faultLocationLat": {
            "type": "number",
            "format": "double"
          },
          "rescueType": {
            "type": "integer",
            "format": "int32"
          },
          "rescueTypeDesc": {
            "type": "string",
            "nullable": true
          },
          "faultType": {
            "type": "integer",
            "format": "int32"
          },
          "faultTypeDesc": {
            "type": "string",
            "nullable": true
          },
          "faultTypeOne": {
            "type": "integer",
            "format": "int32"
          },
          "faultTypeOneDesc": {
            "type": "string",
            "nullable": true
          },
          "faultTypeSecond": {
            "type": "integer",
            "format": "int32"
          },
          "faultTypeSecondDesc": {
            "type": "string",
            "nullable": true
          },
          "isEmergency": {
            "type": "boolean"
          },
          "isCarSelf": {
            "type": "boolean"
          },
          "isScene": {
            "type": "boolean",
            "nullable": true
          },
          "isNeedCompensation": {
            "type": "boolean"
          },
          "carSelfType": {
            "type": "boolean"
          },
          "isCarChange": {
            "type": "boolean"
          },
          "rescueWay": {
            "type": "integer",
            "format": "int32"
          },
          "rescueWayDesc": {
            "type": "string",
            "nullable": true
          },
          "flowRescueWay": {
            "type": "integer",
            "format": "int32"
          },
          "flowRescueWayDesc": {
            "type": "string",
            "nullable": true
          },
          "dockingCode": {
            "type": "string",
            "nullable": true
          },
          "dockingName": {
            "type": "string",
            "nullable": true
          },
          "dockingPhoneNo": {
            "type": "string",
            "nullable": true
          },
          "repairNo": {
            "type": "string",
            "nullable": true
          },
          "kaolaRescueNo": {
            "type": "string",
            "nullable": true
          },
          "kolaStoreId": {
            "type": "integer",
            "format": "int32"
          },
          "kolaStoreName": {
            "type": "string",
            "nullable": true
          },
          "flowStoreId": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "flowStoreName": {
            "type": "string",
            "nullable": true
          },
          "repairAmount": {
            "type": "number",
            "format": "double"
          },
          "specificCause": {
            "type": "string",
            "nullable": true
          },
          "rescuer": {
            "type": "string",
            "nullable": true
          },
          "rescuerName": {
            "type": "string",
            "nullable": true
          },
          "rescuerPhoneNo": {
            "type": "string",
            "nullable": true
          },
          "rescueComments": {
            "type": "string",
            "nullable": true
          },
          "processModeStatus": {
            "type": "integer",
            "format": "int32"
          },
          "faultFactors": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "faultFactorsDesc": {
            "type": "integer",
            "format": "int32"
          },
          "faultReasonDesc": {
            "type": "string",
            "nullable": true
          },
          "ortherRpFeeType": {
            "type": "integer",
            "format": "int32"
          },
          "ortherRpFee": {
            "type": "number",
            "format": "double"
          },
          "accidentRescue": {
            "type": "integer",
            "format": "int32"
          },
          "currentMile": {
            "type": "number",
            "format": "double"
          },
          "repairReason": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "isSelfToKoala": {
            "type": "boolean",
            "nullable": true
          },
          "repairShopName": {
            "type": "string",
            "nullable": true
          },
          "repairShopPhone": {
            "type": "string",
            "nullable": true
          },
          "isCustomerUpload": {
            "type": "boolean",
            "nullable": true
          },
          "uploadStoreId": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "distanceToWorkshop": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "totalCount": {
            "type": "integer",
            "format": "int32"
          },
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "reimburseId": {
            "type": "integer",
            "format": "int32"
          },
          "reimburseApprovalStatus": {
            "type": "integer",
            "format": "int32"
          },
          "orderId": {
            "type": "string",
            "nullable": true
          },
          "inComingCallTime": {
            "type": "string",
            "format": "date-time"
          },
          "customerType": {
            "type": "integer",
            "format": "int32"
          },
          "customerTypeDesc": {
            "type": "string",
            "nullable": true
          },
          "carNo": {
            "type": "string",
            "nullable": true
          },
          "carType": {
            "type": "integer",
            "format": "int32"
          },
          "carTypeDesc": {
            "type": "string",
            "nullable": true
          },
          "region": {
            "type": "string",
            "nullable": true
          },
          "cityId": {
            "type": "integer",
            "format": "int32"
          },
          "cityName": {
            "type": "string",
            "nullable": true
          },
          "storeId": {
            "type": "integer",
            "format": "int32"
          },
          "storeName": {
            "type": "string",
            "nullable": true
          },
          "dropoffStoreId": {
            "type": "integer",
            "format": "int32"
          },
          "telephoneNumber": {
            "type": "string",
            "nullable": true
          },
          "telephoneNumberEnc": {
            "type": "string",
            "nullable": true
          },
          "customerName": {
            "type": "string",
            "nullable": true
          },
          "registrant": {
            "type": "string",
            "nullable": true
          },
          "registerTelephone": {
            "type": "string",
            "nullable": true
          },
          "registerTelephoneEnc": {
            "type": "string",
            "nullable": true
          },
          "statusType": {
            "type": "integer",
            "format": "int32"
          },
          "statusTypeDesc": {
            "type": "string",
            "nullable": true
          },
          "flowStatusType": {
            "type": "integer",
            "format": "int32"
          },
          "flowStatusTypeDesc": {
            "type": "string",
            "nullable": true
          },
          "cancelType": {
            "type": "integer",
            "format": "int32"
          },
          "isOverTime": {
            "type": "boolean"
          },
          "overTimeStatus": {
            "type": "integer",
            "format": "int32"
          },
          "consumeTime": {
            "type": "integer",
            "format": "int32"
          },
          "customerDocumentary": {
            "type": "string",
            "nullable": true
          },
          "customerDocumentaryName": {
            "type": "string",
            "nullable": true
          },
          "remarks": {
            "type": "string",
            "nullable": true
          },
          "cancelRemarks": {
            "type": "string",
            "nullable": true
          },
          "reviewReason": {
            "type": "string",
            "nullable": true
          },
          "oprComments": {
            "type": "string",
            "nullable": true
          },
          "createTime": {
            "type": "string",
            "format": "date-time"
          },
          "lastModifyTime": {
            "type": "string",
            "format": "date-time"
          },
          "isDeleted": {
            "type": "boolean"
          },
          "pickUpCarTime": {
            "type": "string",
            "format": "date-time"
          },
          "callStatus": {
            "type": "integer",
            "format": "int32"
          },
          "callStatusName": {
            "type": "string",
            "nullable": true
          },
          "rescuePlatform": {
            "type": "integer",
            "format": "int32"
          },
          "priceAuditLable": {
            "type": "string",
            "nullable": true
          },
          "repairItemList": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.CarSupport.Dto.AccidentRescue.AccidentRescueRepairItemOdto"
            },
            "nullable": true
          },
          "orderStartMile": {
            "type": "number",
            "format": "double"
          },
          "orderEndMile": {
            "type": "number",
            "format": "double"
          },
          "isCarSaleVehicle": {
            "type": "integer",
            "format": "int32"
          },
          "salesmanName": {
            "type": "string",
            "nullable": true
          },
          "enterpriseName": {
            "type": "string",
            "nullable": true
          },
          "maintenanceManName": {
            "type": "string",
            "nullable": true
          },
          "flowRemark": {
            "type": "string",
            "nullable": true
          },
          "revisitStatus": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "wasFlowed": {
            "type": "integer",
            "format": "int32"
          },
          "rescueFee": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "isRescueFeePaid": {
            "type": "boolean"
          },
          "carTierAdjustment": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "carTierAdjustmentDesc": {
            "type": "string",
            "nullable": true
          },
          "orderEnterer": {
            "type": "string",
            "nullable": true
          },
          "lastMaintenanceMileage": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "lastMaintenanceTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "repairShopDealerType": {
            "$ref": "#/components/schemas/eHi.CarSupport.Dto.AccidentRescue.RepairShopDealerType"
          }
        },
        "additionalProperties": false
      },
      "eHi.CarSupport.Dto.AccidentRescue.RepairShopDealerType": {
        "enum": [
          1,
          2
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.AfterSale.Dto.AddRepairApplyLicenseAttachesInput": {
        "type": "object",
        "properties": {
          "repairId": {
            "type": "string",
            "nullable": true
          },
          "fileInfos": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.AfterSale.Dto.AttachDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.AfterSale.Dto.AttachDto": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "nullable": true
          },
          "url": {
            "type": "string",
            "nullable": true
          },
          "attachType": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.AfterSale.Dto.CheckAddMaintenanceOutput": {
        "type": "object",
        "properties": {
          "needSyncLong": {
            "type": "boolean"
          },
          "canMaintenance": {
            "type": "boolean"
          },
          "errorMessage": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.AfterSale.Dto.RepairApplyLicenseAttachDto": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "nullable": true
          },
          "url": {
            "type": "string",
            "nullable": true
          },
          "attachType": {
            "$ref": "#/components/schemas/eHi.Common.AfterSale.Enums.RepairAttachType"
          },
          "attachTypeDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.AfterSale.Dto.RepairCreatorDto": {
        "type": "object",
        "properties": {
          "repairId": {
            "type": "string",
            "nullable": true
          },
          "creatorUserNo": {
            "type": "string",
            "nullable": true
          },
          "creatorUserName": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.AfterSale.Enums.RepairAttachType": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          7
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.Dto.Common.ApiResult": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.ExportAccidentInfoExcelOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.ExportAccidentInfoExcelOutput"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentAnnualInspectionCountOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentAnnualInspectionCountOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentInfoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentInfoOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetOrderLinkOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Accident.Dto.GetOrderLinkOutput"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.RepairItemPriceRulesDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.RepairItemPriceRulesDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Annual.Dto.GetAnnualInspectionsCountOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Annual.Dto.GetAnnualInspectionsCountOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Common.Dto.CityNameByLocationOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.CityNameByLocationOutput"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetRepairReimburseInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.GetRepairReimburseInfosDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetRepairReimburseInfosOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.GetRepairReimburseInfosOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetUserInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.GetUserInfoDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarCarNoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarCarNoDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarKilometerDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.OcrCarKilometerDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintThreeVerifyUsersOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintThreeVerifyUsersOutput"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintTypeDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintTypeDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintVerifyLogsOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintVerifyLogsOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintInfoDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintVerifyInfosOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintVerifyInfosOutput"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.GetOrderInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.GetOrderInfoDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.GetUserOrderCountDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.GetUserOrderCountDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentSummaryDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentSummaryDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ApplyMaintenanceOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ApplyMaintenanceOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ExportExcelBaseDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ExportExcelBaseDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAccidentsForH5OutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAccidentsForH5OutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAfterSaleIndexInfoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAfterSaleIndexInfoOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAnnualInspectionCountOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAnnualInspectionCountOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyAccountInfoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyAccountInfoOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyMaintenanceInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyMaintenanceInfoDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyMaintenanceOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyMaintenanceOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyUserInfoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyUserInfoOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetEarlyApplyInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetEarlyApplyInfoDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetIndexAccidentsOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetIndexAccidentsOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetJgTicketDetailsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetJgTicketDetailsDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetLicenseInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetLicenseInfoDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOrderDetailLinkOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOrderDetailLinkOutput"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairDetailInfosByRepairIdOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairDetailInfosByRepairIdOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfoForWxDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfoForWxDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosByDriverNoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosByDriverNoOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosForWxOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosForWxOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairKmInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairKmInfoDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetTicketGroupByBizTypeOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetTicketGroupByBizTypeOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetrepairInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetrepairInfoDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReimburseMiddleResponseDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.ReimburseMiddleResponseDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.RepairRescueUrlOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.RepairRescueUrlOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.UpLoadFilesOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.UpLoadFilesOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.UserReimburseNotMatchInfosOutput, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.UserReimburseNotMatchInfosOutput"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.CoreBusiness.Accident.Manager.Dto.UpdateAccidentStateCurrentsOutput, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Accident.Manager.Dto.UpdateAccidentStateCurrentsOutput"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.CoreBusiness.Repair.Dto.GetApplyMaintenanceDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.GetApplyMaintenanceDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.CoreBusiness.Repair.Dto.GetOrderTypeExpandDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.GetOrderTypeExpandDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.CoreBusiness.Repair.Dto.ImportItemPriceRuleOutput, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Dto.ImportItemPriceRuleOutput"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.CoreBusiness.Repair.Manager.Dto.RepairItemPriceRuleDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.CoreBusiness.Repair.Manager.Dto.RepairItemPriceRuleDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.GetOrderInfoByCarNoAndTimeDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.GetOrderInfoByCarNoAndTimeDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.GetOrderTypeDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.GetOrderTypeDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.GetRepairInfoOutPut, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.DjBlockOrderApi.GetRepairInfoOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.DjEoWork.GetReimburseMiddlePageUrlOutPut, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.DjEoWork.GetReimburseMiddlePageUrlOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetWbOrderInfoDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetWbOrderInfoDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetBankDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetBankDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetCitiesDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetCitiesDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetReimburseInfoOutPut, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetReimburseInfoOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetSubBankDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetSubBankDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetAccidentInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetAfterSaleAccidentInfoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Accident.Dto.GetAfterSaleAccidentInfoOutPut, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.RepairItemPriceRulesDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.AfterSaleSetting.Dto.RepairItemPriceRulesDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Annual.Dto.GetAnnualInspectionsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Annual.Dto.GetAnnualInspectionsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.GetComplaintInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.ForDriver.Dto.GetJgAccidentDetailsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAccessLogsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAccessLogsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetEarlyApplyInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetEarlyApplyInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetFieldsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetFieldsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetJgTicketDetailsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetJgTicketDetailsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintainAlarmsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintainAlarmsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintenanceInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetMaintenanceInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOperationLogsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOperationLogsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], Eo.Aegis.DapperExtension, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Aegis.DapperExtension.Page.PageResult`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetRepairInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Common.SignalR.Dto.GetNotificationDetailDto, Eo.Common, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Common.SignalR.Dto.GetNotificationDetailDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Eo.Common.SignalR.Dto.GetUserNotificationsOutPut, Eo.Common, Version=10.0.5.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Eo.Common.SignalR.Dto.GetUserNotificationsOutPut"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[Microsoft.AspNetCore.Mvc.ActionResult, Microsoft.AspNetCore.Mvc.Core, Version=10.0.0.0, Culture=neutral, PublicKeyToken=adb9793829ddae60]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ActionResult"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Boolean, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.IEnumerable`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOperationLogsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetOperationLogsDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.IList`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetAccDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.GetAccDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetAccountsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.GetAccountsDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetAreasDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.GetAreasDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.Common.Dto.GetKaolaStationsResultDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.GetKaolaStationsResultDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfosDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Common.Dto.ResolveSensitiveInfosDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintTypeDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintTypeDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintVerifyLogsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.Complaint.Dto.ComplaintVerifyLogsDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.CustomerServiceDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.CustomerServiceDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAfterSaleRepairItemsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetAfterSaleRepairItemsDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyAccountInfoDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetApplyAccountInfoDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetIndexMaintainsDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.GetIndexMaintainsDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Application.Contracts.RepairInfo.Dto.MaintenanceRecordDto, Corp.AfterSale.Application.Contracts, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Application.Contracts.RepairInfo.Dto.MaintenanceRecordDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.CarSupportApi.GetInsuranceCustomerOutPut, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.CarSupportApi.GetInsuranceCustomerOutPut"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.DriverApi.GetDriverDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.DriverApi.GetDriverDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetDistrictsDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetDistrictsDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaoLaRepairItemsDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaoLaRepairItemsDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaCitiesDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaCitiesDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaProvincesOriginalDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaProvincesOriginalDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaRepeatShopsDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetKaolaRepeatShopsDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetRepairshopsConditionsDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetRepairshopsConditionsDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetStocksDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.KoalaRepairBillApi.GetStocksDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetBankDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetBankDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetCitiesDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetCitiesDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetSubBankDto, Corp.AfterSale.Core, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Corp.AfterSale.Core.ExternalService.Dto.ReimburseApi.GetSubBankDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[eHi.Common.AfterSale.Dto.RepairApplyLicenseAttachDto, eHi.Common.AfterSale, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.AfterSale.Dto.RepairApplyLicenseAttachDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Collections.Generic.List`1[[eHi.Common.AfterSale.Dto.RepairCreatorDto, eHi.Common.AfterSale, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]], System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.AfterSale.Dto.RepairCreatorDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.Int32, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[System.String, System.Private.CoreLib, Version=10.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[eHi.CarSupport.Dto.AccidentRescue.ModelAccidentOrderOdto, eHi.CarSupport.Dto, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/eHi.CarSupport.Dto.AccidentRescue.ModelAccidentOrderOdto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.Dto.Common.ApiResult`1[[eHi.Common.AfterSale.Dto.CheckAddMaintenanceOutput, eHi.Common.AfterSale, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]": {
        "type": "object",
        "properties": {
          "isSuccess": {
            "type": "boolean"
          },
          "errorCode": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string",
            "nullable": true
          },
          "operationId": {
            "type": "string",
            "nullable": true
          },
          "result": {
            "$ref": "#/components/schemas/eHi.Common.AfterSale.Dto.CheckAddMaintenanceOutput"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.FileInfo": {
        "type": "object",
        "properties": {
          "fileType": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.ReimburseAttachmentType"
          },
          "locationType": {
            "type": "integer",
            "format": "int32"
          },
          "categoryId": {
            "type": "integer",
            "format": "int32"
          },
          "url": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "fileName": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.Account.AccountChildType": {
        "enum": [
          0,
          1,
          2,
          3,
          4
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.BackStage.IdAndNameDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "code": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.BankRefund.enum.BankRefundStatus": {
        "enum": [
          0,
          1,
          2,
          3
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.PartVerification.PartVerificationFlag": {
        "enum": [
          0,
          1,
          2
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMain.Enum.AuditStatusChildType": {
        "enum": [
          1
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMain.Enum.CurrencyType": {
        "enum": [
          1,
          2
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMain.Enum.FinanceStatusChildType": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMain.Enum.OperationType": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11,
          12,
          13,
          14,
          15,
          16,
          17,
          18,
          19,
          20,
          21,
          22,
          23,
          24,
          25,
          26,
          27,
          28,
          29,
          30,
          31,
          32,
          33,
          34,
          35,
          36,
          37,
          38,
          39,
          40,
          41,
          42,
          43,
          44,
          45,
          46,
          47,
          48,
          49,
          50,
          51,
          52,
          53,
          54,
          55,
          56,
          57,
          58,
          59,
          60,
          61,
          62,
          63,
          64,
          65,
          66,
          67,
          68,
          69,
          70,
          71,
          72,
          73,
          74,
          75,
          76,
          77,
          78,
          79,
          80,
          81,
          82,
          83,
          84,
          85,
          86,
          87,
          88,
          89,
          90,
          91,
          92,
          93,
          94,
          95,
          96,
          97,
          98,
          99,
          100,
          101,
          102,
          103,
          104,
          105,
          106,
          107,
          108,
          109,
          110,
          111,
          112,
          113,
          114,
          115,
          116,
          117,
          118,
          119,
          120,
          121,
          122,
          123,
          124,
          125,
          126,
          127,
          128,
          129,
          130,
          131,
          132,
          133,
          134,
          135,
          136,
          137,
          138,
          139,
          140,
          141,
          142,
          143,
          144,
          145,
          146,
          147,
          148,
          149,
          150,
          151,
          152,
          153,
          154,
          155,
          156,
          157,
          158,
          159,
          160,
          161,
          162,
          163,
          164,
          165,
          166,
          167,
          168,
          169,
          170,
          171,
          172,
          173,
          174,
          175,
          176,
          177,
          178,
          179,
          180,
          181,
          182,
          183,
          184,
          185,
          186,
          187,
          188,
          189,
          190,
          191,
          192,
          193,
          194,
          195,
          196,
          197,
          198,
          199,
          200,
          201,
          202,
          203,
          204,
          205,
          206,
          207,
          208,
          209,
          210,
          211,
          212,
          213,
          214,
          215,
          216,
          217,
          218,
          219,
          220,
          221,
          222,
          223,
          224,
          225,
          226,
          227,
          228,
          229,
          230,
          231,
          232,
          233,
          234,
          235,
          236,
          237,
          238,
          239,
          240,
          241,
          242,
          243,
          244,
          245,
          246,
          247,
          248,
          249,
          250,
          251,
          252,
          253,
          254,
          255,
          256,
          257,
          258,
          259,
          260,
          261,
          262,
          263,
          264,
          265,
          266,
          267,
          268,
          269,
          270,
          271,
          272,
          273,
          274,
          275,
          276,
          277,
          278,
          279,
          280,
          281,
          282,
          283,
          284,
          285,
          286,
          287,
          288,
          289,
          290,
          291,
          292,
          293,
          294,
          295,
          296,
          297,
          298,
          299,
          300,
          301,
          302,
          303,
          304,
          305,
          306,
          307,
          308,
          309,
          310,
          311,
          312,
          313,
          314,
          315,
          316,
          317,
          318,
          319,
          320,
          321,
          322,
          323,
          324,
          325,
          326,
          327,
          328,
          329,
          330,
          331,
          332,
          333,
          334,
          335,
          336,
          337,
          338,
          339,
          340,
          341,
          342,
          343,
          344,
          345,
          346,
          347,
          348,
          349,
          350,
          351,
          352,
          353,
          354,
          355,
          356,
          357,
          358,
          359,
          360,
          361,
          362,
          363,
          364,
          365,
          366,
          367,
          368,
          369,
          370,
          371,
          372,
          373,
          374,
          375,
          376,
          377,
          378,
          379,
          380,
          381,
          382,
          383,
          384,
          385,
          386,
          387,
          388,
          389,
          390,
          391,
          392,
          393,
          394,
          395,
          396,
          397,
          398,
          399,
          400,
          401,
          402,
          403,
          404,
          405,
          406,
          407,
          408,
          409,
          410,
          411,
          412,
          413,
          414,
          415,
          416,
          417,
          418,
          419,
          420,
          421,
          422,
          423,
          424,
          425,
          426,
          427,
          428,
          429,
          430,
          431,
          432,
          433,
          434,
          435,
          436,
          437,
          438,
          439,
          440,
          441,
          442,
          443,
          444,
          445,
          446,
          447
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMain.Enum.PayType": {
        "enum": [
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11,
          12
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMain.OperationInfo": {
        "type": "object",
        "properties": {
          "operator": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.User.UserDto"
          },
          "type": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMain.Enum.OperationType"
          },
          "operationTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "connectId": {
            "type": "string",
            "nullable": true
          },
          "taskId": {
            "type": "string",
            "nullable": true
          },
          "index": {
            "type": "string",
            "nullable": true
          },
          "excelName": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ChargeOffStatus": {
        "enum": [
          0,
          1,
          2
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.Enum.InvoiceSummaryType": {
        "enum": [
          0,
          1,
          2,
          3
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.Enum.MiddlePagePlatform": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11,
          12,
          13,
          14,
          15,
          16,
          17,
          18,
          19,
          20,
          21,
          22,
          23,
          24,
          25,
          26,
          27,
          28,
          29,
          30,
          31,
          32,
          33,
          34,
          35,
          36,
          37,
          38,
          39,
          40,
          41,
          42,
          43,
          44,
          45,
          46,
          47,
          48,
          49,
          50,
          51,
          52,
          53,
          54,
          55,
          56,
          57,
          58,
          59,
          60,
          61,
          62,
          63,
          64,
          65,
          66,
          67,
          68,
          69,
          70,
          71,
          72,
          73,
          74,
          75,
          76,
          77,
          78,
          79,
          80,
          81,
          82,
          83,
          84
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.Enum.MiddlePageThirdPartBusinessType": {
        "enum": [
          0,
          1,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11,
          12,
          13,
          14,
          15
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.Enum.NameConsistencyType": {
        "enum": [
          0,
          1,
          2,
          3
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.InvoiceDetailOption": {
        "type": "object",
        "properties": {
          "ocrMainId": {
            "type": "integer",
            "format": "int32"
          },
          "amount": {
            "type": "number",
            "format": "double"
          },
          "invoiceTaxRatio": {
            "type": "integer",
            "format": "int32"
          },
          "amountNoTax": {
            "type": "number",
            "format": "double"
          },
          "amountTax": {
            "type": "number",
            "format": "double"
          },
          "invoiceTitle": {
            "type": "string",
            "nullable": true
          },
          "invoiceNo": {
            "type": "string",
            "nullable": true
          },
          "invoiceCode": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.InvoiceMiddleInfo": {
        "type": "object",
        "properties": {
          "invoiceNo": {
            "type": "string",
            "nullable": true
          },
          "faceAmount": {
            "type": "number",
            "format": "double"
          },
          "remainingAmount": {
            "type": "number",
            "format": "double"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.InvoiceReceiptOption": {
        "type": "object",
        "properties": {
          "invoiceReceiptId": {
            "type": "integer",
            "format": "int32"
          },
          "amount": {
            "type": "number",
            "format": "double"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.MainAdditionalInfo": {
        "type": "object",
        "properties": {
          "parameterName": {
            "type": "string",
            "nullable": true
          },
          "htmlValue": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.MiddleInvoiceInfo": {
        "type": "object",
        "properties": {
          "url": {
            "type": "string",
            "nullable": true
          },
          "name": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleDetail": {
        "type": "object",
        "properties": {
          "basicInfo": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleDetailBasic"
          },
          "optionInfo": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleDetailOption"
          },
          "childDetails": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleSubDetail"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleDetailBasic": {
        "type": "object",
        "properties": {
          "expenseId": {
            "type": "integer",
            "format": "int32"
          },
          "startTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "endTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "amount": {
            "type": "number",
            "format": "double"
          },
          "count": {
            "type": "integer",
            "format": "int32"
          },
          "note": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "expenseDesc": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleDetailOption": {
        "required": [
          "ExpenseListID"
        ],
        "type": "object",
        "properties": {
          "isOurCompanyCarNo": {
            "type": "boolean",
            "nullable": true
          },
          "carPowerType": {
            "$ref": "#/components/schemas/eHi.Car.Dto.Enum.PowerType"
          },
          "finalAuditGroupId": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "subCompanyId": {
            "type": "integer",
            "format": "int32"
          },
          "invoiceTitle": {
            "type": "string",
            "nullable": true
          },
          "invoiceDetailOptions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.InvoiceDetailOption"
            },
            "nullable": true
          },
          "invoiceReceiptOptions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.InvoiceReceiptOption"
            },
            "nullable": true
          },
          "BudgetYear": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "DetailID": {
            "type": "integer",
            "format": "int32"
          },
          "ExpenseListID": {
            "type": "integer",
            "format": "int32",
            "deprecated": true
          },
          "expenseName": {
            "maxLength": -1,
            "type": "string",
            "nullable": true,
            "deprecated": true
          },
          "carNo": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "priceUnit": {
            "type": "number",
            "format": "double",
            "deprecated": true
          },
          "priceCount": {
            "type": "integer",
            "format": "int32",
            "deprecated": true
          },
          "year": {
            "type": "string",
            "nullable": true,
            "deprecated": true
          },
          "month": {
            "type": "string",
            "nullable": true,
            "deprecated": true
          },
          "front_day": {
            "type": "string",
            "nullable": true,
            "deprecated": true
          },
          "to_year": {
            "type": "string",
            "nullable": true,
            "deprecated": true
          },
          "to_month": {
            "type": "string",
            "nullable": true,
            "deprecated": true
          },
          "to_day": {
            "type": "string",
            "nullable": true,
            "deprecated": true
          },
          "CostID": {
            "type": "string",
            "nullable": true
          },
          "costCenter": {
            "type": "string",
            "nullable": true
          },
          "costCenterStoreInValidTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "priceSubTotal": {
            "type": "number",
            "format": "double"
          },
          "invoiceTaxRatio": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "invoiceTaxRatioDisplay": {
            "type": "string",
            "nullable": true
          },
          "priceSubTotalNoTax": {
            "type": "number",
            "format": "double"
          },
          "priceSubTax": {
            "type": "number",
            "format": "double"
          },
          "invoiceNo": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "InvoiceTypeValue": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "invoiceSummaryType": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.Enum.InvoiceSummaryType"
          },
          "InvoiceTypeName": {
            "type": "string",
            "nullable": true
          },
          "accidentDate": {
            "type": "string",
            "nullable": true
          },
          "illegalDate": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "illegalTips": {
            "type": "string",
            "nullable": true
          },
          "guid": {
            "type": "string",
            "nullable": true
          },
          "isValid": {
            "type": "boolean",
            "deprecated": true
          },
          "currencyId": {
            "type": "integer",
            "format": "int32"
          },
          "contract_no": {
            "type": "string",
            "nullable": true
          },
          "storeAddress": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "drawerParty": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "carNoTips": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "contractAmount": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "insuranceNo": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "invoiceAmount": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "confirmationNo": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "sourceDetailId": {
            "type": "integer",
            "format": "int32"
          },
          "businessType": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.Enum.MiddlePageThirdPartBusinessType"
          },
          "businessTypeDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "leaseTypes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.OA.Dto.Select"
            },
            "nullable": true
          },
          "punishmentDecisionNo": {
            "type": "string",
            "nullable": true
          },
          "invoiceOcrGitIds": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32"
            },
            "nullable": true
          },
          "invoiceReceiptIds": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "int32"
            },
            "nullable": true
          },
          "referKey": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "invoiceMiddleInfos": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.InvoiceMiddleInfo"
            },
            "nullable": true
          },
          "notCheckOcr": {
            "type": "boolean",
            "nullable": true
          },
          "civilAviationDevelopmentFundAmount": {
            "type": "number",
            "format": "double"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseAuditInfo": {
        "type": "object",
        "properties": {
          "bankRefundStatus": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.BankRefund.enum.BankRefundStatus"
          },
          "auditStatusFlag": {
            "type": "string",
            "nullable": true
          },
          "auditStatusChildType": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMain.Enum.AuditStatusChildType"
          },
          "auditStatusDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "financeStatusFlag": {
            "type": "string",
            "nullable": true
          },
          "financeStatusChildType": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMain.Enum.FinanceStatusChildType"
          },
          "financeStatusDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "auditTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "finaceTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "auditUser": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.User.UserDto"
          },
          "lastAuditUser": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.User.UserDto"
          },
          "nextAuditUser": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.User.UserDto"
          },
          "selectedAuditUser": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.User.UserDto"
          },
          "billReceiveUser": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.User.UserDto"
          },
          "billReceiveDate": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "billCancelUser": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.User.UserDto"
          },
          "billCancelDate": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "remittanceDate": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "remittanceUser": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.User.UserDto"
          },
          "refuseDate": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "refuseUser": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.User.UserDto"
          },
          "refuseNote": {
            "type": "string",
            "nullable": true
          },
          "payType": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMain.Enum.PayType"
          },
          "payTypeDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseBasicInfo": {
        "required": [
          "details",
          "oprUserCode",
          "platform",
          "typeFlag"
        ],
        "type": "object",
        "properties": {
          "partVerificationId": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "partVerificationFlag": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.PartVerification.PartVerificationFlag"
          },
          "currentPartVerificationNo": {
            "type": "string",
            "nullable": true
          },
          "referNo": {
            "type": "string",
            "nullable": true
          },
          "serialNo": {
            "type": "string",
            "nullable": true
          },
          "isLockSerialNo": {
            "type": "boolean",
            "deprecated": true
          },
          "detailUrl": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "isLockType": {
            "type": "boolean",
            "deprecated": true
          },
          "platform": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.Enum.MiddlePagePlatform"
          },
          "details": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleDetail"
            }
          },
          "typeFlag": {
            "maxLength": -1,
            "minLength": 1,
            "type": "string"
          },
          "oprUserCode": {
            "maxLength": -1,
            "minLength": 1,
            "type": "string"
          },
          "reimburseUserCode": {
            "type": "string",
            "nullable": true
          },
          "platformDesc": {
            "type": "string",
            "nullable": true
          },
          "typeDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseFunction": {
        "type": "object",
        "properties": {
          "nameConsistencyType": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.Enum.NameConsistencyType"
          },
          "nameConsistencyTypeDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "overrideCollectionTypeByContractNoIfExist": {
            "type": "boolean",
            "nullable": true
          },
          "isGoPreAuditFlow": {
            "type": "boolean",
            "nullable": true
          },
          "reimburseVersionNumber": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseVersionNumber"
          },
          "auditFlowBusinessId": {
            "type": "string",
            "nullable": true
          },
          "autoFinalAuditUserCode": {
            "type": "string",
            "nullable": true
          },
          "autoFinalAuditTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseOptionInfo": {
        "type": "object",
        "properties": {
          "chargeOffStatus": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ChargeOffStatus"
          },
          "paidAmount": {
            "type": "number",
            "format": "double"
          },
          "isInvoiceOverused": {
            "type": "boolean"
          },
          "duePaymentDate": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "isVerificationByInvoiceReceipt": {
            "type": "boolean"
          },
          "versionNumber": {
            "type": "integer",
            "format": "int32"
          },
          "supplierType": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.SupplierType"
          },
          "middleInvoiceInfos": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.MiddleInvoiceInfo"
            },
            "nullable": true
          },
          "additionalInfos": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.MainAdditionalInfo"
            },
            "nullable": true
          },
          "invoiceTitle": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "paymentTypeFlag": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "bankAccountTypeFlag": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "accountChildType": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.Account.AccountChildType"
          },
          "accountUserCode": {
            "type": "string",
            "nullable": true
          },
          "accountUserName": {
            "type": "string",
            "nullable": true
          },
          "accountNameIsOurCompanyUser": {
            "type": "boolean"
          },
          "accountName": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "bankName": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "accountNo": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "expectPaymentDate": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "note": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "subCompanyId": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "subCompanyDesc": {
            "type": "string",
            "nullable": true
          },
          "headBankDesc": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "subBankCityDesc": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "headBankCode": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "subBankOrCityCode": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "subBankCode": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "thirdPartAccountUserCode": {
            "type": "string",
            "nullable": true
          },
          "thirdPartAccountUserName": {
            "type": "string",
            "nullable": true
          },
          "thirdPartAccountNameIsOurCompanyUser": {
            "type": "boolean"
          },
          "thirdPartAccountName": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "thirdPartBankName": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "thirdPartAccountNo": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "thirdPartHeadBankDesc": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "thirdPartSubBankCityDesc": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "thirdPartHeadBankCode": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "thirdPartSubBankOrCityCode": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "thirdPartSubBankCode": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "thirdPartCollectionTypeFlag": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "thirdPartCollectionTypeFlagDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "paymentTypeDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "currencyType": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMain.Enum.CurrencyType"
          },
          "deptId": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "deptDesc": {
            "type": "string",
            "nullable": true
          },
          "auditUserId": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "auditUserName": {
            "type": "string",
            "nullable": true
          },
          "auditUserCode": {
            "type": "string",
            "nullable": true
          },
          "invoiceSubmitAddress": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "groupId": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "groupDesc": {
            "type": "string",
            "nullable": true
          },
          "parentId": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "thirdPartAddress": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "currencyTypeDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "bankAccountTypeDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "businessType": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.Enum.MiddlePageThirdPartBusinessType"
          },
          "businessTypeDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "initInfoUrl": {
            "type": "string",
            "nullable": true
          },
          "selectedThirdPartAccountId": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "selectedCompanyAccountText": {
            "type": "string",
            "nullable": true
          },
          "finalAuditUser": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.User.UserDto"
          },
          "finalAuditDate": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "finalAuditNote": {
            "maxLength": -1,
            "type": "string",
            "nullable": true
          },
          "createTime": {
            "type": "string",
            "format": "date-time"
          },
          "lastModifyTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "priceTotal": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "isBillReceived": {
            "type": "boolean"
          },
          "voucherCenterId": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "applyUserCode": {
            "type": "string",
            "nullable": true
          },
          "topTip": {
            "type": "string",
            "nullable": true
          },
          "voucherCenterSyncStatusDesc": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseSplitInfo": {
        "type": "object",
        "properties": {
          "reimburseId": {
            "type": "integer",
            "format": "int32"
          },
          "serialNo": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseThirdPartInfo": {
        "type": "object",
        "properties": {
          "reimburseUserCode": {
            "type": "string",
            "nullable": true
          },
          "canAddOrDeleteDetails": {
            "type": "boolean"
          },
          "hotelExpenseStandard": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "allowanceExpenseStandard": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "hotelExpense": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "allowance": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "postBackUrl": {
            "type": "string",
            "nullable": true
          },
          "businessType": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.Enum.MiddlePageThirdPartBusinessType"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleResponseUserInfo": {
        "type": "object",
        "properties": {
          "userId": {
            "type": "integer",
            "format": "int32"
          },
          "groupDeptId": {
            "type": "integer",
            "format": "int32"
          },
          "groupDeptDesc": {
            "type": "string",
            "nullable": true
          },
          "groupId": {
            "type": "integer",
            "format": "int32"
          },
          "groupDesc": {
            "type": "string",
            "nullable": true
          },
          "cityWorkId": {
            "type": "integer",
            "format": "int32"
          },
          "userName": {
            "type": "string",
            "nullable": true
          },
          "userCode": {
            "type": "string",
            "nullable": true
          },
          "entyTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "leaveTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "lastWorkTime": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "applyUser": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.User.UserDto"
          },
          "reimburseUser": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.User.UserDto"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleSubDetail": {
        "type": "object",
        "properties": {
          "basicInfo": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleDetailBasic"
          },
          "optionInfo": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseMiddleDetailOption"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.ReimburseVersionNumber": {
        "enum": [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Reimburse.ReimburseMiddlePage.SupplierType": {
        "enum": [
          0,
          1
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.ReimburseAttachmentType": {
        "enum": [
          0,
          1,
          2
        ],
        "type": "integer",
        "format": "int32"
      },
      "eHi.Common.OA.Dto.Select": {
        "type": "object",
        "properties": {
          "description": {
            "type": "string",
            "nullable": true
          },
          "id": {
            "type": "string",
            "nullable": true
          },
          "extraInfo": {
            "type": "string",
            "nullable": true
          },
          "isSelect": {
            "type": "boolean"
          },
          "key": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "eHi.Common.OA.Dto.User.UserDto": {
        "type": "object",
        "properties": {
          "userCode": {
            "type": "string",
            "nullable": true
          },
          "userName": {
            "type": "string",
            "nullable": true
          },
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "statusFlag": {
            "type": "string",
            "nullable": true
          },
          "statusDesc": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "userChildStatus": {
            "type": "string",
            "nullable": true
          },
          "email": {
            "type": "string",
            "nullable": true
          },
          "isLeave": {
            "type": "boolean",
            "readOnly": true
          },
          "groupDto": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.BackStage.IdAndNameDto"
          },
          "cityWork": {
            "$ref": "#/components/schemas/eHi.Common.OA.Dto.Reimburse.BackStage.IdAndNameDto"
          },
          "levelId": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "levelCode": {
            "type": "string",
            "nullable": true
          },
          "userSexId": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      }
    },
    "securitySchemes": {
      "JWT": {
        "type": "apiKey",
        "description": "JWT模式授权，请输入 Bearer <Token> 进行身份验证",
        "name": "Authorization",
        "in": "header"
      }
    }
  },
  "tags": [
    {
      "name": "Accident",
      "description": "事故"
    },
    {
      "name": "AfterSaleSetting",
      "description": "系统配置"
    },
    {
      "name": "Annual",
      "description": "年检"
    },
    {
      "name": "Common",
      "description": ""
    },
    {
      "name": "Complaint",
      "description": "客诉服务"
    },
    {
      "name": "ForAccount",
      "description": "外部系统-政企服务"
    },
    {
      "name": "ForCrm",
      "description": "CRM系统"
    },
    {
      "name": "ForDriver",
      "description": "驾管相关"
    },
    {
      "name": "ForEo",
      "description": "对长包的接口"
    },
    {
      "name": "ForH5",
      "description": "移动端专用"
    },
    {
      "name": "ForSupport",
      "description": "救援系统接口"
    },
    {
      "name": "Home",
      "description": ""
    },
    {
      "name": "Job",
      "description": "交互同步类服务接口"
    },
    {
      "name": "Repair",
      "description": "维保服务"
    },
    {
      "name": "Report",
      "description": "报表类服务接口 首页报表"
    },
    {
      "name": "SignalRNotify"
    },
    {
      "name": "Sync",
      "description": "交互同步类服务接口"
    },
    {
      "name": "Test",
      "description": ""
    }
  ]
}