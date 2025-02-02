import numpy as np

def generate_recommendations(predicted_dropout, predicted_completion, predicted_tsr):
    """
    Generates recommendations based on predicted values.
    """

    recommendations = []

    # Dropout Rate Recommendations
    if predicted_dropout > 20:
        recommendations.append("Increase student retention programs (mentorship, financial aid, extracurricular activities).")
        recommendations.append("Improve school infrastructure (libraries, clean water, digital classrooms).")

    # Completion Rate Recommendations
    if predicted_completion < 80:
        recommendations.append("Enhance curriculum relevance with real-world applications.")
        recommendations.append("Provide better access to study materials and e-learning resources.")

    # TSR Recommendations
    if predicted_tsr < 30:
        recommendations.append("Hire additional teachers to improve student-to-teacher ratio.")
        recommendations.append("Implement teacher training workshops for better engagement.")

    return recommendations


def recommend_resource_allocation(division_data):
    """
    Generates resource allocation recommendations based on division statistics.
    """
    
    avg_dropout = division_data["Dropout_Rate"].mean()
    avg_completion = division_data["Completion_Rate"].mean()
    avg_tsr = division_data["TSR"].mean()
    avg_infra_score = division_data["Infrastructure_Score"].mean()

    recommendations = []
    
    if avg_dropout > 20:
        recommendations.append("Increase funding for student support programs in high-dropout areas.")
        recommendations.append("Provide scholarships or financial incentives for students in need.")

    if avg_completion < 80:
        recommendations.append("Improve curriculum with practical learning techniques.")
        recommendations.append("Introduce technology-driven education like smart classrooms.")

    if avg_tsr < 30:
        recommendations.append("Hire additional teachers and conduct teacher training programs.")

    if avg_infra_score < 10:
        recommendations.append("Upgrade school infrastructure (Internet, labs, libraries, sanitation).")

    return recommendations
