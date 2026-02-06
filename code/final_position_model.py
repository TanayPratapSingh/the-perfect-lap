"""
F1 Final Position Prediction Model
Separate logic file to be imported into main Streamlit app
"""

import numpy as np
import pandas as pd

def get_driver_performance_data():
    """Driver database with performance metrics for position prediction"""
    return {
        # Championship Winners (High Performance)
        'Lewis Hamilton': {'driverId': 1, 'constructorId': 131, 'constructor': 'Mercedes', 'championships': 7, 'experience_level': 5, 'avg_finish': 3.2, 'win_rate': 0.31},
        'Max Verstappen': {'driverId': 830, 'constructorId': 9, 'constructor': 'Red Bull', 'championships': 3, 'experience_level': 4, 'avg_finish': 2.8, 'win_rate': 0.58},
        'Fernando Alonso': {'driverId': 4, 'constructorId': 117, 'constructor': 'Aston Martin', 'championships': 2, 'experience_level': 5, 'avg_finish': 6.1, 'win_rate': 0.09},
        
        # Top Drivers (No Championships)
        'Charles Leclerc': {'driverId': 844, 'constructorId': 6, 'constructor': 'Ferrari', 'championships': 0, 'experience_level': 3, 'avg_finish': 5.4, 'win_rate': 0.05},
        'Lando Norris': {'driverId': 846, 'constructorId': 1, 'constructor': 'McLaren', 'championships': 0, 'experience_level': 3, 'avg_finish': 6.8, 'win_rate': 0.02},
        'George Russell': {'driverId': 847, 'constructorId': 131, 'constructor': 'Mercedes', 'championships': 0, 'experience_level': 3, 'avg_finish': 5.9, 'win_rate': 0.01},
        'Carlos Sainz': {'driverId': 832, 'constructorId': 6, 'constructor': 'Ferrari', 'championships': 0, 'experience_level': 4, 'avg_finish': 6.2, 'win_rate': 0.01},
        'Oscar Piastri': {'driverId': 857, 'constructorId': 1, 'constructor': 'McLaren', 'championships': 0, 'experience_level': 2, 'avg_finish': 7.8, 'win_rate': 0.01},
        'Sergio Pérez': {'driverId': 815, 'constructorId': 9, 'constructor': 'Red Bull', 'championships': 0, 'experience_level': 4, 'avg_finish': 4.6, 'win_rate': 0.03},
        
        # Midfield Drivers
        'Pierre Gasly': {'driverId': 842, 'constructorId': 214, 'constructor': 'Alpine F1 Team', 'championships': 0, 'experience_level': 3, 'avg_finish': 9.2, 'win_rate': 0.001},
        'Esteban Ocon': {'driverId': 31, 'constructorId': 214, 'constructor': 'Alpine F1 Team', 'championships': 0, 'experience_level': 3, 'avg_finish': 8.9, 'win_rate': 0.001},
        'Alexander Albon': {'driverId': 848, 'constructorId': 3, 'constructor': 'Williams', 'championships': 0, 'experience_level': 3, 'avg_finish': 12.1, 'win_rate': 0.0},
        'Lance Stroll': {'driverId': 840, 'constructorId': 117, 'constructor': 'Aston Martin', 'championships': 0, 'experience_level': 3, 'avg_finish': 10.4, 'win_rate': 0.0},
        'Yuki Tsunoda': {'driverId': 852, 'constructorId': 215, 'constructor': 'RB F1 Team', 'championships': 0, 'experience_level': 2, 'avg_finish': 11.8, 'win_rate': 0.0},
        'Daniel Ricciardo': {'driverId': 817, 'constructorId': 215, 'constructor': 'RB F1 Team', 'championships': 0, 'experience_level': 4, 'avg_finish': 10.6, 'win_rate': 0.01},
        'Kevin Magnussen': {'driverId': 20, 'constructorId': 210, 'constructor': 'Haas F1 Team', 'championships': 0, 'experience_level': 3, 'avg_finish': 13.2, 'win_rate': 0.0},
        'Nico Hülkenberg': {'driverId': 807, 'constructorId': 210, 'constructor': 'Haas F1 Team', 'championships': 0, 'experience_level': 4, 'avg_finish': 12.8, 'win_rate': 0.0},
        'Valtteri Bottas': {'driverId': 822, 'constructorId': 15, 'constructor': 'Sauber', 'championships': 0, 'experience_level': 4, 'avg_finish': 14.1, 'win_rate': 0.01},
        'Guanyu Zhou': {'driverId': 855, 'constructorId': 15, 'constructor': 'Sauber', 'championships': 0, 'experience_level': 2, 'avg_finish': 15.3, 'win_rate': 0.0},
        'Logan Sargeant': {'driverId': 858, 'constructorId': 3, 'constructor': 'Williams', 'championships': 0, 'experience_level': 1, 'avg_finish': 16.2, 'win_rate': 0.0}
    }

def get_circuit_position_factors():
    """Circuit characteristics that affect final positions"""
    return {
        'Monaco': {'circuitId': 6, 'overtaking_difficulty': 0.9, 'strategy_impact': 0.8, 'grid_advantage': 0.95, 'position_variance': 0.2},
        'Silverstone': {'circuitId': 9, 'overtaking_difficulty': 0.4, 'strategy_impact': 0.6, 'grid_advantage': 0.7, 'position_variance': 0.6},
        'Spa': {'circuitId': 13, 'overtaking_difficulty': 0.2, 'strategy_impact': 0.7, 'grid_advantage': 0.6, 'position_variance': 0.7},
        'Monza': {'circuitId': 14, 'overtaking_difficulty': 0.3, 'strategy_impact': 0.6, 'grid_advantage': 0.6, 'position_variance': 0.7},
        'Suzuka': {'circuitId': 22, 'overtaking_difficulty': 0.6, 'strategy_impact': 0.7, 'grid_advantage': 0.8, 'position_variance': 0.4},
        'Hungary': {'circuitId': 11, 'overtaking_difficulty': 0.8, 'strategy_impact': 0.9, 'grid_advantage': 0.85, 'position_variance': 0.3},
        'Singapore': {'circuitId': 15, 'overtaking_difficulty': 0.7, 'strategy_impact': 0.8, 'grid_advantage': 0.8, 'position_variance': 0.4},
        'Australia': {'circuitId': 1, 'overtaking_difficulty': 0.5, 'strategy_impact': 0.5, 'grid_advantage': 0.7, 'position_variance': 0.5},
        'Bahrain': {'circuitId': 3, 'overtaking_difficulty': 0.4, 'strategy_impact': 0.6, 'grid_advantage': 0.7, 'position_variance': 0.6},
        'Interlagos': {'circuitId': 18, 'overtaking_difficulty': 0.4, 'strategy_impact': 0.7, 'grid_advantage': 0.6, 'position_variance': 0.6},
        'Barcelona': {'circuitId': 4, 'overtaking_difficulty': 0.6, 'strategy_impact': 0.7, 'grid_advantage': 0.8, 'position_variance': 0.4},
        'Red Bull Ring': {'circuitId': 70, 'overtaking_difficulty': 0.3, 'strategy_impact': 0.6, 'grid_advantage': 0.6, 'position_variance': 0.7},
        'Zandvoort': {'circuitId': 39, 'overtaking_difficulty': 0.7, 'strategy_impact': 0.6, 'grid_advantage': 0.8, 'position_variance': 0.3},
        'COTA': {'circuitId': 69, 'overtaking_difficulty': 0.5, 'strategy_impact': 0.7, 'grid_advantage': 0.7, 'position_variance': 0.5},
        'Las Vegas': {'circuitId': 80, 'overtaking_difficulty': 0.4, 'strategy_impact': 0.5, 'grid_advantage': 0.6, 'position_variance': 0.6},
        'Miami': {'circuitId': 79, 'overtaking_difficulty': 0.6, 'strategy_impact': 0.6, 'grid_advantage': 0.7, 'position_variance': 0.5},
        'Shanghai': {'circuitId': 17, 'overtaking_difficulty': 0.5, 'strategy_impact': 0.6, 'grid_advantage': 0.7, 'position_variance': 0.5},
        'Abu Dhabi': {'circuitId': 24, 'overtaking_difficulty': 0.6, 'strategy_impact': 0.6, 'grid_advantage': 0.75, 'position_variance': 0.4},
        'Jeddah': {'circuitId': 77, 'overtaking_difficulty': 0.5, 'strategy_impact': 0.7, 'grid_advantage': 0.7, 'position_variance': 0.5},
        'Baku': {'circuitId': 73, 'overtaking_difficulty': 0.4, 'strategy_impact': 0.6, 'grid_advantage': 0.6, 'position_variance': 0.7}
    }

def get_constructor_strength_2024():
    """Constructor performance ratings for position prediction"""
    return {
        9: {'constructor': 'Red Bull', 'strength': 0.95, 'consistency': 0.9, 'avg_points_per_race': 18.2},      # Dominant
        1: {'constructor': 'McLaren', 'strength': 0.88, 'consistency': 0.85, 'avg_points_per_race': 14.8},     # Championship contender
        6: {'constructor': 'Ferrari', 'strength': 0.85, 'consistency': 0.8, 'avg_points_per_race': 13.2},      # Championship contender  
        131: {'constructor': 'Mercedes', 'strength': 0.82, 'consistency': 0.88, 'avg_points_per_race': 11.6},  # Championship contender
        117: {'constructor': 'Aston Martin', 'strength': 0.65, 'consistency': 0.7, 'avg_points_per_race': 4.8}, # Midfield
        214: {'constructor': 'Alpine F1 Team', 'strength': 0.55, 'consistency': 0.6, 'avg_points_per_race': 3.2}, # Midfield
        3: {'constructor': 'Williams', 'strength': 0.45, 'consistency': 0.5, 'avg_points_per_race': 1.8},     # Points contender
        215: {'constructor': 'RB F1 Team', 'strength': 0.5, 'consistency': 0.55, 'avg_points_per_race': 2.4}, # Sister team
        210: {'constructor': 'Haas F1 Team', 'strength': 0.4, 'consistency': 0.45, 'avg_points_per_race': 1.2}, # Points contender
        15: {'constructor': 'Sauber', 'strength': 0.35, 'consistency': 0.4, 'avg_points_per_race': 0.6}       # Development team
    }

def calculate_position_probability(driver_name, circuit_name, grid_pos, optimal_pit_lap):
    """
    Calculate probability of finishing in different position ranges
    Returns: (predicted_position, position_description, confidence, position_probabilities)
    """
    
    # Get data
    driver_data = get_driver_performance_data()
    circuit_data = get_circuit_position_factors()
    constructor_data = get_constructor_strength_2024()
    
    # Handle missing data
    driver_info = driver_data.get(driver_name, driver_data['Lewis Hamilton'])
    circuit_info = circuit_data.get(circuit_name, circuit_data['Silverstone'])
    constructor_info = constructor_data.get(driver_info['constructorId'], constructor_data[131])
    
    # Feature engineering for position prediction
    features = {
        'grid_advantage': max(0, 11 - grid_pos) / 10,  # Grid position advantage (P1=1.0, P10=0.1, P20=0)
        'constructor_strength': constructor_info['strength'],
        'driver_skill': (driver_info['experience_level'] / 5) * 0.7 + (1 - driver_info['avg_finish'] / 20) * 0.3,
        'pit_strategy_quality': 1.0 if 12 <= optimal_pit_lap <= 22 else 0.7,  # Optimal pit window
        'circuit_grid_importance': circuit_info['grid_advantage'],
        'strategy_impact': circuit_info['strategy_impact'],
        'position_variance': circuit_info['position_variance']  # How much positions can change
    }
    
    # Base performance score (0-1)
    base_score = (
        features['grid_advantage'] * 0.35 +          # Grid position is most important
        features['constructor_strength'] * 0.25 +    # Car performance
        features['driver_skill'] * 0.15 +            # Driver ability
        features['pit_strategy_quality'] * 0.1 +     # Strategy advantage
        features['circuit_grid_importance'] * 0.1 +  # Circuit-specific grid advantage
        features['strategy_impact'] * 0.05           # Strategy importance
    )
    
    # Add realistic variance based on circuit characteristics
    variance = features['position_variance'] * 0.15
    performance_score = max(0, min(1, base_score + np.random.normal(0, variance)))
    
    # Calculate position probabilities
    position_probabilities = calculate_position_probabilities(performance_score, grid_pos, circuit_info)
    
    # Determine most likely position range
    predicted_position, position_description, confidence = determine_position_prediction(position_probabilities)
    
    return predicted_position, position_description, confidence, position_probabilities, features

def calculate_position_probabilities(performance_score, grid_pos, circuit_info):
    """Calculate probability distribution across position ranges"""
    
    # Base probabilities influenced by performance score
    if performance_score >= 0.85:
        probs = {'P1': 0.4, 'P2-P3': 0.35, 'P4-P5': 0.15, 'P6-P10': 0.08, 'P11+': 0.02}
    elif performance_score >= 0.75:
        probs = {'P1': 0.15, 'P2-P3': 0.4, 'P4-P5': 0.25, 'P6-P10': 0.15, 'P11+': 0.05}
    elif performance_score >= 0.65:
        probs = {'P1': 0.05, 'P2-P3': 0.2, 'P4-P5': 0.35, 'P6-P10': 0.3, 'P11+': 0.1}
    elif performance_score >= 0.5:
        probs = {'P1': 0.01, 'P2-P3': 0.08, 'P4-P5': 0.25, 'P6-P10': 0.46, 'P11+': 0.2}
    elif performance_score >= 0.35:
        probs = {'P1': 0.0, 'P2-P3': 0.02, 'P4-P5': 0.1, 'P6-P10': 0.48, 'P11+': 0.4}
    else:
        probs = {'P1': 0.0, 'P2-P3': 0.0, 'P4-P5': 0.05, 'P6-P10': 0.25, 'P11+': 0.7}
    
    # Adjust for grid position reality (back of grid rarely wins)
    if grid_pos >= 15:
        probs['P1'] *= 0.1
        probs['P2-P3'] *= 0.3
        probs['P11+'] = min(1.0, probs['P11+'] * 1.5)
    elif grid_pos >= 10:
        probs['P1'] *= 0.5
        probs['P2-P3'] *= 0.7
    
    # Circuit-specific adjustments
    grid_importance = circuit_info['grid_advantage']
    if grid_importance > 0.8:  # Monaco-type circuits
        # Grid position matters more
        if grid_pos <= 3:
            probs['P1'] *= 1.5
            probs['P2-P3'] *= 1.3
        else:
            probs['P1'] *= 0.5
            probs['P2-P3'] *= 0.7
    
    # Normalize probabilities
    total = sum(probs.values())
    probs = {k: v/total for k, v in probs.items()}
    
    return probs

def determine_position_prediction(position_probabilities):
    """Determine most likely position range and confidence"""
    
    # Find highest probability outcome
    max_prob_range = max(position_probabilities.items(), key=lambda x: x[1])
    predicted_range = max_prob_range[0]
    confidence = max_prob_range[1]
    
    # Generate specific position and description
    if predicted_range == 'P1':
        return 1, "P1 - Race Winner! 🏆", confidence
    elif predicted_range == 'P2-P3':
        pos = np.random.choice([2, 3], p=[0.6, 0.4])  # Slight bias toward P2
        return pos, f"P{pos} - Podium Finish! 🥈🥉", confidence
    elif predicted_range == 'P4-P5':
        pos = np.random.choice([4, 5])
        return pos, f"P{pos} - Strong Points Finish ⭐", confidence
    elif predicted_range == 'P6-P10':
        pos = np.random.choice([6, 7, 8, 9, 10])
        return pos, f"P{pos} - Points Finish 📊", confidence
    else:  # P11+
        pos = np.random.randint(11, 21)
        return pos, f"P{pos} - Outside Points 🔹", confidence

def get_position_insights(features, driver_name, circuit_name, predicted_position, grid_pos):
    """Generate strategic insights about the position prediction"""
    
    driver_data = get_driver_performance_data()
    circuit_data = get_circuit_position_factors()
    constructor_data = get_constructor_strength_2024()
    
    driver_info = driver_data[driver_name]
    circuit_info = circuit_data[circuit_name]
    constructor_info = constructor_data[driver_info['constructorId']]
    
    insights = []
    
    # Grid position analysis
    if grid_pos <= 5:
        insights.append(f"🏁 Strong grid position (P{grid_pos}) provides solid foundation")
    elif grid_pos <= 10:
        insights.append(f"🏁 Midfield start (P{grid_pos}) requires strategic excellence")
    else:
        insights.append(f"🏁 Back of grid start (P{grid_pos}) - uphill battle")
    
    # Constructor strength analysis
    if constructor_info['strength'] >= 0.9:
        insights.append(f"🏎️ Dominant car ({constructor_info['constructor']}) enables front-running pace")
    elif constructor_info['strength'] >= 0.8:
        insights.append(f"🏎️ Competitive car ({constructor_info['constructor']}) capable of podium fights")
    elif constructor_info['strength'] >= 0.6:
        insights.append(f"🏎️ Midfield car ({constructor_info['constructor']}) fighting for points")
    else:
        insights.append(f"🏎️ Struggling car ({constructor_info['constructor']}) - points require perfect execution")
    
    # Driver skill analysis
    if driver_info['championships'] > 0:
        insights.append(f"👑 Championship winner's experience provides strategic advantage")
    elif driver_info['experience_level'] >= 4:
        insights.append(f"🎯 Veteran driver maximizes car potential")
    else:
        insights.append(f"🌟 Developing talent with room for strategic growth")
    
    # Circuit-specific analysis
    if circuit_info['grid_advantage'] > 0.8:
        insights.append(f"🏟️ {circuit_name}: Track position crucial - overtaking extremely difficult")
    elif circuit_info['overtaking_difficulty'] < 0.4:
        insights.append(f"🏟️ {circuit_name}: Overtaking friendly - position recovery possible")
    else:
        insights.append(f"🏟️ {circuit_name}: Balanced circuit - strategy and pace both important")
    
    # Position change analysis
    position_change = predicted_position - grid_pos
    if position_change < -3:
        insights.append(f"📈 Significant position gain predicted (+{abs(position_change)} places)")
    elif position_change < 0:
        insights.append(f"📈 Modest position improvement expected (+{abs(position_change)} places)")
    elif position_change == 0:
        insights.append(f"➡️ Maintaining grid position - consistent performance")
    else:
        insights.append(f"📉 Some positions likely lost (-{position_change} places)")
    
    return insights

def format_probability_display(position_probabilities):
    """Format position probabilities for display"""
    display_probs = []
    for pos_range, prob in position_probabilities.items():
        if prob >= 0.05:  # Only show probabilities >= 5%
            display_probs.append(f"{pos_range}: {prob*100:.0f}%")
    return " | ".join(display_probs)