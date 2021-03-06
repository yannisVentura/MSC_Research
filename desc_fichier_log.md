#Qu'es ce qu'un bon fichier de log ?

Tout d'abbord avant de comprendre ce qu'est un bon fichier de log (ou journal) il est important d'en connaitre la définition.

Wikipedia: "En informatique, le concept d'historique des événements ou de logging désigne l'enregistrement séquentiel
dans un fichier ou une base de données de tous les événements affectant un processus particulier (application, activité d'un réseau informatique…).
Le journal (en anglais log file ou plus simplement log), désigne alors le fichier contenant ces enregistrements.
Généralement datés et classés par ordres chronologiques, ces derniers permettent d'analyser pas à pas l'activité interne du processus et ses interactions avec son environnement."

Un fichier de log est donc un journal, prenant généralement la forme d'un fichier textuel dans lequel sont enregistrés diverses informations concernant l'activité d'un serveur, ou d'un équipement.
Ainsi bien qu'il soit généré par un programme informatique, un fichier de log doit donc être suffisamment clair, lisible et compréhensible par un humain que nous appellerons un analyste.

On peut ainsi distinguer une seconde propriété d'un fichier de log. Si ce dernier doit être compréhensible par un humain, il doit aussi être compréhensible par ce dernier
sans qu'il n'ait accès au contexte du système. Donc, bien qu'une multitude d'informations puissent être généré par un système (au sens large du terme), toutes ne sont pas pertinente.
On pourrait donc se poser la question suivante : quels types d'informations doit-on retrouver dans un bon fichier de logs ?

## a. Quelles informations doit-on retrouver dans un fichier de log ?


Tout d'abbord, un fichier de logs dois répondre à plusieurs questions : Que c'est-il passé ? Quand ? Où ? Comment ?

Bien que simpliste ces informations permetrons de filtrer les données issues du système. Mais comment répondre à ces questions ?
Dans leurs articles " How to Do Application Logging Rigth", Anton Chuvakin et Gunnar Peterson tentant de répondre ensemble à cette problématique. Selon ces derniers plusieurs types
d'évènements sont à renseigné dans un fichier de log :

Tout d'abbord, les évènements concernant l'authentification(authentification réussites ou non):

    > Les accès ( accès distant, accès aux données etc)
    > Les Autorisations
 
Ensuite les informations concernant les changements : 

    > Changmeent de privilège (élévation de privilège etc)
    > Changement de données ( Création, destruction etc)
    > Installation d'application et changement

Troisièmement, les informations concernant la disponiblité du système comprenant l'enregistrement des évènements conernant :

    > Le lancement, l'arret ou le redémarage d'un service, d'un module, d'un composant etc.
    > Les erreurs et défauts (faults) et plus particulièrement les erreurs affectant la disponibilité du système
    > Les informations concernant la sauvegarde du système

Viennent en suivant les informations concernant les problèmes de ressources :

    > Ressources non disponible, capacités matériels atteintes etc...
    > Problèmes de connectivités etc
    > Atteintes de limite (limite d'espace disque etc)

Enfin le dernier type d'erreur à enregistrer dans un fichier de log concerne les menaces et doivent contenir des informations concernant : 
    
    > Invalidité de l'application
    > Problèmes de sécurités connues

Cette première classification permet en effet de connaitre les différents évènements qui seront consignés dans un fichier journal. Cependant Anton Chuvakin et Gunnar Peterson
vont plus loin expliquant pour chaque évènements quels types de données devraient être enregistré.
Pour répondre à cette question il est important de se poser encore une fois diverses questions répondant aux 5 W :

   >"Who was involved ?
   
   > What happened ?
   
   > Where did it happen ?
   
   > When did it happen ? 
   
   > Why did it happen ? 
   
   > How did it happen ?" 
    
 
Premièrement, le nom de l'utilisateur permet de répondre à la question "qui" ("who"), en incluant le nom de l'utilisateur ou de l'entité concernée dans le log
ce dernier donne directement une information sur son contexte d'exécution.
Par exemple 'user:kkpo try to logging' Dans ce simple message, on obtien l'information selon laquelle un utilisateur a essayer de se connecter. En connaissant le nom de l'utilisateur, il serait
alors possible de vérifier par la suite si son authentification à échoué ou non.

Ensuite il est important de spécifier l'objet (object), permet de répondre à la question quoi "what".
Ainsi si on reprend le message précédent "user:kkpo try to logging", est incomplet. Une correction pourrait être : "user:kkpo try to logging to the database01"
Le fait de renseigner la source vers laquelle l'utilisateur essaye de s'authentifier rajoute une information essencielle. L'analyse sait désormais qu'une authentification sur la base de donnée 'database01'
a été effectué.

Le status de l'action dois ensuite apparaitre dans le message. Cette action est-elle réussite ou non ?
Dans notre exemple le message "user:kkpo try to logging to the database01" ne fais aucun cas de la réussite ou non de l'authentification. Une correction pourrait être
"user:kkpo try to logging to the database01 but fail". Le status renvoie donc à la question "what".


Puis, le système, l'application ou le composant concerné par le message doit être renseignés.
Le message "user:kkpo try to logging to the database01 on main server but fail" enrichie l'information en répondant à la question où ("where")
La source de cette information peut être également nécessaire et contrinu à répondre à cette question.
"user:kkpo on 127.0.0.1 try to logging to the database01 on main server but fail".

Ajouter un "time stamp" à un message de log permet de répondre à la question "when". Ainsi notre message pourrait être enrichie de la manière suivante
"Tue 01-01-2009 6:00 user:kkpo try to logging to the database01 on main server but fail". Il est également important de noter que dans les applications
distribuées, le timestamp est une donnée essencielle et indispensable à la compréhension d'un fichier log.

De plus, la cause du message (the reason) est également essencielle à l'analyste. Notre message deviendrait alors : 
"Tue 01-01-2009 6:00 user:kkpo try to logging to the database01 on main server but fail -- password incorrect"
Cela répond donc à la question du "pourquoi" (why).

Enfin l'action aide à répondre à la question "how" en fournissant le contexte du message, dans notre exemple ce paramètre est implicite car en lisant le message
nous savons qu'il s'agit de l'authentification et plus particulièrement du login.

Ainsi, au travers de cet ensemble de recommandation, nous pouvons d'ores et déjà observer qu'un fichier journal ne s'écrit pas de manière anodine.
Ce dernier à un but précis, et doit forunir un certain nombre d'informations à son lecteur.

(ne pas oublier de donner des exemples de fichiers de logs notamment à la fin)

_________________________________


## Quel format pour un fichier de log ? (Recommandations... Evolution...)

https://www.loggly.com/blog/why-json-is-the-best-application-log-format-and-how-to-switch/

https://www.loggly.com/blog/8-handy-tips-consider-logging-json/

Selon diverses sources, le format JSON semble être le plus adapté au format de log.

###Avantages du format JSON :

> Interprétable par une multitude de langage
> Format de donnée structuré -> Permet d'utiliser des outils d'analyse de logs (Ou stockage dans une bd noSQL)
> Facilement lisible par un analyste (couple clé - valeurs )

###Inconv : 

> Plus volumineux qu'un fichier en texte plat
_________________________________