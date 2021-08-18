# 食品目录
class food_order:
    ordering_fodd_name =['酸菜鱼','鱼香肉丝', '烧排骨','鸡肉炒蛋']
    order_food_price =[32,42,43,21]
    order_list=[]

    def __init__(self):
        self.do_order_food()
    def welcome(self):
        print("++++++++++++++++++++++++")
        print("欢迎来到点餐系统")
        print("1.套餐类")
        print("2.结账")
        print("3.退出")
        print("+++++++++++++++++++++++++")
    def order_list_(self,b=2):
        total_price=0.0
        if b==1:
            f =open('./order.txt','a',encoding='UTF-8')
            import time
            f.write("========================================")
            f.write("打印订单时间："+time.strftime("%Y-%m-%D %H:%M:%S",time.localtime())+"\n")
            for v in self.order_list:
                value =v.split("@@")
                f.write(value[0]+"\t"+value[1]+"份\t"+value[2]+'元\n')
                total_price =float(total_price)+float(value[2])
            f.write("\t\t\t\t总价" +str(total_price)+"\n")
            f.write("++++++++++++++++++++++++++++++++++++++++++")
            f.close()
            return total_price
        else:
            import time
            print("========================================")
            print("打印订单时间："+time.strftime("%Y-%m-%D %H:%M:%S",time.localtime())+"\n")
            for v in self.order_list:
                value =v.split("@@")
                print(value[0]+"\t"+value[1]+"份\t"+value[2]+'元\n')
                total_price =float(total_price)+float(value[2])
            print("\t\t\t\t总价" +str(total_price)+"\n")
            print("++++++++++++++++++++++++++++++++++++++++++")
           
            return total_price
# 食品订单
    def do_order_food(self):
        while True:
            self.welcome()
            num =input("请选择")
            index =0
            if num =="1":
                print("--------套餐清单------------")
                ordering_food_len =self.ordering_fodd_name.__len__()
                print(ordering_food_len)
                for k in range (ordering_food_len):
                    index =index +1
                    print (str(index)+"~"+str(self.ordering_fodd_name[k])+"\t\t"+str(self.order_food_price[k])+'元')
                print("------------------------------")
                food_index =int(input("请选择套餐"))
                food_index =food_index-1
                if food_index >=0 and food_index<ordering_food_len:
                    order_list_index =-1
                    b =True# 去重 ，如果没有想同商品则，重新添加，如果有，则修改
                    for each in self.order_list:
                        order_list_index =order_list_index +1
                        food_name =self.ordering_fodd_name[food_index]
                        food_name_len =food_name.__len__()
                        if food_name ==each[0:food_name_len]:
                            b =False
                            break
                    f =input("请输入购买份数")
                    if b:
                        price =float(self.order_food_price[food_index]*int(f))
                        print("您选择了:"+self.ordering_fodd_name[food_index]+"\t"+f+"份\t总价："+str(price)+"元")
                        self.order_list.append(self.ordering_fodd_name[food_index]+"@@"+str(f)+"@@"+str(price))
                    else:
                        list =self.order_list[order_list_index].split('@@')
                        sum =int(list[1])+int(f)  
                        price =float(self.order_food_price[food_index]*sum)
                        self.order_list[order_list_index] =self.ordering_fodd_name[food_index]+"@@"+str(sum)+"@@"+str(price)
                        print("你选择了"+self.ordering_fodd_name[food_index]+"\t"+f+"份\t总价："+str(price)+"元")
                            
                else:
                    print("没有该商品")
            elif num=='2':
                print('=======清单列表=========')
                total_price =self.order_list_()
                print("-------------------------")
                while True:
                    if self.order_list:
                        money =input('输入支付金额')
                        import re
                        res =re.match(r'\d+',money)
                        if res:
                            if int(money)>=total_price:
                                print('支付成功'+str(float(money)-float(total_price))+'元，欢迎再次光临')
                                self.order_list_(1)
                                self.order_list=[]
                                break
                            else:
                                print("金额不够")
                        else:
                            print("这不是人民比")
                    else:
                        print("没有购物清单无法结账")
                        break
            elif num=='3':
                exit()

            else:
                print('重新输入')
ds =food_order()


                                # 已有列表份数相加


                                
















            


