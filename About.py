
import streamlit as st 
from main import MultiApp


def app():
  
    
    
  
    st.markdown('# Helmet Detection with CNN')
    st.markdown("----")

    
    st.subheader("About")
    st.write("Assuring safety in various situations has become a top priority in today's technological environment which is continually expanding. In the past couple of years, there has been a significant amount of injuries and deaths of motorcyclists due to non-wearing of helmets. In order to reduce these road accidents, the detection of helmetless motorcycles is essential. Wearing of helmets is a crucial in abiding traffic rules and regulations. In spite of these orders, a massive number of motorcycles still do not adhere to these rules. ")
    st.write("Earlier, various researchers have applied traditional image processing methods for feature extraction for detecting helmets. Nowadays, we have been introduced to a new and upcoming technology known as Deep Learning. In the field of computer vision, deep learning can be implemented with the help of Convolutional Neural Networks (CNN). CNN along with a quality dataset can be tuned optimally in order to create a well-structured ‘Helmet Detection’ Model. Automatic feature extraction with the help of CNN will help boost the accuracy of model. ")
    st.write("This project primarily aims to ensure safety of motorcyclists by detecting whether they are wearing a helmet or not.  Detecting the absence of helmets helps reduce the risk of head injuries which can lead to extreme consequences. In addition to this, our project also aims to the streamline surveillance process. When a helmet is not detected on a rider, an alert or notification can be triggered and this information can be sent to the rule-enforcing authorities. By promoting safety and alleviating human errors, our model can create a safer environment on the roads with the help of CNN.")
    


    st.write("As a result of these traffic violations, surveillance cameras have been set up by the Government to maintain protocol. Helmets are an essential piece of safety equipment that greatly lowers the risk of head injuries and also saves lives. In counties like Dubai and Pakistan, all major cities have already deployed large scale camera networks for video surveillance purposed to keep watching on this crisis. A recent study has discovered that human surveillance is highly inefficient and causes error as the time period increases. Therefore, we find it vital to have a reliable and robust system which can detect the rule-violators from surveillance images and videos.")

    col1, col2 ,col3 = st.columns([55,1,55]) 
    
    
    
    with col3:
        st.image("1.jpeg", caption='Template Matching using SQDIFF', use_column_width=True)
        

    with col1:
        st.image("3.jpeg", caption='Helmet Feature Matching with SIFT features using FLANN based matcher', use_column_width=True)

        
