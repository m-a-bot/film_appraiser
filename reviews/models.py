import re
import string
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AlbertForSequenceClassification
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

device = "cpu"

def preprocess_text(text):
    new_text = text.lower().replace('<br />', '')
    
    new_text = re.sub("[%s]" % re.escape(string.punctuation), '', new_text)
    
    return new_text

class ReviewModel:
    def __init__(self, review_text):
        self.review_text = review_text

        self.tokenizer = AutoTokenizer.from_pretrained(current_directory + '/AlbertForClassification', local_files_only=True)
        self.model = AlbertForSequenceClassification.from_pretrained(current_directory + "/AlbertForClassification", local_files_only=True,
                                                      num_labels=8, ignore_mismatched_sizes=True,
                                                     problem_type="multi_label_classification").to(device)

        self.rating = self.rate_text(self.review_text)
        self.sentiment = self.analyze_sentiment()

    def rate_text(self, text):
        new_text = preprocess_text(text)

        inputs = self.tokenizer(new_text, 
                           return_tensors="pt", 
                           max_length=128, 
                           truncation=True, 
                           padding=True,
                           return_attention_mask=True).to(device)
        
        outputs = self.model(**inputs)

        logits = outputs.logits

        _, predicted = torch.max(logits, dim=1)

        rate = predicted.item()

        if rate > 3:
            rate += 2

        return rate + 1
    
    def analyze_sentiment(self):
        if self.rating <= 4:
            return 'Отрицательный'
        return 'Положительный'
