# film_appraiser

## Классификатор отзывов о фильмах
Была обучена модель на основе трансформера AlbertForSequenceClassification для классификации отзывов о фильмах

Веб-сервис на базе фреймворка Django для ввода отзыва о фильме с автоматическим присвоением рейтинга (от 1 до 10) и статуса комментария (положительный или отрицательный)

## Установка
pip install -r requirements.txt

## Запуск сервера
python manage.py runserver

## Веса
https://drive.google.com/file/d/1NkH5iKcrzQZL7gwoF2FHm7-p0A2dK7ya/view?usp=drive_link

Распаковать веса архив в /reviews/AlbertForClassification

@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}


