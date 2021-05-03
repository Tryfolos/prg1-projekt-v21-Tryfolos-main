# prg1-projekt-vt21

Detta är slutprojektet i programmeringskursen vt21.
Den tid ni får för projektet är 5 veckor. Projektet ska lämnas in senaste måndag v.22.
Behöver du skriva restprovet så får du arbeta in tiden utanför lektionstid.

| Vecka | Fjärr |           |
|-------|-------|-----------|
| 18    | Åk3   |           |
| 19    | Åk2   |           |
| 20    |       | Restprov  |
| 21    | Åk3   |           |
| 22    | Åk2   | Inlämning |

## Uppgiftsbeskrivning

Du ska omsätta dina programmeringskunskaper och skapa ett verktyg du kan använda
i din framtida yrkesroll.

Programmet baseras på de moment vi har arbetat med. Programmet ska vara en hjälp
till automatisering för skapandet av användare, med tillhörande uppgifter, i ett system.

Programmet ska kunna läsa in en lista med användare, från någon form av fil, hantera 
dessa och skapa användarnamn, lösenord. Resultatet ska sedan sparas i en ny fil.
Detta är de grundläggande kraven, uppgiftens omfång kan självklart utökas för dig som 
behärskar dessa delar.

Du kan
* Läsa från cmdline med argparse
    * Ange vilken fil som ska läsas
    * Ange vilken fil som ska skrivas
* Ange regler för användarnamn och lösenord
* Utöka progammets gränssnitt
    * Låt programmet köras genom en webbsida med Flask
    * Testa att göra ett grafiskt användargränssnitt med TK
* Kontrollera användarens operativsystem med OS modulen och anpassa efter detta
* Skapa faktiskta användare med New-ADUser eller useradd

## Utförande

### Planering

Programmet ska i första stadiet planeras. Du ska skapa pseudokod och/eller 
strukturdiagram/flödesschema för att visa hur det ska fungera. Detta är viktigt, dels 
för dig som ska utöka funktionaliteten på programmet för att visa vad du har tänkt, 
men även för dig som känner att det är väldigt svårt att koda detta program, för då kan 
det räcka med att du visar din förståelse med dessa verktyg.

Mer information finns i kap 7 i kursboken.

Diagram skapas med [draw.io](https://draw.io/)
Pseudokod skrivs i [pseudokod](pseudokod.md)

Om så önskas så kan du skapa din planering som ett Projekt-bräde på GitHub och använda Issues för att lägga till vad du arbetar med.

### Koda

När planeringen är utförd så kan du börja koda på hela programmet eller någon del.
Du ska åtminstone kunna visa att du kan koda viss funtionalitet för programmet för 
godkänt på uppgiften.

Den kod som lämnas in ska hantera eventuella körtidsfel och inte krascha.

Din kod ska använda sig av någon form av

* kontrollstrukturer
* metoder(inbyggd eller egen)
* variabler
* datastrukturer(lista) 

### Dokumentation

Du ska i arbetet dokumentera vad du gör varje arbetspass. Detta görs dels genom
git commit-meddelanden, men även genom att du skriver en kort anteckning om hur ditt
arbete har gått under lektionen, vad du har arbetat med, hur det har gått och att
du dokumenterar de problem du har löst (och eventuella fel).

Logg skrivs i [loggbok](loggbok.md)

När arbetet är utfört så dokumenteras detta kort i loggboken. Där ska du även beskriva
vad du eventuellt inte har hunnit med att göra samt att ge förbättringsförslag på 
ditt program och arbetssätt.

## Bedömning

Uppgiften kommer att bedömas utifrån planeringen, kodens kvalite och hur självständigt 
ditt arbete med att lösa uppgiften har varit.

För högre betyg behöver du visa att du behärskar programmeringsspråket och kan
arbeta självständigt med uppgiften.
Du bör även kunna utöka programmets funktion enligt listan.
