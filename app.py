import streamlit as st
import tensorflow as tf
import numpy as np

# 网页基本设置
st.set_page_config(
    page_title="股市AI预测大师",
    page_icon="📈",
    layout="centered"
)

# 网页标题
st.title("📊 AI股市预测大师")
st.subheader("预测明天的收盘价，一探趋势端倪 🔮")

# 加载模型
model = tf.keras.models.load_model('model.h5')

# 用户输入区域
st.markdown("请输入今日收盘价，以及其他特征（如成交量、开盘价等）👇")

# 示例：假设模型需要三个输入
close_today = st.number_input("📌 今日收盘价", min_value=0.0, format="%.2f")
volume_today = st.number_input("🔄 今日成交量", min_value=0.0, format="%.0f")
open_today = st.number_input("🟢 今日开盘价", min_value=0.0, format="%.2f")

# 预测按钮
if st.button("✨ 开始预测明天收盘价"):
    input_data = np.array([[close_today, volume_today, open_today]])
    prediction = model.predict(input_data)
    predicted_price = prediction[0][0]

    st.success(f"🧠 预测结果：明日收盘价 ≈ ￥{predicted_price:.2f}")
    st.balloons()

# 页脚
st.markdown("---")
st.caption("由广外数字运营系梁子羿同学研发 · AI助力炒股 · 预测仅供参考 🚫投资建议")
