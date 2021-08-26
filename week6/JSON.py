# # JSON(Javascript Object Notation)- формат обмена данными

# # notebook = {
# #     'model':'Acer',
# #     'model': 'Aspire',
# #     'ram'  : 8,
# #     'hdd'  : 500,
# #     'has_type_c' : True,
# #     'cd drive': None
# # }

# # Используются двойные кавычки
# # ключом может быть только строка

# class Notebook:
#     def __init__(self,brand,model,ram,hdd,accessories):
#         self.brand = brand
#         self.model = model
# #         self.ram = ram
# #         self.hdd = hdd
# #         self.accessories = accessories

# # note1 = Notebook('Apple','Macbook Pro',16,256,['headphones','heads','bag'])
# # note2 = Notebook('Asus','ROF',24,1000,[])
# # notebooks = [note1,note2]

        

# # import json

# # class NotebookEncoder(json.JSONEncoder):
# #     def default(self,obj):
# #         return obj.__dict__

# # res = json.dumps(notebooks,indent=2,   #indent=отступы ,всегда кратные
# # cls=NotebookEncoder)
# # print(res)


# notes = '[{ "model":"Acer","model": "Aspire","ram"  : 8,"hdd"  : 500,"has_type_c" : true,"cd drive": null}]'
# class Notebook:
    
#     def __init__(self,brand,model,ram,hdd,has_type_c,cd_drive):
#         self.brand = brand
#         self.model = model
#         self.ram = ram
#         self.hdd = hdd
#         self.has_type = has_type_c
#         self.cd_drive = cd_drive

import json
# from collections import namedtuple
# def decoder(notebook_dict):
#     return namedtuple('Notebook',notebook_dict.keys())(*notebook_dict.values())

# notebooks  = json.loads(notes,object_hook=decoder)
# print(notebooks)
# print(type(notebooks))


# student = [
#     {'name':'Alisher','age':25},
#     {'name':'Ivan','age':23}
#     ]
# file = open('test.json','w')
# res = json.dumps(student)
# file.write(res)
# file.close()

# file = open('test.json','w')
# json.dump(student,file)
# file.close()


file = open('test.json')

content = file.read()

student = json.loads(content)

file.close()

file = open('test.json')
student = json.load(file)
file.close()
print(student)