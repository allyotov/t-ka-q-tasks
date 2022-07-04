import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(filename)s | %(levelname)s: %(message)s')

def appearance(intervals):
    lesson = intervals['lesson']
    tutor = intervals['tutor']
    pupil = intervals['pupil']

    pupil.sort()

    logger.debug(lesson)

    seconds_of_lesson = {sec for sec in range(lesson[0], lesson[1])}

    # logger.debug(seconds_of_lesson)
    logger.debug('tutor:')
    logger.debug(tutor)
    tutor_entries = []
    for i in range(0, len(tutor), 2):
        logger.debug(i)
        tutor_seconds = {sec for sec in range(tutor[i], tutor[i + 1])}
        logger.debug('tutor sec')
        logger.debug(tutor_seconds)
        tutor_entries.append(tutor_seconds)
    logger.debug('tutor entries')
    logger.debug(tutor_entries)

    pupil_entries = []
    for i in range(0, len(pupil), 2):
        pupil_seconds = {sec for sec in range(pupil[i], pupil[i + 1])}
        pupil_entries.append(pupil_seconds)
    logger.debug('pupil entries')
    logger.debug(pupil_entries)

    tutor_on_lesson = []
    for entry in tutor_entries:
        intersection = seconds_of_lesson.intersection(entry)
        logger.debug('intersection')
        logger.debug(intersection)
        if len(intersection) > 0:
            logger.debug('not zero')
            tutor_on_lesson.append(intersection)

    logger.debug(tutor_on_lesson)

    pupil_and_tutor_on_lesson = []
    for working_tutor in tutor_on_lesson:
        for pupil in pupil_entries:
            intersection = working_tutor.intersection(pupil)
            if len(intersection) > 0:
                pupil_and_tutor_on_lesson.append(intersection)

    logger.debug('pupil and tutor on lesson')
    logger.debug(pupil_and_tutor_on_lesson)
    total_work_seconds = 0
    for work in pupil_and_tutor_on_lesson:
        total_work_seconds += len(work)

    return total_work_seconds


tests = [
    {'data': {'lesson': [0, 30],
             'pupil': [3, 10],
             'tutor': [0, 20]},
     'answer': 7
    },

    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },

    # {'data': {'lesson': [1594702800, 1594706400],
    #          'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
    #          'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    # 'answer': 3577
    # },

    # В данном тесте интервалы ученика идут не последовательно:
    # pupil': [1594702789, 1594704500, 1594702807, 1594704542,
    # данные некорректны

    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    }
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
       logging.info('Test %s passed' % i)
    logging.info('All things must pass...')
