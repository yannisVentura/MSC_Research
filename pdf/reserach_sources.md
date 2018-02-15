Why Json is the best application log format.. And how to switch :
https://www.loggly.com/blog/why-json-is-the-best-application-log-format-and-how-to-switch/

    > L'avantage de créer ces logs directement en JSON résulte dans le fait que ce dernier est écrit sur une base de js et est aujourd'hui interprétable (parser) par tous les langage de programmations récent.
    De plus les bases NoSQL utilisent pour la plupart ce format ( exemple mongoDB ) cela permettrait de stocker directement les informations des logs dans une base de donénes afin d'effectuer des requêtes.

Note : Il est aussi possible de configurer les SGBD Nginx et Apache afin d'avior des logs en JSON. Cela devrait être également possible avec d'autres SGBD.

Inconv : le format JSON Semble plus lourd ( en terme de place que le format de log textuel.) ---> A vérifier !!


>> Une solution pour notre problématique pourrait être de traduire les logs en JSON afin de les stocker dans une base NoSQL.

>> Une autre solution serait de créer le dictionnaire de données (correspondance entre les paterns et la spécification MSC) directement en Json afin qu'elle puisse être lu par n'importe quel langage de programmation.

_______________________________________________________________________________________________


Alternative à Elastic Seacrh pour l'annalyse de logs : https://www.splunk.com/



