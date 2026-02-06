import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

# Import our final position prediction model
try:
    from final_position_model import (
        calculate_position_probability,
        get_position_insights,
        format_probability_display
    )
    POSITION_MODEL_AVAILABLE = True
except ImportError:
    st.error("❌ Final position model not found - please ensure 'final_position_model.py' is in the same folder")
    POSITION_MODEL_AVAILABLE = False

# Page config
st.set_page_config(page_title="🏎️ Team Omega Complete F1 Predictor", page_icon="🏎️", layout="wide")

# CSS styling
st.markdown("""
<style>
    /* Force light background for better text visibility */
    .stApp {
        background-color: #1e1e1e !important;
    }
    
    .main-header { background: linear-gradient(90deg, #ff1801, #ff6b35); padding: 1.5rem; border-radius: 15px; color: white; text-align: center; margin-bottom: 2rem; }
    .prediction-box { background: linear-gradient(135deg, #2E8B57 0%, #228B22 100%); padding: 2rem; border-radius: 15px; text-align: center; color: white; margin: 1rem 0; }
    
    /* Position prediction styling */
    .winner-box { background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%); padding: 2rem; border-radius: 15px; text-align: center; color: #333; margin: 1rem 0; }
    .podium-box { background: linear-gradient(135deg, #C0C0C0 0%, #FFD700 100%); padding: 2rem; border-radius: 15px; text-align: center; color: #333; margin: 1rem 0; }
    .points-box { background: linear-gradient(135deg, #228B22 0%, #32CD32 100%); padding: 2rem; border-radius: 15px; text-align: center; color: white; margin: 1rem 0; }
    .outside-box { background: linear-gradient(135deg, #696969 0%, #808080 100%); padding: 2rem; border-radius: 15px; text-align: center; color: white; margin: 1rem 0; }
    
    .metric-card { background: #f8f9fa; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #228B22; margin: 0.5rem 0; color: #333333 !important; }
    .metric-card h3 { color: #228B22 !important; margin: 0.5rem 0; }
    .metric-card h4 { color: #666666 !important; margin: 0; }
    .suggestion-box { background: #f0f8ff; padding: 0.5rem; border-radius: 5px; margin: 0.5rem 0; border-left: 3px solid #4CAF50; color: #333333 !important; }
    .circuit-match { background: #e8f5e8; padding: 0.3rem 0.8rem; margin: 0.2rem; border-radius: 15px; display: inline-block; font-size: 0.9rem; color: #333333 !important; }
    .driver-card { background: #fff3e0; padding: 1rem; border-radius: 8px; border-left: 4px solid #ff1801; margin: 0.5rem 0; color: #333333 !important; }
    .driver-card h4 { color: #ff1801 !important; margin: 0.5rem 0; font-weight: bold; }
    .driver-card p { color: #333333 !important; margin: 0.3rem 0; font-size: 0.9rem; }
    .driver-card strong { color: #ff1801 !important; }
    .constructor-tag { background: linear-gradient(45deg, #ff1801, #ff6b35); color: white; padding: 0.3rem 0.8rem; border-radius: 12px; font-size: 0.9rem; font-weight: bold; }
    .insights-box { background: #f0f8ff; padding: 1rem; border-radius: 8px; border-left: 4px solid #4CAF50; margin: 1rem 0; color: #333; }
    
    /* Comprehensive text visibility fixes */
    .stSelectbox label { color: #ffffff !important; font-weight: bold; }
    .stTextInput label { color: #ffffff !important; font-weight: bold; }
    .stSlider label { color: #ffffff !important; font-weight: bold; }
    
    /* Custom label styling for better visibility */
    p[style*="color: #ffffff"] { font-weight: bold !important; }
    
    /* Ensure all text in main content area is visible */
    .main .block-container { color: #ffffff; }
    .stMarkdown p { color: inherit !important; }
    .stMarkdown li { color: inherit !important; }
    .stWrite { color: inherit !important; }
    
    /* Subheader styling */
    .stSubheader { color: #ff6b35 !important; }
    
    /* Info/success/warning boxes */
    .stAlert { color: #333333 !important; }
    
    /* Dataframe styling */
    .stDataFrame { background-color: #f8f9fa; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_random_forest_model():
    """Load the trained Random Forest model"""
    try:
        with open('f1_random_forest_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('model_features.pkl', 'rb') as f:
            features = pickle.load(f)
        return model, features
    except FileNotFoundError as e:
        st.error(f"❌ Pit stop model file not found: {e}")
        st.info("Please ensure 'f1_random_forest_model.pkl' and 'model_features.pkl' are in the same directory")
        return None, None

def get_driver_data():
    """Complete 2024 F1 driver database with constructor auto-identification"""
    return {
        # Mercedes Drivers
        'Lewis Hamilton': {
            'driverId': 1, 'constructorId': 131, 'constructor': 'Mercedes',
            'nationality': 'British', 'championships': 7
        },
        'George Russell': {
            'driverId': 847, 'constructorId': 131, 'constructor': 'Mercedes',
            'nationality': 'British', 'championships': 0
        },
        
        # Red Bull Drivers
        'Max Verstappen': {
            'driverId': 830, 'constructorId': 9, 'constructor': 'Red Bull',
            'nationality': 'Dutch', 'championships': 3
        },
        'Sergio Pérez': {
            'driverId': 815, 'constructorId': 9, 'constructor': 'Red Bull',
            'nationality': 'Mexican', 'championships': 0
        },
        
        # Ferrari Drivers
        'Charles Leclerc': {
            'driverId': 844, 'constructorId': 6, 'constructor': 'Ferrari',
            'nationality': 'Monégasque', 'championships': 0
        },
        'Carlos Sainz': {
            'driverId': 832, 'constructorId': 6, 'constructor': 'Ferrari',
            'nationality': 'Spanish', 'championships': 0
        },
        
        # McLaren Drivers
        'Lando Norris': {
            'driverId': 846, 'constructorId': 1, 'constructor': 'McLaren',
            'nationality': 'British', 'championships': 0
        },
        'Oscar Piastri': {
            'driverId': 857, 'constructorId': 1, 'constructor': 'McLaren',
            'nationality': 'Australian', 'championships': 0
        },
        
        # Aston Martin Drivers
        'Fernando Alonso': {
            'driverId': 4, 'constructorId': 117, 'constructor': 'Aston Martin',
            'nationality': 'Spanish', 'championships': 2
        },
        'Lance Stroll': {
            'driverId': 840, 'constructorId': 117, 'constructor': 'Aston Martin',
            'nationality': 'Canadian', 'championships': 0
        },
        
        # Alpine Drivers
        'Pierre Gasly': {
            'driverId': 842, 'constructorId': 214, 'constructor': 'Alpine F1 Team',
            'nationality': 'French', 'championships': 0
        },
        'Esteban Ocon': {
            'driverId': 31, 'constructorId': 214, 'constructor': 'Alpine F1 Team',
            'nationality': 'French', 'championships': 0
        },
        
        # Williams Drivers
        'Alexander Albon': {
            'driverId': 848, 'constructorId': 3, 'constructor': 'Williams',
            'nationality': 'Thai', 'championships': 0
        },
        'Logan Sargeant': {
            'driverId': 858, 'constructorId': 3, 'constructor': 'Williams',
            'nationality': 'American', 'championships': 0
        },
        
        # RB F1 Team Drivers
        'Yuki Tsunoda': {
            'driverId': 852, 'constructorId': 215, 'constructor': 'RB F1 Team',
            'nationality': 'Japanese', 'championships': 0
        },
        'Daniel Ricciardo': {
            'driverId': 817, 'constructorId': 215, 'constructor': 'RB F1 Team',
            'nationality': 'Australian', 'championships': 0
        },
        
        # Haas Drivers
        'Kevin Magnussen': {
            'driverId': 20, 'constructorId': 210, 'constructor': 'Haas F1 Team',
            'nationality': 'Danish', 'championships': 0
        },
        'Nico Hülkenberg': {
            'driverId': 807, 'constructorId': 210, 'constructor': 'Haas F1 Team',
            'nationality': 'German', 'championships': 0
        },
        
        # Sauber Drivers
        'Valtteri Bottas': {
            'driverId': 822, 'constructorId': 15, 'constructor': 'Sauber',
            'nationality': 'Finnish', 'championships': 0
        },
        'Guanyu Zhou': {
            'driverId': 855, 'constructorId': 15, 'constructor': 'Sauber',
            'nationality': 'Chinese', 'championships': 0
        }
    }

def get_circuit_data():
    """All available circuits with smart search capabilities"""
    return {
        # European Circuits
        'Monaco': {'circuitId': 6, 'round': 6, 'laps': 78, 'track_length_km': 3.337, 'race_distance_km': 260.5, 'tyre_deg_level': 1, 'pit_lane_loss': 18, 'fastestLapSpeed': 156.0, 'description': 'Street circuit - Track position crucial', 'aliases': ['monte carlo', 'monaco gp']},
        'Silverstone': {'circuitId': 9, 'round': 10, 'laps': 52, 'track_length_km': 5.891, 'race_distance_km': 306.3, 'tyre_deg_level': 3, 'pit_lane_loss': 22, 'fastestLapSpeed': 228.0, 'description': 'British GP - High speed corners', 'aliases': ['british gp', 'britain', 'uk']},
        'Spa': {'circuitId': 13, 'round': 14, 'laps': 44, 'track_length_km': 7.004, 'race_distance_km': 308.1, 'tyre_deg_level': 3, 'pit_lane_loss': 21, 'fastestLapSpeed': 235.0, 'description': 'Belgian GP - Eau Rouge magic', 'aliases': ['spa-francorchamps', 'belgium', 'belgian gp', 'eau rouge']},
        'Monza': {'circuitId': 14, 'round': 16, 'laps': 53, 'track_length_km': 5.793, 'race_distance_km': 306.7, 'tyre_deg_level': 2, 'pit_lane_loss': 19, 'fastestLapSpeed': 220.0, 'description': 'Italian GP - Temple of Speed', 'aliases': ['italy', 'italian gp', 'temple of speed']},
        'Hungary': {'circuitId': 11, 'round': 13, 'laps': 70, 'track_length_km': 4.381, 'race_distance_km': 306.6, 'tyre_deg_level': 2, 'pit_lane_loss': 20, 'fastestLapSpeed': 185.0, 'description': 'Hungarian GP - Twisty layout', 'aliases': ['hungaroring', 'hungarian gp', 'budapest']},
        'Barcelona': {'circuitId': 4, 'round': 5, 'laps': 66, 'track_length_km': 4.675, 'race_distance_km': 308.4, 'tyre_deg_level': 3, 'pit_lane_loss': 20, 'fastestLapSpeed': 195.0, 'description': 'Spanish GP - Technical test', 'aliases': ['spain', 'spanish gp', 'catalunya']},
        'Red Bull Ring': {'circuitId': 70, 'round': 11, 'laps': 71, 'track_length_km': 4.318, 'race_distance_km': 306.5, 'tyre_deg_level': 2, 'pit_lane_loss': 18, 'fastestLapSpeed': 210.0, 'description': 'Austrian GP - Short & fast', 'aliases': ['austria', 'austrian gp', 'spielberg']},
        'Zandvoort': {'circuitId': 39, 'round': 15, 'laps': 72, 'track_length_km': 4.259, 'race_distance_km': 306.6, 'tyre_deg_level': 2, 'pit_lane_loss': 19, 'fastestLapSpeed': 200.0, 'description': 'Dutch GP - Banked corners', 'aliases': ['netherlands', 'dutch gp', 'holland']},
        'Suzuka': {'circuitId': 22, 'round': 8, 'laps': 53, 'track_length_km': 5.807, 'race_distance_km': 307.8, 'tyre_deg_level': 3, 'pit_lane_loss': 23, 'fastestLapSpeed': 210.0, 'description': 'Japanese GP - Figure-8 layout', 'aliases': ['japan', 'japanese gp']},
        
        # Americas
        'Interlagos': {'circuitId': 18, 'round': 22, 'laps': 71, 'track_length_km': 4.309, 'race_distance_km': 305.9, 'tyre_deg_level': 2, 'pit_lane_loss': 20, 'fastestLapSpeed': 195.0, 'description': 'Brazilian GP - Senna\'s home', 'aliases': ['brazil', 'brazilian gp', 'sao paulo']},
        'Montreal': {'circuitId': 7, 'round': 9, 'laps': 70, 'track_length_km': 4.361, 'race_distance_km': 305.3, 'tyre_deg_level': 2, 'pit_lane_loss': 21, 'fastestLapSpeed': 200.0, 'description': 'Canadian GP - Wall of Champions', 'aliases': ['canada', 'canadian gp', 'gilles villeneuve']},
        'COTA': {'circuitId': 69, 'round': 19, 'laps': 56, 'track_length_km': 5.513, 'race_distance_km': 308.4, 'tyre_deg_level': 3, 'pit_lane_loss': 22, 'fastestLapSpeed': 215.0, 'description': 'US GP - Circuit of Americas', 'aliases': ['austin', 'texas', 'usa', 'us gp', 'america']},
        'Las Vegas': {'circuitId': 80, 'round': 22, 'laps': 50, 'track_length_km': 6.120, 'race_distance_km': 306.0, 'tyre_deg_level': 1, 'pit_lane_loss': 17, 'fastestLapSpeed': 240.0, 'description': 'Vegas GP - High-speed streets', 'aliases': ['vegas', 'las vegas gp', 'nevada']},
        'Miami': {'circuitId': 79, 'round': 5, 'laps': 57, 'track_length_km': 5.412, 'race_distance_km': 308.3, 'tyre_deg_level': 2, 'pit_lane_loss': 18, 'fastestLapSpeed': 205.0, 'description': 'Miami GP - Purpose built', 'aliases': ['florida', 'miami gp']},
        
        # Asia-Pacific
        'Australia': {'circuitId': 1, 'round': 1, 'laps': 58, 'track_length_km': 5.278, 'race_distance_km': 306.1, 'tyre_deg_level': 3, 'pit_lane_loss': 22, 'fastestLapSpeed': 210.0, 'description': 'Australian GP - Season opener', 'aliases': ['melbourne', 'australian gp', 'albert park']},
        'Shanghai': {'circuitId': 17, 'round': 4, 'laps': 56, 'track_length_km': 5.451, 'race_distance_km': 305.1, 'tyre_deg_level': 2, 'pit_lane_loss': 22, 'fastestLapSpeed': 205.0, 'description': 'Chinese GP - Long straight', 'aliases': ['china', 'chinese gp']},
        
        # Middle East
        'Bahrain': {'circuitId': 3, 'round': 1, 'laps': 57, 'track_length_km': 5.412, 'race_distance_km': 308.3, 'tyre_deg_level': 3, 'pit_lane_loss': 21, 'fastestLapSpeed': 215.0, 'description': 'Bahrain GP - Desert heat', 'aliases': ['bahrain gp', 'sakhir']},
        'Abu Dhabi': {'circuitId': 24, 'round': 24, 'laps': 58, 'track_length_km': 5.281, 'race_distance_km': 306.1, 'tyre_deg_level': 2, 'pit_lane_loss': 20, 'fastestLapSpeed': 200.0, 'description': 'Abu Dhabi GP - Season finale', 'aliases': ['uae', 'emirates', 'yas marina']},
        'Jeddah': {'circuitId': 77, 'round': 2, 'laps': 50, 'track_length_km': 6.174, 'race_distance_km': 308.7, 'tyre_deg_level': 1, 'pit_lane_loss': 18, 'fastestLapSpeed': 250.0, 'description': 'Saudi GP - Fastest street circuit', 'aliases': ['saudi arabia', 'saudi gp', 'corniche']},
        'Singapore': {'circuitId': 15, 'round': 18, 'laps': 61, 'track_length_km': 5.063, 'race_distance_km': 308.8, 'tyre_deg_level': 1, 'pit_lane_loss': 23, 'fastestLapSpeed': 175.0, 'description': 'Singapore GP - Night street race', 'aliases': ['singapore gp', 'marina bay']},
        'Baku': {'circuitId': 73, 'round': 4, 'laps': 51, 'track_length_km': 6.003, 'race_distance_km': 306.0, 'tyre_deg_level': 2, 'pit_lane_loss': 19, 'fastestLapSpeed': 230.0, 'description': 'Azerbaijan GP - City of winds', 'aliases': ['azerbaijan', 'azerbaijan gp']}
    }

def smart_circuit_search(user_input, circuit_data):
    """Smart matching for circuit names"""
    if not user_input:
        return []
    
    user_input = user_input.lower().strip()
    matches = []
    
    for circuit_name, info in circuit_data.items():
        # Direct name match
        if user_input in circuit_name.lower():
            matches.append((circuit_name, 'exact'))
            continue
        
        # Alias match
        for alias in info.get('aliases', []):
            if user_input in alias.lower():
                matches.append((circuit_name, 'alias'))
                break
    
    # Sort by match type (exact first, then aliases)
    matches.sort(key=lambda x: (x[1] != 'exact', x[0]))
    return [match[0] for match in matches]

def predict_driver_strategy(model, features, circuit_name, driver_name, grid_pos):
    """Make pit stop prediction using circuit and driver data"""
    
    circuit_data = get_circuit_data()
    driver_data = get_driver_data()
    
    circuit_info = circuit_data.get(circuit_name, circuit_data['Silverstone'])
    driver_info = driver_data.get(driver_name, driver_data['Lewis Hamilton'])
    
    # Create prediction input
    input_data = pd.DataFrame([{
        'grid': grid_pos, 'year': 2025, 'round': circuit_info['round'], 'circuitId': circuit_info['circuitId'],
        'driverId': driver_info['driverId'], 'constructorId': driver_info['constructorId'],
        'tyre_deg_level': circuit_info['tyre_deg_level'], 'pit_lane_loss': circuit_info['pit_lane_loss'],
        'track_length_km': circuit_info['track_length_km'], 'race_distance_km': circuit_info['race_distance_km'],
        'laps': circuit_info['laps'], 'fastestLapSpeed': circuit_info['fastestLapSpeed']
    }])
    
    try:
        prediction = model.predict(input_data)[0]
        return prediction, circuit_info, driver_info, 2025
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return 15.0, circuit_info, driver_info, 2025

def get_position_styling_class(position):
    """Get appropriate CSS class for position display"""
    if position == 1:
        return "winner-box"  # Gold
    elif position in [2, 3]:
        return "podium-box"  # Silver/Bronze
    elif position in [4, 5, 6, 7, 8, 9, 10]:
        return "points-box"  # Green
    else:
        return "outside-box"  # Gray

def main():
    # Header
    st.markdown('''
    <div class="main-header">
        <h1>🏎️ Team Omega Complete F1 Strategy Predictor</h1>
        <h3>Pit Stop Timing + Final Position Prediction</h3>
        <p>Advanced F1 race strategy using machine learning and driver performance analytics</p>
    </div>
    ''', unsafe_allow_html=True)
    
    model, features = load_random_forest_model()
    if model is None:
        st.stop()
    
    status_message = "✅ Complete F1 strategy predictor ready!"
    if not POSITION_MODEL_AVAILABLE:
        status_message += " ⚠️ (Final position model not available - showing pit strategy only)"
    st.success(status_message)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🏎️ Race Strategy Setup")
        
        # Get data
        driver_data = get_driver_data()
        circuit_data = get_circuit_data()
        
        # Driver selection (primary input)
        driver_names = sorted(list(driver_data.keys()))
        st.markdown('<p style="color: #ffffff; font-weight: bold;">🏁 Select F1 Driver:</p>', unsafe_allow_html=True)
        selected_driver = st.selectbox("", driver_names, index=driver_names.index('Lewis Hamilton'), label_visibility="collapsed")
        
        # Auto-identify constructor and show driver info (without style)
        driver_info = driver_data[selected_driver]
        constructor_name = driver_info['constructor']
        
        # Display driver card with auto-identified constructor (no style info)
        st.markdown(f'''
        <div class="driver-card">
            <h4>🏎️ {selected_driver}</h4>
            <span class="constructor-tag">{constructor_name}</span>
            <p><strong>Nationality:</strong> {driver_info['nationality']} | <strong>Championships:</strong> {driver_info['championships']}</p>
        </div>
        ''', unsafe_allow_html=True)
        
        # SMART CIRCUIT SEARCH
        st.markdown('<p style="color: #ffffff; font-weight: bold; margin-bottom: 0.5rem;">🏟️ Circuit Search:</p>', unsafe_allow_html=True)
        circuit_input = st.text_input("", value="Silverstone", placeholder="Type: monaco, spa, vegas, singapore...", help="Start typing any circuit name or country", label_visibility="collapsed")
        
        # Smart search results
        if circuit_input:
            matches = smart_circuit_search(circuit_input, circuit_data)
            
            if matches:
                st.markdown('<div class="suggestion-box">📍 <strong>Circuit Matches:</strong></div>', unsafe_allow_html=True)
                suggestion_html = ""
                for match in matches[:6]:
                    suggestion_html += f'<span class="circuit-match">{match}</span> '
                st.markdown(suggestion_html, unsafe_allow_html=True)
                selected_circuit = matches[0]
                
                if selected_circuit in circuit_data:
                    st.info(f"✅ **{selected_circuit}**: {circuit_data[selected_circuit]['description']}")
            else:
                st.warning(f"🔍 No matches for '{circuit_input}' - try: monaco, spa, vegas")
                selected_circuit = "Silverstone"
        else:
            selected_circuit = "Silverstone"
        
        st.markdown('<p style="color: #ffffff; font-weight: bold; margin-bottom: 0.5rem;">🏁 Expected Grid Position:</p>', unsafe_allow_html=True)
        grid_position = st.slider("", 1, 20, 5, label_visibility="collapsed")
        
        predict_button = st.button("🎯 Generate Complete Race Strategy", type="primary")
        
        # Quick examples
        with st.expander("💡 Try These Searches"):
            st.markdown('<p style="color: #333333;"><strong>Drivers:</strong> Hamilton, Verstappen, Leclerc, Norris</p>', unsafe_allow_html=True)
            st.markdown('<p style="color: #333333;"><strong>Circuits:</strong> monaco, spa, vegas, silverstone, monza</p>', unsafe_allow_html=True)
    
    with col2:
        st.subheader("🏁 Complete Race Strategy Analysis")
        
        if predict_button and selected_circuit in circuit_data:
            with st.spinner(f"🏎️ Analyzing complete race strategy for {selected_driver} at {selected_circuit}..."):
                # STEP 1: Get pit stop strategy
                predicted_lap, circuit_info, driver_info, race_year = predict_driver_strategy(
                    model, features, selected_circuit, selected_driver, grid_position
                )
                
                # Main pit stop prediction display
                st.markdown(f'''
                <div class="prediction-box">
                    <h2>⚡ Optimal Pit Strategy</h2>
                    <h1 style="font-size: 4rem; margin: 0.5rem 0;">Lap {predicted_lap:.0f}</h1>
                    <p style="font-size: 1.3rem;">Recommended pit stop timing</p>
                </div>
                ''', unsafe_allow_html=True)
                
                # STEP 2: Final Position Prediction (if available)
                if POSITION_MODEL_AVAILABLE:
                    try:
                        final_position, position_description, confidence, position_probabilities, features_analysis = calculate_position_probability(
                            selected_driver, selected_circuit, grid_position, predicted_lap
                        )
                        
                        # Position prediction display
                        position_class = get_position_styling_class(final_position)
                        st.markdown(f'''
                        <div class="{position_class}">
                            <h2>🏁 Final Position Prediction</h2>
                            <h1 style="font-size: 4rem; margin: 0.5rem 0;">P{final_position}</h1>
                            <p style="font-size: 1.3rem;">{position_description}</p>
                            <p style="font-size: 1rem;">Confidence: {confidence*100:.0f}%</p>
                        </div>
                        ''', unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.error(f"Final position prediction failed: {e}")
                        final_position = None
                
                # Strategy metrics
                col_a, col_b, col_c, col_d = st.columns(4)
                
                with col_a:
                    st.markdown(f'''
                    <div class="metric-card">
                        <h4>🎯 Pit Window</h4>
                        <h3>Lap {predicted_lap-2:.0f}-{predicted_lap+2:.0f}</h3>
                    </div>
                    ''', unsafe_allow_html=True)
                
                with col_b:
                    st.markdown(f'''
                    <div class="metric-card">
                        <h4>🏁 Race Length</h4>
                        <h3>{circuit_info["laps"]} laps</h3>
                    </div>
                    ''', unsafe_allow_html=True)
                
                with col_c:
                    st.markdown(f'''
                    <div class="metric-card">
                        <h4>🏎️ Constructor</h4>
                        <h3>{constructor_name}</h3>
                    </div>
                    ''', unsafe_allow_html=True)
                
                with col_d:
                    if 'final_position' in locals() and final_position:
                        position_change = final_position - grid_position
                        change_symbol = "📈" if position_change < 0 else "📉" if position_change > 0 else "➡️"
                        st.markdown(f'''
                        <div class="metric-card">
                            <h4>📊 Position Change</h4>
                            <h3>{change_symbol} {abs(position_change)}</h3>
                        </div>
                        ''', unsafe_allow_html=True)
                    else:
                        st.markdown(f'''
                        <div class="metric-card">
                            <h4>🏟️ Circuit ID</h4>
                            <h3>{circuit_info["circuitId"]}</h3>
                        </div>
                        ''', unsafe_allow_html=True)
                
                # Strategic Analysis
                st.subheader("📊 Strategic Analysis")
                
                if POSITION_MODEL_AVAILABLE and 'final_position' in locals() and final_position:
                    # Show position prediction insights
                    insights = get_position_insights(features_analysis, selected_driver, selected_circuit, final_position, grid_position)
                    
                    st.markdown(f'''
                    <div class="insights-box">
                        <h4>🎯 Race Strategy Insights:</h4>
                        {"<br/>".join([f"<p>{insight}</p>" for insight in insights])}
                    </div>
                    ''', unsafe_allow_html=True)
                    
                    # Show position probabilities
                    prob_display = format_probability_display(position_probabilities)
                    st.info(f"📊 **Position Probabilities:** {prob_display}")
                
                else:
                    # Show basic pit strategy insights
                    st.success(f"**{selected_circuit}:** {circuit_info['description']}")
                    st.info(f"**Pit Strategy:** Optimal timing balances tire advantage with track position")
                
                # Detailed analysis table
                analysis_data = [
                    {'Factor': 'Driver', 'Value': f"{selected_driver} (ID: {driver_info['driverId']})"},
                    {'Factor': 'Constructor', 'Value': f"{constructor_name} (ID: {driver_info['constructorId']})"},
                    {'Factor': 'Circuit', 'Value': f"{selected_circuit} (ID: {circuit_info['circuitId']})"},
                    {'Factor': 'Optimal Pit Lap', 'Value': f"Lap {predicted_lap:.0f}"},
                    {'Factor': 'Track Length', 'Value': f"{circuit_info['track_length_km']:.3f} km"},
                    {'Factor': 'Tire Degradation', 'Value': f"Level {circuit_info['tyre_deg_level']}/3"}
                ]
                
                if 'final_position' in locals() and final_position:
                    analysis_data.append({'Factor': 'Predicted Finish', 'Value': f"P{final_position}"})
                
                analysis_df = pd.DataFrame(analysis_data)
                st.dataframe(analysis_df, hide_index=True, use_container_width=True)
                
        else:
            st.info("👈 **Select driver, search for a circuit, and set grid position** for complete race strategy!")
            
            st.subheader("🧠 Complete Strategy Analysis")
            st.markdown('''
            <div class="insights-box">
                <h4>🎯 What This Tool Provides:</h4>
                <p><strong>1. Pit Stop Timing:</strong> Optimal lap for pit stop using Random Forest model (2.78 MAE)</p>
                <p><strong>2. Final Position:</strong> Predicted race finish using pit strategy + performance factors</p>
                <p><strong>3. Strategic Insights:</strong> Complete analysis of grid position, car performance, driver skill</p>
                <p><strong>4. Race Intelligence:</strong> Circuit-specific recommendations for optimal strategy</p>
                <p><strong>5. Professional Tool:</strong> Real F1 team decision-making support system</p>
            </div>
            ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()