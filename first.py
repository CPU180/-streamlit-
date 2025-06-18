import streamlit as st # 导入Streamlit并用st代表它
import numpy as np #导入numpy库调用表格内容
import pandas as pd #导入pandas库调用表格内容
###---------------------------------------------------------
### 当前内部版本号0.6.18.1
### 注释说明，###为分割线及特殊注释，#为普通注释，###>>>>>为数据添加处
###---------------------------------------------------------



###----------------------------------------------------------------------------------
###  主模块
###  网页上方页面设置，侧边栏选项卡设置
###----------------------------------------------------------------------------------

# 必须作为第一个Streamlit命令！
st.set_page_config(
    page_title="这是一个整合多功能的小网站！",
    page_icon="💡",
    layout="wide"
)

# 侧边栏美化 - 宽松版
with st.sidebar:
    # 添加自定义CSS样式
    st.markdown("""
    <style>
        /* 侧边栏整体样式 - 增加内边距 */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #f5f7fa 0%, #e4e8f0 100%);
            border-right: 1px solid #d1d5db;
            box-shadow: 2px 0 10px rgba(0,0,0,0.05);
            padding: 2rem 1.5rem !important;
        }
        
        /* 标题样式 - 增加下边距 */
        .sidebar-title {
            color: #2c3e50;
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 2rem;  /* 从1rem增加到2rem */
            text-align: center;
            padding-bottom: 15px;  /* 从10px增加到15px */
            border-bottom: 2px solid #4a6fa5;
        }
        
        /* 单选按钮样式 - 大幅增加间距 */
        .stRadio [role="radiogroup"] {
            gap: 1rem !important;  /* 从0.5rem增加到1rem */
            margin-top: 1.5rem;
            margin-bottom: 1.5rem;
        }
        
        /* 单选按钮本身加大 */
        .stRadio [role="radio"] {
            padding: 0.75rem 1.25rem !important;  /* 加大内边距 */
            border-radius: 10px !important;  /* 更大的圆角 */
            border: 1px solid #d1d5db;
            transition: all 0.3s;
            margin: 0.5rem 0 !important;  /* 上下增加外边距 */
            font-size: 1rem !important;
        }
        
        /* 悬停效果保持不变 */
        .stRadio [role="radio"]:hover {
            background-color: #f0f4f8;
            border-color: #4a6fa5;
        }
        
        /* 选中状态保持不变 */
        .stRadio [role="radio"][aria-checked="true"] {
            background-color: #4a6fa5 !important;
            color: white !important;
            border-color: #4a6fa5 !important;
        }
        
        /* 分割线上下增加间距 */
        [data-testid="stHorizontalBlock"] hr {
            margin: 1.5rem 0 !important;
        }
        
        /* 快速导航标题增加间距 */
        .sidebar-section-title {
            margin: 1.5rem 0 1rem 0 !important;
        }
        
        /* 版本信息增加上边距 */
        .version-info {
            font-size: 0.8rem;
            color: #6b7280;
            text-align: center;
            margin-top: 3rem !important;  /* 从2rem增加到3rem */
            padding-top: 1rem;
            border-top: 1px solid #e5e7eb;
        }
    </style>
    """, unsafe_allow_html=True)

    # 侧边栏标题
    st.markdown('<div class="sidebar-title">🦁 南宁动物园导航</div>', unsafe_allow_html=True)
    
    # 页面选择器 - 现在选项间距更大
    page = st.radio(
        "选择您想访问的页面",
        ["首页", "员工档案", "园内一瞥", "附近美食", "招聘个人信息简历投稿", "企鹅分类"],
        index=0,
        label_visibility="collapsed"
    )
    
       


###----------------------------------------------------------------------------------
###  模块①
###  动物园图片及信息展示，此处分割有横向选项卡
###----------------------------------------------------------------------------------

if page == "首页":
    # 添加自定义CSS样式
    st.markdown("""
    <style>
        /* 主标题样式 */
        .main-title {
            color: #2c3e50;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            text-align: center;
            background: linear-gradient(90deg, #4a6fa5, #3a86ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding-bottom: 0.5rem;
        }
        
        /* 标签页样式 */
        .stTabs [role="tablist"] {
            gap: 0.5rem;
            margin-bottom: 1.5rem;
        }
        
        .stTabs [role="tab"] {
            padding: 0.75rem 1.5rem;
            border-radius: 12px 12px 0 0;
            background-color: #f0f4f8;
            border: 1px solid #d1d5db;
            transition: all 0.3s;
            font-weight: 600;
            color: #4a5568;
        }
        
        .stTabs [role="tab"]:hover {
            background-color: #e2e8f0;
            color: #2d3748;
        }
        
        .stTabs [role="tab"][aria-selected="true"] {
            background-color: #4a6fa5;
            color: white !important;
            border-color: #4a6fa5;
        }
        
        /* 图片容器样式 */
        .image-container {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        
        /* 文本内容样式 */
        .content-text {
            font-size: 1.05rem;
            line-height: 1.8;
            color: #4a5568;
            text-align: justify;
        }
        
        /* 响应式调整 */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

    # 主标题
    st.markdown('<div class="main-title">南宁动物园：城市绿洲中的自然奇趣王国</div>', unsafe_allow_html=True)
    
    # 创建标签页
    tab1, tab2= st.tabs(["🦁 动物园简介", "🦁 动物介绍"])

    with tab1:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        images = ['https://n.sinaimg.cn/sinacn10/90/w1000h690/20180831/d4e3-hinpmnq5016932.jpg']
        st.image(images, width=400)  # 设置固定宽度为400像素
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="content-text">
        南宁动物园，全称南宁市动物园，位于广西壮族自治区首府南宁市西乡塘区大学东路73号，是一座集动物保护、科普教育、休闲娱乐、科研繁育于一体的综合性城市动物园。作为国家4A级旅游景区和全国科普教育基地，它不仅承载着野生动物迁地保护的重要职能，更是南宁市民亲子游玩、亲近自然的首选目的地。以下从历史沿革、园区布局、特色展区、科普功能、服务设施及游览建议等方面，为您展开详细介绍。

        <h3 style="color:#2c3e50;margin-top:1.5rem;">一、历史沿革：从植物园到现代化动物园</h3>
        南宁动物园的前身可追溯至1973年成立的南宁市植物园，1975年正式转型为动物园并向公众开放。经过近50年的发展，园区从最初的简单笼舍逐步升级为现代化生态展区：

        <ul style="margin-left:1.5rem;">
            <li><strong>20世纪80年代：</strong>引入大熊猫、亚洲象等珍稀动物，成为广西首个大型动物园。</li>
            <li><strong>2005年：</strong>完成首次大规模改造，新增热带雨林馆、海豚馆等特色展区。</li>
            <li><strong>2010年至今：</strong>持续优化动物福利，推行"沉浸式展区"设计，如仿自然生态的"熊猫苑""长臂猿岛"等。</li>
        </ul>

        如今，南宁动物园占地约42公顷，饲养动物超250种、数量逾3000只（头），年接待游客量突破200万人次。

        <h3 style="color:#2c3e50;margin-top:1.5rem;">二、园区布局：四大主题区域</h3>
        动物园按功能划分为动物展区、游乐区、科普区、休闲服务区，游客可沿导览图有序参观。

        <h4 style="color:#4a6fa5;margin-top:1rem;">1. 动物展区</h4>
        <strong>珍稀动物馆</strong>
        <ul style="margin-left:1.5rem;">
            <li><strong>大熊猫苑：</strong>居住着来自四川的国宝大熊猫，场馆模拟高山竹林环境，配备空调和专属保育团队。</li>
            <li><strong>亚洲象园：</strong>东南亚风格场馆，游客可观看大象洗澡、喷水等自然行为展示。</li>
            <li><strong>灵长类动物区：</strong>包括金丝猴、长臂猿、黑猩猩等，设有攀爬架和树冠走廊。</li>
        </ul>

        <h4 style="color:#4a6fa5;margin-top:1rem;">2. 加勒比水上世界（季节性开放）</h4>
        南宁动物园的招牌游乐项目，占地3万平方米，包含：
        <ul style="margin-left:1.5rem;">
            <li><strong>超级造浪池：</strong>人工海浪体验。</li>
            <li><strong>彩虹滑道：</strong>6条并列滑道，适合亲子互动。</li>
            <li><strong>儿童水寨：</strong>迷你滑梯和喷水设施。</li>
        </ul>

        <h3 style="color:#2c3e50;margin-top:1.5rem;">三、明星动物与特色体验</h3>
        <h4 style="color:#4a6fa5;margin-top:1rem;">1. 不容错过的"动物明星"</h4>
        <ul style="margin-left:1.5rem;">
            <li><strong>"明明"和"阳阳"：</strong>两只大熊猫，以憨态可掬的吃竹姿势圈粉无数。</li>
            <li><strong>亚洲象"波波"：</strong>擅长用鼻子卷起游客投喂的水果（需在饲养员指导下进行）。</li>
            <li><strong>白虎"雷霆"：</strong>罕见的白化孟加拉虎，威严与美丽并存。</li>
        </ul>

        <h3 style="color:#2c3e50;margin-top:1.5rem;">四、实用游览信息</h3>
        <h4 style="color:#4a6fa5;margin-top:1rem;">1. 门票与开放时间</h4>
        <ul style="margin-left:1.5rem;">
            <li><strong>门票：</strong>成人50元，儿童/学生/老人25元（需证件）。</li>
            <li><strong>加勒比水世界：</strong>夏季单独售票，约100元/人。</li>
            <li><strong>开放时间：</strong>旺季（4-10月）7:30-17:30，淡季（11-3月）8:00-17:00。</li>
        </ul>

        <h4 style="color:#4a6fa5;margin-top:1rem;">2. 交通指南</h4>
        <ul style="margin-left:1.5rem;">
            <li><strong>地铁：</strong>1号线"动物园站"C出口直达。</li>
            <li><strong>公交：</strong>4路、33路、604路等至"动物园站"。</li>
            <li><strong>自驾：</strong>停车场收费5元/小时，周末建议早到。</li>
        </ul>

        <h3 style="color:#2c3e50;margin-top:1.5rem;">结语：人与自然和谐共处的典范</h3>
        南宁动物园通过科学的场馆设计、丰富的互动项目和扎实的保育工作，让游客在欢乐中感受生命之美。无论是家庭出游、科普学习，还是摄影爱好者的创作，这里都能满足您的期待。计划行程前，建议关注官方公众号获取最新活动资讯，让您的游览更加充实！ 🦁🐼🌿
        </div>
        """, unsafe_allow_html=True)


    with tab2:
            # 在内存中初始化一个ind,当内存中没有'ind'的时候，才初始化
                if 'ind' not in st.session_state:
                    st.session_state['ind'] = 0

                # 图片数组-装很多的图片

                image_obj = [{
                        'url': 'https://szyl.nanning.gov.cn/nnsdwy/jdjs/dwzs/W020220811629523676964.jpg',
                        'title': '长颈鹿',
                        '介绍':'生活于非洲，拉丁文名字的意思是“长着豹纹的骆驼”。它们是世界上现存最高的陆生动物，我园最高的一头长颈鹿身高达到6米。长颈鹿脾气温柔，喜欢吃鲜嫩多汁的树叶，每天采食量可以达到40公斤。'
                    }, {
                        'url': 'https://szyl.nanning.gov.cn/nnsdwy/jdjs/dwzs/W020220811629861553625.jpg',
                        'title': '金刚鹦鹉',
                        '介绍':'金刚鹦鹉原产于美洲热带地区，是体型最大、色彩最艳丽的鹦鹉，属大型攀禽，共有6属17个品种。目前园内驯养有蓝黄金刚鹦鹉与红绿金刚鹦鹉两种，是全园最为聒噪也是最为美丽的鸟类。'
                    }, {
                        'url': 'https://szyl.nanning.gov.cn/nnsdwy/jdjs/dwzs/W020220811629926516316.jpg',
                        'title': '棕熊',
                        '介绍':'棕熊（学名：Ursus arctos）是熊科熊属的大型哺乳动物，广泛分布于北半球的森林和山地地区，是陆地上体型最大的食肉目动物之一善于游泳，主要分布：北美洲（如阿拉斯加灰熊）、欧洲、亚洲（如西伯利亚、中国东北）'
                    },{
                        'url': 'https://szyl.nanning.gov.cn/nnsdwy/jdjs/dwzs/W020220811630006982402.JPG',
                        'title': '非洲狮',
                        '介绍':'现存非洲最大的猫科动物，是非洲最凶猛的野兽，素有“草原之王..'
                    }]
                a1,a2=st.columns(2)
                with a1:
                     st.image(image_obj[st.session_state['ind']]['url'],width=600)
                with a2:
                    st.title(image_obj[st.session_state['ind']]['title'])
                    st.text(image_obj[st.session_state['ind']]['介绍'])
               

                # 显示按钮

                def nextImg():
                    # 点击下一张按钮要做的事
                    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_obj)


                def lastImg():
                    # 点击上一张按钮要做的事
                    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(image_obj)

                c1, c2 = st.columns(2)

                with c1:
                    st.button('上一张',on_click=lastImg, use_container_width=True)

                with c2:
                    st.button('下一张', on_click=nextImg, use_container_width=True)
       

    

###----------------------------------------------------------------------------------
###  模块②
###  基本信息，streamlit课程进度，代码展示
###----------------------------------------------------------------------------------


if page == "员工档案":
    # 页面标题 - 使用更大的字体和居中
    st.markdown("""
    <style>
    .big-title {
        font-size: 36px !important;
        text-align: center;
        color: #FF4B4B;
        padding: 10px;
        border-radius: 10px;
        background: linear-gradient(90deg, #f8ff00 0%, #3ad59f 100%);
        margin-bottom: 30px;
    }
    .section-title {
        font-size: 24px !important;
        color: #3ad59f;
        border-bottom: 2px solid #3ad59f;
        padding-bottom: 5px;
    }
    .metric-card {
        border-radius: 10px;
        padding: 15px;
        background-color: #f0f2f6;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="big-title">员工档案 —— 芙蓉王源 😇</div>', unsafe_allow_html=True)
    
    # 基本信息部分 - 使用卡片布局
    with st.container():
        st.markdown('<div class="section-title">😃 基本信息</div>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # 添加一个头像占位
            st.image("https://img.icons8.com/color/96/000000/circled-user-male-skin-type-7.png", width=100)
        
        with col2:
            st.markdown("""
            <div style="font-size: 18px; line-height: 2;">
            <b>姓名:</b> <span style="color: #FF4B4B;">芙蓉王源 😁</span><br>
            <b>班级:</b> <span style="color: #3ad59f;">23级练习生一班 😉</span><br>
            <b>学号:</b> <span style="color: #6a5acd;">9527 😇</span>
            </div>
            """, unsafe_allow_html=True)
    
    # 兴趣部分 - 使用标签样式
    st.markdown('<div class="section-title">兴趣爱好</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 20px;">
        <span style="background-color: #FF4B4B; color: white; padding: 5px 15px; border-radius: 20px;">🎮 游戏</span>
        <span style="background-color: #3ad59f; color: white; padding: 5px 15px; border-radius: 20px;">🏊 游泳</span>
        <span style="background-color: #FFA500; color: white; padding: 5px 15px; border-radius: 20px;">🎤 唱跳</span>
        <span style="background-color: #6a5acd; color: white; padding: 5px 15px; border-radius: 20px;">🏀 篮球</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 指标卡片 - 使用更美观的布局
    st.markdown('<div class="section-title">学习指标</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(label="当前学期", value="大二 下学期", delta="稳定进步中 ↑")
        st.markdown('</div>', unsafe_allow_html=True)
        
        cols = st.columns(3)
        with cols[0]:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric(label="当前周数", value="15/20", delta="-5周")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with cols[1]:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric(label="四六级进度", value="1/2", delta="已过四级")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with cols[2]:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric(label="人生进度", value="20%", delta="未来可期 ↑")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # 心情状态 - 使用表情符号和颜色
    st.markdown('<div class="section-title">心情状态</div>', unsafe_allow_html=True)
    mood = st.select_slider(
        "当前心情",
        options=["😭 糟糕", "😞 难过", "😐 一般", "🙂 不错", "😁 很棒"],
        value="😁 很棒"
    )
    st.markdown(f'<div style="text-align: center; font-size: 24px;">{mood}</div>', unsafe_allow_html=True)
    
    # 课程进度 - 使用更美观的进度条
    st.markdown('<div class="section-title">Streamlit课程进度</div>', unsafe_allow_html=True)
    progress = st.slider("进度百分比", 0, 100, 20)
    st.progress(progress, text=f"已完成 {progress}%")
    
    # 课程日志 - 使用更美观的表格
    st.markdown('<div class="section-title">课程日志</div>', unsafe_allow_html=True)
    
    data = {
        '课程': ['高等数学', '大学英语', 'C语言程序设计'],
        '期末达标分数': [90, 101, 97],
        '状态': ['通过', '通过', '补考'], 
        '难度': ['中等', '简单', '困难']
    }
    
    df = pd.DataFrame(data)
    
    # 使用st.dataframe并添加样式
    st.dataframe(
        df.style
        .applymap(lambda x: 'color: green' if x == '通过' else 'color: red' if x == '补考' else '')
        .applymap(lambda x: 'color: orange' if x == '困难' else 'color: #3ad59f' if x == '简单' else ''),
        height=150
    )
    
    # 代码展示 - 使用标签页组织
    st.markdown('<div class="section-title">代码展示</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Python", "Java", "JavaScript"])
    
    with tab1:
        python_code = '''def hello():
    print('你好，Streamlit！')'''
        st.code(python_code, language='python', line_numbers=True)
    
    with tab2:
        java_code = '''public class Hello {
    public static void main(String[] args) {
        System.out.println("你好！ Streamlit！");
    }
}'''
        st.code(java_code, language='java', line_numbers=True)
    
    with tab3:
        javascript_code = '''<p id="demo"></p>
<script>
    document.getElementById('demo').innerHTML = '你好！ Streamlit！';
</script>'''
        st.code(javascript_code, language='javascript', line_numbers=True)
        
if page == "园内一瞥":
    # 全局CSS样式
    st.markdown("""
    <style>
        /* 主标题样式 */
        .main-title {
            font-size: 2.5rem;
            text-align: center;
            color: #00a1d6;
            margin: 1.5rem 0;
            font-weight: bold;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
            background: linear-gradient(90deg, #00a1d6, #3a86ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        /* 副标题样式 */
        .section-title {
            font-size: 1.5rem;
            color: #2c3e50;
            margin: 1.2rem 0 0.8rem;
            border-left: 4px solid #00a1d6;
            padding-left: 0.8rem;
        }
        
        /* 图片画廊样式 */
        .image-gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
            margin: 1.5rem 0;
        }
        .image-gallery img {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s;
            width: 100%;
            height: auto;
        }
        .image-gallery img:hover {
            transform: scale(1.02);
        }
        
        /* 媒体播放器样式 */
        .media-player {
            background: #f8f9fa;
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        
        /* 按钮样式 */
        .stButton>button {
            border: 2px solid #00a1d6;
            color: #00a1d6;
            background: white;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background: #e6f7ff;
            color: #0084b4;
            border-color: #0084b4;
        }
    </style>
    """, unsafe_allow_html=True)

    # 图片展示模块
    st.markdown('<p class="main-title">园内精彩瞬间</p>', unsafe_allow_html=True)
    
    with st.expander("📸 风景图片集", expanded=True):
        images = [
            "https://wallpaperaccess.com/full/1414728.jpg",
            "https://wallpaperaccess.com/full/1167990.jpg",
            "https://wallpapercave.com/wp/D3r6gVH.jpg"
        ]
        
        # 使用columns创建响应式图片布局
        cols = st.columns(3)
        for idx, img in enumerate(images):
            with cols[idx % 3]:
                st.image(img, use_container_width=True, caption=f"风景图片 {idx+1}")

    # 音频播放模块
    with st.expander("🎵 背景音乐", expanded=True):
        audio_files = {
            "轻音乐1": "https://music.163.com/song/media/outer/url?id=28263184.mp3",
            "轻音乐2": "https://music.163.com/song/media/outer/url?id=1359356908.mp3",
            
        }
        
        selected_audio = st.selectbox("选择音频", options=list(audio_files.keys()))
        st.audio(audio_files[selected_audio])

    # 视频播放模块
    st.markdown('<p class="main-title">精彩视频展播</p>', unsafe_allow_html=True)
    
    video_data = {
        "高山风景视频": "BV1ST411E7wb",  
        "美到窒息的感觉": "BV13A4y1Z7m2",
        "童话世界": "BV1co7Bz6Ehp",
        "蓝调时刻": "BV1gLB4YwEXH",  
        "自然风光": "BV1exrdYZEfM",
        "峡湾地貌": "BV1d9f4YoEwV"
    }

    # 初始化session_state
    if "current_video_index" not in st.session_state:
        st.session_state.current_video_index = 0

    # 视频选择器
    selected_video = st.selectbox(
        "选择视频",
        options=list(video_data.keys()),
        index=st.session_state.current_video_index
    )

    # 更新当前视频索引
    current_index = list(video_data.keys()).index(selected_video)
    if current_index != st.session_state.current_video_index:
        st.session_state.current_video_index = current_index
        st.rerun()

    # 视频播放器
    with st.container():
        st.markdown("""
        <div style="margin:1rem 0; border-radius:12px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.1)">
            <iframe 
                width="100%" 
                height="500" 
                src="//player.bilibili.com/player.html?bvid={}&page=1&high_quality=1&autoplay=0" 
                scrolling="no" 
                frameborder="no" 
                allowfullscreen="true">
            </iframe>
        </div>
        """.format(video_data[selected_video]), unsafe_allow_html=True)

        # 导航按钮
        col1, col2, col3 = st.columns([1,1,6])
        with col1:
            if st.button("◀ 上一个"):
                st.session_state.current_video_index = (st.session_state.current_video_index - 1) % len(video_data)
                st.rerun()
        with col2:
            if st.button("下一个 ▶"):
                st.session_state.current_video_index = (st.session_state.current_video_index + 1) % len(video_data)
                st.rerun()

    # 当前播放信息
    st.success(f"正在播放: {selected_video}")



###----------------------------------------------------------------------------------
###  模块③
###  餐厅内容展示，包含数据，条形图，面积图，折线图，进阶地图
###----------------------------------------------------------------------------------




       
if page == "附近美食":
    restaurants = pd.DataFrame({
    "餐厅名称": ["舒记老友粉", "天福香老友粉", "三品王牛肉粉", "姜胖胖自助烤肉", "牛扒大亨西餐厅","素宴·蔬食(素食自助餐厅科德店)","隆江猪脚饭(衡阳店)","尝回家猪脚饭·烧卤·白切(友爱店)","乐观面屋(东盟店)","重庆江湖拌面","三兄弟小龙虾馆","苏格里岛自助海鲜烤肉","吉布鲁牛排海鲜自助(南宁江南万达店)","鹿客臻鲜·海鲜烤肉自助餐厅(蓝鲸世界店)","今邕烧烤(园湖店)","舌战烧烤酒馆(三街两巷店)","亿口香龙虾","炙爱烧烤(万秀店)","夏朗蛋糕(城市花园店)","卡卡米苏·生日蛋糕(西乡塘店)","盛记顺德高佬猪杂粥店","南宁市雲菌瑶酒楼","啫啫村-生料啫啫煲(埌西店)"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐","自助","堂食","堂食","粉","粉","小吃","自助","自助","自助","烧烤","烧烤","小吃","烧烤","糕点","糕点","粥","自助","堂食"],
    "评分": [4.4, 4.1,  4.9, 4.3,4.6,4.7,4.4,4.5,4.2,4.7,4.6,4.6,4.5,4.3,4.8,4.6,4.3,4.2,4.6,4.7,4.4,4.2,4.7],
    "人均消费(元)": [15, 15, 20, 60, 80,30,30,39,21,20,103,78,80,90,123,90,120,89,68,134,15,200,34],
    "营业时间": ["6:00-22:00","5:00-23:00","10:00-23:00","12:00-24:00","17:00-20:30","10:30-20:00","9:00-19:00","9:00-20:00","9:00-20:00","12:00-23:00","12:00-23:00","12:300-23:00","12:00-23:00","17:00-23:00","17:00-02:00","17:00-02:00","12:300-23:00","12:300-23:00","17:30-22:00","7:30-22:00","7:30-22:00","7:30-22:00","7:30-22:00"],
    "latitude": [22.809728,22.822481,22.838432,22.789523,22.808867,22.848224,22.831269,22.839999,22.689112,22.810435,22.756756,22.813919,22.790188,22.769671,22.826847,22.813768,22.845349,22.789165,22.808243,22.688017,22.819031,22.798990,22.805077],
    "longitude": [108.324614,108.387910,108.262110,108.313493,108.326838,108.257296,108.310691,108.309224,108.267817,108.284216,108.332567,108.321484,108.312827,108.306724,108.339396,108.320656,108.315969,108.318908,108.370764,108.300288,108.343062,108.378891,108.368414]
    })

    tab1, tab2, tab3 = st.tabs(["门店数据详情", "门店数据可视化", "店铺分布"])
    with tab1:
        st.markdown('### 门店详细数据（仅展示评分大于4.5的店铺）')

        #仅展示评分大于4.5的店
        high_rating = restaurants[restaurants["评分"] >= 4.5]
        # 显示表格（可排序、搜索）
        st.dataframe(high_rating[["餐厅名称", "类型", "评分", "人均消费(元)","营业时间"]])

    with tab2:
        st.markdown("### 人均消费数据")
        st.bar_chart(restaurants.set_index("餐厅名称")["人均消费(元)"])
        st.markdown('### 门店评分数据（仅展示评分大于4.5的店铺）')

        # 设置餐厅名称为索引（X轴）
        data_for_chart = restaurants.set_index("餐厅名称")["评分"]

        # 绘制面积图
        st.area_chart(data_for_chart)
        

        # 绘制折线图
        st.markdown('### 价格走势折线图')

        data = {
            '月份': ['一月', '二月', '三月', '四月', '五月', '六月', 
                   '七月', '八月', '九月', '十月', '十一月', '十二月'],
            '书记老友粉': [15, 18, 14, 17, 19, 31, 22, 13, 17, 13, 11, 21],
            '天福香老友粉': [18, 16, 21, 24, 45, 21, 12, 24, 26, 16, 18, 25],
            '三品王牛肉粉': [23, 21, 34, 23, 25, 35, 53, 27, 21, 24, 32, 14],
            '姜胖胖自助烤肉': [115, 145, 95, 122, 165, 116, 131, 151, 125, 99, 123, 156],
            '乐观面屋(东盟店)': [27, 25, 34, 35, 21, 41, 12, 35, 23, 34, 28, 45]
        }

        df = pd.DataFrame(data)
        df.index = pd.RangeIndex(start=1, stop=13, name='序号')  # 更规范的设置索引方式
        st.line_chart(df, x='月份')

    with tab3:    
        import pydeck as pdk
        import streamlit.components.v1 as components  # 确保这行在最前面
        
        # API配置
        TENCENT_API_KEY = "7QTBZ-NDMLM-GAQ6N-6YN54-XVWL2-5WFQS"

        st.title("🍜 南宁餐厅地图（腾讯卫星图）")
    
        # 显示原始数据前几行
        
        # 列名重命名
        restaurants = restaurants.rename(columns={
            '餐厅名称': 'name',
            '类型': 'category',
            '评分': 'rating',
            '人均消费(元)': 'price',
            '营业时间': 'hours'
            # latitude和longitude不需要重命名
        })
        
        # 检查必要列
        required_columns = ['name', 'latitude', 'longitude']
        missing_cols = [col for col in required_columns if col not in restaurants.columns]
        if missing_cols:
            st.error(f"缺少必要列: {missing_cols}")
            st.stop()
        
        # 确保经纬度是数值
        restaurants['latitude'] = pd.to_numeric(restaurants['latitude'], errors='coerce')
        restaurants['longitude'] = pd.to_numeric(restaurants['longitude'], errors='coerce')
        
        # 移除无效坐标
        restaurants = restaurants.dropna(subset=['latitude', 'longitude'])
        
        
        # 检查是否有有效数据
        if restaurants.empty:
            st.error("没有有效的餐厅数据可供显示！")
            st.stop()

        # 地图HTML代码
        map_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <script src="https://map.qq.com/api/gljs?v=2.exp&key={TENCENT_API_KEY}"></script>
            <style>
                #map-container {{
                    width: 100%;
                    height: 500px;
                }}
                .info-window {{
                    min-width: 200px;
                    padding: 10px;
                }}
            </style>
        </head>
        <body>
            <div id="map-container">
                <div id="map" style="width:100%;height:100%;"></div>
                <div id="loading">地图加载中...</div>
            </div>
            
            <script>
                function initMap() {{
                    try {{
                        document.getElementById('loading').style.display = 'none';
                        
                        var restaurantData = {restaurants.to_json(orient='records', force_ascii=False)};
                        
                        // 设置默认中心点（南宁市中心）
                        var center = new TMap.LatLng(22.817, 108.366);
                        
                        if (restaurantData.length > 0) {{
                            var avgLat = restaurantData.reduce((sum, r) => sum + r.latitude, 0) / restaurantData.length;
                            var avgLng = restaurantData.reduce((sum, r) => sum + r.longitude, 0) / restaurantData.length;
                            center = new TMap.LatLng(avgLat, avgLng);
                        }}
                        
                        // 创建地图
                        var map = new TMap.Map(document.getElementById('map'), {{
                            center: center,
                            zoom: 12
                        }});
                        
                        // 添加标记
                        var markers = new TMap.MultiMarker({{
                            map: map,
                            styles: {{
                                default: new TMap.MarkerStyle({{
                                    width: 25,
                                    height: 35,
                                    src: 'https://mapapi.qq.com/web/lbs/javascriptGL/demo/img/markerDefault.png'
                                }})
                            }},
                            geometries: restaurantData.map(r => ({{
                                position: new TMap.LatLng(r.latitude, r.longitude),
                                properties: {{
                                    title: r.name || '未知餐厅',
                                    category: r.category || '未知',
                                    rating: r.rating || '无',
                                    price: r.price || '未知',
                                    hours: r.hours || '未知'
                                }}
                            }}))
                        }});
                        
                        // 点击事件
                        markers.on('click', function(evt) {{
                            var info = new TMap.InfoWindow({{
                                map: map,
                                position: evt.geometry.position,
                                content: `
                                    <div style="padding:10px">
                                        <h4>${{evt.geometry.properties.title}}</h4>
                                        <p>类型: ${{evt.geometry.properties.category}}</p>
                                        <p>评分: ${{evt.geometry.properties.rating}}</p>
                                        <p>人均: ${{evt.geometry.properties.price}}</p>
                                        <p>营业: ${{evt.geometry.properties.hours}}</p>
                                    </div>
                                `
                            }});
                        }});
                        
                    }} catch (error) {{
                        console.error('地图初始化错误:', error);
                        document.getElementById('loading').innerHTML = 
                            '地图加载失败: ' + error.message;
                    }}
                }}
                
                // 检查API是否加载
                function checkAPI() {{
                    if (typeof TMap !== 'undefined') {{
                        initMap();
                    }} else {{
                        setTimeout(checkAPI, 100);
                    }}
                }}
                
                // 页面加载后执行
                document.addEventListener('DOMContentLoaded', checkAPI);
            </script>
        </body>
        </html>
        """
        
        # 显示地图
        components.html(map_html, height=600)
        ###----------------腾讯地图模块-----------------------



###----------------------------------------------------------------------------------
###  模块④
###  个人简历编辑器
###----------------------------------------------------------------------------------

if page=="招聘个人信息简历投稿":
    st.markdown('<p class="main-title">个人简历</p>', unsafe_allow_html=True)


    from datetime import datetime
    from PIL import Image
    import io


    # 初始化session state
    if 'resume_data' not in st.session_state:
        st.session_state.resume_data = {
            'name': '',
            'gender': '',
            'email': '',
            'birth_date': '',
            'work_location': '',
            'position': '',
            'age': '',
            'phone': '',
            'bio': '',
            'avatar': None
        }

    # 创建两列
    col1, col2 = st.columns(2)

    with col1:
        st.header("个人信息表单", divider="rainbow")
        # 表单输入
        with st.form("resume_form"):
            # 头像上传
            uploaded_file = st.file_uploader("上传头像（最大200MB，支持JPG,JEPG,PNG格式）", type=['jpg', 'jpeg', 'png'])
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                image.thumbnail((200, 200))
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='PNG')
                st.session_state.resume_data['avatar'] = img_byte_arr.getvalue()
            
            st.session_state.resume_data['name'] = st.text_input("姓名*(必填)", st.session_state.resume_data['name'])
            st.session_state.resume_data['gender'] = st.selectbox("性别*(必填)", ["", "男", "女"], 
                                                              index=0 if not st.session_state.resume_data['gender'] else ["男", "女"].index(st.session_state.resume_data['gender']))
            st.session_state.resume_data['email'] = st.text_input("邮箱*(必填)", st.session_state.resume_data['email'])
            
            # 日期输入
            birth_date = st.date_input("出生日期*", 
                                     value=datetime.strptime(st.session_state.resume_data['birth_date'], "%Y-%m-%d").date() 
                                     if st.session_state.resume_data['birth_date'] else None,
                                     min_value=datetime(1900, 1, 1),
                                     max_value=datetime.now())
            st.session_state.resume_data['birth_date'] = birth_date.strftime("%Y-%m-%d") if birth_date else ""
            
            st.session_state.resume_data['work_location'] = st.text_input("家庭住址", st.session_state.resume_data['work_location'])
            st.session_state.resume_data['position'] = st.text_input("当前身份（如学生）*(必填)", st.session_state.resume_data['position'])
            
            # 计算年龄
            if st.session_state.resume_data['birth_date']:
                birth_year = datetime.strptime(st.session_state.resume_data['birth_date'], "%Y-%m-%d").year
                current_year = datetime.now().year
                st.session_state.resume_data['age'] = str(current_year - birth_year)
            else:
                st.session_state.resume_data['age'] = ""
            
            st.session_state.resume_data['phone'] = st.text_input("联系电话", st.session_state.resume_data['phone'], placeholder="010-0000-0001")
            st.session_state.resume_data['bio'] = st.text_area("个人简介", st.session_state.resume_data['bio'], 
                                                            placeholder="请简要介绍自己...", height=150)
            
            submitted = st.form_submit_button("更新简历", use_container_width=True)
            if submitted:
                if not st.session_state.resume_data['name'] or not st.session_state.resume_data['gender'] or not st.session_state.resume_data['email'] or not st.session_state.resume_data['birth_date'] or not st.session_state.resume_data['position']:
                    st.error("请填写所有带*号的必填项")

    with col2:
        st.header("简历预览", divider="rainbow")
        
        # 简历样式
        st.markdown("""<style>.resume-box {
            border: 1px solid #e0e0e0;
            padding: 25px;
            border-radius: 15px;
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .resume-header {
            border-bottom: 2px solid #4a6fa5;
            margin-bottom: 20px;
            padding-bottom: 15px;
        }
        .empty-field {
            color: #999999;
            font-style: italic;
        }
        .section-title {
            color: #4a6fa5;
            font-weight: bold;
            margin-bottom: 10px;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # 简历内容
        with st.container():
            st.markdown('<div class="resume-box">', unsafe_allow_html=True)
            
            # 头部信息
            col_header1, col_header2 = st.columns([1, 3])
            with col_header1:
                if st.session_state.resume_data['avatar']:
                    st.image(Image.open(io.BytesIO(st.session_state.resume_data['avatar'])), width=100)
                else:
                    st.image(Image.new('RGB', (100, 100), color='lightgray'), width=100)
            
            # 基本信息
            st.markdown('<p class="section-title">基本信息</p>', unsafe_allow_html=True)
            cols = st.columns(2)
            with cols[0]:
                st.text(f"年龄: {st.session_state.resume_data['age'] or '未填写'}")
                st.text(f"性别: {st.session_state.resume_data['gender'] or '未填写'}")
            with cols[1]:
                st.text(f"邮箱: {st.session_state.resume_data['email'] or '未填写'}")
                st.text(f"电话: {st.session_state.resume_data['phone'] or '010-0000-0001'}")
            
            st.divider()
            
            # 个人信息
            st.markdown('<p class="section-title">个人信息</p>', unsafe_allow_html=True)
            cols = st.columns(2)
            with cols[0]:
                st.text(f"出生日期: {st.session_state.resume_data['birth_date'] or '未填写'}")
            with cols[1]:
                st.text(f"工作地点: {st.session_state.resume_data['work_location'] or '未填写'}")
            
            st.divider()
            
            # 个人简介
            st.markdown('<p class="section-title">个人简介</p>', unsafe_allow_html=True)
            st.text(st.session_state.resume_data['bio'] or "请简要介绍自己...")
            
            st.markdown('</div>', unsafe_allow_html=True)



###----------------------------------------------------------------------------------
###  模块⑤
###  企鹅分类器
###----------------------------------------------------------------------------------


if page == "企鹅分类":


    # 第八章/explore_data.py
    import pandas as pd

    # 设置输出右对齐，防止中文不对齐
    pd.set_option('display.unicode.east_asian_width', True)
    # 读取数据集，并指定字符编码为gbk，防止中文报错
    penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')

    # 输出数据框的前5行
    print(penguin_df.head())



    # 第八章/data_preprocess.py
    import pandas as pd


    # 设置输出右对齐，防止中文不对齐
    pd.set_option('display.unicode.east_asian_width', True)
    # 读取数据集，并指定字符编码为gbk，防止中文报错
    penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')
    # 删除缺失值所在的行
    penguin_df.dropna(inplace=True)
    # 定义企鹅的种类为目标输出变量
    output = penguin_df['企鹅的种类']
    # 将去除年份列不作为特征列
    # 使用企鹅栖息的岛屿、喙的长度、翅膀的长度、身体质量、性别作为特征列
    features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]
    # 对特征列进行独热编码
    features = pd.get_dummies(features)
    # 将目标输出变量，进行转换为离散数值表示
    output_codes, output_uniques = pd.factorize(output)


    print('下面是去重后，目标输出变量的数据：')
    print(output_uniques)
    print('下面是独热编码后，特征列的数据：')
    print(features.head())




    # 第八章/generate_model.py
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split

    # 读取数据集，并指定字符编码为gbk，防止中文报错
    penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')
    # 删除缺失值所在的行
    penguin_df.dropna(inplace=True)
    # 定义企鹅的种类为目标输出变量
    output = penguin_df['企鹅的种类']
    # 将去除年份列不作为特征列
    # 使用企鹅栖息的岛屿、喙的长度、翅膀的长度、身体质量、性别作为特征列
    features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]
    # 对特征列进行独热编码
    features = pd.get_dummies(features)
    # 将目标输出变量，进行转换为离散数值表示
    output_codes, output_uniques = pd.factorize(output)

    # 从features和output_codes 这两个数组中划分数据集为训练集和测试集。
    # 训练集为80%，测试集为20%（1-80%）
    # 返回的x_train和 y_train为划分得到的训练集特征和标签。
    # x_test和y_test为划分得到的测试集特征和标签。
    # 这里标签和目标输出变量是一个意思

    x_train, x_test, y_train, y_test = train_test_split(features, output_codes, train_size=0.8)

    # 构建一个随机森林分类器
    rfc = RandomForestClassifier()

    # 使用训练集数据x_train和y_train来拟合(训练)模型。
    rfc.fit(x_train, y_train)

    # 用训练好的模型rfc对测试集数据x_test进行预测，预测结果存储在y_pred中
    y_pred = rfc.predict(x_test)

    # 计算测试集上模型的预测准确率。
    # 方法是使用accuracy_score方法，比对真实标签y_test和预测标签y_pred
    # 返回预测正确的样本占全部样本的比例，即准确率。
    score = accuracy_score(y_test, y_pred)
    print(f'该模型的准确率是：{score}')



    # 第八章/save_model.py
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    import pickle  # 用来保存模型和output_uniques变量


    # 读取数据集，并指定字符编码为gbk，防止中文报错
    penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')
    # 删除缺失值所在的行
    penguin_df.dropna(inplace=True)
    # 定义企鹅的种类为目标输出变量
    output = penguin_df['企鹅的种类']
    # 将去除年份列不作为特征列
    # 使用企鹅栖息的岛屿、喙的长度、翅膀的长度、身体质量、性别作为特征列
    features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]
    # 对特征列进行独热编码
    features = pd.get_dummies(features)
    # 将目标输出变量，进行转换为离散数值表示
    output_codes, output_uniques = pd.factorize(output)

    # 从features和output_codes 这两个数组中划分数据集为训练集和测试集。
    # 训练集为80%，测试集为20%（1-80%）
    # 返回的x_train和 y_train为划分得到的训练集特征和标签。
    # x_test和y_test为划分得到的测试集特征和标签。
    # 这里标签和目标输出变量是一个意思

    x_train, x_test, y_train, y_test = train_test_split(features, output_codes, train_size=0.8)

    # 构建一个随机森林分类器
    rfc = RandomForestClassifier()

    # 使用训练集数据x_train和y_train来拟合(训练)模型。
    rfc.fit(x_train, y_train)

    # 用训练好的模型rfc对测试集数据x_test进行预测，预测结果存储在y_pred中
    y_pred = rfc.predict(x_test)

    # 计算测试集上模型的预测准确率。
    # 方法是使用accuracy_score方法，比对真实标签y_test和预测标签y_pred
    # 返回预测正确的样本占全部样本的比例，即准确率。
    score = accuracy_score(y_pred, y_test)

    # 使用with语句，简化文件操作
    # open()函数和'wb'参数用于创建并写入字节流
    # pickle.dump()方法将模型对象转成字节流
    with open('rfc_model.pkl', 'wb') as f:
        pickle.dump(rfc, f)

    # 同上
    # 将映射变量写入文件中
    with open('output_uniques.pkl', 'wb') as f:
        pickle.dump(output_uniques, f)

    print('保存成功，已生成相关文件。')



    import streamlit as st
    import pickle
    import pandas as pd


    # 加载模型（只需加载一次）
    @st.cache_resource  # 使用缓存避免重复加载
    def load_model():
        with open('rfc_model.pkl', 'rb') as f:
            rfc_model = pickle.load(f)
        with open('output_uniques.pkl', 'rb') as f:
            output_uniques_map = pickle.load(f)
        return rfc_model, output_uniques_map

    rfc_model, output_uniques_map = load_model()

    # 侧边栏导航
    with st.sidebar:
        st.image('images/rigth_logo.png', width=100)
        st.title('请选择页面')
        page = st.selectbox("请选择页面", ["简介页面", "预测分类页面"], label_visibility='collapsed')

    if page == "简介页面":
        st.title("企鹅分类器 :penguin:")
        st.header('数据集介绍')
        st.markdown("""帕尔默群岛企鹅数据集是用于数据探索和数据可视化的一个出色的数据集...""")
        st.header('三种企鹅的卡通图像')
        st.image('images/penguins.png')

    elif page == "预测分类页面":
        st.header("预测企鹅分类")
        st.markdown("输入6个信息，预测企鹅物种：")

        col_form, _, col_logo = st.columns([3, 1, 2])
        
        with col_form:
            with st.form('user_inputs'):
                island = st.selectbox(
                    '企鹅栖息的岛屿', 
                    options=['托尔森岛', '比斯科群岛', '德里姆岛'],
                    key="island_selectbox"
                )
                sex = st.selectbox('性别', options=['雄性', '雌性'], key="sex_selectbox")
                bill_length = st.number_input('喙的长度（毫米）', min_value=0.0, key="bill_length")
                bill_depth = st.number_input('喙的深度（毫米）', min_value=0.0, key="bill_depth")
                flipper_length = st.number_input('翅膀的长度（毫米）', min_value=0.0, key="flipper_length")
                body_mass = st.number_input('身体质量（克）', min_value=0.0, key="body_mass")
                submitted = st.form_submit_button('预测分类')

        # 数据预处理
        island_map = {
            '比斯科群岛': (0, 0, 1),
            '德里姆岛': (0, 1, 0),
            '托尔森岛': (1, 0, 0)
        }
        island_dream, island_torgerson, island_biscoe = island_map.get(island, (0, 0, 0))
        sex_male = 1 if sex == '雄性' else 0
        sex_female = 1 if sex == '雌性' else 0

        format_data = [
            bill_length, bill_depth, flipper_length, body_mass,
            island_dream, island_torgerson, island_biscoe, sex_female, sex_male
        ]

        # 预测逻辑
        if submitted:
            format_data_df = pd.DataFrame(data=[format_data], columns=rfc_model.feature_names_in_)
            predict_result_code = rfc_model.predict(format_data_df)
            predict_result_species = output_uniques_map[predict_result_code][0]
            
            st.success(f'预测结果：**{predict_result_species}**')
            with col_logo:
                st.image(f'images/{predict_result_species}.png', width=300)






###=====================================================================
# 请在此段代码上方添加新代码！
# 添加页脚
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    <p>© 2025 CPU180 个人网页制作演示 |  主版本号：1.0.0 | 内部版本号：0.6.18.1</p>
</div>
""", unsafe_allow_html=True)
###=====================================================================

