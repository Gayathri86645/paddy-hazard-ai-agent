import random

def get_synthetic_sensor_state(irrigation_active: bool = False) -> dict:
    """
    Generates synthetic multi-layer farm telemetry to test the Meta Model API 
    predictive agent without exposing proprietary hardware or math parameters.
    """
    if irrigation_active:
        return {
            "sensor_protection_mode": "CLOSED_FOR_MUD_PROTECTION",
            "live_vibration_reading": None,  # Blind spot active
            "seismic_tremor_detected": False,
            "weather_storm_noise": "HIGH",
            "action_required": "RUN_META_AI_BLIND_SPOT_PREDICTION"
        }
    
    return {
        "sensor_protection_mode": "ACTIVE_SENSING",
        "bio_rhythm_confidence": round(random.uniform(0.70, 0.95), 2),
        "tractor_or_footstep_noise": "FILTERED_OUT",
        "seismic_tremor_detected": False,
        "weather_storm_noise": "LOW",
        "action_required": "MONITOR_NORMAL"
    }

if _name_ == "_main_":
    print("Normal Mode:", get_synthetic_sensor_state(irrigation_active=False))
    print("Blind-Spot Mode:", get_synthetic_sensor_state(irrigation_active=True))
