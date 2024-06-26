# QRdoc
# Функциональные требования к системе доступа к документам по QR-кодам

На текущий момент декларации и сертификаты соответствия TP TC (а также гигиенические сертификаты и прочее) хранятся в единой базде данных T-Flex DOCs. Руководства по эксплуатации (РЭ) централизованно не хранится. Все типы документов так или иначе привязаны к номеру ТУ на продукцию.

Задачи для реализации
   1. Создать файловое хранилище для хранения РЭ. Названия папок должны соответствовать обозначениям ТУ (web).
   2. Разместить РЭ на файловом хранилище (ОГК заводов).
   3. Включить ответственность за актуальность файлов в маршрут извещений об измении в части ТУ и РЭ (ОГК заводов).
   4. На серверной стороне реализовать приложение, позволяющее получить запрос клиента, содержащий номер ТУ; найти в базе DOCs все файлы, в поле описания которых содержится требуемое ТУ; найти файлы РЭ в файловом хранилище; создать временную паапку на сервере и поместить туда найденные файлы; сгенерировать ссылку на временную папку и передать её клиенту (web).
   5. На серверной стороне реализовать фоновый процесс для удаления временных папок старше X дней (web).
   6. Сгенерировать QR-код содержащий вызов серверного приложения с приложения с параметром "Номер ТУ", разместить QR-коды на макете паспорта (ОКач заводов, УПТК, web).
