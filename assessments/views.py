from django.shortcuts import render


ASSESSMENTS = {
    'mood': {
        'title': 'Mood Self-Check',
        'summary': 'A short self-check to help you notice how your mood has been feeling lately.',
        'accent': '#2D6A4F',
        'questions': [
            {'name': 'q1', 'text': 'I have felt low, flat, or discouraged.'},
            {'name': 'q2', 'text': 'I have found it hard to enjoy normal daily activities.'},
            {'name': 'q3', 'text': 'I have felt withdrawn or less connected to others.'},
            {'name': 'q4', 'text': 'I have struggled to get going with everyday tasks.'},
        ],
    },
    'stress': {
        'title': 'Stress Self-Check',
        'summary': 'A quick check to help you spot when pressure may be building up too much.',
        'accent': '#2D6A4F',
        'questions': [
            {'name': 'q1', 'text': 'I have felt tense or on edge during the day.'},
            {'name': 'q2', 'text': 'My mind has felt overloaded by responsibilities or worries.'},
            {'name': 'q3', 'text': 'I have found it difficult to switch off or relax.'},
            {'name': 'q4', 'text': 'Stress has affected my focus, patience, or sleep.'},
        ],
    },
    'sleep': {
        'title': 'Sleep Habits Check',
        'summary': 'A practical review of whether your current routine is supporting restful sleep.',
        'accent': '#D4A017',
        'questions': [
            {'name': 'q1', 'text': 'I have struggled to fall asleep at a reasonable time.'},
            {'name': 'q2', 'text': 'I have woken feeling unrefreshed or still tired.'},
            {'name': 'q3', 'text': 'My evening routine has felt irregular or overstimulating.'},
            {'name': 'q4', 'text': 'Poor sleep has affected my mood or concentration.'},
        ],
    },
}


RESPONSE_OPTIONS = [
    (0, 'Not at all'),
    (1, 'Sometimes'),
    (2, 'Often'),
    (3, 'Nearly every day'),
]


def build_result(tool_key, total_score):
    if total_score <= 3:
        level = 'Low concern'
    elif total_score <= 7:
        level = 'Moderate concern'
    else:
        level = 'Higher concern'

    guidance = {
        'mood': {
            'Low concern': 'Your answers suggest your mood is relatively steady right now. Keep using routines that support rest, structure, and connection.',
            'Moderate concern': 'Your answers suggest some strain in mood. It may help to reduce pressure, keep a gentle routine, and speak to someone you trust.',
            'Higher concern': 'Your answers suggest your mood may need closer support. If these feelings continue or worsen, speaking with a GP or qualified professional would be a sensible next step.',
        },
        'stress': {
            'Low concern': 'Your responses suggest stress is present but may be manageable. Short breaks, movement, and realistic boundaries can help keep it that way.',
            'Moderate concern': 'Your stress levels may be building. It could help to identify the main pressure points and choose one practical action to reduce overload.',
            'Higher concern': 'Your responses suggest stress may be affecting your wellbeing more strongly. Consider reaching out for support and reviewing workload, sleep, and recovery time.',
        },
        'sleep': {
            'Low concern': 'Your sleep habits look reasonably steady. A consistent wake-up time and calm evening routine can help maintain that progress.',
            'Moderate concern': 'Your answers suggest your sleep routine may need some attention. Small changes to bedtime habits and screen use may help.',
            'Higher concern': 'Your answers suggest sleep difficulties may be having a stronger impact. If the pattern continues, it would be sensible to speak with a healthcare professional.',
        },
    }

    next_steps = {
        'mood': 'Suggested next step: choose one small, supportive action today such as getting outside, messaging someone you trust, or completing one manageable task.',
        'stress': 'Suggested next step: write down the top one or two stressors and decide what can be done today, what can wait, and what support may be needed.',
        'sleep': 'Suggested next step: try a calmer wind-down routine tonight and keep your wake-up time consistent tomorrow morning.',
    }

    return {
        'score': total_score,
        'level': level,
        'message': guidance[tool_key][level],
        'next_step': next_steps[tool_key],
    }


def index_view(request):
    selected_key = request.POST.get('assessment_type') or request.GET.get('tool', 'mood')
    if selected_key not in ASSESSMENTS:
        selected_key = 'mood'

    selected_assessment = ASSESSMENTS[selected_key]
    result = None

    if request.method == 'POST':
        total_score = 0
        for question in selected_assessment['questions']:
            total_score += int(request.POST.get(question['name'], 0))
        result = build_result(selected_key, total_score)

    context = {
        'assessments': ASSESSMENTS,
        'selected_key': selected_key,
        'selected_assessment': selected_assessment,
        'response_options': RESPONSE_OPTIONS,
        'result': result,
    }
    return render(request, 'assessments/index.html', context)
