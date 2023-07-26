#!/usr/bin/python
# -*- coding:GBK -*-
import json
import logging
import unittest

from k3cloud_webapi_sdk.main import K3CloudApiSdk

# ���ȹ���һ��SDKʵ��
api_sdk = K3CloudApiSdk()

# Ȼ���ʼ��SDK����ָ����ز���������ᵼ��SDK��ʼ��ʧ�ܶ��޷�ʹ�ã�

# ��ʼ������һ��Init��ʼ��������ʹ��conf.ini�����ļ�
# config_path:�����ļ�����Ի����·��������ʹ�þ���·��
# config_node:�����ļ��еĽڵ�����
api_sdk.Init(config_path='../conf.ini', config_node='config')


# ��ʼ������������������InitConfig��ʼ��������ֱ�Ӵ��Σ���ʹ�������ļ�
# acct_id:������ϵͳ��¼��Ȩ������ID,user_name:������ϵͳ��¼��Ȩ���û�,app_id:������ϵͳ��¼��Ȩ��Ӧ��ID,app_sec:������ϵͳ��¼��Ȩ��Ӧ����Կ
# server_url:k3cloud����url(��˽���ƻ�����Ҫ����),lcid:������ϵ(Ĭ��2052),org_num:��֯����(���ö���֯ʱ���ö�Ӧ����֯�������Ч)
# api_sdk.InitConfig('62e25034af8811', 'Administrator', '231784_3d9r4dHJ5OgZ4aUJwe6rTxSMVjTdWooF', 'aae9d547ffde46fe9236fdea40472854')

# �˴������챣��ӿڵĲ����ֶ�����ʾ����ʹ��ʱ��ο�WebAPI����ӿڵ�ʵ�ʲ����б�


def Check_response(res):
    res = json.loads(res)
    if res["Result"]["IsSuccess"]:
        return True
    else:
        logging.error(res)
        return False


def gl_accountbalance_GetSysReportData(**kwargs):
    """
    ��Ŀ���� (GL_RPT_AccountBalance) �Ĳ�ѯ�������ݹ���
    :param kwargs:  �滻para�в�����ʾ����
    :return:
    """
    para = {
        "FieldKeys": "FBALANCEID,FBALANCENAME,FACCTTYPE,FACCTGROUP,FDETAILNUMBER,FDETAILNAME,FCyName",
        "SchemeId": "97ffa1271acc4846b209ea05ac8dec9c",
        "StartRow": 0,
        "Limit": 2000,
        "IsVerifyBaseDataField": "false",
        "Model": {
            "FACCTBOOKID": {
                "FNumber": "001"
            },
            "FCURRENCY": "1",
            "FSTARTYEAR": "2021",
            "FSTARTPERIOD": "12",
            "FENDYEAR": "2021",
            "FBALANCELEVEL": "1",
            "FENDPERIOD": "12",
            "FFORBIDBALANCE": True,
            "FBALANCEZERO": True,
            "FPERIODNOBALANCE": True,
            "FYEARNOBALANCE": True,
        },
        "PkEntryIds": []
    }
    if kwargs:
        para.update(kwargs)
    response = api_sdk.getSysReportData("GL_RPT_AccountBalance", para)
    print("��Ŀ�������ѯ�ӿڣ�", response)
    return Check_response(response)


class glAccountBalanceTestCase(unittest.TestCase):
    def testb_voucher_Save(self):
        self.assertTrue(gl_accountbalance_GetSysReportData())


if __name__ == '__main__':
    unittest.main()
