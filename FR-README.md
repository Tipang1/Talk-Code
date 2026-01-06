# Talk-Code
## Codez en parlant
Talk-Code est un langage basé sur Python, conçu pour être lisible comme le langage naturel.
Ce langage de programmation est prévu pour ceux qui ne veulent pas apprendre quelque chose de compliqué, ou veulent commencer par quelque chose de simple. Pour coder, il vous suffit d'écrire comme si vous parliez !

## Comment utiliser
Écrivez votre code dans un document, quelque soit son extension. Ça peut être un fichier texte (\*.txt), Python (\*.py), C# (*.cs), ou même quelque chose d'inexistant !
<br>Mais les extensions que je recommande pour organiser plus facilement vos fichiers sont tout de même :
  - *.tlk
  - *.say
  - *.talk

### Les fonctionnalités disponibles ?
Peu nombreuses actuellement, elles vont vite le devenir !
#### Variables :
- Commençons par le commencement. Si vous savez déjà ce qu'est une variable, passez à la suite (sauf si vous avez du temps à perdre). Sinon, ***restez ici***.
   <br>Une variable est... (description d'une variable)
- Comment en déclarer une ? Dans ce langage, c'est très simple ! Indiquez le nom que vous souhaitez lui donner, ajoutez `is`, puis sa valeur.
- Exemples :
   <br>`x is 10`                      => Vaut 10
   <br>`y is "Hello World!"`          => Vaut "Hello World!"
   <br>`z is 'Salut ' + "le monde !"` => Vaut "Salut le monde !"
- Une variable peut être plusieurs choses : un nombre entier (int) ou décimal (float), une chaîne de caractères (string → str), un booléen (True/False), ou rien (None).
---
#### Types de valeurs :
- Le nombre entier est raccourci en `int`. C'est juste un nombre entier.
- Le nombre décimal est appelé `float`. C'est comme un nombre entier, mais avec ou sans chiffre après la virgule.
- La chaîne de caractères, appelée `string`, est raccourcie en `str`. On y met ce qu'on veut, entre `" "` ou `' '`.
- Le boooléen est soit vrai, soit faux. True ou False. Il est raccourci en `bool`.
- Le _rien_, c'est rien. Il n'a rien de spécial, c'est juste _rien_. À ma connaissance, il n'a même pas de nom. Sa valeur est `None`.
---
#### Calculs et concaténation :
- D'abord, qu'est ce qu'une concaténation ? Une concaténation, c'est quand on regroupe 2 strings. C'est utile si on veut écrire plusieurs variables de type str sur la même ligne, par exemple. Le calcul, ça sert à rien d'expliquer, du moins je l'espère.
- Dans ce langage, les calculs sont effectués dans l'ordre de priorité des opérations, pas de gauche à droite. Donc `2+3*2` donnera `8` et non `10`.
- Pour concaténer, il suffit d'écrire `str1 + str2`. On peut en concaténer plus de 2 en même temps.
---
#### Écrire quelque chose à l'écran :
- Comme je l'ai dit, c'est pour afficher du texte à l'écran. C'est l'équivalent de `print()` en Python, ou de `console.log()` en JavaScript.
- Écrivez simplement `say`, suivi de ce que vous voulez écrire.
- Exemples :
   <br>`say y + z` => Affichera `Hello World!Salut le monde !`
   <br>`say 31 + x * 2` => Affichera `51` (31 + 10 * 2 = 31 + 20 = 51)
   <br>`say "1. " + y` => Affichera `1. Hello World!`
---
#### Comparaisons :
- Comme l'indique leur nom, ça sert à comparer, je ne pense pas avoir besoin d'expliquer ça.
- Les comparaisons possibles :
  - `=` : est égal à
  - `<` : plus petit que
  - `>` : plus grand que
---
#### Conditions :
- Comme son nom l’indique, c’est pour faire quelque chose **si** une condition est vraie.
- Écrivez `if`, suivi de la condition, puis de ce que vous voulez exécuter **entre accolades `{ }`**.
- Si la condition est fausse, ce qui est dans les accolades n’est tout simplement pas exécuté.

- Exemples :
   <br>`if x = 10 { say "x vaut 10" }`                    => Affichera "x vaut 10"
   <br>`if y != "Bonjour" { say "Ce n'est pas Bonjour" }` => SyntaxError → `!=` n'existe pas encore
   <br>`if x > 5 { say x }`                               => Affichera '10'

- Vous pouvez aussi prévoir un autre cas avec `else` :
   <br>`if x > 10 { say "Grand nombre" } else { say "Petit nombre" }` => Affichera "Petit nombre" (→ 10 est égal à 10, pas supérieur)

---
#### Commentaires :
- Les commentaires servent à écrire des notes dans le code.
- Ils ne sont jamais exécutés.

- Un commentaire commence par `(`. Si il n'y a pas de **parenthèse fermante `)`**, alors ***l'entièreté*** de ce qui suit sera ignorée.

- Exemple :
   <br>`(Ceci est un commentaire)`
   <br>`x is 10 (x vaut 10)`

---
### À venir !
#### Boucles :
- Une boucle peut servir à répéter une action plusieurs fois.
- Dans Talk-Code, on pourra utiliser `repeat`.

- Pour répéter un nombre précis de fois :
   <br>`repeat 5 { say "Bonjour" }`
   <br>→ Affichera "Bonjour" 5 fois

- Il sera aussi possible d’utiliser une variable :
   <br>`repeat x { say "Test" }`
  
#### Boucle avec condition :
- Parfois, on veut répéter quelque chose **tant qu’une condition est vraie**.
- Pour ça, on utilisera `while`.

- Exemple :
   <br>```while x > 0
      say x
      x is x - 1
   }```

- Ici, le programme affiche `x`, puis diminue sa valeur jusqu’à ce qu’elle atteigne 0.


#### Comparaisons :
 Elles ne sont pas encore toutes disponibles ! Voici les prochaines :
  - `!=` : est différent de
    - Exemple d'utilisation : `if y != "Bonjour" { say "Ce n'est pas Bonjour" }`
  - `<=` : plus petit ou égal
    - Exemple d'utilisation : `if x <= 10 { say "x est inférieur ou égal à 10" }`
  - `>=` : plus grand ou égal
    - Exemple d'utilisation : `if x >= 10 { say "x est supérieur ou égal à 10" }`

#### Conditions multiples :
- Il sera possible de combiner plusieurs conditions.
- `and` signifie **et**. On pourra peut-être utiliser `&`.
- `or` signifie **ou**. On pourra aussi utiliser `||`.

- Exemples :
   <br>`if x > 0 and x < 100 { say "x est entre 0 et 100" }`           => Affichera "x est entre 0 et 100"
   <br>`if y = "Hello" or y = "Salut" { say "Salutation détectée" }` => Ne fera rien

---
### Pour résumer :
- Talk-Code est fait pour être :
  - lisible
  - simple
  - proche du langage humain
- Si une ligne **se lit à voix haute et a du sens**, alors elle est probablement valide

---
