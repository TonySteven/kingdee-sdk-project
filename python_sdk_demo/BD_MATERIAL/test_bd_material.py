#!/usr/bin/python
# -*- coding:GBK -*-
import json
import logging
import time
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
current_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
save_data = {
    "FCreateOrgId": {"FNumber": 100},
    "FUserOrgId": {"FNumber": 100},
    "FNumber": "xtwl" + current_time + "10001",
    "FName": "��������" + current_time + "10001"
}
FNumber = "xtwl" + current_time + "10001"


def Check_response(res):
    res = json.loads(res)
    if res["Result"]["ResponseStatus"]["IsSuccess"]:
        return True
    else:
        logging.error(res)
        return False


def material_ExecuteBillQuery(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) �ĵ��ݲ�ѯ����
    :param kwargs:  �滻para�в�����ʾ����FieldKeys=��Fname",Limit=1000
    :return:
    """
    para = {
        "FormId": "BD_MATERIAL",
        "FieldKeys": "FName,FNumber",
        "FilterString": "'FNumber'=""",
        "OrderString": "",
        "TopRowCount": 100,
        "StartRow": 0,
        "Limit": 2000,
        "SubSystemId": ""
    }
    if kwargs:
        para.update(kwargs)
    response = api_sdk.ExecuteBillQuery(para)
    print("���ϵ��ݲ�ѯ�ӿڣ�" + response)
    res = json.loads(response)
    if len(res) > 0:
        return True
    return False


def material_Save(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) �ı��湦��
    :param kwargs:  �滻para�в�����ʾ���� Model = {"FCreateOrgId": {"FNumber": 100},"FUserOrgId": {"FNumber": 100},"FNumber": "Webb10001","FName": "��������10001"}
    :return:
    """
    para = {
        "NeedUpDateFields": [],
        "NeedReturnFields": [],
        "IsDeleteEntry": "True",
        "SubSystemId": "",
        "IsVerifyBaseDataField": "False",
        "IsEntryBatchFill": "True",
        "ValidateFlag": "True",
        "NumberSearch": "True",
        "IsAutoAdjustField": "False",
        "InterationFlags": "",
        "IgnoreInterationFlag": "",
        "IsControlPrecision": "False",
        "Model": {}
    }
    if kwargs:
        para.update(kwargs)
    response = api_sdk.Save("BD_Material", para)
    print("���ϱ���ӿڣ�", response)
    if Check_response(response):
        res = json.loads(response)
        materialid = res["Result"]["Id"]
        return Check_response(response), materialid
    return False, ""


def material_Submit(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) ���ύ����
    :param kwargs:  �滻para�в�����ʾ����   Numbers = []
    :return:
    """
    para = {"CreateOrgId": 0, "Numbers": [], "Ids": "", "SelectedPostId": 0,
            "NetworkCtrl": "",
            "IgnoreInterationFlag": "",
            }
    if kwargs:
        para.update(kwargs)
    response = api_sdk.Submit("BD_Material", para)
    print("�����ύ�ӿڣ�", response)
    return Check_response(response)


def material_Audit(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) ����˹���
    :param kwargs:  �滻para�в�����ʾ����   Numbers = []
    :return:
    """
    para = {"CreateOrgId": 0, "Numbers": [], "Ids": "", "SelectedPostId": 0,
            "NetworkCtrl": "",
            "IgnoreInterationFlag": "",
            "IsVerifyProcInst": "",
            }
    if kwargs:
        para.update(kwargs)
    response = api_sdk.Audit("BD_Material", para)
    print("������˽ӿڣ�", response)
    return Check_response(response)


def material_Allocate(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) �ķ��书��
    :param kwargs:  �滻para�в�����ʾ����   PkIds ="" ,TOrgIds=""
    :return:
    """
    para = {"PkIds": "", "TOrgIds": ""}
    if kwargs:
        para.update(kwargs)
    response = api_sdk.Allocate("BD_Material", para)
    print("���Ϸ���ӿڣ�", response)
    return Check_response(response)


def material_cancelAllocate(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) ��ȡ�����书��
    :param kwargs:  �滻para�в�����ʾ����   PkIds ="" ,TOrgIds=""
    :return:
    """

    para = {"PkIds": "", "TOrgIds": ""}
    if kwargs:
        para.update(kwargs)
    response = api_sdk.cancelAllocate("BD_Material", para)
    print("����ȡ������ӿڣ�", response)
    return Check_response(response)


def material_UnAudit(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) �ķ���˹���
    �������
    :param kwargs:  �滻para�в�����ʾ����   Numbers = []
    :return:
    """
    para = {"PkIds": "", "TOrgIds": ""}
    if kwargs:
        para.update(kwargs)
    response = api_sdk.UnAudit("BD_Material", para)
    print("���Ϸ���˽ӿڣ�", response)
    return Check_response(response)


def material_attachmentUpload(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) ���ϴ�����
    �������
    :param kwargs:  �滻para�в�����ʾ����   InterId="", BillNO="
    :return:
    """
    para = {"FileName": "1016.txt",
            "FEntryKey": "",
            "FormId": "BD_MATERIAL",
            "IsLast": True,
            "InterId": "",
            "BillNO": "",
            "AliasFileName": "test",
            "SendByte": "6L+Z5piv5rWL6K+V5paH5Lu25ZKMYmFzZTY05a2X56ym5Liy5LqS6L2s"
            }
    if kwargs:
        para.update(kwargs)
    response = api_sdk.attachmentUpload(para)
    print("���ϸ����ϴ��ӿڣ�", response)
    if Check_response(response):
        res = json.loads(response)
        fileid = res["Result"]["FileId"]
        return Check_response(response), fileid
    return False, ""


def material_attachmentDownLoad(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) �����ع���
    �������
    :param kwargs:  �滻para�в�����ʾ����   Numbers = []
    :return:
    """
    para = {"FileId": "", "StartIndex": 0}
    if kwargs:
        para.update(kwargs)
    response = api_sdk.attachmentDownLoad(para)
    print("���ϸ������ؽӿڣ�", response)
    return Check_response(response)


def material_ExcuteOperation(type, **kwargs):
    """

    :param type: Forbid������ Enable��������
    :param kwargs:
    :return:
    """

    para = {"CreateOrgId": 0, "Numbers": [], "Ids": "", "PkEntryIds": [],
            "NetworkCtrl": "",
            "IgnoreInterationFlag": "",
            }
    if kwargs:
        para.update(kwargs)
    response = api_sdk.ExcuteOperation("BD_Material", type, para)
    print(f"����{type}�ӿڣ�", response)
    return Check_response(response)


def material_View(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) �ķ��鿴����
    �������
    :param kwargs:  �滻para�в�����ʾ����   Number = web0002
    :return:
    """
    para = {"CreateOrgId": 0, "Number": "", "Id": "", "IsSortBySeq": "false", }
    if kwargs:
        para.update(kwargs)
    response = api_sdk.View("BD_Material", para)
    print("���Ϸ��鿴�ӿڣ�", response)
    return Check_response(response)


def material_Delete(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) ��ɾ������
    �������
    :param kwargs:  �滻para�в�����ʾ����   Number = web0002
    :return:
    """
    para = {"CreateOrgId": 0, "Numbers": [], "Ids": "", "NetworkCtrl": ""}
    if kwargs:
        para.update(kwargs)
    response = api_sdk.Delete("BD_Material", para)
    print("����ɾ���ӿڣ�", response)
    return Check_response(response)


def material_GroupSave(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) �ķ��鱣�湦��
    �������
    :param kwargs:  �滻para�в�����ʾ����   FNumber = "",  FName=""
    :return:
    """
    para = {
        "GroupFieldKey": "",
        "GroupPkId": 0,
        "FParentId": 0,
        "FNumber": "",
        "FName": "",
        "FDescription": ""
    }
    if kwargs:
        para.update(kwargs)
    response = api_sdk.GroupSave("BD_Material", para)
    print("���Ϸ��鱣��ӿڣ�", response)
    if Check_response(response):
        res = json.loads(response)
        groupid = res["Result"]["ResponseStatus"]["SuccessEntitys"][0]["Id"]
        return Check_response(response), groupid
    return False, ""


def material_QueryGroupInfo(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) �ķ����ѯ����
    �������
    :param kwargs:  �滻para�в�����ʾ����   GroupPkIds=''
    :return:
    """
    para = {
        "FormId": "BD_MATERIAL",
        "GroupFieldKey": "FMaterialGroup",
        "GroupPkIds": "",
        "Ids": ""
    }
    if kwargs:
        para.update(kwargs)
    response = api_sdk.QueryGroupInfo(para)
    print("���Ϸ����ѯ�ӿڣ�", response)
    return Check_response(response)


def material_GroupDelete(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) �ķ���ɾ������
    �������
    :param kwargs:  �滻para�в�����ʾ����   GroupPkIds = ''
    :return:
    """
    para = {
        "FormId": "BD_MATERIAL",
        "GroupFieldKey": "FMaterialGroup",
        "GroupPkIds": "",
    }
    if kwargs:
        para.update(kwargs)
    response = api_sdk.GroupDelete(para)
    print("���Ϸ���ɾ���ӿڣ�", response)
    return Check_response(response)


def material_SwitchOrg(**kwargs):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) ���л���֯����
    �������
    :param kwargs:  �滻para�в�����ʾ����   OrgNumber = ''
    :return:
    """
    para = {"OrgNumber": ""}
    if kwargs:
        para.update(kwargs)
    response = api_sdk.SwitchOrg(para)
    print("�����л���֯�ӿڣ�", response)
    return Check_response(response)


def material_SendMsg(**kwargs):
    """
    ���ӿ�����ʵ�ַ�����Ϣ����
    �������
    :param kwargs:  �滻para�в�����ʾ����
    :return:
    """
    para = {"Model": [{"FTitle": "���Ǳ���", "FContent": "��������", "FReceivers": "demo", "FType": "1"}]}
    if kwargs:
        para.update(kwargs)
    response = api_sdk.SendMsg(para)
    print("������Ϣ�ӿڣ�", response)
    return Check_response(response)


def material_BatchSave(n):
    """
    ���ӿ�����ʵ������ (BD_MATERIAL) ���������湦��
    �������
    :param kwargs:  �滻para�в�����ʾ����
    :return:
    """

    modellist = []
    for i in range(n):
        current_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        model_data = {
            "FCreateOrgId": {"FNumber": 100},
            "FUserOrgId": {"FNumber": 100},
            "FNumber": "xtwl" + current_time + "10001",
            "FName": "��������" + current_time + "10001"
        }
        modellist.append(model_data)
        time.sleep(1)

    para = {
        "NumberSearch": "true",
        "ValidateFlag": "true",
        "IsDeleteEntry": "true",
        "IsEntryBatchFill": "true",
        "NeedUpDateFields": [],
        "NeedReturnFields": [],
        "SubSystemId": "",
        "InterationFlags": "",
        "Model": modellist,
        "BatchCount": 0,
        "IsVerifyBaseDataField": "false",
        "IsAutoAdjustField": "false",
        "IgnoreInterationFlag": "false",
        "IsControlPrecision": "false",
        "ValidateRepeatJson": "false"
    }
    response = api_sdk.BatchSave("BD_Material", para)
    print("������������ӿڣ�", response)
    return Check_response(response)


class MaterialTestCase(unittest.TestCase):
    materialid = ""
    fileid = ""
    groupid = ""

    def testa_material_Save(self):
        result = material_Save(Model=save_data)
        self.assertTrue(result[0])
        MaterialTestCase.materialid = result[1]

    def testb_material_Submit(self):
        self.assertTrue(material_Submit(Numbers=[FNumber]))

    def testc_material_Audit(self):
        self.assertTrue(material_Audit(Numbers=[FNumber]))

    def testd_material_Allocate(self):
        self.assertTrue(material_Allocate(PkIds=MaterialTestCase.materialid, TOrgIds="100002"))

    def teste_material_cancelAllocate(self):
        self.assertTrue(material_cancelAllocate(PkIds=MaterialTestCase.materialid, TOrgIds="100002"))

    def testf_material_UnAudit(self):
        self.assertTrue(material_UnAudit(Numbers=[FNumber]))

    def testg_material_attachmentUpload(self):
        result = material_attachmentUpload(InterId=MaterialTestCase.materialid, BillNO=FNumber)
        self.assertTrue(result[0])
        MaterialTestCase.fileid = result[1]

    def testh_material_attachmentDownLoad(self):
        self.assertTrue(material_attachmentDownLoad(FileId=MaterialTestCase.fileid))

    def testi_material_ExcuteOperation(self):
        self.assertTrue(material_ExcuteOperation("Forbid", Numbers=[FNumber]))

    def testj_material_ExcuteOperation(self):
        self.assertTrue(material_ExcuteOperation("Enable", Numbers=[FNumber]))

    def testk_material_View(self):
        self.assertTrue(material_View(Number=FNumber))

    def testl_material_ExecuteBillQuery(self):
        self.assertTrue(material_ExecuteBillQuery(Limit=1000, FilterString="FNumber=" + "\'" + FNumber + "\'"))

    def testm_material_Delete(self):
        self.assertTrue(material_Delete(Numbers=FNumber))

    def testn_material_GroupSave(self):
        result = material_GroupSave(FNumber=FNumber, FName=FNumber)
        self.assertTrue(result[0])
        MaterialTestCase.groupid = result[1]

    def testo_material_QueryGroupInfo(self):
        self.assertTrue(material_QueryGroupInfo(GroupPkIds=MaterialTestCase.groupid))

    def testp_material_GroupDelete(self):
        self.assertTrue(material_GroupDelete(GroupPkIds=MaterialTestCase.groupid))

    def testq_material_SwitchOrg(self):
        self.assertTrue(material_SwitchOrg(OrgNumber=200))

    # �л���֯�������л�����
    def testr_material_SwitchOrg(self):
        self.assertTrue(material_SwitchOrg(OrgNumber=100))

    def testr_material_SendMsg(self):
        self.assertTrue(material_SendMsg())

    def tests_material_material_BatchSave(self):
        self.assertTrue(material_BatchSave(2))


if __name__ == '__main__':
    unittest.main()
