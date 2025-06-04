import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Marketing Intern
    **Chinese Arts & Crafts** | *March 2025 - June 2025*
    
    - Planned daily contents for Facebook, Instagram and Xiaohongshu, including copywriting, co-ordination of visual materials and regular posting, to maintain the brand's online activity
    - Connected with KOLs/KOCs to expand brand exposure through content co-operation, topic management, etc. to accurately reach target customer groups
    """)
    
    st.markdown("""
    ### Public relations intern
    **Hill+Knowlton Strategies** | *March 2023 - June 2023*
    
    - Produced 10 news reports for clients including large-scale industrial companies; succeeded in having each report released by 15 leading media, such as People's Daily and Tencent News, with 1,000+ viewership on every media platform
    - Conducted desk research on available media reporting styles and focuses; recommended vertical media for clients according to their brand and product attributes to optimize the media matrix
    """)
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R
        - **Video Editing:** Adobe Premiere, Vegas
        - **Photo Editing:** Photoshop
        - **Visualization:** Matplotlib, Seaborn
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication in both Chinese and English
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 
