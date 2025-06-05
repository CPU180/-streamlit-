import streamlit as st # 导入Streamlit并用st代表它

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

import pandas as pd #导入pandas库调用表格内容

data = {
   '课程': ['高等数学', '大学英语', 'C语言程序设计'],
   '期末达标分数': [90,101,97],
   '状态': ['***通过✅***','***通过✅***','***补考❌***'], 
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
