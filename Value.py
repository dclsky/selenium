#erp地址
def url():
    erp_url="http://172.16.104.126:9085/zkf-erp/"
    return erp_url

#订单日期
def order_date():
    date="2017-03-16"
    return date

#堂食人员身份证号码
def  identity_card_tangshi():
     identity_card="420200198409238002"
     return  identity_card

#外卖人员身份证号码
def identity_card_waimai():
    identity_card = "420200198804259022"
    return identity_card

#选择订货日期
def select_date():
    value = "2017-03-24"
    return value

#检验订货日期
def order_date_test():
    value = "日订 [送货:03-26]"
    return value

#预估管理日期
def estimate_date():
    value = "2017-04-01"
    return value

#异动日期必须选择1号且每次运行时月份不可重复
def transaction_date():
    value = "2017-08-01"
    return value

def sid():
    # for i in range(2):
    #     li = ["CN020010", "CN020089"]
    #     for i in range(len(li)):
    #         return li[i]
    li = ["CN020010", "CN020089"]
    for app_id in li:
        return app_id