# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Version: 2.2
# https://stefanoflore.it
# https://ai-wiz.art

# 汉化 + 优化为读取json文件：Zho
# 版本：2.2

import json
import os

def read_json_file(file_path):
    try:
        # Open file, load JSON content into python dictionary, and return it.
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_name(json_data):
    # Check that data is a list
    if not isinstance(json_data, list):
        print("Error: input data must be a list")
        return None

    names = []

    # Iterate over each item in the data list
    for item in json_data:
        # Check that the item is a dictionary
        if isinstance(item, dict):
            # Check that 'name' is a key in the dictionary
            if 'name' in item:
                # Append the value of 'name' to the names list
                names.append(item['name'])

    return names

def get_prompt(json_data, template_name):
    try:
        # Check if json_data is a list
        if not isinstance(json_data, list):
            raise ValueError("Invalid JSON data. Expected a list of templates.")
            
        for template in json_data:
            # Check if template contains 'name' and 'prompt' fields
            if 'name' not in template or 'prompt' not in template:
                raise ValueError("Invalid template. Missing 'name' or 'prompt' field.")
            
            if template['name'] == template_name:
                prompt = template.get('prompt', "")
                print("Extracted prompt:", prompt)
                return prompt

        # If function hasn't returned yet, no matching template was found
        raise ValueError(f"No template found with name '{template_name}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


class PortraitMaster_中文版:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        # Get current file's directory
        p = os.path.dirname(os.path.realpath(__file__))

        # Paths for various JSON files
        shot_file_path = os.path.join(p, 'lists/shot_list.json')
        gender_file_path = os.path.join(p, 'lists/gender_list.json')
        eyes_color_file_path = os.path.join(p, 'lists/eyes_color_list.json')
        face_shape_file_path = os.path.join(p, 'lists/face_shape_list.json')
        facial_expressions_file_path = os.path.join(p, 'lists/face_expression_list.json')
        nationality_file_path = os.path.join(p, 'lists/nationality_list.json')
        hair_style_file_path = os.path.join(p, 'lists/hair_style_list.json')
        hair_color_file_path = os.path.join(p, 'lists/hair_color_list.json')
        light_type_file_path = os.path.join(p, 'lists/light_type_list.json')
        light_direction_file_path = os.path.join(p, 'lists/light_direction_list.json')
        #v2.2
        body_type_file_path = os.path.join(p, 'lists/body_type_list.json')
        beard_file_path = os.path.join(p, 'lists/beard_list.json')
        model_pose_file_path = os.path.join(p, 'lists/model_pose_list.json')

        # Read JSON from file
        self.shot_data = read_json_file(shot_file_path)
        self.gender_data = read_json_file(gender_file_path)
        self.eyes_color_data = read_json_file(eyes_color_file_path)
        self.face_shape_data = read_json_file(face_shape_file_path)
        self.facial_expressions_data = read_json_file(facial_expressions_file_path)
        self.nationality_data = read_json_file(nationality_file_path)
        self.hair_style_data = read_json_file(hair_style_file_path)
        self.hair_color_data = read_json_file(hair_color_file_path)
        self.light_type_data = read_json_file(light_type_file_path)
        self.light_direction_data = read_json_file(light_direction_file_path)
        #V2.2
        self.body_type_data = read_json_file(body_type_file_path)
        self.beard_data = read_json_file(beard_file_path)
        self.model_pose_data = read_json_file(model_pose_file_path)

        # Retrieve name from JSON data
        shot_list = get_name(self.shot_data)
        shot_list = ['-'] + shot_list
        gender_list = get_name(self.gender_data)
        gender_list = ['-'] + gender_list
        eyes_color_list = get_name(self.eyes_color_data)
        eyes_color_list = ['-'] + eyes_color_list
        face_shape_list = get_name(self.face_shape_data)
        face_shape_list = ['-'] + face_shape_list
        facial_expressions_list = get_name(self.facial_expressions_data)
        facial_expressions_list = ['-'] + facial_expressions_list
        nationality_list = get_name(self.nationality_data)
        nationality_list = ['-'] + nationality_list
        hair_style_list = get_name(self.hair_style_data)
        hair_style_list = ['-'] + hair_style_list
        hair_color_list = get_name(self.hair_color_data)
        hair_color_list = ['-'] + hair_color_list
        light_type_list = get_name(self.light_type_data)
        light_type_list = ['-'] + light_type_list
        light_direction_list = get_name(self.light_direction_data)
        light_direction_list = ['-'] + light_direction_list
        #V2.2
        body_type_list = get_name(self.body_type_data)
        body_type_list = ['-'] + body_type_list
        beard_list = get_name(self.beard_data)
        beard_list = ['-'] + beard_list
        model_pose_list = get_name(self.model_pose_data)
        model_pose_list = ['-'] + model_pose_list
        
        
        max_float_value = 1.75

        return {
            "required": {
                "镜头类型": (shot_list, {
                    "default": shot_list[0],
                }),
                "镜头权重": ("FLOAT", {
                    "default": 1.5,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "性别": (gender_list, {
                    "default": gender_list[0],
                }),
                "年龄": ("INT", {
                    "default": 20,
                    "min": 18,
                    "max": 90,
                    "step": 1,
                    "display": "slider",
                }),
                "国籍_1": (nationality_list, {
                    "default": nationality_list[0],
                }),
                "国籍_2": (nationality_list, {
                    "default": nationality_list[0],
                }),
                "国籍混合": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": 1,
                    "step": 0.05,
                    "display": "slider",
                }),
                "体型": (body_type_list, {
                    "default": body_type_list[0],
                }),
                "体型权重": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "姿势": (model_pose_list, {
                    "default": model_pose_list[0],
                }),
                "眼睛颜色": (eyes_color_list, {
                    "default": eyes_color_list[0],
                }),
                "面部表情": (facial_expressions_list, {
                    "default": facial_expressions_list[0],
                }),
                "面部表情权重": ("FLOAT", {
                    "default": 1.5,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "脸型": (face_shape_list, {
                    "default": face_shape_list[0],
                }),
                "脸型权重": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "面部对称性": ("FLOAT", {
                    "default": 0.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "发型": (hair_style_list, {
                    "default": hair_style_list[0],
                }),
                "头发颜色": (hair_color_list, {
                    "default": hair_color_list[0],
                }),
                "头发蓬松度": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "胡子": (beard_list, {
                    "default": beard_list[0],
                }),
                "皮肤细节": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤毛孔": ("FLOAT", {
                    "default": 0.3,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "酒窝": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皱纹": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "雀斑": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "痣": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤瑕疵": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "痘痘": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "小麦色肤色": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "眼睛细节": ("FLOAT", {
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "虹膜细节": ("FLOAT", {
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "圆形虹膜": ("FLOAT", {
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "圆形瞳孔": ("FLOAT", {
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "灯光类型": (light_type_list, {
                    "default": light_type_list[0],
                }),
                "灯光方向": (light_direction_list, {
                    "default": light_direction_list[0],
                }),
                "灯光权重": ("FLOAT", {
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "提高照片真实感": (["enable", "disable"],),
                "起始提示词": ("STRING", {
                    "multiline": True,
                    "default": "raw photo, (realistic:1.5)"
                }),
                "补充提示词": ("STRING", {
                    "multiline": True,
                    "default": "(white background:1.5)"
                }),
                "结束提示词": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "负面提示词": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            }
        }

    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("positive", "negative",)
    FUNCTION = "pm"
    CATEGORY = "📸肖像大师"

    def pm(self, 镜头类型="-", 镜头权重=1, 性别="-", 体型="-", 体型权重=0, 眼睛颜色="-", 面部表情="-", 面部表情权重=0, 脸型="-", 脸型权重=0, 国籍_1="-", 国籍_2="-", 国籍混合=0.5, 年龄=20, 发型="-", 头发颜色="-", 头发蓬松度=0, 酒窝=0, 雀斑=0, 皮肤毛孔=0, 皮肤细节=0, 痣=0, 皮肤瑕疵=0, 皱纹=0, 小麦色肤色=0,  眼睛细节=1, 虹膜细节=1, 圆形虹膜=1, 圆形瞳孔=1, 面部对称性=0, 补充提示词="", 起始提示词="", 结束提示词="", 灯光类型="-", 灯光方向="-", 灯光权重=0, 负面提示词="", 提高照片真实感="disable", 胡子="-", 姿势="-", 痘痘=0):

        shot = get_prompt(self.shot_data, 镜头类型)
        gender = get_prompt(self.gender_data, 性别)
        eyes_color = get_prompt(self.eyes_color_data, 眼睛颜色)
        face_shape = get_prompt(self.face_shape_data, 脸型)
        facial_expressions = get_prompt(self.facial_expressions_data, 面部表情)
        nationality_1 = get_prompt(self.nationality_data, 国籍_1)
        nationality_2 = get_prompt(self.nationality_data, 国籍_2)
        hair_style = get_prompt(self.hair_style_data, 发型)
        hair_color = get_prompt(self.hair_color_data, 头发颜色)
        light_type = get_prompt(self.light_type_data, 灯光类型)
        light_direction = get_prompt(self.light_direction_data, 灯光方向)
        #V2.2
        body_type = get_prompt(self.body_type_data, 体型)
        beard = get_prompt(self.beard_data, 胡子)
        model_pose = get_prompt(self.model_pose_data, 姿势)

        prompt = []

        if 性别 == "-":
            性别 = ""
        else:
            性别 = " " + gender + " "

        if 国籍_1 != '-' and 国籍_2 != '-':
            Anationality = f"[{nationality_1}:{nationality_2}:{round(国籍混合, 2)}]"
        elif 国籍_1 != '-':
            Anationality = nationality_1 + " "
        elif 国籍_2 != '-':
            Anationality = nationality_2 + " "
        else:
            Anationality = ""

        if 起始提示词 != "":
            prompt.append(f"{起始提示词}")

        if 镜头类型 != "-" and 镜头权重 > 0:
            prompt.append(f"({shot}:{round(镜头权重, 2)})")

        prompt.append(f"({Anationality}{性别}{round(年龄)}-years-old:1.5)")

        if 体型 != "-" and 体型权重 > 0:
            prompt.append(f"({body_type}, {body_type} body:{round(体型权重, 2)})")

        if 姿势 != "-":
            prompt.append(f"({model_pose}:1.5)")

        if 眼睛颜色 != "-":
            prompt.append(f"({eyes_color} eyes:1.25)")
        
        if 面部表情 != "-" and 面部表情权重 > 0:
            prompt.append(f"({facial_expressions}, {facial_expressions} expression:{round(面部表情权重, 2)})")

        if 脸型 != "-" and 脸型权重 > 0:
            prompt.append(f"({face_shape} shape face:{round(脸型权重, 2)})")

        if 发型 != "-":
            prompt.append(f"({hair_style} hairstyle:1.25)")

        if 头发颜色 != "-":
            prompt.append(f"({hair_color} hair:1.25)")

        if 胡子 != "-":
            prompt.append(f"({beard}:1.15)")
        
        if 头发蓬松度 != "-":
            prompt.append(f"(disheveled:{round(头发蓬松度, 2)})")

        if 补充提示词 != "":
            prompt.append(f"{补充提示词}")

        if 皮肤细节 > 0:
            prompt.append(f"(skin details, skin texture:{round(皮肤细节, 2)})")

        if 皮肤毛孔 > 0:
            prompt.append(f"(skin pores:{round(皮肤毛孔, 2)})")

        if 皮肤瑕疵 > 0:
            prompt.append(f"(skin imperfections:{round(皮肤瑕疵, 2)})")

        if 痘痘 > 0:
            prompt.append(f"(acne, skin with acne:{round(痘痘, 2)})")

        if 皱纹 > 0:
            prompt.append(f"(skin imperfections:{round(皱纹, 2)})")

        if 小麦色肤色 > 0:
            prompt.append(f"(tanned skin:{round(小麦色肤色, 2)})")

        if 酒窝 > 0:
            prompt.append(f"(dimples:{round(酒窝, 2)})")

        if 雀斑 > 0:
            prompt.append(f"(freckles:{round(雀斑, 2)})")

        if 痣 > 0:
            prompt.append(f"(skin pores:{round(痣, 2)})")

        if 眼睛细节 > 0:
            prompt.append(f"(eyes details:{round(眼睛细节, 2)})")

        if 虹膜细节 > 0:
            prompt.append(f"(iris details:{round(虹膜细节, 2)})")

        if 圆形虹膜 > 0:
            prompt.append(f"(circular iris:{round(圆形虹膜, 2)})")

        if 圆形瞳孔 > 0:
            prompt.append(f"(circular pupil:{round(圆形瞳孔, 2)})")

        if 面部对称性 > 0:
            prompt.append(f"(facial asymmetry, face asymmetry:{round(面部对称性, 2)})")

        if 灯光类型 != '-' and 灯光权重 > 0:
            if 灯光方向 != '-':
                prompt.append(f"({light_type} {light_direction}:{round(灯光权重, 2)})")
            else:
                prompt.append(f"({light_type}:{round(灯光权重, 2)})")
        
        if 结束提示词 != "":
            prompt.append(f"{结束提示词}")

        prompt = ", ".join(prompt)
        prompt = prompt.lower()

        if 提高照片真实感 == "enable":
            prompt = prompt + ", (detailed, professional photo, perfect exposition:1.25), (film grain:1.5)"

        if 提高照片真实感 == "enable":
            negative_prompt = 负面提示词 + ", (shinny skin, reflections on the skin, skin reflections:1.5)"
        else:
            negative_prompt = 负面提示词

        
        print("Portrait Master as generate the prompt:")
        print(prompt)

        return (prompt,negative_prompt,)



NODE_CLASS_MAPPINGS = {
    "PortraitMaster_中文版": PortraitMaster_中文版
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PortraitMaster_中文版": "📸 肖像大师_中文版_2.2"
}
