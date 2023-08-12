import survey

survey_instance = survey.Survey()
print(survey_instance.debug())


def generate(mood, nbr):
    for i in range(0, nbr):
        match mood:
            case 'positive':
                survey = survey_instance.generate_positive_survey()
            case 'neutral':
                survey = survey_instance.generate_neutral_survey()
            case 'negative':
                survey = survey_instance.generate_negative_survey()
        survey_instance.append_survey_to_file(survey)


generate('positive', 10000)
generate('neutral', 10000)
generate('negative', 10000)
