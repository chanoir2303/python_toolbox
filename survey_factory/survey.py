import sequence_data as sd
import json
import random


class Survey:
    def __init__(self):
        self.issues = sd.issues
        self.devices = sd.devices
        self.positive_sequences = sd.positive_sequences
        self.neutral_sequences = sd.neutral_sequences
        self.negative_sequences = sd.negative_sequences
        self.positive_templates = sd.positive_templates
        self.neutral_templates = sd.neutral_templates
        self.negative_templates = sd.negative_templates

    def _generate_survey(self, templates, sequences, label):
        template = random.choice(templates)
        sequence = random.choice(sequences)
        device = random.choice(self.devices)
        issue = random.choice(self.issues)

        text = template.format(device=device, issue=issue, positive_sequence=sequence,
                               neutral_sequence=sequence, negative_sequence=sequence)

        survey = {
            "text": text,
            "label": label
        }

        return survey

    def generate_positive_survey(self):
        return self._generate_survey(self.positive_templates, self.positive_sequences, "positive")

    def generate_neutral_survey(self):
        return self._generate_survey(self.neutral_templates, self.neutral_sequences, "neutral")

    def generate_negative_survey(self):
        return self._generate_survey(self.negative_templates, self.negative_sequences, "negative")

    def append_survey_to_file(self, survey):
        # Read the existing surveys from the file
        try:
            with open('surveys.json', 'r') as file:
                existing_surveys = json.load(file)
        except FileNotFoundError:
            existing_surveys = {"surveys": []}
        except json.JSONDecodeError:
            existing_surveys = {"surveys": []}

        # Append the new survey to the existing surveys
        existing_surveys["surveys"].append(survey)

        # Write the updated surveys back to the file
        with open('surveys.json', 'w') as file:
            json.dump(existing_surveys, file, indent=4)

    @staticmethod
    def debug():
        return 'zebi'
