Простой crawler для сбора цитат с `quotes.toscrape.com`.
# Запуск
```bash
cd homework;
scrapy crawl quotes -s CLOSESPIDER_ITEMCOUNT=100 -o quotes.jl
```
Цитаты сохраняются в `quotes.jl`. Параметр `CLOSESPIDER_ITEMCOUNT` можно менять в зависимости от того, насколько много цитат нужно загрузить.
