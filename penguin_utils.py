import streamlit as st
import time

def get_user_inputs():
    """获取用户输入并返回所有数据（带动态key）"""
    unique_key = str(time.time_ns())  # 纳秒级时间戳确保唯一性
    
    inputs = {
        'island': st.selectbox(
            '企鹅栖息的岛屿', 
            options=['托尔森岛', '比斯科群岛', '德里姆岛'],
            key=f"island_selectbox_{unique_key}"
        ),
        'sex': st.selectbox(
            '性别', 
            options=['雄性', '雌性'],
            key=f"sex_selectbox_{unique_key}"
        ),
        'bill_length': st.number_input(
            '喙的长度（毫米）', 
            min_value=0.0, 
            key=f"bill_length_{unique_key}"
        ),
        'bill_depth': st.number_input(
            '喙的深度（毫米）', 
            min_value=0.0, 
            key=f"bill_depth_{unique_key}"
        ),
        'flipper_length': st.number_input(
            '翅膀的长度（毫米）', 
            min_value=0.0, 
            key=f"flipper_length_{unique_key}"
        ),
        'body_mass': st.number_input(
            '身体质量（克）', 
            min_value=0.0, 
            key=f"body_mass_{unique_key}"
        )
    }
    return inputs

def format_inputs(inputs):
    """将用户输入转换为模型需要的格式"""
    # 岛屿处理
    island_map = {
        '比斯科群岛': (0, 0, 1),
        '德里姆岛': (0, 1, 0),
        '托尔森岛': (1, 0, 0)
    }
    island_dream, island_torgerson, island_biscoe = island_map.get(inputs['island'], (0, 0, 0))
    
    # 性别处理
    sex_male = 1 if inputs['sex'] == '雄性' else 0
    sex_female = 1 if inputs['sex'] == '雌性' else 0
    
    return [
        inputs['bill_length'],
        inputs['bill_depth'],
        inputs['flipper_length'],
        inputs['body_mass'],
        island_dream,
        island_torgerson,
        island_biscoe,
        sex_female,
        sex_male
    ]
