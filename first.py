import streamlit as st # 导入Streamlit并用st代表它
import numpy as np #导入numpy库调用表格内容
import pandas as pd #导入pandas库调用表格内容

# 标题格式
st.markdown('# 学生小陆-数学档案😇')

st.markdown('# 😃基本信息')

st.markdown('''# 姓名: *陆小陆😁*
#### 班级: *23级练习生一班😉*
#### 学号: *007😇*''')


# 创建一个为基本信息的标题，并指定锚点为基本信息
st.header('兴趣:smiley:', anchor='text!')
st.markdown('### :red[游戏] 🎮, :blue[游泳]🏊︎ ,:orange[唱跳]🎤 , :green[篮球]🏀')

#调用指标类展示元素metric
st.subheader('')
st.metric(label="当前学期", value="大二 上学期")
st.subheader('学习情况')

c1, c2, c3 = st.columns(3)
c1.metric(label="当前周数", value="15/20", delta="剩余5周")
c2.metric(label="四年级进度", value="1/2", delta="已过四级")
c3.metric(label="人生进度", value="20/100", delta="未来可期")

#对于箭头的表示通过在内容前使用+或-进行展示
st.metric(label="-心情状态",value="心情状态",delta="愉悦",label_visibility='visible')

# Streamlit课程进度部分
st.header('Streamlit课程进度')
st.progress(0.2, text="Streamlit课程进度") # 此处设置参数为20%



data = {
   '课程': ['高等数学', '大学英语', 'C语言程序设计'],
   '期末达标分数': [90,101,97],
   '状态': ['***通过***','***通过***','***补考***'], 
   '难度': ['***中等***','***简单***','***困难***']
}

# 字体样式
#st.markdown('*斜体文本*')
#st.markdown(' 斜体文本 ')
#st.markdown('**斜体文本**')
#st.markdown('_*斜体文本 ')
#st.markdown('**斜体文本***')
#st.markdown('_* 斜体文本 ')

index = pd.Series(['1','2','3'], name='') 
# 根据上面创建的data和index，创建数据框 
df = pd.DataFrame(data, index=index) 

st.subheader('课程日志')
st.table(df)
#使用datatrame可以增加用户对数据的处理，此处使用table表示仅进行展示

# 创建一个代码块，用于展示python_code的内容
# line_numbers=True 表示显示代码行数
# language为None，即该代码块无法满足高亮
st.subheader('Python代码展示')
python_code = '''def hello():
    print('你好，Streamlit！')'''

st.code(python_code, line_numbers=True)

st.subheader('java代码展示')
java_code = '''public class Hello {
    public static void main(String[] args) {
        System.out.println('你好！ Streamlit！');
    }
}'''

st.code(java_code, language='java',line_numbers=True)

st.subheader('JavaScript代码展示')
javascript_code = '''<p id="demo"></p>
<script>
    document.getElementById('demo').innerHTML ='你好！ Streamlit！';
</script>'''

st.code(javascript_code, language='javascript',line_numbers=True)





# 餐厅数据
restaurants = pd.DataFrame({
    "餐厅名称": ["舒记老友粉", "天福香老友粉", "三品王牛肉粉", "姜胖胖自助烤肉", "牛扒大亨西餐厅"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
    "评分": [4.4, 4.1, 4.5, 4.9, 4.3],
    "人均消费(元)": [15, 15, 20, 60, 80],
    "营业时间": ["6:00-22:00","9:00-22:00","5:00-23:00","10:00-23:00","12:00-24:00"],
    "latitude": [22.809728,22.822481,22.838432,22.789523,22.808867],
    "longitude": [108.324614,108.387910,108.262110,108.313493,108.326838]
})





st.markdown('### 门店详细数据（仅展示评分大于4.5的店铺）')

#仅展示评分大于4.5的店
high_rating = restaurants[restaurants["评分"] >= 4.5]
# 显示表格（可排序、搜索）
st.dataframe(high_rating[["餐厅名称", "类型", "评分", "人均消费(元)","营业时间"]])




st.markdown("### 人均消费数据")

st.bar_chart(restaurants.set_index("餐厅名称")["人均消费(元)"])


st.markdown('### 门店评分数据（仅展示评分大于4.5的店铺）')

# 设置餐厅名称为索引（X轴）
data_for_chart = restaurants.set_index("餐厅名称")["评分"]

# 绘制面积图
st.area_chart(data_for_chart)



import pydeck as pdk

# 方法1：修复 st.map() 的悬停
st.header("基础地图（自动悬停）")
st.map(restaurants[["latitude", "longitude", "餐厅名称"]])  # 只传需要的列



import streamlit.components.v1 as components



# 配置
TENCENT_API_KEY = "7QTBZ-NDMLM-GAQ6N-6YN54-XVWL2-5WFQS"
restaurants = pd.DataFrame({
    "name": ["舒记老友粉", "天福香老友粉", "三品王牛肉粉"],
    "lat": [22.809728, 22.822481, 22.838432],
    "lng": [108.324614, 108.387910, 108.262110],
    "price": [15, 15, 20]
})

# 生成地图
map_html = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://map.qq.com/api/gljs?v=1.exp&key={TENCENT_API_KEY}"></script>
    <style>#map {{ width:100%; height:500px; }}</style>
</head>
<body>
    <div id="map"></div>
    <script>
        var map = new TMap.Map("map", {{
            center: new TMap.LatLng(22.82, 108.35),
            zoom: 12,
            mapStyleId: "卫星图"
        }});

        // 动态加载Python数据
        var restaurants = {restaurants.to_json(orient="records")};
        
        restaurants.forEach(restaurant => {{
            var marker = new TMap.Marker({{
                position: new TMap.LatLng(restaurant.lat, restaurant.lng),
                map: map,
                content: '<div style="background:#FF6D00;color:white;padding:4px 8px;">' + restaurant.name + '</div>'
            }});

            marker.on("click", () => {{
                new TMap.InfoWindow({{
                    map: map,
                    position: new TMap.LatLng(restaurant.lat, restaurant.lng),
                    content: `
                        <h3>${{restaurant.name}}</h3>
                        <p>人均: ￥${{restaurant.price}}元</p>
                    `
                }}).open();
            }});
        }});
    </script>
</body>
</html>
"""

# 显示
st.title("🍜 南宁餐厅地图（腾讯卫星图）")
components.html(map_html, height=550)
