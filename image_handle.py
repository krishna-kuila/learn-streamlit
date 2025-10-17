import streamlit as st
import time
from PIL import Image


# --- Page Configuration and Setup (for aesthetics) ---
st.set_page_config(
    page_title="Visual Intelligence Assistant",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Custom CSS for a clean, modern look (subtle shadows and primary color emphasis)
st.markdown("""
<style>
    /* Ensure Streamlit containers have rounded corners and shadows */
    .st-emotion-cache-1kyxhtm {
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        border: 1px solid #e0e0e0;
    }
    .st-emotion-cache-zt5igj {
        /* Container for the main content to match the clean aesthetic */
        padding: 2rem;
        border-radius: 15px;
        background-color: #f9f9f9; 
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.05);
    }
    /* Main title styling */
    .st-emotion-cache-10trblm {
        color: #4A90E2; /* Primary blue color */
        font-weight: 700;
    }
    /* Set a nice, legible font */
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }
</style>
""", unsafe_allow_html=True)


# --- Simulated LLM Analysis Function ---
# In a real application, you would replace this function with an API call 
# to a model like Gemini to perform image understanding.
def analyze_image_with_llm(uploaded_file):
    """
    Simulates sending the image data to an LLM API for analysis.
    In a live environment, you would use a library like 'requests' 
    to send the image and prompt in the required API structure.
    """
    
    # 1. Image preparation (simulated for simplicity)
    image_name = uploaded_file.name
    
    # 2. Simulate API request payload
    # This JSON structure represents what you would send to a tool like Gemini.
    mock_payload = {
        "model": "gemini-2.5-flash-preview-05-20",
        "systemInstruction": "You are a professional image analysis assistant. Provide a highly detailed description and analysis of the uploaded image.",
        "contents": [
            {"parts": [
                {"text": f"Analyze this image named {image_name}. What do you see? Provide a structured JSON output."},
                # In a real application, the image base64 data would go here
                {"inlineData": {"mimeType": uploaded_file.type, "data": "BASE64_IMAGE_DATA_HERE..."}}
            ]}
        ]
    }
    
    # 3. Simulate network latency and processing
    time.sleep(3) # Simulate 3 seconds of network time and model processing
    
    # 4. Mock (Simulated) LLM Response (structured for better display)
    if "dog" in image_name.lower():
        analysis_text = "This appears to be a high-quality photograph of a golden retriever sitting patiently in a sunlit park. The background is slightly blurred (bokeh effect), suggesting a professional camera and shallow depth of field, which effectively highlights the subject. The dog's expression is curious and gentle."
        confidence = 0.98
        tags = ["Golden Retriever", "Park", "Pet Photography", "Sunny"]
    elif "cat" in image_name.lower():
        analysis_text = "The image captures a tabby cat curled up on a velvet armchair. The lighting is soft and warm, indicating an indoor setting. The color palette is rich and cozy, suggesting a focus on comfort and domestic life. The cat is relaxed and potentially sleeping."
        confidence = 0.95
        tags = ["Tabby Cat", "Indoor", "Cozy", "Animal"]
    else:
        analysis_text = "The image shows a vast, sweeping landscape, possibly a mountain range or a coast. The colors are dominated by cool blues and greens. The composition uses the rule of thirds effectively, placing the horizon line low to emphasize the dramatic sky. Further details are needed for a precise analysis."
        confidence = 0.85
        tags = ["Landscape", "Unknown", "Artistic", "Outdoors"]
        
    structured_response = {
        "analysis_summary": analysis_text,
        "model_confidence": confidence,
        "keywords": tags,
        "mock_api_call_details": mock_payload
    }

    return structured_response


# --- Main Application Layout ---
st.title("Image Intelligence Assistant")
st.markdown("Upload an image below to receive a detailed, AI-generated analysis and description.")

# Use columns for a modern, two-pane layout
col1, col2 = st.columns([1, 2], gap="large")

# --- COLUMN 1: UPLOAD/INPUT ---
with col1:
    st.subheader("1. Upload Image")
    
    uploaded_file = st.file_uploader(
        "Choose a file...",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False
    )
    
    process_button = st.button(
        "Analyze Image",
        use_container_width=True,
        type="primary",
        disabled=(uploaded_file is None) # Disable button until a file is uploaded
    )

    # Image Preview in the input column
    if uploaded_file is not None:
        st.markdown("<hr style='border: 1px solid #ccc; margin: 20px 0;'>", unsafe_allow_html=True)
        st.subheader("Image Preview")
        
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption=uploaded_file.name, use_column_width=True)


# --- COLUMN 2: OUTPUT/RESULTS ---
with col2:
    st.subheader("2. Analysis Results")
    
    # Placeholder for the results container
    results_container = st.empty()

    if process_button and uploaded_file is not None:
        
        # Use a spinner to enhance the user experience during the 'processing' time
        with st.spinner('Analyzing image with AI... This may take a moment.'):
            analysis_data = analyze_image_with_llm(uploaded_file)
        
        # Once analysis is complete, update the results container
        with results_container.container():
            st.success("✅ Analysis Complete!")

            # Display the main analysis summary prominently
            st.markdown("### 💡 AI-Generated Summary")
            st.info(analysis_data['analysis_summary'])

            # Display structured data using columns and clean markdown
            st.markdown("---")
            
            detail_col1, detail_col2 = st.columns(2)
            
            with detail_col1:
                st.metric(
                    label="Model Confidence", 
                    value=f"{analysis_data['model_confidence'] * 100:.1f}%",
                    delta="High Accuracy"
                )
            with detail_col2:
                st.markdown("**Keywords**")
                st.code(", ".join(analysis_data['keywords']), language='text')

            # Optional: Show the raw structured output for developers/debugging
            with st.expander("View Raw JSON Output (For Debugging)"):
                st.json(analysis_data)
                

    elif uploaded_file is None:
        # Initial state or after clearing upload
        with results_container.container():
            st.info("Upload an image on the left and click 'Analyze Image' to begin the process.")

# --- Footer (for clean design) ---
st.markdown("---")
st.markdown("<sub>*This is a demo application. The analysis is simulated.*</sub>", unsafe_allow_html=True)
